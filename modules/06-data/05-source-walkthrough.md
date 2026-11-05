# Lesson 6.5: Inspect fitted vocabulary and ambiguous predictions

[Download the matching notebook](/downloads/06-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m06.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

TRAIN contains six invented labelled messages; TEST contains three different messages. make_pipeline joins CountVectorizer and LogisticRegression. During fit, the vectorizer learns its vocabulary from training messages only and the classifier estimates category parameters. predict applies that fitted transformation to the test messages before selecting categories. accuracy_score compares the selected categories with reference labels. random_state fixes the relevant estimator randomness; it does not make the tiny test set representative.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Consider a message containing invoice and damaged delivery. Which team should own it? Explain why fitting more accurately to historical single-team labels might worsen the service.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m06 import fit_baseline
model = fit_baseline()
print(model.named_steps["countvectorizer"].get_feature_names_out().tolist())
assert "secretzzzz" not in model.named_steps["countvectorizer"].vocabulary_
```

**Interpretation.** The case may require joint work or an intake owner rather than one exclusive specialist. Annotation rules must say what the target represents: first reviewer, accountable owner or final resolver. A model cannot resolve that organisational ambiguity merely by imitating past labels. Revise the task definition before treating disagreement as label noise.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The test predictions and their score are computed from the fitted pipeline. With the supplied invented messages, the classifier should distinguish finance language from delivery language. Passing the three examples establishes execution of this baseline, not a reliable routing service for ambiguous or new work.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A majority-category baseline establishes whether learned text features add anything. Rules can be clearer when vocabulary and policy are stable. Learned classifiers can generalise across combinations, but confidence calibration, abstention and ambiguous categories need separate design and evaluation.

The [research connection](../../reference/research/03-decisions.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
