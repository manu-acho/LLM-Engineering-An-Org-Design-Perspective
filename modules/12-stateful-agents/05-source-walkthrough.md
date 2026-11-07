# Lesson 12.5: Trace current versions through a delayed decision

[Download the matching notebook](/downloads/12-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Reopen saved state from another process and distinguish graph state from the business record.

[Company and supply-chain context](../../HARBOUR.md) · [Module 12 business situation](../../reference/harbour-learning-journey.md#module-12)

## Practical activity: Reopen an actual graph checkpoint from a separate process.





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

Does inspecting a saved checkpoint need to rerun the model?

```python
from pathlib import Path
from uuid import uuid4
review_path=ROOT/"outputs"/("restart-"+uuid4().hex+".db")
review_path.parent.mkdir(exist_ok=True)
print("The live cell prepares state, then a child Python process reads it without an API call.")
```

No. Reading preserved state should not repeat the preparation call.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

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

Write the prediction before consulting the worked answer: Does inspecting a saved checkpoint need to rerun the model?

**Worked answer.** No. Reading preserved state should not repeat the preparation call.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
