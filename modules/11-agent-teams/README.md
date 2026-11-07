# Module 11: Teams and task dependencies

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Adding specialists can improve local expertise while increasing integration work. The first design question is what depends on what, not how many named agents can be created.

## Harbour at this point

Warehouse and policy questions may sometimes proceed independently, while a conclusion depends on both. A finance adjustment may require a manager’s decision first. Harbour needs to understand these task dependencies before expecting a team of agents to make investigations faster.

**Supply-chain and organisation design question:** Draw the investigation dependency map and identify which contributions can proceed concurrently and which must wait.

Read [Meet Harbour](../../HARBOUR.md) for the company and cross-functional workflow, or revisit [this module’s place in the case](../../reference/harbour-learning-journey.md#module-11). The technical activity examines a selected contribution; it does not establish that the proposed arrangement has been implemented.

## Preparation and route

Complete Module 10 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 11.1: Roles, tasks and dependencies in an agent team](01-concepts.md)
2. [Lesson 11.2: Schedule tasks through their dependencies](02-code-workshop.md)
3. [Lesson 11.3: An agent team needs integration, not just role names](03-business-and-organisation.md)
4. [Lesson 11.4: Read configuration as an executable division of work](04-configuration-and-dependencies.md)
5. [Lesson 11.5: Find missing prerequisites and task cycles](05-source-walkthrough.md)
6. [Lesson 11.6: Divide work where specialisation earns its integration cost](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m11.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

Records and policy preparation precede comparison, which precedes review. Both preparation tasks are independent in this graph, so a runtime could execute them concurrently. The printed sorted sequence is one valid order, not evidence that concurrency occurred.

## Completion exercise

Make policy preparation depend on review while review already depends on compare and compare on policy. Explain why adding a faster worker cannot repair the resulting graph.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/01-organisation-design.md) for the supporting theory and scholarly references.

## Another explanation

[Python language tutorial](https://docs.python.org/3.12/tutorial/) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Prepare the sequential comparison before running a team.
- Find ready work from completed prerequisites.
- Run genuinely overlapping specialist calls and inspect elapsed work.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
