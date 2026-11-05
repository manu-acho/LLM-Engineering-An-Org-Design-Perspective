# Lesson 20.5: Trace comparable evidence and release conditions

[Download the matching notebook](/downloads/20-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m20.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

gate requires baseline and candidate records with the same nonempty evaluation size and dataset hash. It compares unsafe decisions, accuracy and a chosen ten-percent cost tolerance, then requires explicit human approval. It returns reasons rather than silently changing a live version. demo constructs illustrative scores and shows how approval changes the promotion result. The dataset hash names a teaching evaluation identity; it is not proof that hidden test labels were protected or that the sample is statistically adequate.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Suppose an improver repeatedly tests candidates against the same held-out cases. Explain why those cases eventually stop functioning as an independent test, even if their filenames never change.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m20 import gate
baseline = {"n":10,"dataset_hash":"a","accuracy":.8,"unsafe":1,"cost":1.0}
assert not gate(baseline, {**baseline,"accuracy":.9,"unsafe":2}, True)["promote"]
print("Safety regression blocks promotion")
```

**Interpretation.** Selection decisions convey information about the test set. Repeated optimisation against its scores can overfit the selection process without directly displaying labels. Keep separate development and final confirmation sets, restrict evaluation access, record the number of selection rounds and use a new representative comparison when scope changes. Human approval should examine the experiment design as well as the displayed score.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The illustrative candidate is blocked without approval and passes the stated gate with approval. A candidate with more unsafe decisions is blocked even if its accuracy improves. Different dataset identities raise an error because the comparison is not the declared experiment. Promotion does not establish statistical significance or guarantee future performance.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A fixed, periodically reviewed configuration may be safer and cheaper than automatic proposal generation. An improver can suggest changes without holding promotion authority. Versioning and rollback preserve a recovery route, but cannot undo every external consequence already caused by a released version.

The [research connection](../../reference/research/05-routines.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
