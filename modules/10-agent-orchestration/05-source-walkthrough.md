# Lesson 10.5: Separate schema checks from evidence support

[Download the matching notebook](/downloads/10-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m10.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

Contribution is a Pydantic model. Its fields require a case identifier, at least one source, a conclusion and at least one unresolved item; extra fields are forbidden. model_validate checks the payload against that structure. accept then checks that the case identifier is the expected one and every cited source belongs to the allowed set. A successful result is labelled accepted_for_review. That status deliberately stops short of verifying the conclusion or authorising a remedy.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Write a false conclusion using order-17 as its source and determine whether the current acceptance function detects the falsehood. Propose the next check rather than claiming schema validation solved it.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m10 import accept
try:
    accept({"case_id":"H-17", "sources":["invented"], "conclusion":"ok", "unresolved":["receipt"]})
except ValueError:
    print("Unsupported source rejected")
else:
    raise AssertionError("Acceptance failed")
```

**Interpretation.** The function cannot judge entailment. A deterministic quantity comparison, a reviewer or a separately evaluated evidence-support check must examine whether the source supports the conclusion. Each additional checker has its own error modes. An acceptance contract should state exactly which checks were applied and what remains for review.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The supplied H-17 contribution passes the structural and case/source membership checks. An invented source or another case identifier raises ValueError. A conclusion that is false but cites an allowed source may still pass, exposing the distinction between membership validation and factual support.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A specialist-as-tool returns a contribution to its coordinator. A handoff transfers the active interaction to another role. Neither pattern should leave ownership implicit. Plain functions are adequate for many fixed routes and make a useful comparison before introducing a model-driven coordinator.

The [research connection](../../reference/research/02-coordination.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
