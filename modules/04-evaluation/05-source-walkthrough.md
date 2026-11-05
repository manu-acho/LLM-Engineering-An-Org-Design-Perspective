# Lesson 4.5: Trace error categories and the chosen loss rule

[Download the matching notebook](/downloads/04-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m04.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

score accepts equally sized, nonempty lists of reference labels and predictions. zip pairs each reference with the prediction for the same position. Boolean comparisons count correct outcomes, unsafe clearances and unnecessary reviews. The illustrative loss multiplies unsafe clearances by a chosen cost and adds unnecessary reviews. This is an explicit preference model, not a discovered financial valuation. demo compares an always-clear rule with a more conservative rule against the same four fictional reference cases.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Construct two predictions with equal accuracy but different unsafe-clearance counts. Then ask whether the chosen twenty-to-one penalty reflects an agreed business preference or only an author assumption.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m04 import score
for penalty in [1, 5, 20]:
    print(penalty, score(["review", "clear"], ["clear", "clear"], penalty))
```

**Interpretation.** Against [review, clear], predicting [clear, clear] and [review, review] both gives one correct result out of two. The first produces an unsafe clearance; the second produces an unnecessary review. Under the illustrative penalty the losses are twenty and one. The penalty should be agreed and sensitivity-tested rather than presented as an empirical cost.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The always-clear rule has accuracy one half, two unsafe clearances and illustrative loss forty. The conservative rule has accuracy three quarters, no unsafe clearances and loss one. These are exact calculations on invented cases. A larger evaluation and observations of actual work would be needed for a deployment decision.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A confusion matrix exposes the types of error; a single accuracy number conceals them. A randomised or carefully matched service comparison can examine outcomes more credibly than a before-and-after anecdote. Where harmful decisions are rare, deliberately constructed challenge cases complement, rather than replace, representative cases.

The [research connection](../../reference/research/04-implementation.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
