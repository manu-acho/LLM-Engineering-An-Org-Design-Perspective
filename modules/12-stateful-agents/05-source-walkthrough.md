# Lesson 12.5: Build a graph that pauses and reopens its saved state

[Module route](README.md) · [Next: design the review service](06-design-lab.md)

The first run saves information at a point where a human decision is needed. A later run uses the same thread identifier to find the saved information. Trace what gets restored and what must be checked again before any action can proceed.

[Open the companion workshop notebook](../../notebooks/12-stateful-agents.ipynb).

## Connect the source's layers

The course [graph lab](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/4_langchain_langgraph/2_lab2.ipynb) begins with state, nodes and edges before adding tools and memory. The later [agent-layer lab](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/4_langchain_langgraph/3_lab3.ipynb) shows a higher-level assembly. Following both reveals what the abstraction supplies rather than making the graph appear magical.

This independent local lab needs `langgraph` and `langgraph-checkpoint-sqlite`. It calls no model or external service. SQLite stores a checkpoint on disk. Reopening the connection and compiling a new graph demonstrates recovered state through fresh objects; it is not a complete operating recovery test.

```python
from typing import Annotated, TypedDict
from operator import add
from tempfile import TemporaryDirectory
from pathlib import Path
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.sqlite import SqliteSaver

class State(TypedDict):
    case_id: str
    revision: int
    stage: str
    events: Annotated[list[str], add]

def prepare(state):
    return {"stage": "awaiting_review", "events": ["draft_prepared"]}

def review(state):
    decision = interrupt({"case_id": state["case_id"], "revision": state["revision"]})
    if decision["case_id"] != state["case_id"] or decision["revision"] != state["revision"]:
        raise ValueError("Decision does not match the proposal")
    if decision["decision"] not in {"approve", "reject"}:
        raise ValueError("Unknown review decision")
    return {
        "stage": "approved" if decision["decision"] == "approve" else "needs_revision",
        "events": ["review_" + decision["decision"]],
    }

def finish(state):
    return {"stage": "simulated_complete", "events": ["simulation_finished"]}

def build(checkpointer):
    builder = StateGraph(State)
    builder.add_node("prepare", prepare)
    builder.add_node("review", review)
    builder.add_node("finish", finish)
    builder.add_edge(START, "prepare")
    builder.add_edge("prepare", "review")
    builder.add_conditional_edges(
        "review", lambda s: "finish" if s["stage"] == "approved" else "stop",
        {"finish": "finish", "stop": END},
    )
    builder.add_edge("finish", END)
    return builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "C-17"}}
with TemporaryDirectory() as directory:
    database = str(Path(directory) / "checkpoints.sqlite")
    with SqliteSaver.from_conn_string(database) as saver:
        graph = build(saver)
        graph.invoke({"case_id": "C-17", "revision": 1, "stage": "new", "events": []}, config)
        assert graph.get_state(config).next == ("review",)
    with SqliteSaver.from_conn_string(database) as saver:
        graph = build(saver)
        assert graph.get_state(config).values["stage"] == "awaiting_review"
        final = graph.invoke(Command(resume={
            "case_id": "C-17", "revision": 1, "decision": "approve"
        }), config)
        assert final["stage"] == "simulated_complete"
        assert final["events"] == ["draft_prepared", "review_approve", "simulation_finished"]
```

## Follow one case

`prepare` returns only its updated fields. The reducer appends its event to the existing list. `review` interrupts with case and revision information before producing a state update. The first invocation returns with pending work; a final-looking return from `invoke` does not mean the graph reached `END`.

The first connection closes. The second graph reads the checkpoint for the same thread. `Command(resume=...)` supplies the interrupt result. `review` checks that it matches the stored proposal. The conditional route either finishes the simulation or ends with revision needed.

This demonstration trusts the calling application to authenticate the reviewer. It deliberately contains no customer action. A real action node would require the stronger action-identity and reconciliation arrangements from Module 8.

## Inspect the original Sidekick after understanding the smaller graph

[Sidekick](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/4_langchain_langgraph/sidekick.py) builds a worker with middleware for limits, selected review interrupts and error handling. It uses in-memory checkpoints, so it does not establish restart durability. `_advance` streams state, detects `__interrupt__`, gathers selected tool-call names and asks a structured evaluator for feedback. The outer loop stops on success, a need for user input or its attempt limit.

The evaluator receives the task, criteria, latest reply and tool names. That evidence can support some judgements but cannot independently establish all outside effects. Inspect the exact evaluator input before interpreting its success flag.

**Worked experiments:** Resume the local graph with a wrong revision, then reject a separate new case. The first should fail before simulated completion; the second should end with `needs_revision`. Neither requires a model to reveal the state-control issue. For an actual process-restart exercise, persist a chosen database path, run the pause and resume stages in separate processes and retain the same case contract.

## Read the organisational connection

A checkpoint and resume operation have inspectable effects without proving recovery of the wider service. The research chapter explains [materiality in digital systems](../../reference/research/06-technology-in-practice.md#materiality-in-digital-systems).
