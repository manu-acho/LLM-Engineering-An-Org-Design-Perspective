# Lesson 15.2: Turn requirements into executable acceptance cases

[Download the matching notebook](/downloads/15-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Write an example input, expected behaviour and refusal condition before generating code. This makes Harbour's requirements testable in situations where arithmetic alone is insufficient.

## Business context: Harbour

Before asking a model to write code, describe one input, one expected result and one result that must be refused. An acceptance case turns that description into a check the implementation can run. If the dispatch number is missing, decide whether the program should refuse to calculate or show an unresolved difference before looking at the code.

Write acceptance examples that distinguish a useful contribution from a persuasive but unsupported one.

[Company and supply-chain context](../../HARBOUR.md) · [Module 15 business situation](../../reference/harbour-learning-journey.md#module-15)

## Practical activity: Specify acceptance cases before generating implementation code.


### Predict and follow the values

Which route is expected for equal quantities with damaged goods?

```python
from ai_orgdesign.code_generation import acceptance,compile_routing
code='def route_case(case):\n    if case["reported"] is None:\n        return "needs_evidence"\n    if case["category"] == "invoice":\n        return "finance"\n    if case["category"] == "damage":\n        return "review"\n    if case["ordered"] != case["reported"]:\n        return "investigate"\n    return "review"'
checks=acceptance(compile_routing(code))
print(checks)
assert all(row["passed"] for row in checks)
```

### Complete the exercise

**Worked answer.** review. Agreement in quantity does not resolve a damage report.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Acceptance cases turn an expectation into a specific check. Equal quantities can coexist with damage that still needs review.

## What this means for the business process

Have the process owner write cases for damage, missing evidence and restricted access. Include what should happen next when a check refuses the work, so the code supports the real exception process.

For the research behind this design choice, read [Programmes and exceptions](../../reference/research/03-decisions.md#programmes-and-exceptions).

## Next lesson

With concrete tests in hand, next use discovery to find where the actual work and its responsibilities differ from the first proposal. [Lesson 15.3: Design the work, responsibility and learning](03-business-and-organisation.md).
