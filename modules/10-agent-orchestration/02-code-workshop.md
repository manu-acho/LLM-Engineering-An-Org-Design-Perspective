# Lesson 10.2: Validate and accept a specialist contribution

[Download the matching notebook](/downloads/10-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Check a specialist's result for the requested case, supporting evidence and usability. This shows Harbour how to accept a contribution into a brief.

## Business context: Harbour

A specialist's contribution can arrive in the right form and still be unusable. In the lab, inspect the returned fields, compare the claim with the supplied source, then decide if it can enter the combined brief. Validation checks particular requirements; name the check that passed before calling the contribution accepted.

Inspect a specialist contribution with its case identity, sources and unresolved questions.

[Company and supply-chain context](../../HARBOUR.md) · [Module 10 business situation](../../reference/harbour-learning-journey.md#module-10)

## Practical activity: Obtain and accept a real specialist contribution.


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

Which case identifier must the specialist preserve?

```python
from ai_orgdesign.case_data import get_case
case = get_case()
print("Permitted evidence sources:",case["source_ids"])
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import specialist
    result = specialist(gateway,case,"evidence")
    print(result)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** H-17. An answer about another case cannot be accepted merely because its schema is valid.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

An output can have the expected fields and still describe the wrong case. Acceptance depends on the contribution satisfying the receiving step's requirements.

## What this means for the business process

Have the coordinator check the case and evidence against the request before accepting the result. Report a rejected contribution to its owner with the failed condition so it can be repaired.

For the research behind this design choice, read [Four questions for a usable contribution](../../reference/research/02-coordination.md#four-questions-for-a-usable-contribution).

## Next lesson

Next take that distinction outside the software and ask what it takes for a person or team to accept responsibility for a case. [Lesson 10.3: A software handoff is not accepted ownership](03-business-and-organisation.md).
