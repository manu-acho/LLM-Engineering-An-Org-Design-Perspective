# Module 4: Evaluation and business value

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

Two systems can have equal accuracy while imposing very different harms. Harbour needs to distinguish an unnecessary review from clearing a case that still requires investigation, then compare the resulting work with an existing process.

## Preparation and route

Complete Module 3 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 4.1: What would count as evidence that the system is useful?](01-concepts.md)
2. [Lesson 4.2: Compare equal accuracy with unequal consequences](02-code-workshop.md)
3. [Lesson 4.3: Metrics are part of the design of work](03-business-and-organisation.md)
4. [Lesson 4.4: Calculate what a quality score leaves out](04-measures-and-uncertainty.md)
5. [Lesson 4.5: Trace error categories and the chosen loss rule](05-source-walkthrough.md)
6. [Lesson 4.6: Decide whether a measured improvement changes the organisation](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m04.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

The always-clear rule has accuracy one half, two unsafe clearances and illustrative loss forty. The conservative rule has accuracy three quarters, no unsafe clearances and loss one. These are exact calculations on invented cases. A larger evaluation and observations of actual work would be needed for a deployment decision.

## Completion exercise

Construct two predictions with equal accuracy but different unsafe-clearance counts. Then ask whether the chosen twenty-to-one penalty reflects an agreed business preference or only an author assumption.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/04-implementation.md) for the supporting theory and scholarly references.

## Another explanation

[scikit-learn evaluation pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Compare identical accuracy with different consequences.
- Calculate precision and recall with explicit counts.
- Measure actual generated routes rather than inventing a score.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
