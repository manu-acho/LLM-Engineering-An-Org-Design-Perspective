# Lesson 12.4: Decide how state changes and what replay repeats

[Download the matching notebook](/downloads/12-04-reducers-replay-and-memory.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: build a persistent graph](05-source-walkthrough.md)

## What you'll learn and why it matters

Explain how state updates combine and what can happen again when a run replays. This helps Harbour avoid repeating consequential work after interruption.

## Business context: Harbour

If warehouse and carrier each add a note, state must preserve both without duplicating them on replay. A reducer is a rule for combining an update with what is already stored. Replay runs work again from a chosen boundary; it can repeat an operation that had an outside effect. Follow one update and identify what could happen twice.

Reject approval that relies on an obsolete case or policy version.

[Company and supply-chain context](../../HARBOUR.md) · [Module 12 business situation](../../reference/harbour-learning-journey.md#module-12)

## State updates are partial contributions

A node can return an update such as `{"stage": "review"}` without recreating every field in the case. The framework combines that update with existing state. For a scalar stage, replacement can be appropriate. For a list of events, replacement might discard history.

A reducer defines the combination rule. List addition appends one list to another. A message reducer can also use message identifiers to replace updated messages rather than blindly duplicate them. Read the actual reducer instead of treating “memory” as one undifferentiated feature.

```python
from typing import Annotated, TypedDict
from operator import add

class CaseState(TypedDict):
    case_id: str
    stage: str
    events: Annotated[list[str], add]
```

This declaration needs a framework to interpret the reducer metadata. Ordinary Python type hints do not implement persistence or automatic state merging. `TypedDict` describes a dictionary's expected fields; it is not a database table or an enforced permission policy.

## Checkpoints identify a continuation boundary

A checkpointer saves graph state at defined execution points. A thread ID associates runs with the same evolving work. Reusing the wrong ID can mix cases; choosing a fresh ID on every request can lose the intended continuity. Case identity and thread identity should have an explicit relationship rather than relying on coincidentally similar strings.

A store for longer-term cross-thread information serves a different purpose. A user's preferences, a reusable policy interpretation and a pending case's approval state have different scope and revision needs. Placing all of them in one transcript makes those needs difficult to enforce.

## Replay is not simply “continue the next line”

On resuming an interrupted node, code before the interrupt can execute again. If that code sends a message or increments a business counter, replay can repeat the effect. Put irreversible work behind a deliberate state and action boundary, or make it idempotent with a durable identity.

Checkpointing does not create exactly-once external effects. A saved graph can resume reliably while a remote system has already acted and its acknowledgement was lost. Reconciliation and external cooperation remain necessary.

## Bind review to the thing reviewed

An approval should identify case, proposal revision, decision and authorised actor. The actor's identity and scope must come from trusted application context. A model-generated dictionary containing `"approved": true` does not establish authorisation.

If new evidence changes the proposal, an earlier approval may no longer apply. Versioning makes that relationship checkable. A complete operating policy should also address expiry, changed policy and revoked permission, depending on the action.

## Read the Sidekick's two loops

The course wraps a framework worker with a separate evaluator loop. A model-call limit inside the worker and an attempt limit outside it bound different layers. Returning tool errors as messages can let the worker try another approach. It also changes the evidence the evaluator sees.

**Worked check:** An evaluator receives a final reply and the names of tools called. Can it verify that a file contains the requested result? Tool names show an attempted route. File content, output identity and an acceptance check provide stronger evidence. The evaluator's schema makes its judgement inspectable, not automatically well-supported.

## Read the organisational connection

Replaying events and repeating organisational action have different consequences to investigate. The research chapter explains [variation in recurrent work](../../reference/research/05-routines.md#variation-is-a-question-not-a-verdict).

## Practical activity: Compare replacing a state field with appending an update.


### Predict and follow the values

How many messages remain under the append rule?

```python
old={"messages":["case selected"]}
update={"messages":["policy found"]}
replace={**old,**update}
append={"messages":old["messages"]+update["messages"]}
print("Replace:",replace,"Append:",append)
assert len(replace["messages"])==1 and len(append["messages"])==2
```

### Complete the exercise

**Worked answer.** Two. A reducer specifies how updates combine; a type hint alone does not choose that behaviour.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

### Programming practice

Write append_messages(old, new) without mutating either input list.

Start with the placeholder in the notebook, then compare with this worked solution. The contrasting checks are part of understanding the contract.

```python
def append_messages(old, new):
    return old + new

original=["one"]
assert append_messages(original,["two"]) == ["one","two"]
assert original == ["one"]
```

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A reducer combines updates. A checkpoint supplies a restart boundary. Replay may repeat operations performed after that boundary.

## What this means for the business process

Separate replayable preparation from actions that affect another system. Before retrying a possible credit, check its authoritative receipt and keep the decision identity, so recovery accounts for work that may already have happened.

For the research behind this design choice, read [Documentation and auditing support accountability but do not replace it](../../reference/research/08-governance-and-accountability.md#documentation-and-auditing-support-accountability-but-do-not-replace-it).

## Next lesson

Next reopen a saved checkpoint from a separate process and check which facts and permissions need to be current before review resumes. [Lesson 12.5: Trace current versions through a delayed decision](05-source-walkthrough.md).
