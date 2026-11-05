# Lesson 19.5: Start and inspect the local case service

[Download the matching notebook](/downloads/19-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Run the full authenticated draft-read-review HTTP journey.





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

Does the static reading website run the Python application?

```python
print("Start the local server separately with: uv run --locked python -m ai_orgdesign.serve")
print("Its default endpoint is http://127.0.0.1:4192; Ctrl+C stops its Terminal process.")
```

No. The course reader and the Python service are separate processes.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

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

Write the prediction before consulting the worked answer: Does the static reading website run the Python application?

**Worked answer.** No. The course reader and the Python service are separate processes.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
