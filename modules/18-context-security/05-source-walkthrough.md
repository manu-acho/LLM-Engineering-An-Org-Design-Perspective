# Lesson 18.5: Test scope denial and policy freshness

[Download the matching notebook](/downloads/18-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Reject a decision made against an obsolete policy version.





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

Two. The version check detects a mismatch; an organisational policy owner must still decide transition rules.

### Complete the exercise

Write the prediction before consulting the worked answer: Which policy version does the seeded case require?

**Worked answer.** Two. The version check detects a mismatch; an organisational policy owner must still decide transition rules.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

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
