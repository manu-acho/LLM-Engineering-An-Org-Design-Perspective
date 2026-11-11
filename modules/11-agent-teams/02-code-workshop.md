# Lesson 11.2: Schedule tasks through their dependencies

[Download the matching notebook](/downloads/11-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Follow a task schedule and identify which work must wait for a prerequisite. This helps Harbour distinguish avoidable waiting from necessary sequencing.

## Business context: Harbour

A task that needs two records cannot be completed before both records are available. A scheduler chooses which work can start based on dependencies and available capacity. In the lab, identify the tasks that can start immediately and the result that has to wait. Compare the planned order with what the run actually does.

Run a model-backed specialist team and inspect what the coordinator receives.

[Company and supply-chain context](../../HARBOUR.md) · [Module 11 business situation](../../reference/harbour-learning-journey.md#module-11)

## Practical activity: Prepare the sequential comparison before running a team.

 An asynchronous operation can suspend while compatible work proceeds. The notebook uses await to obtain its result; this is different from a business acceptance acknowledgement.


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

Does a sequential arrangement allow the coordinator to run before policy returns?

```python
sequence=["evidence","policy","coordination"]
print("Sequential model contributions:",sequence)
assert sequence[-1] == "coordination"
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import team
    result = await team(gateway,case_id="H-19",parallel=False)
    print(result)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** Not under this declared dependency.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

The scheduler uses declared dependencies to decide when a task can start. A dependent draft must wait for its inputs even when other work can overlap.

## What this means for the business process

Make the waiting reason visible to the person handling the case. If a prerequisite repeatedly blocks a draft, investigate the source or receiving capacity before adding more workers to prepare drafts.

For the research behind this design choice, read [Information demand and capacity](../../reference/research/01-organisation-design.md#information-demand-and-capacity).

## Next lesson

Next examine why correct software sequencing still leaves questions about how people integrate the results. [Lesson 11.3: An agent team needs integration, not just role names](03-business-and-organisation.md).
