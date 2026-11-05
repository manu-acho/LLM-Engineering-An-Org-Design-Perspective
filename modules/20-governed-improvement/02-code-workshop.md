# Lesson 20.2: Evaluate a candidate against a promotion gate

[Download the matching notebook](/downloads/20-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

An improvement loop can optimise a proxy while degrading the service. Harbour treats a proposed configuration as a candidate that must pass comparable evaluation, explicit safety and cost conditions, and a human promotion decision.

The implementation lives in `src/ai_orgdesign/labs/m20.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

gate requires baseline and candidate records with the same nonempty evaluation size and dataset hash. It compares unsafe decisions, accuracy and a chosen ten-percent cost tolerance, then requires explicit human approval. It returns reasons rather than silently changing a live version. demo constructs illustrative scores and shows how approval changes the promotion result. The dataset hash names a teaching evaluation identity; it is not proof that hidden test labels were protected or that the sample is statistically adequate.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m20 import demo
result = demo()
assert not result["without_approval"]["promote"]
assert result["approved"]["promote"]
print(result)
```

The illustrative candidate is blocked without approval and passes the stated gate with approval. A candidate with more unsafe decisions is blocked even if its accuracy improves. Different dataset identities raise an error because the comparison is not the declared experiment. Promotion does not establish statistical significance or guarantee future performance.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Suppose an improver repeatedly tests candidates against the same held-out cases. Explain why those cases eventually stop functioning as an independent test, even if their filenames never change.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** Selection decisions convey information about the test set. Repeated optimisation against its scores can overfit the selection process without directly displaying labels. Keep separate development and final confirmation sets, restrict evaluation access, record the number of selection rounds and use a new representative comparison when scope changes. Human approval should examine the experiment design as well as the displayed score.

## Consider the alternative

A fixed, periodically reviewed configuration may be safer and cheaper than automatic proposal generation. An improver can suggest changes without holding promotion authority. Versioning and rollback preserve a recovery route, but cannot undo every external consequence already caused by a released version.

The [organisation design reading](../../reference/research/05-routines.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
