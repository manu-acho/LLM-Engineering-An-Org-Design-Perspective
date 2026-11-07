# Lesson 4.2: Compare equal accuracy with unequal consequences

[Download the matching notebook](/downloads/04-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Compare errors with different business consequences, including unnecessary review and a discrepancy overlooked.

[Company and supply-chain context](../../HARBOUR.md) · [Module 4 business situation](../../reference/harbour-learning-journey.md#module-4)

## Practical activity: Compare identical accuracy with different consequences.





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

Which prediction has the larger loss under the supplied cost rule: a or b?

```python
from ai_orgdesign.labs.m04 import score
a = score(["review","clear"],["clear","clear"])
b = score(["review","clear"],["review","review"])
print(a, b)
assert a["accuracy"] == b["accuracy"]
assert a["illustrative_loss"] > b["illustrative_loss"]
```

a has the larger loss because it clears a case requiring review. The penalty remains an explicit assumption.

### Complete the exercise

Write the prediction before consulting the worked answer: Which prediction has the larger loss under the supplied cost rule: a or b?

**Worked answer.** a has the larger loss because it clears a case requiring review. The penalty remains an explicit assumption.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
