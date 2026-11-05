# Lesson 15.5: Trace scope, evidence and discrepancy rules

[Download the matching notebook](/downloads/15-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m15.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

REQUIREMENTS pairs three cases with expected outcomes and named owners. route applies scope before evidence checks, then distinguishes a discrepancy from an apparently matching record. demo constructs the three inputs, evaluates them and computes a hash of the exact input data. The hash identifies the examples; it does not validate their quality. Keeping the expected outcomes separate from route makes it possible to detect an implementation that disagrees with the specification.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Add an acceptance example with equal quantities but a damaged box. Identify which missing input and policy rule are needed before the pilot can handle that case.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m15 import route
assert route({"tenant":"south"}) == "deny"
assert route({"tenant":"north"}) == "needs_evidence"
print("Scope and missing-evidence rules precede arithmetic")
```

**Interpretation.** Quantity comparison cannot recognise condition or contractual remedy. The pilot needs an explicit damage report, supporting evidence and an agreed review route. Expanding the schema and examples changes scope; changing a prompt alone would hide that change. Keep damaged-goods cases outside automated handling until the revised specification is tested.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The three routes are review, deny and needs_evidence. matches is true for the supplied examples. Agreement between quantities produces compare_policy rather than automatic closure. This deliberately avoids using numerical agreement as sufficient evidence that the customer problem is resolved.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. An intake form, a record-comparison script or a better source feed may solve the first problem without generation. A coding agent can help implement the agreed slice, but its proposed code must face the same acceptance cases and review as manually written code.

The [research connection](../../reference/research/04-implementation.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
