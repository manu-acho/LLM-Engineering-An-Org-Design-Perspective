# Lesson 12.2: Reopen durable work and resume review

[Download the matching notebook](/downloads/12-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

When a reviewer goes home, the program should not need to stay open with the case on screen. Durable storage keeps information after a process stops. In the lab, look for the case identifier, the saved information and the point at which the graph pauses. Those are what connect tomorrow's review to today's draft.

Create an actual durable graph pause after model preparation and inspect the pending review.

[Company and supply-chain context](../../HARBOUR.md) · [Module 12 business situation](../../reference/harbour-learning-journey.md#module-12)

## Practical activity: Pause an actual model-backed graph at a human-review boundary.


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

Should the prepare node authorise the remedy before human review?

```python
from pathlib import Path
from uuid import uuid4
review_path = ROOT / "outputs" / ("review-" + uuid4().hex + ".db")
review_path.parent.mkdir(exist_ok=True)
print("A new local checkpoint path is prepared for this experiment.")
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.durable_review import start, inspect_pending
    pending=start(review_path,gateway)
    print("Interrupt present:","__interrupt__" in pending)
    print(inspect_pending(review_path))
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. The checkpoint preserves a contribution awaiting an explicit decision.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
