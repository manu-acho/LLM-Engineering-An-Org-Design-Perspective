# Lesson 12.5: Trace current versions through a delayed decision

[Download the matching notebook](/downloads/12-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m12.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

The example writes a pending case to a SQLite file, then constructs a second CaseStore using that same file. Reading the saved version provides the basis for a later return decision. The stored version is checked again inside the transaction that records the decision. This is a real database reopen and resume exercise. It does not kill an operating-system process, checkpoint a neural model or claim distributed crash recovery.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Distinguish a snapshot used to display a review screen from authority to commit a decision. What should happen after a policy change while the screen remains open?

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m12 import demo
result = demo()
assert result["after_resume"]["version"] > result["before_restart"]["version"]
print("Resume produced a new version")
```

**Interpretation.** The snapshot describes what was read. It cannot guarantee that the case or policy remains current. Decision-time checks must compare the submitted versions with the authoritative current versions, then require a fresh review if either changed. Durable storage preserves facts about work; it does not make an old approval valid forever.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

Before the reopen, H-17 is in review at version one. The resumed return decision becomes version two with status returned. A later command based on version one is stale. Replaying the exact committed command with its original key retrieves its original result.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A graph checkpointer can persist execution state; a business database records authoritative case decisions. These may be separate stores with different lifecycles. Event logs aid reconstruction but do not automatically reproduce side effects safely. An outbox and reconciliation become relevant when external actions cross the database boundary.

The [research connection](../../reference/research/05-routines.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
