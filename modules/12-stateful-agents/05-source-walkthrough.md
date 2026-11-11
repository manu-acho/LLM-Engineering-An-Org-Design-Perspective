# Lesson 12.5: Trace current versions through a delayed decision

[Download the matching notebook](/downloads/12-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Trace saved state and current versions through a delayed review. Learn which checks must be run again before Harbour can rely on a previous decision.

## Business context: Harbour

The policy or case may change while a draft waits for review. Follow the checkpoint loaded by the second process and distinguish what it restores from what must be checked again. A saved draft shows what was proposed earlier; it does not guarantee that the proposal is still valid.

Reopen saved state from another process and distinguish graph state from the business record.

[Company and supply-chain context](../../HARBOUR.md) · [Module 12 business situation](../../reference/harbour-learning-journey.md#module-12)

## Practical activity: Reopen an actual graph checkpoint from a separate process.


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

Does inspecting a saved checkpoint need to rerun the model?

```python
from pathlib import Path
from uuid import uuid4
review_path=ROOT/"outputs"/("restart-"+uuid4().hex+".db")
review_path.parent.mkdir(exist_ok=True)
print("The live cell prepares state, then a child Python process reads it without an API call.")
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.durable_review import start
    import subprocess,sys
    start(review_path,gateway)
    script="from ai_orgdesign.durable_review import inspect_pending; print(inspect_pending("+repr(str(review_path))+"))"
    completed=subprocess.run([sys.executable,"-c",script],capture_output=True,text=True,check=True)
    print(completed.stdout)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. Reading preserved state should not repeat the preparation call.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A separate process can read a checkpoint without repeating preparation. Restored information describes the earlier proposal and may need renewed validation.

## What this means for the business process

At review, compare the saved proposal with current case and policy information. Send material changes back for review with the reason visible, so the authorised decision rests on current premises.

For the research behind this design choice, read [Decision premises](../../reference/research/03-decisions.md#decision-premises).

## Next lesson

The next lesson uses these checks to design a review service that can handle ordinary workload and exceptions. [Lesson 12.6: Design review as a service with capacity and discretion](06-design-lab.md).
