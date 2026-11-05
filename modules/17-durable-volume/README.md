# Module 17: Durable case handling at volume

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Preparing more cases per minute can overload the people who accept or investigate them. Harbour therefore examines technical concurrency and human review capacity together, while preserving ownership when workers fail or become slow.

## Preparation and route

Complete Module 16 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 17.1: Durable case handling at volume](01-concepts.md)
2. [Lesson 17.2: Limit concurrent work and recover an expired lease](02-code-workshop.md)
3. [Lesson 17.3: Design the work, responsibility and learning](03-business-and-organisation.md)
4. [Lesson 17.4: Make the operating contract inspectable](04-operating-contract.md)
5. [Lesson 17.5: Inspect ownership, waiting and completion](05-source-walkthrough.md)
6. [Lesson 17.6: Complete a defensible service decision](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m17.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

At concurrency two, the peak counter never exceeds two. The first worker can claim job-1 at time zero; a second cannot claim it at time five, but can reclaim it at eleven after a ten-second lease. A former owner cannot finish after the transfer. These are local ownership tests, not a benchmark of distributed throughput.

## Completion exercise

Assume thirty cases per hour enter review and reviewers can finish twenty per hour. What changes if agent preparation becomes twice as fast? How should a lease handle an external action completed just before a worker fails?

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/02-coordination.md) for the supporting theory and scholarly references.

## Another explanation

[Python coroutines and tasks](https://docs.python.org/3.12/library/asyncio-task.html) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.
