"""Offline contracts for the learner-focused revision. No network calls."""

import asyncio
import json
from types import SimpleNamespace

import httpx
import pytest
from openai import OpenAI

from ai_orgdesign.case_data import CASES, get_case
from ai_orgdesign.code_generation import acceptance, compile_routing
from ai_orgdesign.durable_review import inspect_pending, resume, start
from ai_orgdesign.governance import Versions
from ai_orgdesign.investigation import evaluate, team, validate_brief
from ai_orgdesign.provider import Gateway, ModelRunError, RunRecord, TextResult, estimated_cost


def payload(case):
    reference = next(c for c in CASES if c["id"] == case["id"])
    return {
        "case_id": case["id"],
        "ordered": case["ordered"],
        "reported": case["reported"],
        "route": reference["expected"],
        "summary": "Fictional fixture, not model output",
        "receipt_status": "unverified",
        "sources": case["source_ids"],
        "unresolved": ["actual_received_quantity"],
        "permitted_output": "investigation_brief_only",
    }


class FixtureGateway:
    def __init__(self):
        self.records = []
        self.calls = 0

    def generate(self, prompt, *, schema=None, instructions=None, **kwargs):
        self.calls += 1
        value = json.loads(prompt)
        if "findings" in schema.get("properties", {}):
            if "policy" in value:
                case = get_case(value["case_id"])
                sources = [p["id"] for p in value["policy"]]
            else:
                case = value
                sources = case["source_ids"]
            output = {
                "case_id": case["id"],
                "findings": ["Explicit test fixture"],
                "sources": sources,
                "unresolved": ["receipt"],
            }
        else:
            output = payload(value["case"])
        record = RunRecord(
            "fixture", "offline-fixture", f"fixture-{self.calls}", "completed", 10, 20, 0.0
        )
        self.records.append(record)
        return TextResult(json.dumps(output), record, output)


def real_sdk_response(status="completed", text="A response", usage=True):
    body = {
        "id": "resp_fixture",
        "object": "response",
        "created_at": 1,
        "model": "offline-test",
        "status": status,
        "output": [
            {
                "id": "message_fixture",
                "type": "message",
                "role": "assistant",
                "status": "completed",
                "content": [{"type": "output_text", "text": text, "annotations": []}],
            }
        ],
        "usage": {"input_tokens": 12, "output_tokens": 4, "total_tokens": 16} if usage else None,
    }
    return body


def sdk_gateway(response):
    transport = httpx.MockTransport(lambda request: httpx.Response(200, json=response))
    client = OpenAI(
        api_key="offline-test-key",
        base_url="https://course.invalid/v1",
        http_client=httpx.Client(transport=transport),
    )
    return Gateway(client=client, model="offline-test", max_requests=2)


def test_actual_sdk_transport_and_usage():
    gateway = sdk_gateway(real_sdk_response())
    result = gateway.generate("fixture")
    assert result.text == "A response"
    assert result.record.input_tokens == 12 and result.record.output_tokens == 4
    assert estimated_cost(gateway.records, 1, 2) == 20 / 1_000_000


@pytest.mark.parametrize("status", ["incomplete", "failed", "cancelled"])
def test_incomplete_never_accepted_as_answer(status):
    gateway = sdk_gateway(real_sdk_response(status, ""))
    with pytest.raises(ModelRunError, match="status"):
        gateway.generate("fixture")
    assert gateway.records[0].status == status


def test_empty_completed_and_missing_usage():
    with pytest.raises(ModelRunError, match="no answer"):
        sdk_gateway(real_sdk_response(text="")).generate("fixture")
    gateway = sdk_gateway(real_sdk_response(usage=False))
    gateway.generate("fixture")
    with pytest.raises(ValueError, match="complete"):
        estimated_cost(gateway.records, 1, 1)


def test_budget_counts_attempts():
    gateway = sdk_gateway(real_sdk_response())
    gateway.generate("one")
    gateway.generate("two")
    with pytest.raises(ModelRunError, match="limit"):
        gateway.generate("three")


