# Lesson 18.2: Assemble context inside an access boundary

[Download the matching notebook](/downloads/18-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Practical activity: Deny a wrong-region case before preparing a prompt.





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

Does an authenticated north identity imply access to south?

```python
from ai_orgdesign.case_data import get_case
try:
    get_case("H-18","north")
except PermissionError:
    print("Denied before prompt assembly")
else:
    raise AssertionError("Scope failed")
```

No. Authentication and resource-specific authorisation are different checks.

### Complete the exercise

Write the prediction before consulting the worked answer: Does an authenticated north identity imply access to south?

**Worked answer.** No. Authentication and resource-specific authorisation are different checks.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
