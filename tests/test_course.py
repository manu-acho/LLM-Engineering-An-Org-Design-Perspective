"""Independent behavioural, failure and integration checks for course implementations."""

import asyncio
import copy
import json
from concurrent.futures import ThreadPoolExecutor
from importlib import import_module
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from ai_orgdesign.business import DOCUMENTS, CaseStore, dispatch
from ai_orgdesign.labs import m04, m05, m07, m09, m10, m11, m13, m14, m17, m19, m20
from ai_orgdesign.live import ask


@pytest.mark.parametrize("number", range(2, 21))
def test_every_module_demo_runs(number):
    result = import_module(f"ai_orgdesign.labs.m{number:02d}").demo()
    assert isinstance(result, dict)


@pytest.mark.parametrize(
    "name,args,tenant,error",
    [
        ("write_case", {"case_id": "H-17"}, "north", ValueError),
        ("lookup_case", {"case_id": "H-18"}, "north", PermissionError),
        ("lookup_case", {"case_id": "H-17", "role": "manager"}, "north", ValueError),
        ("lookup_case", {"case_id": 17}, "north", ValueError),
    ],
)
def test_dispatch_boundary(name, args, tenant, error):
    with pytest.raises(error):
        dispatch(name, args, tenant)


def test_asymmetric_evaluation_cost():
    a = m04.score(["review", "clear"], ["clear", "clear"])
    b = m04.score(["review", "clear"], ["review", "review"])
    assert a["accuracy"] == b["accuracy"] == 0.5
    assert a["illustrative_loss"] > b["illustrative_loss"]


def test_retrieval_filters_before_fit_and_does_not_mutate():
    before = copy.deepcopy(DOCUMENTS)
    hits = m05.retrieve("delivery evidence", k=5)
    assert {d["id"] for d in hits} == {"P-2"}
    assert DOCUMENTS == before
    assert m05.retrieve("unmatchedzzzz") == []
    assert m05.retrieve("delivery", tenant="unknown") == []


def test_low_rank_update_and_reload(tmp_path):
    result = m07.adapt(tmp_path / "weights.pt")
    assert result["loss_after"] < result["loss_before"] / 10
    assert result["base_unchanged"] and result["reload_equal"]


def test_agent_stops_and_fails_closed():
    call = {"kind": "tool", "id": "same", "name": "lookup_case", "arguments": {"case_id": "H-17"}}
    assert m09.run(lambda _: call)["stop"] == "repeated_call"
    assert m09.run(lambda _: call, budget=1)["stop"] == "budget"
    with pytest.raises(ValueError):
        m09.run(lambda _: {"kind": "shell"})


def test_specialist_acceptance_is_not_only_schema():
    payload = {
        "case_id": "H-17",
        "sources": ["invented"],
        "conclusion": "ok",
        "unresolved": ["receipt"],
    }
    with pytest.raises(ValueError):
        m10.accept(payload)
    payload["sources"] = ["order-17"]
    payload["case_id"] = "H-18"
    with pytest.raises(ValueError):
        m10.accept(payload)


def test_task_graph_cycles_and_missing_dependencies():
    with pytest.raises(ValueError):
        m11.order_tasks({"a": ["b"], "b": ["a"]})
    with pytest.raises(ValueError):
        m11.order_tasks({"a": ["missing"]})


def test_framework_equivalence():
    assert m13.demo()["same"]


def test_real_mcp_transport():
    result = asyncio.run(m14.exchange())
    assert set(result["tools"]) == {"read_case", "search_policy"}
    assert "H-17" in json.dumps(result["content"])


@pytest.fixture
def store(tmp_path):
    result = CaseStore(tmp_path / "case.db")
    result.seed()
    return result


def test_durable_scope_stale_policy_and_version(store):
    with pytest.raises(PermissionError):
        store.read("H-17", "south")
    with pytest.raises(PermissionError):
        store.decide("H-17", "north", "a", "reader", 1, "approve", "k")
    with pytest.raises(ValueError):
        store.decide("H-17", "north", "a", "manager", 2, "approve", "k")
    with pytest.raises(ValueError):
        store.decide("H-17", "north", "a", "manager", 1, "approve", "k", policy_version=1)
    assert store.read("H-17", "north")["version"] == 1


