# Module 14: MCP and business capabilities

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

MCP gives clients a common way to discover and call capabilities. Discovery tells a client that a tool exists; it does not give the client authority over every case the backing service can see.

## Preparation and route

Complete Module 13 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 14.1: MCP connects capabilities, not business authority](01-concepts.md)
2. [Lesson 14.2: Expose a narrow case-reading capability](02-code-workshop.md)
3. [Lesson 14.3: A reusable agent capability needs a service owner](03-business-and-organisation.md)
4. [Lesson 14.4: Build an AI integration plan around the work](04-integration-plan.md)
5. [Lesson 14.5: Run the actual MCP client and server exchange](05-source-walkthrough.md)
6. [Lesson 14.6: Read a completed AI integration proposal](06-design-lab.md)
7. [Lesson 14.7: Connect the interface, feedback and ongoing service](07-service-evaluation.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m14.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The actual MCP exchange lists read_case and returns the H-17 fictional record. The direct demo has a clear label stating that it bypasses transport. Neither path authorises a remedy. The fixed scope is appropriate for a narrow local lab, not a substitute for authenticated per-user scope in a shared deployment.

## Completion exercise

Compare calling read_case directly with awaiting exchange. Which additional failure modes does the second path expose, and which security questions remain untested?

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/06-technology-in-practice.md) for the supporting theory and scholarly references.

## Another explanation

[Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Inspect the capability's direct Python result before transport.
- Preserve source and status in an integration contract.
- Let a model use tools discovered through a real MCP exchange.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
