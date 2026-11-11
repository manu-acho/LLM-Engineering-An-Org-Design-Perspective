# Lesson 6.2: Fit a text-routing baseline without leakage

[Download the matching notebook](/downloads/06-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Fit and test a text-routing baseline while keeping held-out cases out of training. The baseline gives Harbour a fair comparison before it funds a more elaborate model.

## Business context: Harbour

A routing baseline is a simple reference system that a more complex one must beat. Keep some messages aside to check the result. If a word from those messages helps build the vocabulary during training, the check is no longer independent. In the lab, look for where the vocabulary is learned and where the held-out messages are first used.

Prepare messages and labels without hiding missing information or changing the intended recipient.

[Company and supply-chain context](../../HARBOUR.md) · [Module 6 business situation](../../reference/harbour-learning-journey.md#module-6)

## Practical activity: Fit preprocessing on training data and inspect predictions.


### Predict and follow the values

Which component learns the vocabulary: CountVectorizer or the classifier?

```python
from ai_orgdesign.labs.m06 import fit_baseline, TEST
model = fit_baseline()
predictions = model.predict([text for text, label in TEST]).tolist()
print(list(zip(TEST, predictions)))
print(model.classes_.tolist())
```

### Complete the exercise

**Worked answer.** CountVectorizer establishes the text columns; the classifier learns category relationships using them.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

The vectorizer learns text columns from training examples. The classifier learns how those columns relate to labels. Evaluation applies the fitted steps to examples set aside for checking.

## What this means for the business process

Retain the split and fitted preprocessing for each comparison. Agree a simple baseline and compare the same cases, so an apparent improvement cannot come from changing the test or learning from it in advance.

For the research behind this design choice, read [Benefits need a population and a comparison](../../reference/research/04-implementation.md#benefits-need-a-population-and-a-comparison).

## Next lesson

Next inspect the meaning of the labels themselves and ask whether past routing reflects the work Harbour wants today. [Lesson 6.3: Historical labels contain an operating model](03-business-and-organisation.md).
