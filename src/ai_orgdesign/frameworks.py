"""A common evidence contract through two actual model-backed runtimes."""

import json
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from ai_orgdesign.case_data import get_case
from ai_orgdesign.investigation import (
    INSTRUCTIONS,
    ROUTE_DEFINITIONS,
    Brief,
    draft,
    policy_hits,
    validate_brief,
)


class State(TypedDict):
    case_id: str
    result: dict


def langgraph_run(gateway, case_id="H-17"):
    builder = StateGraph(State)
    builder.add_node("investigate", lambda state: {"result": draft(gateway, state["case_id"])})
    builder.add_edge(START, "investigate")
    builder.add_edge("investigate", END)
    return builder.compile().invoke({"case_id": case_id})["result"]


async def agents_sdk_run(gateway, case_id="H-17", async_client=None):
    from agents import Agent, ModelSettings, OpenAIResponsesModel, RunConfig, Runner

    case = get_case(case_id)
    hits = policy_hits(case)
    gateway._reserve()
    from openai import AsyncOpenAI

    client = async_client or AsyncOpenAI(
        api_key=gateway.client.api_key, base_url=gateway.client.base_url, timeout=45, max_retries=0
    )
    agent = Agent(
        name="Harbour evidence contributor",
        instructions=INSTRUCTIONS + " " + ROUTE_DEFINITIONS,
        model=OpenAIResponsesModel(model=gateway.model, openai_client=client),
        model_settings=ModelSettings(
            max_tokens=gateway.max_output_tokens,
            store=False,
            reasoning={"effort": "none"} if gateway.model.startswith("gpt-6") else None,
        ),
        output_type=Brief,
    )
    try:
        result = await Runner.run(
            agent,
            json.dumps({"case": case, "policy_evidence": hits}),
            max_turns=1,
            run_config=RunConfig(tracing_disabled=True),
        )
    finally:
        if async_client is None:
            await client.close()
    brief = validate_brief(result.final_output.model_dump(), case, hits)
    usage = result.context_wrapper.usage
    return {
        "brief": brief.model_dump(),
        "sdk_usage": {
            "requests": usage.requests,
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
        },
        "ledger_scope": "SDK usage is separate from gateway.records; the SDK has its own one-turn limit",
    }
