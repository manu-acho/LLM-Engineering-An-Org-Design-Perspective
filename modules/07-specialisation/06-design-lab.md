# Lesson 7.6: Make a specialisation decision and keep categories revisable

[Module route](README.md) · [Next module](../08-agents/README.md)

## What you'll learn and why it matters

Recommend whether to specialise a model after comparing results, costs and who can revise the task. Explain what evidence would change the decision.

Suppose extra training produces a better-looking complaint brief but still treats “reported” as “confirmed”. That is the failure the decision needs to address. Compare a revised instruction, better evidence and further training on the same cases. Include who will maintain the examples and what happens when a case no longer fits an approved category.

## State the remaining failure

**Fictional case.** Harbour has a stable routing guide and labelled examples. A prompted model handles ordinary requests but repeatedly confuses “delivery evidence needed” with “financial remedy ready”. The team compares better instructions, retrieval of the category guide, a smaller classifier and adaptation. Training is a candidate intervention because a measured behavioural weakness remains.

The comparison uses a fixed holdout of 200 cases, including 40 exceptions. The labels identify the next contribution, not a transfer of customer ownership. This task definition carries forward the redesign from Module 6.

## Compare outcomes and complete costs

| Illustrative result | Prompt plus guide | Small classifier | Adapted model |
|---|---|---|---|
| Correct next-contribution recommendations | 172/200 | 176/200 | 184/200 |
| Consequential exception misses | 8 | 6 | 2 |
| Invalid outputs | 4 | 0 | 1 |
| Main maintenance work | Prompt and guide | Vocabulary/model and labels | Base/adapter compatibility and labels |

These are synthetic teaching results. Invalid outputs must be included in coverage reporting and not counted as correct. The decision weighs the eight additional correct recommendations over the classifier against adaptation, evaluation, serving and ongoing revision costs. A higher score alone does not establish worthwhile net value.

If the adapted model saves 20 monthly review hours worth £600 but requires £900 in additional operation and maintenance, the financial capacity argument is weak under those assumptions. Avoided consequential errors may still matter, but must be evaluated explicitly rather than smuggled into a broad accuracy claim.

## Categories allocate organisational attention

The model learns the selected definitions. A category can determine which specialist sees a case, which evidence must be collected and what delay is tolerated. It is a decision premise with an organisational owner. Engineers maintain the learning system; a process or policy owner must govern the categories it is meant to apply.

Harbour creates a taxonomy review route. Staff can record an override reason and propose a new category. The policy owner distinguishes misinterpretation, label ambiguity, new work and temporary workload routing. Only adjudicated changes become training targets.

This avoids a feedback loop in which every workaround is automatically treated as the desired standard. A record of what happened is evidence about practice, not necessarily a specification of what should happen next.

## Follow a change over time

After three months, Harbour introduces a regional service team. Requests that previously went to operations now need local evidence. Staff initially override the model. Their repeated performances reveal a changed division of work. The taxonomy is revised, affected cases are relabelled, and the new model is evaluated against both old and new populations.

The routines perspective explains this sequence: recurrent performance can modify shared understandings and artefacts. Specialisation should support that learning rather than make yesterday's categories expensive to contest. The model's consistency is valuable only relative to a legitimate and current task.

## Complete the release decision

Harbour selects a bounded adaptation pilot because the fictional exception results justify further investigation. It retains the simpler classifier as a comparator and rollback option. The release record names compatible artefacts, evaluation cases, known exclusions, category owner and override review. Expansion depends on actual effort, error and outcome evidence.

**Worked decision:** The adapted model becomes less accurate after a new team starts work. Should Harbour immediately add more epochs? First check whether the task and category meanings changed. More training against the old target can make the new arrangement harder to implement.

**Research basis:** [Decision theory](../../reference/research/03-decisions.md), [routines](../../reference/research/05-routines.md) and [technology in practice](../../reference/research/06-technology-in-practice.md).

## Read the organisational connection

Corrections need interpretation before they become durable training or procedure changes. The research chapter explains [repeated action and learning](../../reference/research/05-routines.md#repeated-action-and-learning).

The research chapter also explains [the organisational effects of categories](../../reference/research/07-infrastructure-and-standards.md#classification-changes-what-an-organisation-can-see).

## What to remember

The useful comparison starts with a specific failure and tests realistic alternatives. Categories remain open to challenge even when a specialised model handles the current examples well.

## What this means for the business process

Specify who can propose a label change, how it is tested, and how advisers handle unfamiliar cases in the meantime. Evaluate maintenance and review effort along with model quality before selecting a design.

For the research behind this design choice, read [Repeated action and learning](../../reference/research/05-routines.md#repeated-action-and-learning).

## Next lesson

Module 8 puts an AI contribution inside a whole operating workflow, where a stronger component still needs controls, owners and recovery. [Lesson 8.1: An agent is part of a workflow, not a complete operating model](../08-agents/01-concepts.md).
