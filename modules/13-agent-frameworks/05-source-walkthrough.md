# Lesson 13.5: Compare runtime outputs and failure boundaries

[Download the matching notebook](/downloads/13-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Compare two runtime outputs on stable facts and inspect where each can fail. This helps Harbour judge whether implementations can substitute for one another.

## Business context: Harbour

Run the two versions on the same facts. Compare the recorded and reported quantities separately from wording, then see what each version returns if an input is missing. A runtime is the machinery that carries out the defined work; similar successful output does not show that the runtimes handle failure the same way.

Compare stable factual fields across frameworks without demanding identical prose.

[Company and supply-chain context](../../HARBOUR.md) · [Module 13 business situation](../../reference/harbour-learning-journey.md#module-13)

## Practical activity: Compare two actual runtimes on stable factual fields.

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

Must independently generated summaries be identical strings?

```python
fields=["case_id","ordered","reported","receipt_status","permitted_output"]
print("Fields compared:",fields)
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.frameworks import langgraph_run,agents_sdk_run
    a=langgraph_run(gateway)
    b=await agents_sdk_run(gateway)
    print({field:(a["brief"][field],b["brief"][field]) for field in fields})
    assert all(a["brief"][field]==b["brief"][field] for field in fields)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. Compare the declared contract and evaluate meaning; string equality is not a general semantic test.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Wording can differ while required facts agree. The comparison still needs declared rules for missing inputs, incomplete results and invalid facts.

## What this means for the business process

Accept a replacement only after testing both the factual contribution and the way failure reaches its receiver. A common success response does not establish that both services support the same recovery work.

For the research behind this design choice, read [Infrastructure is a relationship with organised work](../../reference/research/07-infrastructure-and-standards.md#infrastructure-is-a-relationship-with-organised-work).

## Next lesson

Next specify who owns the shared meanings and how several teams can maintain them together. [Lesson 13.6: Design interoperability across teams, meanings and maintenance](06-design-lab.md).
