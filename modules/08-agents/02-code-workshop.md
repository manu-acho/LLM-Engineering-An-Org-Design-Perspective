# Lesson 8.2: Record a simulated decision and safe retry

[Download the matching notebook](/downloads/08-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Trace a decision and its retry through a local database. Harbour needs to know whether an interrupted request already changed a case before asking someone to try again.

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

## What to remember

A repeat of the same command can return its stored result. The case version records which state was reviewed. The exercise checks one local decision.

## What this means for the business process

Give each decision request a stable identity and show the stored outcome to the adviser on retry. For a credit handled in another system, agree how Finance checks that system before retrying an uncertain action.

For the research behind this design choice, read [Documentation and auditing support accountability but do not replace it](../../reference/research/08-governance-and-accountability.md#documentation-and-auditing-support-accountability-but-do-not-replace-it).

## Next lesson

Next put that recording mechanism beside the people, dependencies and acceptance rules needed to operate the workflow. [Lesson 8.3: Designing an operating organisation around the workflow](03-business-and-organisation.md).
