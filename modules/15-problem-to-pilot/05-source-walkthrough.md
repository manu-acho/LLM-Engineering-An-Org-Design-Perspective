# Lesson 15.5: Trace scope, evidence and discrepancy rules

[Download the matching notebook](/downloads/15-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Inspect code proposed by a model and run the acceptance cases. Learn why understanding the code's allowed operations and checking its behaviour are separate tasks.

## Business context: Harbour

A model can propose code that subtracts two quantities. The application still needs to establish that both are present and preserve where each came from. In the lab, compare the proposed code with each acceptance case before running it. A function that handles twelve and ten can still fail when one number is missing.

Inspect and constrain model-generated routing code before relying on its behaviour.

[Company and supply-chain context](../../HARBOUR.md) · [Module 15 business situation](../../reference/harbour-learning-journey.md#module-15)

## Practical activity: Ask a live model for a small function, inspect it and run acceptance cases.


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

Should generated code be accepted just because it parses?

```python
from ai_orgdesign.code_generation import SPEC
print(SPEC)
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.code_generation import propose
    proposal=propose(gateway)
    print(proposal["code"])
    print(proposal["checks"])
    assert all(row["passed"] for row in proposal["checks"])
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. Parsing, allowed operations and behavioural acceptance are separate checks.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Code can be readable and still fail on a missing value. Parsing the proposal, restricting what it may do and testing the result each check something different.

## What this means for the business process

Assign engineering the execution checks and give the process owner responsibility for approving the expected cases. A generated change should pass both before it can affect the work.

For the research behind this design choice, read [Select controls for the work that can actually be assessed](../../reference/research/08-governance-and-accountability.md#select-controls-for-the-work-that-can-actually-be-assessed).

## Next lesson

Next combine those technical checks with evidence about receiving capacity and business outcomes to make a pilot decision. [Lesson 15.6: Complete a defensible service decision](06-design-lab.md).
