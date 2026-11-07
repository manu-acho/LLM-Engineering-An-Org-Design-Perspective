# Module 19: Deployment and continuing service ownership

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Deployment exposes a service to more clients, failures and responsibilities. Harbour starts with an authenticated local HTTP application so its identity, state and failure contracts can be exercised before selecting a hosting provider.

## Harbour at this point

An investigation service used beyond one developer needs support, access management, change windows and a way to handle outages. Harbour’s business customers still need a response when the model or application is unavailable. Finance must not lose its review boundary because an endpoint is reachable.

**Supply-chain and organisation design question:** Write a service acceptance record covering users, owner, support hours, access, rollback, fallback and unresolved deployment requirements.

Read [Meet Harbour](../../HARBOUR.md) for the company and cross-functional workflow, or revisit [this module’s place in the case](../../reference/harbour-learning-journey.md#module-19). The technical activity examines a selected contribution; it does not establish that the proposed arrangement has been implemented.

## Preparation and route

Complete Module 18 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 19.1: Deployment and continuing service ownership](01-concepts.md)
2. [Lesson 19.2: Exercise authenticated HTTP routes](02-code-workshop.md)
3. [Lesson 19.3: Design the work, responsibility and learning](03-business-and-organisation.md)
4. [Lesson 19.4: Make the operating contract inspectable](04-operating-contract.md)
5. [Lesson 19.5: Start and inspect the local case service](05-source-walkthrough.md)
6. [Lesson 19.6: Complete a defensible service decision](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m19.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The public health route reports teaching simulation. An unauthenticated case read receives 401. A correctly authenticated north caller can read H-17. Readers cannot approve, a stale decision receives a conflict response, and an extra actor field is rejected by schema validation. No payment or external customer integration is included.

## Completion exercise

Identify what must be added before the local token-based teaching application can be offered to several organisations on the public internet. Distinguish those requirements from the fact that a local endpoint returned HTTP 200.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/04-implementation.md) for the supporting theory and scholarly references.

## Another explanation

[FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Authenticate a local request before reading case state.
- Inspect a release record for data compatibility and recovery.
- Run the full authenticated draft-read-review HTTP journey.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
