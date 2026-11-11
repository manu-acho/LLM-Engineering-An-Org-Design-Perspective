# Lesson 8.2: Record a simulated decision and safe retry

[Download the matching notebook](/downloads/08-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

If an adviser clicks twice after a slow response, Harbour should not record two decisions. A retry is a repeated attempt after an uncertain result. In the local simulation, follow the identifier that tells the program it has already handled that command, and distinguish it from the version number used to tell whether the case has changed.

Inspect the case state and evidence needed before a contribution can enter review.

[Company and supply-chain context](../../HARBOUR.md) · [Module 8 business situation](../../reference/harbour-learning-journey.md#module-8)

## Practical activity: Commit a versioned simulated decision exactly once in the local database.


A `with` block manages a resource lifetime. The indented operations run while the resource is open; cleanup follows when the block exits.

### Predict and follow the values

Which version should the committed result contain?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from ai_orgdesign.business import CaseStore
with TemporaryDirectory() as directory:
    store = CaseStore(Path(directory)/"case.db")
    store.seed()
    first = store.decide("H-17","north","reviewer","manager",1,"return","one-command")
    retry = store.decide("H-17","north","reviewer","manager",1,"return","one-command")
    assert first == retry
    print(first)
```

### Complete the exercise

**Worked answer.** Version two. The identical retry retrieves the first result rather than adding another decision.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
