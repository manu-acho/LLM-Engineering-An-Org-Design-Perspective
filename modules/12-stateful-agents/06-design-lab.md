# Lesson 12.6: Design review as a service with capacity and discretion

[Module route](README.md) · [Next module](../13-agent-frameworks/README.md)

## What you'll learn and why it matters

Compare ways to staff review and preserve real discretion. Recommend a design that works under Harbour's expected demand, including difficult cases.

Imagine twenty cases waiting for one reviewer. More drafts will not create more reviewing time. Compare a dedicated reviewer, shared coverage, escalation or a narrower scope in terms of who receives each case and what they can decide. Choose a design that makes sense when the queue is busy, not just in a demonstration.

## A pause creates a dependency

**Fictional case.** Harbour's graph correctly pauses 50 cases a day. Finance has 90 minutes of review capacity. At three minutes per case, it can review 30. The pending queue grows by approximately 20 a day before accounting for variation, absence and rework.

The interrupt works technically. The implementation has not supplied a sufficient review arrangement. The next redesign should examine who needs to review which cases and what makes a review useful.

## Compare four responses

| Response | What it changes | What must be checked |
|---|---|---|
| Add protected capacity | More reviewer time | Whether effort is justified and expertise available |
| Narrow interrupted scope | Fewer cases require the same review | Whether remaining automatic cases meet an explicit rule |
| Improve evidence presentation | Less effort per valid review | Whether reviewers still perform substantive checking |
| Delegate a bounded category | Different allocation of decision opportunity | Competence, authority, incentives and escalation |

Harbour combines evidence improvement with a narrower rule. Clear, supported drafts take two minutes. Only 35 daily cases need finance review, giving an expected 70-minute load. The margin within 90 minutes is not a guaranteed service level: arrival variation and complex cases still matter. Monitor waiting rather than planning exactly at average capacity.

## Meaningful discretion requires more than a button

Reviewers need to see the evidence, understand it, reject a proposal and obtain correction. A formal right to reject can coexist with pressure to approve. A performance target based solely on clearing the queue can undermine the purpose of review.

Harbour measures unsupported approvals and justified revisions alongside turnaround. Recurrent rule disputes reach the policy owner. The reviewer is not expected to solve every category problem through individual exceptions.

The [decision theory review](../../reference/research/03-decisions.md) distinguishes permission, practical influence and accepted authority. Those distinctions help identify why a technically complete interrupt might produce superficial confirmation.

## Follow a delayed case

Case C-17 waits overnight. In the morning, operations updates the quantity record. The reviewer sees proposal revision one, prepared against the old source. The system must either invalidate it or make the changed evidence explicit and issue a revised proposal. Approval of revision one should not silently become approval of revision two.

The case owner handles the customer's waiting. The reviewer handles the decision opportunity. The operator handles checkpoint or service recovery. These responsibilities connect without becoming interchangeable.

## Observe the routine, including work outside the graph

At first, reviewers call operations when a field is unclear. Those calls are useful repair work. If recurrent, they may reveal a missing data field or an unsuitable category. Recording only checkpoint transitions would miss the work making the process usable.

Over several weeks, Harbour changes the evidence panel and annotation rule. Review effort falls and fewer calls are needed. That is a possible actualisation process to investigate: actors learn and alter an arrangement over time. A single screenshot of the panel cannot establish it.

## Make the expansion decision

The pilot can expand when supported review decisions, waiting, effort and customer outcomes meet stated conditions on representative cases. It should not expand merely because all paused cases can eventually be resumed in a test.

**Worked challenge:** Review reduces wrong remedies but doubles elapsed time. The answer is not automatically to remove review. Compare which errors were prevented, where waiting arose and whether scope, capacity or evidence can be redesigned. The appropriate trade-off follows the service's consequences and conditions.

**Research basis:** [Coordination](../../reference/research/02-coordination.md), [routines](../../reference/research/05-routines.md) and [technology in practice](../../reference/research/06-technology-in-practice.md).

## Read the organisational connection

Meaningful review depends on access, expertise, time and a practical route to respond. The research chapter explains [actualisation](../../reference/research/06-technology-in-practice.md#actualisation-from-possibility-to-action).

The research chapter also explains [what a reviewer needs beyond an approval button](../../reference/research/08-governance-and-accountability.md#meaningful-review-needs-resources-and-a-practical-alternative).

## What to remember

A pause creates a queue. Capacity determines how long it waits, while discretion determines whether reviewers can return or challenge work.

## What this means for the business process

Match intake to review capacity and reserve a way to handle cases requiring specialist judgement. Monitor waiting and returned cases, so apparent success in drafting does not hide a growing review problem.

For the research behind this design choice, read [Information demand and capacity](../../reference/research/01-organisation-design.md#information-demand-and-capacity).

## Next lesson

Module 13 keeps the service requirement fixed while comparing different frameworks that could implement it. [Lesson 13.1: Compare frameworks by the work they help you organise](../13-agent-frameworks/01-concepts.md).
