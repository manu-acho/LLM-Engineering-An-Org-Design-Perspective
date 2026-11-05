# Lesson 4.2: Compare equal accuracy with unequal consequences

[Download the matching notebook](/downloads/04-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Two systems can have equal accuracy while imposing very different harms. Harbour needs to distinguish an unnecessary review from clearing a case that still requires investigation, then compare the resulting work with an existing process.

The implementation lives in `src/ai_orgdesign/labs/m04.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

score accepts equally sized, nonempty lists of reference labels and predictions. zip pairs each reference with the prediction for the same position. Boolean comparisons count correct outcomes, unsafe clearances and unnecessary reviews. The illustrative loss multiplies unsafe clearances by a chosen cost and adds unnecessary reviews. This is an explicit preference model, not a discovered financial valuation. demo compares an always-clear rule with a more conservative rule against the same four fictional reference cases.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m04 import score, demo
print(demo())
a = score(["review", "clear"], ["clear", "clear"])
b = score(["review", "clear"], ["review", "review"])
assert a["accuracy"] == b["accuracy"]
assert a["illustrative_loss"] > b["illustrative_loss"]
```

The always-clear rule has accuracy one half, two unsafe clearances and illustrative loss forty. The conservative rule has accuracy three quarters, no unsafe clearances and loss one. These are exact calculations on invented cases. A larger evaluation and observations of actual work would be needed for a deployment decision.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Construct two predictions with equal accuracy but different unsafe-clearance counts. Then ask whether the chosen twenty-to-one penalty reflects an agreed business preference or only an author assumption.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** Against [review, clear], predicting [clear, clear] and [review, review] both gives one correct result out of two. The first produces an unsafe clearance; the second produces an unnecessary review. Under the illustrative penalty the losses are twenty and one. The penalty should be agreed and sensitivity-tested rather than presented as an empirical cost.

## Consider the alternative

A confusion matrix exposes the types of error; a single accuracy number conceals them. A randomised or carefully matched service comparison can examine outcomes more credibly than a before-and-after anecdote. Where harmful decisions are rare, deliberately constructed challenge cases complement, rather than replace, representative cases.

The [organisation design reading](../../reference/research/04-implementation.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
