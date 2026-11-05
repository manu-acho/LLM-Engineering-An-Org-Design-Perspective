# Module 9: Agent loops and bounded autonomy

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

An agent loop chooses another step after observing an earlier result. That flexibility can help an investigation, but also creates repeated calls, unexpected branches and uncertain completion. The application must bound the execution independently of the planner.

## Preparation and route

Complete Module 8 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 9.1: An agent chooses steps inside an application](01-concepts.md)
2. [Lesson 9.2: Run a bounded investigation loop](02-code-workshop.md)
3. [Lesson 9.3: Design the work before delegating the next step](03-business-and-organisation.md)
4. [Lesson 9.4: Turn a plan into a bounded investigation](04-plans-budgets-and-evidence.md)
5. [Lesson 9.5: Test repeated calls and independent stopping limits](05-source-walkthrough.md)
6. [Lesson 9.6: Design the front door and the promise behind it](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m09.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The supplied planner first reads H-17 and then returns an investigation statement. With a budget of one, the tool can run but the loop stops at budget before a final answer. Repeated call identifiers stop the loop instead of executing indefinitely. Reaching a stop condition does not mean the business case is resolved.

## Completion exercise

Supply a planner that always asks for the same call. Then change the call identifier on every step. Which independent bound remains necessary?

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/03-decisions.md) for the supporting theory and scholarly references.

## Another explanation

[OpenAI function-calling protocol](https://developers.openai.com/api/docs/guides/function-calling) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.
