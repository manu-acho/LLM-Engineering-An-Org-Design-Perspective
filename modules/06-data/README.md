# Module 6: Data, categories and baselines

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Routing labels record a decision about which team should receive work. A clean spreadsheet can therefore encode obsolete ownership rules. Harbour begins with a deliberately small text classifier so the preparation, fitting and evaluation boundary remains visible.

## Preparation and route

Complete Module 5 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 6.1: How examples become a prediction system](01-concepts.md)
2. [Lesson 6.2: Fit a text-routing baseline without leakage](02-code-workshop.md)
3. [Lesson 6.3: Historical labels contain an operating model](03-business-and-organisation.md)
4. [Lesson 6.4: Calculate a training update and a task error](04-learning-an-update.md)
5. [Lesson 6.5: Inspect fitted vocabulary and ambiguous predictions](05-source-walkthrough.md)
6. [Lesson 6.6: Redesign a routing task before learning its labels](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m06.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The test predictions and their score are computed from the fitted pipeline. With the supplied invented messages, the classifier should distinguish finance language from delivery language. Passing the three examples establishes execution of this baseline, not a reliable routing service for ambiguous or new work.

## Completion exercise

Consider a message containing invoice and damaged delivery. Which team should own it? Explain why fitting more accurately to historical single-team labels might worsen the service.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/03-decisions.md) for the supporting theory and scholarly references.

## Another explanation

[scikit-learn preprocessing and leakage](https://scikit-learn.org/stable/common_pitfalls.html) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Fit preprocessing on training data and inspect predictions.
- Calculate an actual gradient-descent trace from the written lesson.
- Keep a test-only word outside the fitted vocabulary.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
