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


def create_app(database_path, principals):
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
