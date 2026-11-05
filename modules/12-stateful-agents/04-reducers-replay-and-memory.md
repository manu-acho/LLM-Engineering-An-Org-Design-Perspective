# Lesson 12.4: Decide how state changes and what replay repeats

[Download the matching notebook](/downloads/12-04-reducers-replay-and-memory.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: build a persistent graph](05-source-walkthrough.md)

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
