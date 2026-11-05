# Module 13: Frameworks and interoperable contributions

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Frameworks package execution conventions. A framework change should not silently change what counts as evidence, how errors are represented or who accepts an output. A plain-Python baseline makes those invariants visible.

## Preparation and route

Complete Module 12 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 13.1: Compare frameworks by the work they help you organise](01-concepts.md)
2. [Lesson 13.2: Run the same task in Python and LangGraph](02-code-workshop.md)
3. [Lesson 13.3: A common interface does not create a common organisation](03-business-and-organisation.md)
4. [Lesson 13.4: Compare runtime responsibilities through a common task](04-framework-tour.md)
5. [Lesson 13.5: Compare runtime outputs and failure boundaries](05-source-walkthrough.md)
6. [Lesson 13.6: Design interoperability across teams, meanings and maintenance](06-design-lab.md)
7. [Lesson 13.7: Write an adapter that preserves uncertainty](07-common-contracts.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m13.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

Both routes return case H-17 in north, difference two and status review. Equality checks observable output for this one contract. It does not establish equivalent persistence, retries, streaming or remote-service behaviour. This is a real framework run with deterministic nodes, not a framework-generated language answer.

## Completion exercise

List three features that would require additional comparison tests before replacing an established runtime. Explain why passing this one equivalence check is useful but insufficient.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/02-coordination.md) for the supporting theory and scholarly references.

## Another explanation

[LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Run a model-backed contribution inside LangGraph.
- Run the same evidence contract through the OpenAI Agents SDK.
- Compare two actual runtimes on stable factual fields.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
