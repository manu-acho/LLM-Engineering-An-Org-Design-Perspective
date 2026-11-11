# Lesson 18.5: Test scope denial and policy freshness

[Download the matching notebook](/downloads/18-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

A case can be accessible while the policy used to draft a decision has since changed. Follow one denied lookup and one decision refused for using an older policy. Both checks can prevent action, but they answer different questions and may need different remedies.

Trace policy selection, validation and failure handling through the actual implementation.

[Company and supply-chain context](../../HARBOUR.md) · [Module 18 business situation](../../reference/harbour-learning-journey.md#module-18)

## Practical activity: Reject a decision made against an obsolete policy version.


### Predict and follow the values

Which policy version does the seeded case require?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from ai_orgdesign.business import CaseStore
with TemporaryDirectory() as directory:
    store=CaseStore(Path(directory)/"case.db");store.seed()
    try:
        store.decide("H-17","north","reviewer","manager",1,"return","stale",policy_version=1)
    except ValueError:
        print("Stale policy rejected before commit")
    else:
        raise AssertionError("Stale policy accepted")
```

### Complete the exercise

**Worked answer.** Two. The version check detects a mismatch; an organisational policy owner must still decide transition rules.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

### Programming practice

Write current(submitted, required) to reject a stale policy version.

Start with the placeholder in the notebook, then compare with this worked solution. The contrasting checks are part of understanding the contract.

```python
def current(submitted, required):
    return submitted == required

assert current(2,2) is True
assert current(1,2) is False
```


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
