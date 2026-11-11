# Lesson 9.5: Test repeated calls and independent stopping limits

[Download the matching notebook](/downloads/09-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

If the model asks for the same record again, compare what the second request adds. An observation is the result returned after a tool runs. Follow the observations and the stop reason separately. The loop must be able to stop even when the model keeps proposing another step.

Follow the trace to distinguish a proposed lookup from evidence actually obtained.

[Company and supply-chain context](../../HARBOUR.md) · [Module 9 business situation](../../reference/harbour-learning-journey.md#module-9)

## Practical activity: Inspect bounded model execution through returned observations.


A `lambda` is a short function written as an expression. Here it supplies a callback; it does not run until the receiving operation calls it.

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

Which independent bound is still needed when identifiers are always different?

```python
from ai_orgdesign.labs.m09 import run
request = {"kind":"tool","id":"same","name":"lookup_case","arguments":{"case_id":"H-17"}}
result = run(lambda observations:request)
print(result)
assert result["stop"] == "repeated_call"
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    from ai_orgdesign.agent_loop import investigate
    result = investigate(gateway,"Read H-19 and identify what still needs review.",max_rounds=4,max_tools=3)
    for row in result["trace"]:
        print(row)
    print(gateway.ledger())
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** The iteration or request budget still bounds repeated work with new identifiers.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
