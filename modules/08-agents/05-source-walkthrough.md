# Lesson 8.5: Trace the decision transaction and command identity

[Download the matching notebook](/downloads/08-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Trace command identity, case version and the transaction that records a decision. Harbour needs to prevent a second decision based on an outdated case.

## Business context: Harbour

Two advisers open version 3. The first records a decision and advances the case; the second tries to submit a different decision based on what they saw earlier. A stale version is one that is no longer current. Follow the check that rejects the second action and the transaction that keeps the accepted update together as one unit.

Trace retry identity and current versions through a simulated business decision.

[Company and supply-chain context](../../HARBOUR.md) · [Module 8 business situation](../../reference/harbour-learning-journey.md#module-8)

## Practical activity: Reject a different decision based on a stale case version.


A `try` block attempts an operation. A matching `except` handles the stated failure. An `else` after the handler runs only when no exception occurred; here it can expose an expected refusal that failed to happen.

### Predict and follow the values

Should the second manager silently overwrite the first decision?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from ai_orgdesign.business import CaseStore
with TemporaryDirectory() as directory:
    store=CaseStore(Path(directory)/"case.db");store.seed()
    store.decide("H-17","north","a","manager",1,"return","first")
    try:
        store.decide("H-17","north","b","manager",1,"approve","second")
    except ValueError as error:
        print("Expected conflict:",error)
    else:
        raise AssertionError("A stale decision must fail")
```

### Complete the exercise

**Worked answer.** No. The second action must use a current, permitted state and a fresh review.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A repeated command and a different command based on a stale version are different situations. The transaction keeps the accepted change together as one unit.

## What this means for the business process

When the version check refuses a decision, show what changed and send the case for renewed review. The software can detect a stale basis; the authorised reviewer must decide whether the updated evidence changes the remedy.

For the research behind this design choice, read [Meaningful review needs resources and a practical alternative](../../reference/research/08-governance-and-accountability.md#meaningful-review-needs-resources-and-a-practical-alternative).

## Next lesson

Next put the approval and refusal paths into a complete pilot operating design with clear receiving responsibilities. [Lesson 8.6: Complete a pilot operating design](06-design-lab.md).
