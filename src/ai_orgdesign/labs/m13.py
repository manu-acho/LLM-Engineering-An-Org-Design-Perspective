"""Equivalent local contributions through plain Python and actual LangGraph."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from ai_orgdesign.business import lookup


class State(TypedDict, total=False):
    case_id: str
    tenant: str
    difference: int
    status: str


def inspect_record(state):
    case = lookup(state["case_id"], state["tenant"])
    return {"difference": case["ordered"] - case["reported"], "status": "review"}


def plain(state):
    return {**state, **inspect_record(state)}


def graph():
    workflow = StateGraph(State)
    workflow.add_node("inspect", inspect_record)
    workflow.add_edge(START, "inspect")
    workflow.add_edge("inspect", END)
    return workflow.compile()


def demo():
    inputs = {"case_id": "H-17", "tenant": "north"}
    baseline = plain(inputs)
    framed = graph().invoke(inputs)
    return {
        "plain": baseline,
        "langgraph": framed,
        "same": baseline == framed,
        "boundary": "Deterministic nodes in a real framework; no model or remote handoff",
    }
