# Lesson 6.2: Fit a text-routing baseline without leakage

[Download the matching notebook](/downloads/06-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Routing labels record a decision about which team should receive work. A clean spreadsheet can therefore encode obsolete ownership rules. Harbour begins with a deliberately small text classifier so the preparation, fitting and evaluation boundary remains visible.

The implementation lives in `src/ai_orgdesign/labs/m06.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

TRAIN contains six invented labelled messages; TEST contains three different messages. make_pipeline joins CountVectorizer and LogisticRegression. During fit, the vectorizer learns its vocabulary from training messages only and the classifier estimates category parameters. predict applies that fitted transformation to the test messages before selecting categories. accuracy_score compares the selected categories with reference labels. random_state fixes the relevant estimator randomness; it does not make the tiny test set representative.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m06 import fit_baseline, TEST
model = fit_baseline()
predicted = model.predict([row[0] for row in TEST]).tolist()
print(predicted)
print(model.predict(["invoice damaged delivery"]).tolist())
```

The test predictions and their score are computed from the fitted pipeline. With the supplied invented messages, the classifier should distinguish finance language from delivery language. Passing the three examples establishes execution of this baseline, not a reliable routing service for ambiguous or new work.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Consider a message containing invoice and damaged delivery. Which team should own it? Explain why fitting more accurately to historical single-team labels might worsen the service.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** The case may require joint work or an intake owner rather than one exclusive specialist. Annotation rules must say what the target represents: first reviewer, accountable owner or final resolver. A model cannot resolve that organisational ambiguity merely by imitating past labels. Revise the task definition before treating disagreement as label noise.

## Consider the alternative

A majority-category baseline establishes whether learned text features add anything. Rules can be clearer when vocabulary and policy are stable. Learned classifiers can generalise across combinations, but confidence calibration, abstention and ambiguous categories need separate design and evaluation.

The [organisation design reading](../../reference/research/03-decisions.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
