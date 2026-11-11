# Lesson 6.5: Inspect fitted vocabulary and ambiguous predictions

[Download the matching notebook](/downloads/06-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Check that a word found only in test data stays outside the fitted vocabulary. Use an uncertain prediction to identify where Harbour needs an exception path.

## Business context: Harbour

Imagine a held-out message contains a word the training messages never used. A fitted vocabulary is the list of words the program learned to represent from its training examples. In the lab, check that the new word stays outside that list. Then compare the uncertain prediction with the original message instead of treating the selected queue as self-explanatory.

Inspect how preparation, fitting and evaluation stay separate in the classifier implementation.

[Company and supply-chain context](../../HARBOUR.md) · [Module 6 business situation](../../reference/harbour-learning-journey.md#module-6)

## Practical activity: Keep a test-only word outside the fitted vocabulary.


### Predict and follow the values

Should transform add the test-only word to the learned vocabulary?

```python
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer().fit(["invoice tax", "delivery missing"])
before = dict(vectorizer.vocabulary_)
encoded = vectorizer.transform(["secretzzzz delivery"])
print(before, encoded.toarray())
assert "secretzzzz" not in vectorizer.vocabulary_
```

### Complete the exercise

**Worked answer.** No. Transform applies the existing mapping. Fitting again would change the preprocessing experiment.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Transforming text applies the existing vocabulary. Refitting would change the comparison. A selected label may still hide ambiguity in the source message.

## What this means for the business process

Keep a route for cases the fitted categories handle poorly. Let the receiving team flag recurring exceptions and review whether they need new examples, a revised label or a different allocation rule.

For the research behind this design choice, read [Variation is a question, not a verdict](../../reference/research/05-routines.md#variation-is-a-question-not-a-verdict).

## Next lesson

Next define that allocation rule clearly enough for two people to label the same difficult request consistently. [Lesson 6.6: Redesign a routing task before learning its labels](06-design-lab.md).
