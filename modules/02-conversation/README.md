# Module 2: Conversations, tools and action boundaries

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

A conversation can appear coherent while the application has lost the selected case or confused two users. Harbour therefore keeps the selected case as explicit state and treats each tool request as a proposal that still needs validation.

## Preparation and route

Complete Module 1 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 2.1: How a conversation becomes a controlled interaction](01-concepts.md)
2. [Lesson 2.2: Follow a conversation through a validated tool](02-code-workshop.md)
3. [Lesson 2.3: Who decides when the assistant can act?](03-business-and-organisation.md)
4. [Lesson 2.4: What changes when a conversation streams or uses media?](04-streaming-caching-and-media.md)
5. [Lesson 2.5: Trace call identity, scope and incremental output](05-source-walkthrough.md)
6. [Lesson 2.6: Allocate discretion across a conversational service](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m02.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The selected case is H-17, its ordered quantity is twelve and its reported quantity is ten. The tool observation has call_id equal to call-1. Joining the stream pieces reconstructs Evidence awaits review, with a trailing space. Nothing approves a remedy.

## Completion exercise

Request H-18 while keeping the north scope. Predict whether the record will be returned and whether changing a name inside a model message should alter that decision.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/03-decisions.md) for the supporting theory and scholarly references.

## Another explanation

[OpenAI function-calling protocol](https://developers.openai.com/api/docs/guides/function-calling) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.
