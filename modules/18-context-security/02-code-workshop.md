# Lesson 18.2: Assemble context inside an access boundary

[Download the matching notebook](/downloads/18-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Trace where a wrong-region case is denied before the application assembles a prompt. Learn which inputs have to come from a trusted identity check.

## Business context: Harbour

The safest point to protect a record the model does not need is before building the request. In the lab, inspect how the application rejects a case outside the caller's region before it gathers material for the prompt. Compare a permitted request and a denied request at that boundary rather than looking only at the reply.

Inspect trusted regional scope and permitted case reads.

[Company and supply-chain context](../../HARBOUR.md) · [Module 18 business situation](../../reference/harbour-learning-journey.md#module-18)

## Practical activity: Deny a wrong-region case before preparing a prompt.


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

### Complete the exercise

**Worked answer.** No. Authentication and resource-specific authorisation are different checks.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A caller can be authenticated and still lack access to a given case. The application controls what reaches the model.

## What this means for the business process

Test a denied request at the evidence boundary. Give the access owner a way to resolve legitimate denials without widening every caller's scope or exposing the case to the model.

For the research behind this design choice, read [Permission and authority](../../reference/research/03-decisions.md#permission-and-authority).

## Next lesson

Next examine who can change the definitions and policies that even properly scoped requests rely on. [Lesson 18.3: Design the work, responsibility and learning](03-business-and-organisation.md).
