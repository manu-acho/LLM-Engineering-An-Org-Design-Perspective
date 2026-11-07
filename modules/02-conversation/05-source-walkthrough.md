# Lesson 2.5: Trace call identity, scope and incremental output

[Download the matching notebook](/downloads/02-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Inspect whether the returned object is an answer or a request to fetch evidence before treating the lookup as performed.

[Company and supply-chain context](../../HARBOUR.md) · [Module 2 business situation](../../reference/harbour-learning-journey.md#module-2)

## Practical activity: Inspect the actual response object before hiding it behind a helper.

The SDK returns an object with named attributes such as status and output. A function_call is an output item requesting an operation; it is not a receipt proving the operation ran.



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

May the lookup accept an extra role field under this schema?

```python
from ai_orgdesign.agent_loop import TOOLS
print(TOOLS[0]["name"])
print(TOOLS[0]["parameters"])
assert TOOLS[0]["parameters"]["additionalProperties"] is False
```

No. The tool schema permits case_id only; the application still performs its own permission check.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

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

Write the prediction before consulting the worked answer: May the lookup accept an extra role field under this schema?

**Worked answer.** No. The tool schema permits case_id only; the application still performs its own permission check.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
