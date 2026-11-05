"""An executable end-to-end service slice using fictional cases and no paid API."""

from fastapi.testclient import TestClient

from ai_orgdesign.labs.m05 import grounded_context, retrieve
from ai_orgdesign.labs.m10 import accept
from ai_orgdesign.labs.m19 import create_app
from ai_orgdesign.labs.m20 import gate


def run(database_path):
    hits = retrieve("delivery discrepancy evidence")
    if not hits:
        raise RuntimeError("No permitted policy evidence: refer rather than generate")
    contribution = accept(
        {
            "case_id": "H-17",
            "sources": ["order-17", "customer-17"],
            "conclusion": "Recorded order and customer report differ",
            "unresolved": ["actual receipt", "cause"],
        }
    )
    token = "fictional-capstone-manager-token"
    principals = {token: {"id": "manager-a", "role": "manager", "tenant": "north"}}
    app = create_app(database_path, principals)
    headers = {"x-course-token": token}
    with TestClient(app) as client:
        before = client.get("/cases/H-17", headers=headers).json()
        payload = {
            "expected_version": before["version"],
            "policy_version": before["policy_version"],
            "action": "return",
            "key": "capstone-command",
        }
        first = client.post("/cases/H-17/decisions", headers=headers, json=payload)
        replay = client.post("/cases/H-17/decisions", headers=headers, json=payload)
        if first.status_code != 200 or replay.json() != first.json():
            raise RuntimeError("Decision or replay contract failed")
    baseline = {
        "n": 10,
        "dataset_hash": "fictional-confirmation-v1",
        "accuracy": 0.8,
        "unsafe": 1,
        "cost": 1.0,
    }
    candidate = {**baseline, "accuracy": 0.9, "unsafe": 0, "cost": 1.05}
    return {
        "policy_context": grounded_context(hits),
        "contribution": contribution,
        "decision": first.json(),
        "replay_equal": first.json() == replay.json(),
        "candidate_gate": gate(baseline, candidate, human_approved=True),
        "boundary": "Scripted contribution, human role simulated, in-process HTTP, invented metrics; no model, cloud or payment call",
    }
