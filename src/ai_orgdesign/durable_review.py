"""A checkpointed graph whose model contribution waits for a human decision."""

from contextlib import contextmanager
from pathlib import Path
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from ai_orgdesign.business import CaseStore
from ai_orgdesign.investigation import draft


class ReviewState(TypedDict, total=False):
    case_id: str
    tenant: str
    case_version: int
    policy_version: int
    contribution: dict
    decision: dict


@contextmanager
def workflow(path, gateway=None):
    path = Path(path)
    store = CaseStore(path.with_suffix(".cases.db"))

    def prepare(state):
        if gateway is None:
            raise RuntimeError("A gateway is needed only when preparing a new contribution")
        store.seed(state["case_id"], state["tenant"])
        current = store.read(state["case_id"], state["tenant"])
        result = draft(gateway, state["case_id"], state["tenant"])
        return {
            "contribution": result,
            "case_version": current["version"],
            "policy_version": current["policy_version"],
        }

    def human_review(state):
        # On resume this node restarts. Keep consequential effects after interrupt.
        action = interrupt(
            {
                "case_id": state["case_id"],
                "brief": state["contribution"]["brief"],
                "allowed_decisions": ["return", "approve_simulation"],
            }
        )
        if action not in {"return", "approve_simulation"}:
            raise ValueError("Choose a stated review decision")
        result = store.decide(
            state["case_id"],
            state["tenant"],
            "local-course-reviewer",
            "manager",
            state["case_version"],
            "return" if action == "return" else "approve",
            f"review:{state['case_id']}:{state['case_version']}:{action}",
            state["policy_version"],
        )
        return {"decision": result}

    graph = StateGraph(ReviewState)
    graph.add_node("prepare", prepare)
    graph.add_node("human_review", human_review)
    graph.add_edge(START, "prepare")
    graph.add_edge("prepare", "human_review")
    graph.add_edge("human_review", END)
    with SqliteSaver.from_conn_string(str(path)) as saver:
        yield graph.compile(checkpointer=saver)


def start(path, gateway, case_id="H-17", thread_id="review-H-17"):
    with workflow(path, gateway) as graph:
        return graph.invoke(
            {"case_id": case_id, "tenant": "north"}, {"configurable": {"thread_id": thread_id}}
        )


def resume(path, action="return", thread_id="review-H-17"):
    with workflow(path) as graph:
        return graph.invoke(Command(resume=action), {"configurable": {"thread_id": thread_id}})


def inspect_pending(path, thread_id="review-H-17"):
    with workflow(path) as graph:
        snapshot = graph.get_state({"configurable": {"thread_id": thread_id}})
        return {"values": snapshot.values, "next": list(snapshot.next)}