@pytest.mark.parametrize("price", [float("nan"), float("inf"), -1, True])
def test_price_inputs_finite(price):
    with pytest.raises(ValueError):
        estimated_cost([], price, 1)


def test_grounded_validation_checks_facts_sources_and_unknowns():
    case = get_case()
    original = payload(case)
    validate_brief(original, case, [])
    for changed in [
        {**original, "reported": 12},
        {**original, "sources": ["fabricated"]},
        {**original, "unresolved": []},
    ]:
        with pytest.raises(ValueError):
            validate_brief(changed, case, [])


def test_references_are_not_model_inputs():
    case = get_case()
    assert "expected" not in case and "group" not in case
    assert case["reported"] == 10
    with pytest.raises(PermissionError):
        get_case("H-18", "north")


def test_specialist_team_and_measured_evaluation():
    gateway = FixtureGateway()
    output = asyncio.run(team(gateway, parallel=True))
    assert len(output["specialists"]) == 2 and len(gateway.records) == 3
    report = evaluate(gateway, ["H-17", "H-19"])
    assert report["accuracy"] == 1 and report["cost"] == 60 and report["n"] == 2
    assert report["cost_unit"] == "observed_tokens_not_currency"


def test_real_graph_interrupt_reopen_resume_without_model_call(tmp_path):
    gateway = FixtureGateway()
    path = tmp_path / "review.db"
    state = start(path, gateway)
    assert "__interrupt__" in state
    assert inspect_pending(path)["next"] == ["human_review"]
    result = resume(path, "return")
    assert result["decision"]["status"] == "returned" and gateway.calls == 1
    assert inspect_pending(path)["next"] == []


def test_durable_rejects_stale_policy(tmp_path):
    from ai_orgdesign.business import CaseStore

    path = tmp_path / "review.db"
    start(path, FixtureGateway())
    store = CaseStore(path.with_suffix(".cases.db"))
    with store.connect() as db:
        db.execute("UPDATE cases SET policy_version=3 WHERE id=?", ("H-17",))
    with pytest.raises(ValueError, match="Policy changed"):
        resume(path)


def test_restricted_generated_function():
    code = """def route_case(case):
    if case["reported"] is None:
        return "needs_evidence"
    if case["category"] == "invoice":
        return "finance"
    if case["category"] == "damage":
        return "review"
    if case["ordered"] != case["reported"]:
        return "investigate"
    return "review"
"""
    assert all(row["passed"] for row in acceptance(compile_routing(code)))
    for source in [
        "import os",
        'def route_case(case):\n return open("/tmp/file")',
        "def route_case(case):\n while True: pass",
        "def route_case(case):\n return case.__class__",
    ]:
        with pytest.raises(ValueError):
            compile_routing(source)


def test_version_proposal_does_not_promote_and_rollback_requires_decision(tmp_path):
    registry = Versions(tmp_path / "versions.json")
    registry.propose("candidate", "Preserve evidence status")
    assert registry.read()["current"] == "baseline"
    report = {
        "n": 2,
        "dataset_hash": "d",
        "accuracy": 1.0,
        "unsafe": 0,
        "cost": 20,
        "cost_unit": "observed_tokens_not_currency",
    }
    assert not registry.promote("candidate", report, report)["promote"]
    assert registry.promote("candidate", report, report, human_approved=True)["promote"]
    with pytest.raises(PermissionError):
        registry.rollback()
    assert registry.rollback(human_approved=True) == "baseline"


