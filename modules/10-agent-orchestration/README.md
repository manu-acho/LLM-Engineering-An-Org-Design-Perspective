# Module 10: Orchestration and accepted handoffs

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

A specialist can return a well-formed object about the wrong case. Orchestration therefore needs both a structural contract and acceptance rules linking the contribution to the task that requested it.

## Preparation and route

Complete Module 9 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 10.1: Orchestration decides how pieces of work connect](01-concepts.md)
2. [Lesson 10.2: Validate and accept a specialist contribution](02-code-workshop.md)
3. [Lesson 10.3: A software handoff is not accepted ownership](03-business-and-organisation.md)
4. [Lesson 10.4: Structure the contribution and read the execution trace](04-structured-results-and-traces.md)
5. [Lesson 10.5: Separate schema checks from evidence support](05-source-walkthrough.md)
6. [Lesson 10.6: Compare central coordination with specialist ownership](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m10.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The supplied H-17 contribution passes the structural and case/source membership checks. An invented source or another case identifier raises ValueError. A conclusion that is false but cites an allowed source may still pass, exposing the distinction between membership validation and factual support.

## Completion exercise

Write a false conclusion using order-17 as its source and determine whether the current acceptance function detects the falsehood. Propose the next check rather than claiming schema validation solved it.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/02-coordination.md) for the supporting theory and scholarly references.

## Another explanation

[LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.
