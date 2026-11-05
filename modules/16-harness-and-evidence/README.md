# Module 16: Agent harnesses and operational evidence

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

A model result without its inputs, configuration and stopping reason is difficult to investigate. Harbour needs enough execution evidence to diagnose a failed contribution while avoiding a second uncontrolled store of customer information.

## Preparation and route

Complete Module 15 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 16.1: Agent harnesses and operational evidence](01-concepts.md)
2. [Lesson 16.2: Measure a bounded run without inventing usage](02-code-workshop.md)
3. [Lesson 16.3: Design the work, responsibility and learning](03-business-and-organisation.md)
4. [Lesson 16.4: Make the operating contract inspectable](04-operating-contract.md)
5. [Lesson 16.5: Trace instruction identity, time and assumed cost](05-source-walkthrough.md)
6. [Lesson 16.6: Complete a defensible service decision](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m16.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The supplied loop uses one tool call and stops with final. Elapsed time is measured at runtime and will vary. The assumed cost calculation for one thousand input tokens at one unit per million and two hundred output tokens at four units per million is 0.0018 currency units. No actual provider usage is claimed.

## Completion exercise

Suppose a run stopped after reading the case but before writing its final response. Decide which trace fields distinguish that failure from a denied tool call and from an unresolved business investigation.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/05-routines.md) for the supporting theory and scholarly references.

## Another explanation

[OpenAI function-calling boundaries](https://developers.openai.com/api/docs/guides/function-calling) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.
