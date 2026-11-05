"""Authenticated local HTTP teaching service. No payment integration."""

from hmac import compare_digest

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, ConfigDict

from ai_orgdesign.business import CaseStore


class Decision(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    expected_version: int
    action: str
    key: str
    policy_version: int


def create_app(database_path, principals, gateway=None):
    if not principals or any(len(key) < 16 for key in principals):
        raise ValueError("Configure nonempty principal mapping with long random tokens")
    app = FastAPI(title="Harbour teaching service")
    store = CaseStore(database_path)
    store.seed()

    def identity(token):
        for secret, principal in principals.items():
            if compare_digest(token, secret):
                return principal
        raise HTTPException(401, "Authentication required")

    @app.get("/health")
    def health():
        return {"status": "ok", "mode": "teaching simulation"}

    @app.get("/cases/{case_id}")
    def read(case_id: str, x_course_token: str = Header(default="")):
        actor = identity(x_course_token)
        try:
            return store.read(case_id, actor["tenant"])
        except PermissionError:
            raise HTTPException(404, "Case unavailable") from None

    @app.post("/cases/{case_id}/decisions")
    def decide(case_id: str, command: Decision, x_course_token: str = Header(default="")):
        actor = identity(x_course_token)
        try:
            return store.decide(
                case_id,
                actor["tenant"],
                actor["id"],
                actor["role"],
                command.expected_version,
                command.action,
                command.key,
                command.policy_version,
            )
        except PermissionError:
            raise HTTPException(403, "Decision not permitted") from None
        except ValueError as error:
            raise HTTPException(409, str(error)) from None

    @app.post("/cases/{case_id}/drafts")
    def prepare_draft(case_id: str, x_course_token: str = Header(default="")):
        actor = identity(x_course_token)
        if actor["role"] not in {"manager", "investigator"}:
            raise HTTPException(403, "Draft preparation is not permitted for this role")
        if gateway is None:
            raise HTTPException(503, "Live drafting is disabled for this service session")
        from ai_orgdesign.case_data import get_case
        from ai_orgdesign.investigation import draft
        from ai_orgdesign.provider import ModelRunError

        try:
            get_case(case_id, actor["tenant"])
            store.seed(case_id, actor["tenant"])
            current = store.read(case_id, actor["tenant"])
            result = draft(gateway, case_id, actor["tenant"])
            with store.connect() as db:
                db.execute(
                    "CREATE TABLE IF NOT EXISTS drafts (case_id TEXT PRIMARY KEY, case_version INTEGER, payload TEXT)"
                )
                db.execute("BEGIN IMMEDIATE")
                latest = db.execute("SELECT version FROM cases WHERE id=?", (case_id,)).fetchone()
                if latest["version"] != current["version"]:
                    raise HTTPException(409, "Case changed while the model worked; review again")
                import json

                db.execute(
                    "INSERT OR REPLACE INTO drafts VALUES (?, ?, ?)",
                    (case_id, current["version"], json.dumps(result)),
                )
            return {"case_version": current["version"], "result": result}
        except PermissionError:
            raise HTTPException(404, "Case unavailable") from None
        except (ModelRunError, ValueError):
            raise HTTPException(
                502, "No accepted draft: inspect the model session ledger"
            ) from None

    @app.get("/cases/{case_id}/drafts")
    def read_draft(case_id: str, x_course_token: str = Header(default="")):
        actor = identity(x_course_token)
        try:
            current = store.read(case_id, actor["tenant"])
        except PermissionError:
            raise HTTPException(404, "Case unavailable") from None
        with store.connect() as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS drafts (case_id TEXT PRIMARY KEY, case_version INTEGER, payload TEXT)"
            )
            row = db.execute("SELECT * FROM drafts WHERE case_id=?", (case_id,)).fetchone()
        if row is None:
            raise HTTPException(404, "No draft prepared")
        import json

        return {
            "case_version": row["case_version"],
            "current_case_version": current["version"],
            "result": json.loads(row["payload"]),
        }

    return app


def demo():
    import tempfile
    from pathlib import Path

    from fastapi.testclient import TestClient

    token = "fictional-test-token-only"
    with tempfile.TemporaryDirectory() as folder:
        app = create_app(
            Path(folder) / "service.db",
            {token: {"id": "manager-a", "role": "manager", "tenant": "north"}},
        )
        with TestClient(app) as client:
            return {
                "health": client.get("/health").json(),
                "unauthenticated": client.get("/cases/H-17").status_code,
                "authorised": client.get(
                    "/cases/H-17", headers={"x-course-token": token}
                ).status_code,
            }
