# Lesson 2.2: Follow a conversation through a validated tool

[Download the matching notebook](/downloads/02-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Trace an allowed lookup through validation before using a model.

A tool is a named application capability. A model can request a tool, but application code checks its name, arguments and scope before execution.



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

A tenant names the caller's authorised organisational scope. This exercise uses north and south as regions. It is an application parameter supplied from trusted identity, not a role a model can grant itself.

### Predict and follow the values

What reported quantity should the allowed lookup return?

```python
from ai_orgdesign.agent_loop import execute
record = execute("lookup_case", {"case_id":"H-17"}, "north")
print(record)
assert record["reported"] == 10
```

Ten is the customer report, while actual receipt remains unknown.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

```python
if RUN_LIVE:
    from ai_orgdesign.agent_loop import investigate
    result = investigate(gateway, "Read H-17 and explain what the record establishes.")
    print(result)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

Write the prediction before consulting the worked answer: What reported quantity should the allowed lookup return?

**Worked answer.** Ten is the customer report, while actual receipt remains unknown.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
