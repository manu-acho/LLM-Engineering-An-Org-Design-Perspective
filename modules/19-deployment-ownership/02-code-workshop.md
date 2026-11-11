# Lesson 19.2: Exercise authenticated HTTP routes

[Download the matching notebook](/downloads/19-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Follow an authenticated local request to the permitted route. Use the returned status to distinguish an identity failure from the result of reading a case.

## Business context: Harbour

HTTP is a set of rules for exchanging requests and responses. A route combines the kind of request with a path, such as a request to read a case. In the local lab, find the authentication check that happens before the case is returned. Compare the response for a valid caller with what the service sends when it cannot establish identity.

Inspect authentication, scoped reads and versioned simulated decisions.

[Company and supply-chain context](../../HARBOUR.md) · [Module 19 business situation](../../reference/harbour-learning-journey.md#module-19)

## Practical activity: Authenticate a local request before reading case state.


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

### Complete the exercise

**Worked answer.** 401. The token in this cell is an explicit fictional fixture, not a credential for a real service.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

An HTTP route combines a request method and path. The service checks the request before returning protected case state.

## What this means for the business process

Make rejected authentication actionable for support without disclosing case data. Define how advisers regain legitimate access and continue urgent work if that route is unavailable.

For the research behind this design choice, read [Select controls for the work that can actually be assessed](../../reference/research/08-governance-and-accountability.md#select-controls-for-the-work-that-can-actually-be-assessed).

## Next lesson

Next decide who handles faults after release and how they distinguish a running process from a service ready to handle cases. [Lesson 19.3: Design the work, responsibility and learning](03-business-and-organisation.md).
