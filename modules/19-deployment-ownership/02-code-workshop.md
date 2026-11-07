# Lesson 19.2: Exercise authenticated HTTP routes

[Download the matching notebook](/downloads/19-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Inspect authentication, scoped reads and versioned simulated decisions.

[Company and supply-chain context](../../HARBOUR.md) · [Module 19 business situation](../../reference/harbour-learning-journey.md#module-19)

## Practical activity: Authenticate a local request before reading case state.





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

Which status does the unauthenticated read receive?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from fastapi.testclient import TestClient
from ai_orgdesign.labs.m19 import create_app
token="fictional-notebook-token"
with TemporaryDirectory() as directory:
    app=create_app(Path(directory)/"api.db",{token:{"id":"reviewer","role":"manager","tenant":"north"}})
    with TestClient(app) as client:
        assert client.get("/cases/H-17").status_code==401
        response=client.get("/cases/H-17",headers={"x-course-token":token})
        response.raise_for_status()
        print(response.json())
```

401. The token in this cell is an explicit fictional fixture, not a credential for a real service.

### Complete the exercise

Write the prediction before consulting the worked answer: Which status does the unauthenticated read receive?

**Worked answer.** 401. The token in this cell is an explicit fictional fixture, not a credential for a real service.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
