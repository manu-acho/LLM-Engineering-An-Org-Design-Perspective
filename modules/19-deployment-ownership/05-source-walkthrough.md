# Lesson 19.5: Start and inspect the local case service

[Download the matching notebook](/downloads/19-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Start the local service and follow a case through three distinct requests: draft, read and review. Inspect the response at each stage and locate where it checks identity. Reading the draft confirms what is stored; reviewing is a separate request with a different effect.

Follow an actual generated draft through local HTTP persistence and later retrieval.

[Company and supply-chain context](../../HARBOUR.md) · [Module 19 business situation](../../reference/harbour-learning-journey.md#module-19)

## Practical activity: Run the full authenticated draft-read-review HTTP journey.


The notebook is the easiest way to run this activity. Its first cell loads the course settings. `ROOT` records where the course files are, and `RUN_LIVE` records whether the optional provider call is enabled. The local steps can be read with live mode off. When running the snippets outside the notebook, use this setup once from a prepared checkout:

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

Does the static reading website run the Python application?

```python
print("Start the local server separately with: uv run --locked python -m ai_orgdesign.serve")
print("Its default endpoint is http://127.0.0.1:4192; Ctrl+C stops its Terminal process.")
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from fastapi.testclient import TestClient
    from ai_orgdesign.labs.m19 import create_app
    token="fictional-live-http-token"
    with TemporaryDirectory() as directory:
        app=create_app(Path(directory)/"service.db",{token:{"id":"reviewer","role":"manager","tenant":"north"}},gateway=gateway)
        with TestClient(app) as client:
            headers={"x-course-token":token}
            prepared=client.post("/cases/H-17/drafts",headers=headers)
            prepared.raise_for_status()
            saved=client.get("/cases/H-17/drafts",headers=headers)
            saved.raise_for_status()
            print(saved.json())
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. The course reader and the Python service are separate processes.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
