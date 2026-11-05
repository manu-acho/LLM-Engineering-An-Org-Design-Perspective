# Lesson 8.2: Record a simulated decision and safe retry

[Download the matching notebook](/downloads/08-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

A technically successful brief is only one contribution to a service. Harbour also needs an accountable investigator, a remedy decision and a route for retries, errors and corrections. These arrangements belong in the operating model.

The implementation lives in `src/ai_orgdesign/labs/m08.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

CaseStore initialises three operational tables and a job table in SQLite. seed creates a pending review only if the case is absent. read returns a scoped current version. decide requires a manager role, a recognised action, a matching case version and the same policy version before recording a simulated decision. A command key stores a fingerprint and result in the same transaction. Repeating the same key and command returns the prior result; reusing it for a different command fails. These are local transactional controls, not a distributed exactly-once guarantee.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m08 import demo
result = demo()
assert result["retry_same"]
assert result["decision"]["version"] == 2
assert result["money_moved"] is False
print(result)
```

The pending case starts at version one in review. Approval changes it to version two with status approved_simulation. Retrying the identical command returns the same result without an additional audit event. No money moves and no customer message is sent.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Specify who should investigate a case when the evidence is incomplete, and what should happen if two managers act on version one at the same time.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** An explicit case owner should obtain and reconcile evidence before requesting a decision. Two managers may both have read version one, but only one decision should commit. The second must receive a conflict and read the new state. Quietly accepting both would turn a stale view into a new consequential decision.

## Consider the alternative

A human work queue may be sufficient before an autonomous agent is justified. A workflow engine adds state management but needs explicit ownership and recovery rules. A local SQLite transaction provides a useful learning boundary; external payments require an additional protocol and reconciliation arrangements.

The [organisation design reading](../../reference/research/01-organisation-design.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
