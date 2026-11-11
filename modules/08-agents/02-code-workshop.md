# Lesson 8.2: Follow state before performing an action

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

An approved handoff might be requested twice if the first reply is slow. Give the same simulated request to the program twice and follow the identifier it uses to find the earlier result. The receipt describes a local simulation. It does not show that any outside team received the work.

[Open the companion workshop notebook](../../notebooks/08-agents.ipynb).

## A dry-run action service

We will simulate an approved handoff without sending anything. The code stores synthetic execution receipts in memory. It demonstrates sequential state checks and a local duplicate guard. It is not a durable, concurrent or external transaction system.

```python
def simulate_handoff(case, receipts):
    action_id = case["action_id"]
    if action_id in receipts:
        return receipts[action_id]
    if case["state"] != "approved":
        return {"status": "blocked", "reason": "Approval is required"}
    if not case.get("evidence_ids"):
        return {"status": "blocked", "reason": "Evidence is required"}
    receipt = {
        "action_id": action_id,
        "status": "simulated",
        "destination": case["destination"],
    }
    receipts[action_id] = receipt
    return receipt

case = {
    "action_id": "R-17-handoff-v1",
    "state": "approved",
    "evidence_ids": ["order-O-17", "policy-P-1"],
    "destination": "operations-review",
}
receipts = {}
first = simulate_handoff(case, receipts)
second = simulate_handoff(case, receipts)
```

## Trace the checks

The function first reads a stable action identifier. If that identifier is already in `receipts`, it returns the previous result. It does not create another local receipt. This permits repeated sequential calls against the same dictionary to reuse a result.

The next condition checks state. A case at `proposed` is blocked; a generated recommendation does not automatically become approval. The following condition checks that evidence IDs are present. This only establishes presence, not the content, validity or access status of those sources. A real service must perform the relevant checks against trusted records.

The final dictionary is a receipt for a simulation. The word `simulated` is deliberate. Labelling it `sent` would falsely describe an effect that never occurred. Storing it changes the supplied `receipts` dictionary; this is a side effect within the program.

After two calls, the dictionary still contains one entry. If you recreate `receipts = {}` and call again, that protection is gone. If two workers inspect an empty store simultaneously, both could proceed unless a stronger mechanism coordinates them. The demonstration makes the limitation visible rather than promising exactly-once execution.

## Where real execution complicates the picture

Imagine replacing receipt creation with a notification service call. The call succeeds, but the program crashes before storing the receipt. The local record says nothing happened, while the external effect occurred. Simply writing to a local file earlier creates a different failure: the record may say “done” when the external service never executed.

Approaches include external idempotency keys, transactional action/outbox designs and reconciliation using service receipts. Their suitability depends on the participating systems. The general lesson is to identify the uncertainty between requesting, executing and acknowledging an action.

## Read the capstone by responsibility

Open [deal_agent_framework.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/deal_agent_framework.py). It reads saved opportunities, initialises components when needed, calls the planner and writes returned opportunities. This separates persistent application state from the model's context. The stored opportunities do not represent every scanned URL.

Open [planning_agent.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/planning_agent.py). Python fixes the scan–estimate–rank–threshold sequence. Compare [autonomous_planning_agent.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/autonomous_planning_agent.py): it exposes tools and repeats model requests until generation finishes without further tool calls. The latter needs explicit step/time limits and stronger validation of action premises.

Open [ensemble_agent.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/agents/ensemble_agent.py). Inspect the actual arithmetic combining predictions. A comment describing learned regression weights is not a substitute for the executable expression, which uses fixed coefficients in this snapshot.

## Threads, queues and a responsive interface

The final UI uses a **thread**, an execution path within a process, to perform work while the interface receives updates. A **queue** transfers messages between producer and consumer. One side places logs/results in it; another reads them and yields UI updates.

The consumer needs a terminal outcome, success or failure. If a worker raises an exception before posting a result, an interface that only waits for results can keep waiting. A useful design sends an explicit terminal error and associates it with the request ID. It also handles cancellation and timeout.

A queue is a communication mechanism. It does not automatically persist work, enforce business authority or know whether an external action completed.

## Alternatives and practice

For a fixed process, keep Python or a state machine in charge of transitions and use a model within a bounded task. For variable investigation, permit model-selected read tools within a step budget, then route a proposal through controlled execution.

Change `approved` to `proposed` and predict the result. Empty the evidence list and try again. Then explain what additional checks you would need before replacing simulation with a real handoff.

**What the example shows:** Both modified cases are blocked without creating a receipt. The real version still needs authenticated authority, validated evidence, destination controls, durable state and acknowledged outcome handling. A simple successful run cannot establish those properties.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

State should distinguish proposals, authorisation, execution and recorded results. The research chapter explains [distinct acts in a workflow](../../reference/research/03-decisions.md#distinct-acts-in-one-workflow).
