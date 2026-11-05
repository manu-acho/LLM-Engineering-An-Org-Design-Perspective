# Lesson 8.2: Record a simulated decision and safe retry

[Download the matching notebook](/downloads/08-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Commit a versioned simulated decision exactly once in the local database.



A `with` block manages a resource lifetime. The indented operations run while the resource is open; cleanup follows when the block exits.

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

Version two. The identical retry retrieves the first result rather than adding another decision.

### Complete the exercise

Write the prediction before consulting the worked answer: Which version should the committed result contain?

**Worked answer.** Version two. The identical retry retrieves the first result rather than adding another decision.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
