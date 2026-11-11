# Lesson 2.5: Trace call identity, scope and incremental output

[Download the matching notebook](/downloads/02-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Suppose two requests ask for the same case at the same time. The case number identifies the subject of both requests; a call identifier tells the application which request a result belongs to. Inspect that identifier separately from the region and the partial text. A correct identifier does not make a cross-region lookup permissible.

Inspect whether the returned object is an answer or a request to fetch evidence before treating the lookup as performed.

[Company and supply-chain context](../../HARBOUR.md) · [Module 2 business situation](../../reference/harbour-learning-journey.md#module-2)

## Practical activity: Inspect the actual response object before hiding it behind a helper.

The SDK returns an object with named attributes such as status and output. A function_call is an output item requesting an operation; it is not a receipt proving the operation ran.


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

May the lookup accept an extra role field under this schema?

```python
from ai_orgdesign.agent_loop import TOOLS
print(TOOLS[0]["name"])
print(TOOLS[0]["parameters"])
assert TOOLS[0]["parameters"]["additionalProperties"] is False
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    raw, record = gateway.request([{"role":"user","content":"Read case H-17 using the tool."}], instructions="Use lookup_case; do not invent the case facts.", tools=TOOLS)
    print("Status:", raw.status)
    print("Output item types:", [item.type for item in raw.output])
    print(record)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. The tool schema permits case_id only; the application still performs its own permission check.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
