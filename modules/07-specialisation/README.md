# Module 7: Model adaptation and specialisation

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Fine-tuning changes numerical parameters, while retrieval changes the supplied evidence. This module exposes a real parameter update on a small enough task that every trained quantity and saved artefact can be inspected.

## Preparation and route

Complete Module 6 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 7.1: What fine-tuning changes, and what it cannot settle](01-concepts.md)
2. [Lesson 7.2: Train and reconstruct a low-rank update](02-code-workshop.md)
3. [Lesson 7.3: A specialised model still needs people to question its categories](03-business-and-organisation.md)
4. [Lesson 7.4: Understand an adapter, a training batch and a loss](04-adaptation-mechanics.md)
5. [Lesson 7.5: Follow gradients, frozen weights and saved state](05-source-walkthrough.md)
6. [Lesson 7.6: Make a specialisation decision and keep categories revisable](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m07.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The final training loss should be substantially below the initial loss. Reloading should reproduce the trained outputs, and the frozen base should equal the identity matrix. The test checks these properties rather than requiring platform-identical final decimal digits. There is no held-out generalisation claim from this four-pair training exercise.

## Completion exercise

Explain why matching the saved outputs proves neither successful business adaptation nor the quality of a quantized language model. Identify what additional artefacts would be needed to reproduce a real adapter deployment.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/05-routines.md) for the supporting theory and scholarly references.

## Another explanation

[LoRA original paper](https://arxiv.org/abs/2106.09685) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.
