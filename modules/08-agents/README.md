# Module 8: An AI service within an operating model

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

A technically successful brief is only one contribution to a service. Harbour also needs an accountable investigator, a remedy decision and a route for retries, errors and corrections. These arrangements belong in the operating model.

## Preparation and route

Complete Module 7 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 8.1: An agent is part of a workflow, not a complete operating model](01-concepts.md)
2. [Lesson 8.2: Record a simulated decision and safe retry](02-code-workshop.md)
3. [Lesson 8.3: Designing an operating organisation around the workflow](03-business-and-organisation.md)
4. [Lesson 8.4: From an AI feature to a way of working](04-technology-in-practice.md)
5. [Lesson 8.5: Trace the decision transaction and command identity](05-source-walkthrough.md)
6. [Lesson 8.6: Complete a pilot operating design](06-design-lab.md)
7. [Lesson 8.7: Make failures terminal, visible and recoverable](07-failures-and-queues.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m08.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The pending case starts at version one in review. Approval changes it to version two with status approved_simulation. Retrying the identical command returns the same result without an additional audit event. No money moves and no customer message is sent.

## Completion exercise

Specify who should investigate a case when the evidence is incomplete, and what should happen if two managers act on version one at the same time.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/01-organisation-design.md) for the supporting theory and scholarly references.

## Another explanation

[SQLite transaction boundaries](https://www.sqlite.org/lang_transaction.html) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.
