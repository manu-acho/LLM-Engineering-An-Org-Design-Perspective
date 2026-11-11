# Lesson 14.2: Expose a narrow case-reading capability

[Download the matching notebook](/downloads/14-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Trace the direct result of a narrow case-reading operation. This helps Harbour check which fields and cases the capability exposes before adding transport.

## Business context: Harbour

Before involving a connection or model, call the local function with one case identifier and inspect what comes back. That isolates what the capability itself does. A transport carries requests and replies between programs; changing the transport should not give the capability access to extra fields or make the operation a write.

Inspect a real local MCP exchange and its returned capability information.

[Company and supply-chain context](../../HARBOUR.md) · [Module 14 business situation](../../reference/harbour-learning-journey.md#module-14)

## Practical activity: Inspect the capability's direct Python result before transport.


### Predict and follow the values

Which tenant is fixed for this local teaching server?

```python
from ai_orgdesign.labs.m14 import read_case
record=read_case("H-17")
print(record)
assert record["tenant"]=="north"
```

### Complete the exercise

**Worked answer.** north. A shared service would need authenticated delegated scope rather than this fixed local configuration.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

The Python operation returns a bounded result. Transport moves requests and replies. In the local example, scope is fixed and visible.

## What this means for the business process

Define the permitted fields and derive the region from authenticated identity when teams share the service. Test a denied read alongside a permitted one so expanding access cannot become an unnoticed side effect of integration.

For the research behind this design choice, read [Permission and authority](../../reference/research/03-decisions.md#permission-and-authority).

## Next lesson

Next decide who will own that capability as several applications start to depend on it. [Lesson 14.3: A reusable agent capability needs a service owner](03-business-and-organisation.md).
