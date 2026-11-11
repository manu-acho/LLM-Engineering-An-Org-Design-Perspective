# Lesson 5.5: Follow filtering, vectorisation and ranking

[Download the matching notebook](/downloads/05-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Follow the route from allowed documents to a generated brief, then check the source and quantity fields. This gives Harbour a way to see where a claim changed.

## Business context: Harbour

A draft that sounds right may still turn a reported quantity into a verified fact. Follow the exercise from the set of documents it may search, to the pieces it finds, to the brief it returns. Check the actual fields for quantities and source labels, even if the prose sounds natural. Matching the expected fields in this example is one check on the draft.

Trace the selected evidence into the actual generated brief and inspect unsupported additions.

[Company and supply-chain context](../../HARBOUR.md) · [Module 5 business situation](../../reference/harbour-learning-journey.md#module-5)

## Practical activity: Retrieve evidence, generate a brief and check its structured facts.


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

What customer-reported quantity must the generated brief preserve?

```python
from ai_orgdesign.case_data import get_case
from ai_orgdesign.investigation import policy_hits
case = get_case()
hits = policy_hits(case)
print({"case":case,"retrieved_policy_ids":[hit["id"] for hit in hits]})
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import draft
    result = draft(gateway)
    print(result["brief"])
    print(result["record"])
    assert result["brief"]["reported"] == 10
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** Ten. Supplying context is only the start; the returned facts and sources still need checking.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Finding and supplying evidence are different from checking the resulting draft. A field can hold the right number but assign it the wrong status.

## What this means for the business process

Before displaying a generated brief as usable, check that each key claim points to a permitted source and preserves whether it was recorded or reported. Route unsupported fields back for investigation instead of making the adviser reverse-engineer the draft.

For the research behind this design choice, read [Worked design: a quantity agreement](../../reference/research/07-infrastructure-and-standards.md#worked-design-a-quantity-agreement).

## Next lesson

Next design the source registry and correction process that keep those checks reliable as records and policies change. [Lesson 5.6: Build an organisational knowledge service](06-design-lab.md).
