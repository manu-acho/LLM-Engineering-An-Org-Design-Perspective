# Lesson 15.2: Turn requirements into executable acceptance cases

[Download the matching notebook](/downloads/15-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Write acceptance examples that distinguish a useful contribution from a persuasive but unsupported one.

[Company and supply-chain context](../../HARBOUR.md) · [Module 15 business situation](../../reference/harbour-learning-journey.md#module-15)

## Practical activity: Specify acceptance cases before generating implementation code.





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

Which route is expected for equal quantities with damaged goods?

```python
from ai_orgdesign.code_generation import acceptance,compile_routing
code='def route_case(case):\n    if case["reported"] is None:\n        return "needs_evidence"\n    if case["category"] == "invoice":\n        return "finance"\n    if case["category"] == "damage":\n        return "review"\n    if case["ordered"] != case["reported"]:\n        return "investigate"\n    return "review"'
checks=acceptance(compile_routing(code))
print(checks)
assert all(row["passed"] for row in checks)
```

review. Agreement in quantity does not resolve a damage report.

### Complete the exercise

Write the prediction before consulting the worked answer: Which route is expected for equal quantities with damaged goods?

**Worked answer.** review. Agreement in quantity does not resolve a damage report.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