def test_http_model_backed_draft_persistence(tmp_path):
    from fastapi.testclient import TestClient

    from ai_orgdesign.labs.m19 import create_app

    token = "offline-course-session-token"
    gateway = FixtureGateway()
    with TestClient(
        create_app(
            tmp_path / "http.db",
            {token: {"id": "manager", "role": "manager", "tenant": "north"}},
            gateway,
        )
    ) as client:
        assert client.post("/cases/H-17/drafts").status_code == 401
        result = client.post("/cases/H-17/drafts", headers={"x-course-token": token})
        assert result.status_code == 200
        saved = client.get("/cases/H-17/drafts", headers={"x-course-token": token})
        assert saved.json()["result"] == result.json()["result"]
        assert (
            client.post("/cases/H-18/drafts", headers={"x-course-token": token}).status_code == 404
        )


def test_live_capstone_measures_outputs(tmp_path):
    from ai_orgdesign.capstone import run_live

    result = run_live(FixtureGateway(), tmp_path / "capstone.db")
    assert result["replay_equal"]
    assert result["candidate"]["cost"] == 60
    assert not result["promotion"]["promote"]


def test_agent_sdk_uses_async_transport_without_network():
    from openai import AsyncOpenAI

    from ai_orgdesign.frameworks import agents_sdk_run

    body = real_sdk_response(text=json.dumps(payload(get_case())))

    async def exercise():
        async with httpx.AsyncClient(
            transport=httpx.MockTransport(lambda request: httpx.Response(200, json=body))
        ) as http:
            async with AsyncOpenAI(
                api_key="offline-test-key", base_url="https://course.invalid/v1", http_client=http
            ) as client:
                gateway = Gateway(
                    client=SimpleNamespace(api_key="unused", base_url="https://course.invalid/v1"),
                    model="offline-test",
                )
                return await agents_sdk_run(gateway, async_client=client)

    result = asyncio.run(exercise())
    assert result["brief"]["receipt_status"] == "unverified"


def test_usage_details_preserved():
    response = real_sdk_response()
    response["usage"]["input_tokens_details"] = {"cached_tokens": 3}
    response["usage"]["output_tokens_details"] = {"reasoning_tokens": 1}
    record = sdk_gateway(response).generate("fixture").record
    assert record.cached_input_tokens == 3
    assert record.reasoning_output_tokens == 1


def test_draft_role_and_concurrent_version_check(tmp_path):
    from fastapi.testclient import TestClient

    from ai_orgdesign.business import CaseStore
    from ai_orgdesign.labs.m19 import create_app

    path = tmp_path / "conflict.db"

    class ChangingGateway(FixtureGateway):
        def generate(self, *args, **kwargs):
            result = super().generate(*args, **kwargs)
            with CaseStore(path).connect() as db:
                db.execute("UPDATE cases SET version=version+1 WHERE id=?", ("H-17",))
            return result

    gateway = ChangingGateway()
    reader, manager = "fictional-reader-session-token", "fictional-manager-session-token"
    principals = {
        reader: {"id": "reader", "role": "reader", "tenant": "north"},
        manager: {"id": "manager", "role": "manager", "tenant": "north"},
    }
    with TestClient(create_app(path, principals, gateway)) as client:
        denied = client.post("/cases/H-17/drafts", headers={"x-course-token": reader})
        assert denied.status_code == 403 and gateway.calls == 0
        conflict = client.post("/cases/H-17/drafts", headers={"x-course-token": manager})
        assert conflict.status_code == 409 and gateway.calls == 1
        assert (
            client.get("/cases/H-17/drafts", headers={"x-course-token": manager}).status_code == 404
        )


def test_followup_appended_without_mutating_saved_history():
    requests = []

    def respond(request):
        requests.append(json.loads(request.content))
        return httpx.Response(200, json=real_sdk_response())

    client = OpenAI(
        api_key="offline-test",
        base_url="https://course.invalid/v1",
        http_client=httpx.Client(transport=httpx.MockTransport(respond)),
    )
    history = [{"role": "user", "content": "Inspect O-17"}]
    Gateway(client=client, model="offline-test").generate("Who reviews it?", messages=history)
    assert len(history) == 1
    assert requests[0]["input"][-1]["content"] == "Who reviews it?"
    assert requests[0]["input"][0] == history[0]
