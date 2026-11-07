# Lesson 6.5: Inspect fitted vocabulary and ambiguous predictions

[Download the matching notebook](/downloads/06-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Inspect how preparation, fitting and evaluation stay separate in the classifier implementation.

[Company and supply-chain context](../../HARBOUR.md) · [Module 6 business situation](../../reference/harbour-learning-journey.md#module-6)

## Practical activity: Keep a test-only word outside the fitted vocabulary.





The exercise code below runs from a prepared course checkout. In the matching notebook, the setup cell already supplies ROOT and RUN_LIVE. If following the code here, run this setup first:

```python
from ai_orgdesign.workspace import project_root, live_mode
ROOT = project_root()
RUN_LIVE = live_mode()
if RUN_LIVE:
    from ai_orgdesign.provider import Gateway
    gateway = Gateway(max_requests=12, max_output_tokens=1000)
print("Live mode:", RUN_LIVE)
```

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

No. Transform applies the existing mapping. Fitting again would change the preprocessing experiment.

### Complete the exercise

Write the prediction before consulting the worked answer: Should transform add the test-only word to the learned vocabulary?

**Worked answer.** No. Transform applies the existing mapping. Fitting again would change the preprocessing experiment.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
