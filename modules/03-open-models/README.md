# Module 3: Open models and inference

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Choosing local inference changes who operates the model, where data travels and which resources are needed. It does not settle whether the output is accurate enough to enter a meeting record or resolve a case.

## Preparation and route

Complete Module 2 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 3.1: What changes when you run a model yourself?](01-concepts.md)
2. [Lesson 3.2: Inspect a real neural forward pass](02-code-workshop.md)
3. [Lesson 3.3: When meeting notes become an organisational record](03-business-and-organisation.md)
4. [Lesson 3.4: Follow numbers through a small language model](04-inside-inference.md)
5. [Lesson 3.5: Load weights, inspect shapes and diagnose inference](05-source-walkthrough.md)
6. [Lesson 3.6: Design the meeting record and its correction process](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m03.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The logits have shape [1, 8]: one sequence and eight candidate tokens. The eight probabilities sum approximately to one. The notebook reports the parameter count and CPU device from the actual model. Neither a fluent sentence nor business knowledge should be expected.

## Completion exercise

Explain why replacing the random model with downloaded pretrained weights changes the source of its behaviour, while leaving the need to inspect context, scope and record ownership.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/06-technology-in-practice.md) for the supporting theory and scholarly references.

## Another explanation

[Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.
