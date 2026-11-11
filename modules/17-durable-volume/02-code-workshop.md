# Lesson 17.2: Limit concurrent work and recover an expired lease

[Download the matching notebook](/downloads/17-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Run a bounded batch and trace how another worker can claim expired work. This shows what Harbour can expect from local limits and what it must test at a wider scale.

## Business context: Harbour

Picture two advisers able to handle one case each. Starting a third job requires a place to wait. In the lab, follow the limit on simultaneous work, then inspect what happens when a worker's temporary claim expires. A replacement worker should be able to proceed without letting the former worker finish the same claim.

Run bounded concurrent preparation and inspect each case’s independent outcome.

[Company and supply-chain context](../../HARBOUR.md) · [Module 17 business situation](../../reference/harbour-learning-journey.md#module-17)

## Practical activity: Bound local concurrency before substituting actual model work.


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

What is the maximum permitted local overlap?

```python
from ai_orgdesign.labs.m17 import bounded_work
result=await bounded_work(["a","b","c"],limit=2)
print(result)
assert result["peak"]<=2
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import batch
    results=await batch(gateway,["H-17","H-19","H-20"],concurrency=2)
    print(results)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** Two. This semaphore does not by itself control separate worker processes.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A semaphore limits simultaneous tasks in one process. A lease governs a temporary claim. Those mechanisms address different problems.

## What this means for the business process

Use a concurrency limit to protect downstream capacity and a claim rule to protect ownership. Test each in the intended deployment, and give someone responsibility for jobs that repeatedly expire.

For the research behind this design choice, read [Fit is a relationship among choices](../../reference/research/01-organisation-design.md#fit-is-a-relationship-among-choices).

## Next lesson

Next examine how priority rules and human review capacity determine which cases wait after the application prepares them. [Lesson 17.3: Design the work, responsibility and learning](03-business-and-organisation.md).
