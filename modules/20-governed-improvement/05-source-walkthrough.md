# Lesson 20.5: Trace comparable evidence and release conditions

[Download the matching notebook](/downloads/20-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

If a release turns out to be worse, rollback restores a previously selected version. It should not rewrite what that version was or erase the record of the release. Follow what was measured before promotion and what remains available to restore the service.

Trace proposal, promotion and rollback without treating a candidate as already in use.

[Company and supply-chain context](../../HARBOUR.md) · [Module 20 business situation](../../reference/harbour-learning-journey.md#module-20)

## Practical activity: Keep a rollback target without rewriting immutable versions.


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

### Complete the exercise

**Worked answer.** No. It changes the selected configuration; external consequences require reconciliation.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
