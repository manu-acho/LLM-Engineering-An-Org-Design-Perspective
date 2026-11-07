# Lesson 20.5: Trace comparable evidence and release conditions

[Download the matching notebook](/downloads/20-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Trace proposal, promotion and rollback without treating a candidate as already in use.

[Company and supply-chain context](../../HARBOUR.md) · [Module 20 business situation](../../reference/harbour-learning-journey.md#module-20)

## Practical activity: Keep a rollback target without rewriting immutable versions.





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

Does rollback unsend a customer message already delivered?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from ai_orgdesign.governance import Versions
with TemporaryDirectory() as directory:
    registry=Versions(Path(directory)/"versions.json");registry.propose("candidate","New wording")
    report={"n":2,"dataset_hash":"same","accuracy":1.,"unsafe":0,"cost":10,"cost_unit":"tokens"}
    registry.promote("candidate",report,report,human_approved=True)
    assert registry.read()["current"]=="candidate"
    print("Rollback target selected:",registry.rollback(human_approved=True))
```

No. It changes the selected configuration; external consequences require reconciliation.

### Complete the exercise

Write the prediction before consulting the worked answer: Does rollback unsend a customer message already delivered?

**Worked answer.** No. It changes the selected configuration; external consequences require reconciliation.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
