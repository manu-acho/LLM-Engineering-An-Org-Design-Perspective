# Lesson 20.2: Evaluate a candidate against a promotion gate

[Download the matching notebook](/downloads/20-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Compare two versions on the same cases and interpret the promotion gate. Learn how an apparently better average can coexist with an unacceptable failure.

## Business context: Harbour

Run the current and proposed instructions on the same cases. A promotion gate is a set of conditions the candidate must meet before it can be selected. Compare the measured results with those conditions and identify any case that should block release even if the average improves.

Compare actual candidate outputs with a baseline on the same teaching cases.

[Company and supply-chain context](../../HARBOUR.md) · [Module 20 business situation](../../reference/harbour-learning-journey.md#module-20)

## Practical activity: Measure the current and candidate instruction paths on the same cases.


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

Should the comparison use different denominators for the two versions?

```python
from ai_orgdesign.case_data import CONFIRMATION_IDS
print("Teaching confirmation cases:",CONFIRMATION_IDS)
print("The live comparison below uses returned predictions, not supplied accuracy figures.")
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import evaluate
    baseline=evaluate(gateway,["H-23","H-24"],version="unassisted-v1")
    candidate=evaluate(gateway,["H-23","H-24"],version="grounded-v3")
    print("Baseline:",baseline)
    print("Candidate:",candidate)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. Preserve the declared population, reference decisions and resource units.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

The comparison needs the same cases, expected behaviour and resource units. A gate can require a particular safety or quality condition alongside an average improvement.

## What this means for the business process

Agree with the receiving team which failures block a release, such as turning an unverified report into a confirmed claim. Keep the evidence and the decision rule visible to the release owner.

For the research behind this design choice, read [Select controls for the work that can actually be assessed](../../reference/research/08-governance-and-accountability.md#select-controls-for-the-work-that-can-actually-be-assessed).

## Next lesson

Next decide who may challenge the comparison and how a problem should reach the owner who can fix it. [Lesson 20.3: Design the work, responsibility and learning](03-business-and-organisation.md).