def test_duplicate_and_conflicting_commands(store):
    args = ("H-17", "north", "a", "manager", 1, "approve", "k")
    assert store.decide(*args) == store.decide(*args)
    with pytest.raises(ValueError):
        store.decide("H-17", "north", "a", "manager", 1, "return", "k")
    with store.connect() as db:
        assert db.execute("SELECT count(*) FROM audit").fetchone()[0] == 1


def test_concurrent_decisions_only_one_wins(store):
    def act(key):
        try:
            return store.decide("H-17", "north", "a", "manager", 1, "approve", key)["status"]
        except ValueError:
            return "conflict"

    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(act, ["one", "two"]))
    assert sorted(results) == ["approved_simulation", "conflict"]


def test_lease_reclaim_fences_old_owner(store):
    store.enqueue("one")
    assert store.claim("one", "a", 0)
    assert not store.claim("one", "b", 5)
    assert store.claim("one", "b", 11)
    with pytest.raises(ValueError):
        store.finish("one", "a", 12)
    store.finish("one", "b", 12)
    assert not store.claim("one", "c", 30)


def test_async_limit_and_completion():
    result = asyncio.run(m17.bounded_work(list(range(8)), limit=2))
    assert result["peak"] <= 2
    assert [r["id"] for r in result["results"]] == list(range(8))


def test_http_auth_decision_and_retry(tmp_path):
    token = "test-only-manager-token"
    reader = "test-only-reader-token"
    principals = {
        token: {"id": "a", "tenant": "north", "role": "manager"},
        reader: {"id": "b", "tenant": "north", "role": "reader"},
    }
    with TestClient(m19.create_app(tmp_path / "api.db", principals)) as client:
        assert client.get("/cases/H-17").status_code == 401
        payload = {"expected_version": 1, "action": "approve", "key": "api-1", "policy_version": 2}
        assert (
            client.post(
                "/cases/H-17/decisions", json=payload, headers={"x-course-token": reader}
            ).status_code
            == 403
        )
        one = client.post("/cases/H-17/decisions", json=payload, headers={"x-course-token": token})
        two = client.post("/cases/H-17/decisions", json=payload, headers={"x-course-token": token})
        assert one.status_code == two.status_code == 200 and one.json() == two.json()
        assert (
            client.post(
                "/cases/H-17/decisions",
                json={**payload, "actor": "invented"},
                headers={"x-course-token": token},
            ).status_code
            == 422
        )


def test_promotion_requires_evidence_approval_and_no_safety_regression():
    baseline = {"n": 10, "dataset_hash": "a", "accuracy": 0.8, "unsafe": 1, "cost": 1}
    assert not m20.gate(baseline, baseline)["promote"]
    assert not m20.gate(baseline, {**baseline, "unsafe": 2}, True)["promote"]
    with pytest.raises(ValueError):
        m20.gate(baseline, {**baseline, "dataset_hash": "b"}, True)


def test_live_model_adapter_offline_protocol_only():
    call = SimpleNamespace(
        type="function_call", call_id="one", name="lookup_case", arguments='{"case_id":"H-17"}'
    )
    sent = []

    def create(**kwargs):
        sent.append(copy.deepcopy(kwargs))
        return SimpleNamespace(
            status="completed",
            id="offline-response",
            model="offline-test",
            usage=None,
            output=[call] if len(sent) == 1 else [],
            output_text="Review required",
        )

    client = SimpleNamespace(responses=SimpleNamespace(create=create))
    with pytest.raises(ValueError):
        ask("test", client=client, model="test")
    assert ask("test", client=client, model="test", consent=True)["tool_calls"] == 1
    assert sent[1]["input"][-1]["call_id"] == "one"
    assert all(request["store"] is False for request in sent)


def test_complete_capstone_slice(tmp_path):
    from ai_orgdesign.capstone import run

    result = run(tmp_path / "capstone.db")
    assert result["decision"]["status"] == "returned"
    assert result["replay_equal"] and result["candidate_gate"]["promote"]
    assert "P-2" in result["policy_context"]


@pytest.mark.parametrize(
    "change", [{"accuracy": float("nan")}, {"cost": -1}, {"unsafe": -1}, {"n": True}]
)
def test_gate_rejects_invalid_metrics(change):
    baseline = {"n": 10, "dataset_hash": "a", "accuracy": 0.8, "unsafe": 1, "cost": 1.0}
    with pytest.raises(ValueError):
        m20.gate(baseline, {**baseline, **change}, True)
