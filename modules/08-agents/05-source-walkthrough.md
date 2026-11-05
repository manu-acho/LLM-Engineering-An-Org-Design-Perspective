# Lesson 8.5: Trace the decision transaction and command identity

[Download the matching notebook](/downloads/08-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m08.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

CaseStore initialises three operational tables and a job table in SQLite. seed creates a pending review only if the case is absent. read returns a scoped current version. decide requires a manager role, a recognised action, a matching case version and the same policy version before recording a simulated decision. A command key stores a fingerprint and result in the same transaction. Repeating the same key and command returns the prior result; reusing it for a different command fails. These are local transactional controls, not a distributed exactly-once guarantee.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Specify who should investigate a case when the evidence is incomplete, and what should happen if two managers act on version one at the same time.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m08 import demo
result = demo()
print("Read version:", result["pending"]["version"])
print("Decision version:", result["decision"]["version"])
```

**Interpretation.** An explicit case owner should obtain and reconcile evidence before requesting a decision. Two managers may both have read version one, but only one decision should commit. The second must receive a conflict and read the new state. Quietly accepting both would turn a stale view into a new consequential decision.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The pending case starts at version one in review. Approval changes it to version two with status approved_simulation. Retrying the identical command returns the same result without an additional audit event. No money moves and no customer message is sent.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A human work queue may be sufficient before an autonomous agent is justified. A workflow engine adds state management but needs explicit ownership and recovery rules. A local SQLite transaction provides a useful learning boundary; external payments require an additional protocol and reconciliation arrangements.

The [research connection](../../reference/research/01-organisation-design.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
