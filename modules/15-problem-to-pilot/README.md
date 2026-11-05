# Module 15: From a business problem to a pilot

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Harbour wants to reduce the effort of investigating delivery discrepancies. That is a business problem, not yet a requirement for an agent. A useful pilot tests a bounded contribution against an explicit alternative and preserves the case owner's ability to investigate exceptions.

## Preparation and route

Complete Module 14 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 15.1: From a business problem to a pilot](01-concepts.md)
2. [Lesson 15.2: Turn requirements into executable acceptance cases](02-code-workshop.md)
3. [Lesson 15.3: Design the work, responsibility and learning](03-business-and-organisation.md)
4. [Lesson 15.4: Make the operating contract inspectable](04-operating-contract.md)
5. [Lesson 15.5: Trace scope, evidence and discrepancy rules](05-source-walkthrough.md)
6. [Lesson 15.6: Complete a defensible service decision](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m15.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The three routes are review, deny and needs_evidence. matches is true for the supplied examples. Agreement between quantities produces compare_policy rather than automatic closure. This deliberately avoids using numerical agreement as sufficient evidence that the customer problem is resolved.

## Completion exercise

Add an acceptance example with equal quantities but a damaged box. Identify which missing input and policy rule are needed before the pilot can handle that case.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/04-implementation.md) for the supporting theory and scholarly references.

## Another explanation

[Python tutorial for reading proposed implementations](https://docs.python.org/3.12/tutorial/) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Specify acceptance cases before generating implementation code.
- Inspect generated code before allowing a restricted execution.
- Ask a live model for a small function, inspect it and run acceptance cases.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
