"""Original fictional Harbour service. Local teaching code, never a payment system."""

import hashlib
import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path

CASES = {
    "H-17": {
        "id": "H-17",
        "tenant": "north",
        "ordered": 12,
        "reported": 10,
        "source": "customer-17",
    },
    "H-18": {"id": "H-18", "tenant": "south", "ordered": 8, "reported": 8, "source": "customer-18"},
}
DOCUMENTS = [
    {
        "id": "P-1",
        "version": 1,
        "tenant": "north",
        "active": False,
        "text": "Delivery discrepancy investigator reviews order shipment customer evidence.",
    },
    {
        "id": "P-2",
        "version": 2,
        "tenant": "north",
        "active": True,
        "text": "Delivery discrepancy investigator compares order shipment customer evidence. A manager approves any remedy.",
    },
    {
        "id": "P-3",
        "version": 1,
        "tenant": "south",
        "active": True,
        "text": "Delivery discrepancy south records require regional review.",
    },
    {
        "id": "P-4",
        "version": 1,
        "tenant": "north",
        "active": True,
        "text": "Invoice tax correction belongs to finance.",
    },
]


def lookup(case_id, tenant):
    case = CASES.get(case_id)
    if case is None or case["tenant"] != tenant:
        raise PermissionError("Case unavailable in this scope")
    return dict(case)


def dispatch(name, arguments, tenant):
    if name != "lookup_case" or set(arguments) != {"case_id"}:
        raise ValueError("Unknown capability or invalid arguments")
    if not isinstance(arguments["case_id"], str):
        raise ValueError("case_id must be text")
    return lookup(arguments["case_id"], tenant)


class CaseStore:
    """SQLite transitions with optimistic versions and per-command deduplication.

    Tenant and role must come from a trusted application identity, never model text.
    SQLite is used for a single-host exercise, not distributed failover.
    """

    def __init__(self, path):
        self.path = Path(path)
        with self.connect() as db:
            db.executescript("""
            CREATE TABLE IF NOT EXISTS cases (
              id TEXT PRIMARY KEY, tenant TEXT NOT NULL, version INTEGER NOT NULL,
              status TEXT NOT NULL, proposal INTEGER NOT NULL, policy_version INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS commands (
              key TEXT PRIMARY KEY, fingerprint TEXT NOT NULL, result TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS audit (
              seq INTEGER PRIMARY KEY, case_id TEXT NOT NULL, actor TEXT NOT NULL,
              action TEXT NOT NULL, version INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS jobs (
              id TEXT PRIMARY KEY, state TEXT NOT NULL, owner TEXT, lease_until REAL);
            """)

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=5)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def seed(self, case_id="H-17", tenant="north"):
        with self.connect() as db:
            db.execute(
                "INSERT OR IGNORE INTO cases VALUES (?, ?, 1, 'review', 200, 2)", (case_id, tenant)
            )

    def read(self, case_id, tenant):
        with self.connect() as db:
            row = db.execute(
                "SELECT * FROM cases WHERE id=? AND tenant=?", (case_id, tenant)
            ).fetchone()
        if row is None:
            raise PermissionError("Case unavailable in this scope")
        return dict(row)

    def decide(self, case_id, tenant, actor, role, expected_version, action, key, policy_version=2):
        if (
            type(expected_version) is not int
            or expected_version < 1
            or type(policy_version) is not int
            or policy_version < 1
        ):
            raise ValueError("Positive integer versions required")
        if role != "manager" or not actor:
            raise PermissionError("Manager identity required")
        if action not in {"approve", "return"} or not key:
            raise ValueError("Explicit action and idempotency key required")
        payload = [case_id, tenant, actor, expected_version, action, policy_version]
        fingerprint = hashlib.sha256(json.dumps(payload).encode()).hexdigest()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            prior = db.execute("SELECT * FROM commands WHERE key=?", (key,)).fetchone()
            if prior:
                if prior["fingerprint"] != fingerprint:
                    raise ValueError("Key already used for a different command")
                return json.loads(prior["result"])
            row = db.execute(
                "SELECT * FROM cases WHERE id=? AND tenant=?", (case_id, tenant)
            ).fetchone()
            if row is None:
                raise PermissionError("Case unavailable in this scope")
            if row["version"] != expected_version or row["status"] != "review":
                raise ValueError("Stale version or decision already resolved")
            if row["policy_version"] != policy_version:
                raise ValueError("Policy changed: review again")
            status = "approved_simulation" if action == "approve" else "returned"
            db.execute("UPDATE cases SET status=?, version=version+1 WHERE id=?", (status, case_id))
            result = {"id": case_id, "status": status, "version": expected_version + 1}
            db.execute(
                "INSERT INTO commands VALUES (?, ?, ?)", (key, fingerprint, json.dumps(result))
            )
            db.execute(
                "INSERT INTO audit(case_id,actor,action,version) VALUES (?, ?, ?, ?)",
                (case_id, actor, action, result["version"]),
            )
            return result

    def enqueue(self, job_id):
        with self.connect() as db:
            db.execute("INSERT INTO jobs VALUES (?, 'queued', NULL, NULL)", (job_id,))

    def claim(self, job_id, owner, now, seconds=10):
        if not owner or seconds <= 0:
            raise ValueError("Owner and positive lease required")
        with self.connect() as db:
            result = db.execute(
                "UPDATE jobs SET state='running', owner=?, lease_until=? WHERE id=? AND (state='queued' OR (state='running' AND lease_until<=?))",
                (owner, now + seconds, job_id, now),
            )
            return result.rowcount == 1

    def finish(self, job_id, owner, now):
        with self.connect() as db:
            result = db.execute(
                "UPDATE jobs SET state='done' WHERE id=? AND state='running' AND owner=? AND lease_until>?",
                (job_id, owner, now),
            )
            if result.rowcount != 1:
                raise ValueError("Lease no longer owned")


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()
