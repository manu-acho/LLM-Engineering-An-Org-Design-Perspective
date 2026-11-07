# Module 12: Durable state and human review

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

A review that waits overnight cannot rely on a notebook variable. Durable state preserves the pending work across sessions, but it must not preserve expired authority or repeat an already committed decision.

## Harbour at this point

A Harbour case can wait for a recount, carrier information or a reviewer who is unavailable. During that wait, the case or policy may change. Resuming yesterday’s proposed decision against today’s record would confuse durable storage with current authority.

**Supply-chain and organisation design question:** Specify a paused case’s owner, awaited contribution, expiry or review conditions and safe resumption checks.

Read [Meet Harbour](../../HARBOUR.md) for the company and cross-functional workflow, or revisit [this module’s place in the case](../../reference/harbour-learning-journey.md#module-12). The technical activity examines a selected contribution; it does not establish that the proposed arrangement has been implemented.

## Preparation and route

Complete Module 11 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 12.1: State lets a workflow pause, recover and continue](01-concepts.md)
2. [Lesson 12.2: Reopen durable work and resume review](02-code-workshop.md)
3. [Lesson 12.3: A pause creates work for somebody](03-business-and-organisation.md)
4. [Lesson 12.4: Decide how state changes and what replay repeats](04-reducers-replay-and-memory.md)
5. [Lesson 12.5: Trace current versions through a delayed decision](05-source-walkthrough.md)
6. [Lesson 12.6: Design review as a service with capacity and discretion](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m12.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

Before the reopen, H-17 is in review at version one. The resumed return decision becomes version two with status returned. A later command based on version one is stale. Replaying the exact committed command with its original key retrieves its original result.

## Completion exercise

Distinguish a snapshot used to display a review screen from authority to commit a decision. What should happen after a policy change while the screen remains open?

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/05-routines.md) for the supporting theory and scholarly references.

## Another explanation

[SQLite transaction boundaries](https://www.sqlite.org/lang_transaction.html) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Pause an actual model-backed graph at a human-review boundary.
- Compare replacing a state field with appending an update.
- Reopen an actual graph checkpoint from a separate process.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
