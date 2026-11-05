# Lesson 12.2: Reopen durable work and resume review

[Download the matching notebook](/downloads/12-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

A review that waits overnight cannot rely on a notebook variable. Durable state preserves the pending work across sessions, but it must not preserve expired authority or repeat an already committed decision.

The implementation lives in `src/ai_orgdesign/labs/m12.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

The example writes a pending case to a SQLite file, then constructs a second CaseStore using that same file. Reading the saved version provides the basis for a later return decision. The stored version is checked again inside the transaction that records the decision. This is a real database reopen and resume exercise. It does not kill an operating-system process, checkpoint a neural model or claim distributed crash recovery.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m12 import demo
result = demo()
assert result["before_restart"]["status"] == "review"
assert result["after_resume"]["status"] == "returned"
print(result)
```

Before the reopen, H-17 is in review at version one. The resumed return decision becomes version two with status returned. A later command based on version one is stale. Replaying the exact committed command with its original key retrieves its original result.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Distinguish a snapshot used to display a review screen from authority to commit a decision. What should happen after a policy change while the screen remains open?

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** The snapshot describes what was read. It cannot guarantee that the case or policy remains current. Decision-time checks must compare the submitted versions with the authoritative current versions, then require a fresh review if either changed. Durable storage preserves facts about work; it does not make an old approval valid forever.

## Consider the alternative

A graph checkpointer can persist execution state; a business database records authoritative case decisions. These may be separate stores with different lifecycles. Event logs aid reconstruction but do not automatically reproduce side effects safely. An outbox and reconciliation become relevant when external actions cross the database boundary.

The [organisation design reading](../../reference/research/05-routines.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
