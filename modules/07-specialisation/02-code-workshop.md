# Lesson 7.2: Train and reconstruct a low-rank update

[Download the matching notebook](/downloads/07-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Train and reconstruct the small low-rank update. Learn what a successful reload can establish before relying on the resulting model in Harbour's workflow.

## Business context: Harbour

Imagine a large table of numbers that turns an input into an output. An adapter can add a change calculated from two smaller tables. Low rank restricts the form of the change so fewer values need to be fitted. In the lab, follow how the two tables combine and compare the output from using them separately with the output after combining their change into the original transformation.

Inspect a low-rank update and distinguish trainable parameters from the fixed base model.

[Company and supply-chain context](../../HARBOUR.md) · [Module 7 business situation](../../reference/harbour-learning-journey.md#module-7)

## Practical activity: Train and reconstruct the transparent linear update.


### Predict and follow the values

Does reload equality test reconstruction or business usefulness?

```python
from ai_orgdesign.labs.m07 import demo
result = demo()
print(result)
assert result["base_unchanged"] and result["reload_equal"]
assert result["loss_after"] < result["loss_before"]
```

### Complete the exercise

**Worked answer.** It tests reconstruction of the saved model state. Business usefulness needs an appropriate task comparison.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

Two smaller sets of numbers represent a restricted change to the original transformation. Reconstructing the same output checks that the saved change can be used again.

## What this means for the business process

Require a repeatable reconstruction check before handing a trained component to the team that will operate it. Evaluate the work outcome separately with relevant cases and the current baseline.

For the research behind this design choice, read [An evidence path without skipped steps](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).

## Next lesson

Next examine who can question the categories that an adaptation has learned, even when its saved state is sound. [Lesson 7.3: A specialised model still needs people to question its categories](03-business-and-organisation.md).
