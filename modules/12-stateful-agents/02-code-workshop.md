# Lesson 12.2: Resume a case without reusing a stale approval

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

## Separate saved state, approval and effect

This example simulates a pause and resumption using ordinary Python. JSON serialization makes the state easy to inspect. It does not save anything to disk. There is no external execution: the receipt is labelled `simulated`.

```python
import json

def prepare(case_id, revision):
    return {
        "case_id": case_id,
        "proposal_revision": revision,
        "stage": "awaiting_review",
        "proposal": {"action": "prepare_handoff", "source": "order-17"},
        "receipt": None,
    }

def resume(saved_state, approval, reviewer_cases):
    state = json.loads(saved_state)
    if approval["case_id"] not in reviewer_cases:
        raise PermissionError("Reviewer cannot act on this case")
    if approval["case_id"] != state["case_id"]:
        raise ValueError("Approval belongs to another case")
    if approval["proposal_revision"] != state["proposal_revision"]:
        raise ValueError("Approval belongs to an older proposal")
    if approval["decision"] != "approve":
        state["stage"] = "needs_revision"
        return state
    if state["stage"] == "completed" and state["receipt"]:
        return state
    if state["stage"] != "awaiting_review":
        raise ValueError("Case is not awaiting this review")
    state["receipt"] = {
        "status": "simulated",
        "action_id": f"{state['case_id']}:{state['proposal_revision']}",
    }
    state["stage"] = "completed"
    return state

state = prepare("C-17", 1)
snapshot = json.dumps(state)
approval = {"case_id": "C-17", "proposal_revision": 1, "decision": "approve"}
completed = resume(snapshot, approval, {"C-17"})
print(completed["stage"], completed["receipt"]["status"])

changed = prepare("C-17", 2)
try:
    resume(json.dumps(changed), approval, {"C-17"})
except ValueError as error:
    print(str(error))
```

Expected output:

```text
completed simulated
Approval belongs to an older proposal
```

## Trace the representations

`prepare` creates a dictionary with an explicit stage and revision. `json.dumps` converts it to a string. `json.loads` reconstructs a new dictionary inside `resume`. This round trip demonstrates a representation suitable for storage or transport. A real durable workflow must actually write and recover that representation through a storage system.

The checks occur before simulating an effect. The case-scope check represents a reviewer-access boundary. The identity check prevents an approval for one case being applied to another. The revision check binds approval to a particular proposal.

`reviewer_cases` is a trusted application input in this illustration. A real service must derive it from authenticated identity and authorisation. A user-supplied list saying “I may approve every case” would invalidate the boundary. The same applies to the approval record: its structure alone does not prove who created it.

## State controls which transitions are possible

A rejection moves the case to `needs_revision`. An approval can move an awaiting case to `completed`. A repeated approved call using the completed snapshot returns the same receipt. That models one form of repeated-call handling while the correct updated snapshot is retained.

It is not durable idempotency. Calling `resume` twice with the original awaiting-review string creates the simulation twice. Two workers could also read the same old state. An operating service needs transactional state changes or a durable action registry, plus cooperation from the external system where necessary. A local status check alone cannot close the crash/acknowledgement gap from Module 8.

The action identifier combines case and revision. In a richer system, a revision may contain several actions, so each action also needs its own stable identity. A changed source record may invalidate a proposal even when its displayed wording has not changed.

## Read the original graph in layers

In the course's [graph lab](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/4_langchain_langgraph/2_lab2.ipynb), inspect `State`, `StateGraph`, node registration, conditional edges and the loop back from tools to the model. Then follow the checkpointer and `thread_id` used for a second conversation turn. The in-memory example demonstrates continuity in a live process, not recovery after its destruction.

The [agent-layer lab](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/4_langchain_langgraph/3_lab3.ipynb) exposes `create_agent` as a higher-level assembly. The [Deep Agents lab](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/4_langchain_langgraph/4_lab4.ipynb) adds delegated work and filesystem-backed artefacts. Those are additional capabilities and boundaries, not simply longer prompts.

The [Sidekick implementation](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/4_langchain_langgraph/sidekick.py) supplies an especially useful comparison. `HumanInTheLoopMiddleware` names the operations that interrupt, while `ModelCallLimitMiddleware` limits calls within a worker run. The outer evaluator loop also has an attempt limit. These are separate bounds on different layers.

Its error-handling middleware returns some tool failures as messages so the worker can attempt recovery. That makes a failure available to the model; it does not prove recovery succeeded. Its evaluator is a structured model judgement based on the reply and selected tool information. Inspect that evidence before interpreting the evaluator's success flag as verification of an external result.

## Alternatives

A database-backed business state machine may be sufficient when the workflow has few fixed states and no model-selected routing. A graph framework becomes useful when transitions, branching, interrupts and resumption would otherwise create repeated custom machinery.

Either design still needs proposal versioning, approval identity, expiration policy, recovery ownership and compatible stored schemas. A framework can manage execution mechanics without deciding those business rules for you.

**Try it:** Approve the wrong case, reject a proposal and repeat a completed snapshot. Then repeat the original snapshot instead. Explain why the last two repetitions have different implications. No external action needs to run to reveal the design issue.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

An approval should refer to the proposal that was actually reviewed. The research chapter explains [distinct acts in a workflow](../../reference/research/03-decisions.md#distinct-acts-in-one-workflow).
