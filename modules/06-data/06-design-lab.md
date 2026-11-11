# Lesson 6.6: Redesign a routing task before learning its labels

[Module route](README.md) · [Next module](../07-specialisation/README.md)

## What you'll learn and why it matters

Write a routing and labelling rule for cases that need contributions from several teams. Test whether it answers the question Harbour actually needs to ask.

A complaint about a damaged box may need photographs from the warehouse and a reply from customer service. A rule for labelling training examples must say whether it asks for the next useful contribution or the owner of the whole case. Write the rule so two colleagues can apply it to that same example and explain why their answers agree or differ.

## A clear column can contain an unclear task

**Fictional case.** Harbour exports old complaints with an `assigned_team` column. Staff want a classifier to reproduce it. Examination reveals that the value sometimes means the first contacted team, sometimes the final owner and sometimes the only team available that day.

The problem is not simply noisy text. Several organisational decisions have been compressed into one field. Training faithfully on that field could preserve precisely the confusion the proposed system is meant to reduce.

## Separate contribution from ownership

Harbour replaces one target with three questions: what evidence is needed next, which team can supply it, and who retains responsibility for the customer case? A delivery recount can be operations work while account management retains case ownership. A later finance decision does not mean finance should have received the first enquiry.

This is differentiation and integration applied to the dataset. Technical labels now correspond to explicit contributions rather than an accidental history of assignment.

## Complete an annotation rule

| Situation in the initial message | First contribution label | Case ownership |
|---|---|---|
| Missing receipt or disputed quantity | Delivery evidence | Account management retains until accepted transfer |
| Verified discrepancy with remedy question | Policy/remedy review | Named case owner retains during finance review |
| Contradictory or insufficient information | Clarification required | Intake owner obtains missing evidence |

Two reviewers label a development sample independently. They retain disagreement and explain its cause. The policy owner adjudicates the rule, then revises the annotation guide. The held-out set is prepared separately after the task definition is stable. This is governance of the target, not merely cleaning spelling.

## Diagnose misfit and compare responses

Strong and Volkoff's fit/misfit perspective, discussed in the [enterprise systems review](../../reference/research/04-implementation.md), directs attention to data, functionality, roles and controls. Harbour's one-column history contains data and role misfit. A model extension alone cannot resolve it.

Options include changing the process, adding fields, configuring routing rules, using a classifier for ambiguous language or declining automation for certain categories. Harbour chooses rules for explicit order-status requests and a classifier that recommends the next contribution for free-text cases. Uncertain cases enter clarification rather than being forced into a wrong team.

## Measure the new task

Suppose a majority baseline routes 85% of cases to operations and scores 85% overall. It misses every finance-first case. The proposed classifier scores 88%, but that three-point gain is not enough information. Examine category-level precision and recall, missed consequential cases, clarification use, repeated transfers and accepted ownership.

A classifier that correctly predicts “finance” but abandons customer ownership can still harm service. Pair the prediction with the receiving arrangement. A notification does not establish acceptance.

## Learning from actual use

For the first month, staff record why recommendations were overridden: missing evidence, category ambiguity, source error, workload or model interpretation. The label owner reviews recurring patterns. A temporary workload workaround should not automatically become the target for future training.

The [routines review](../../reference/research/05-routines.md) helps explain why recorded performance is a selective representation of work. Informal repairs may be absent from the export. Treat observation and staff accounts as additional evidence, while preserving their own limits.

**Worked decision:** Override rates rise after a policy change. Before retraining, determine whether the label definition changed, the new rule reached the application and the current evaluation still represents the task. New data can help only after the organisation knows what behaviour it wants to learn.

## Read the organisational connection

A routing category can create role or data mismatches even when prediction accuracy is high. The research chapter explains [six kinds of misfit](../../reference/research/04-implementation.md#six-kinds-of-misfit).

The research chapter also explains [how classification changes which work becomes visible](../../reference/research/07-infrastructure-and-standards.md#classification-changes-what-an-organisation-can-see).

## What to remember

The next source of evidence and the owner of the whole investigation can be different roles. A useful annotation rule names which of them the model should predict.

## What this means for the business process

Give the design a separate field or workflow step for the next contributor and for case ownership if both are needed. Let advisers challenge routes that repeatedly delay work, so the category design can improve with practice.

For the research behind this design choice, read [Identify what depends on what](../../reference/research/02-coordination.md#identify-what-depends-on-what).

## Next lesson

Module 7 considers what to do when a clearly specified behaviour remains unreliable even after the task and evidence have been improved. [Lesson 7.1: What fine-tuning changes, and what it cannot settle](../07-specialisation/01-concepts.md).
