# Lesson 4.2: Compare equal accuracy with unequal consequences

[Download the matching notebook](/downloads/04-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Compare two results with the same accuracy and explain why one may cause greater loss. Harbour can then make explicit which routing mistakes it needs to avoid most.

## Business context: Harbour

Two routing systems can each send nine out of ten requests to the right queue. One wrong route delays an ordinary query; the other leaves an urgent complaint unattended. Accuracy counts how often an answer matches the expected answer. In the lab, compare that count with the consequences assigned to the errors, keeping the two results separate.

Compare errors with different business consequences, including unnecessary review and a discrepancy overlooked.

[Company and supply-chain context](../../HARBOUR.md) · [Module 4 business situation](../../reference/harbour-learning-journey.md#module-4)

## Practical activity: Compare identical accuracy with different consequences.


### Predict and follow the values

Which prediction has the larger loss under the supplied cost rule: a or b?

```python
from ai_orgdesign.labs.m04 import score
a = score(["review","clear"],["clear","clear"])
b = score(["review","clear"],["review","review"])
print(a, b)
assert a["accuracy"] == b["accuracy"]
assert a["illustrative_loss"] > b["illustrative_loss"]
```

### Complete the exercise

**Worked answer.** a has the larger loss because it clears a case requiring review. The penalty remains an explicit assumption.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Accuracy counts correct choices. The loss rule attaches stated penalties to particular mistakes, so an unsafe clearance can matter more than an unnecessary review.

## What this means for the business process

Ask operations and customer service to agree how to weigh missed reviews against avoidable referrals. Put those weights beside the results because they express a choice about whose delay or risk the service should prioritise.

For the research behind this design choice, read [Select controls for the work that can actually be assessed](../../reference/research/08-governance-and-accountability.md#select-controls-for-the-work-that-can-actually-be-assessed).

## Next lesson

The next lesson considers what happens when such a measure is used to manage people's work. [Lesson 4.3: Metrics are part of the design of work](03-business-and-organisation.md).
