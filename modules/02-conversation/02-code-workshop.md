# Lesson 2.2: Follow a conversation through a validated tool

[Download the matching notebook](/downloads/02-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Think of a tool as a named operation the application can perform, such as looking up case H-17. The request names the operation and its input, the case identifier. The application also checks which region the caller may access. In the first code block that reads the case, follow those three inputs to the returned record. Ten is the quantity the customer reported. A successful lookup confirms what the record contains, not how many boxes arrived.

A lookup should expose only the case allowed by the application’s trusted regional scope.

[Company and supply-chain context](../../HARBOUR.md) · [Module 2 business situation](../../reference/harbour-learning-journey.md#module-2)

## Practical activity: Trace an allowed lookup through validation before using a model.

A tool is a named application capability. A model can request a tool, but application code checks its name, arguments and scope before execution.


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

A tenant names the caller's authorised organisational scope. This exercise uses north and south as regions. It is an application parameter supplied from trusted identity, not a role a model can grant itself.

### Predict and follow the values

What reported quantity should the allowed lookup return?

```python
from ai_orgdesign.agent_loop import execute
record = execute("lookup_case", {"case_id":"H-17"}, "north")
print(record)
assert record["reported"] == 10
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

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

**Worked answer.** Ten is the customer report, while actual receipt remains unknown.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
