# Lesson 9.5: Test repeated calls and independent stopping limits

[Download the matching notebook](/downloads/09-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Follow the trace to distinguish a proposed lookup from evidence actually obtained.

[Company and supply-chain context](../../HARBOUR.md) · [Module 9 business situation](../../reference/harbour-learning-journey.md#module-9)

## Practical activity: Inspect bounded model execution through returned observations.



A `lambda` is a short function written as an expression. Here it supplies a callback; it does not run until the receiving operation calls it.

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

Which independent bound is still needed when identifiers are always different?

```python
from ai_orgdesign.labs.m09 import run
request = {"kind":"tool","id":"same","name":"lookup_case","arguments":{"case_id":"H-17"}}
result = run(lambda observations:request)
print(result)
assert result["stop"] == "repeated_call"
```

The iteration or request budget still bounds repeated work with new identifiers.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

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

Write the prediction before consulting the worked answer: Which independent bound is still needed when identifiers are always different?

**Worked answer.** The iteration or request budget still bounds repeated work with new identifiers.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
