# Lesson 9.2: Run a bounded investigation loop

[Download the matching notebook](/downloads/09-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Follow a model-selected read through an investigation loop and identify what can make it stop. Learn to recognise the difference between a proposed tool and an available operation.

## Business context: Harbour

Start with the question about H-17 and write down what counts as enough evidence for a brief. In a bounded loop, the application limits what the model may do and how long it can keep trying. Follow one request from the model to a read-only lookup and back. Read-only access allows inspection of a record without changing it.

Trace actual model-proposed lookups through scope checks, tool execution and observations.

[Company and supply-chain context](../../HARBOUR.md) · [Module 9 business situation](../../reference/harbour-learning-journey.md#module-9)

## Practical activity: Let a live model choose read-only investigation steps.


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

Can a model execute approve_payment through this registry?

```python
from ai_orgdesign.agent_loop import TOOLS
print("Permitted capabilities:",[tool["name"] for tool in TOOLS])
assert "approve_payment" not in [tool["name"] for tool in TOOLS]
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.agent_loop import investigate
    result = investigate(gateway,"Investigate H-17. Read the case and current policy, then state unresolved facts.")
    print(result["text"])
    print(result["trace"])
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. It is not an exposed capability; a generated name does not create one.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A requested tool name has to match an exposed capability. The application checks the request, returns the result as context and can stop before an investigation is complete.

## What this means for the business process

Agree the evidence that makes a draft usable and name who receives the case if the agent cannot obtain it. A short allowed run can produce useful information while leaving the investigation with someone to continue it.

For the research behind this design choice, read [Four questions for a usable contribution](../../reference/research/02-coordination.md#four-questions-for-a-usable-contribution).

## Next lesson

Next decide what work the agent should be allowed to take on at the service's first point of contact. [Lesson 9.3: Design the work before delegating the next step](03-business-and-organisation.md).
