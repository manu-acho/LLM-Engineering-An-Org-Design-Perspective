# Lesson 8.6: Complete a pilot operating design

[Module route](README.md) · [Next: failures and queues](07-failures-and-queues.md)

## What you'll learn and why it matters

Specify the contribution, roles and fallback for a bounded Harbour pilot. Use an alternative design to test whether the proposal fits the work.

If the screen says “waiting for carrier”, someone needs to know whose job it is to ask, when to follow up and what to do if no answer arrives. Describe what each case status tells the next person to do. Then test whether the roles and capacity in the pilot support the promised response.

## Select a bounded contribution

**Fictional pilot.** Harbour chooses long, non-urgent delivery disputes with an identifiable order. The assistant gathers permitted records and prepares a referenced proposal. It does not promise a refund or contact a customer automatically. This is a complete pilot scope, not a description of every future capability.

The current process requires account management to collect evidence, operations to reconcile quantity and finance to authorise a remedy. The proposed contribution reduces preparation and highlights missing evidence while preserving accepted case ownership.

## Put responsibilities beside states

| State | Work needed | Accountable operational role | Exit evidence |
|---|---|---|---|
| Received | Establish case and scope | Intake owner | Identified order and permitted purpose |
| Evidence pending | Obtain missing record | Case owner with named contributor | Source/version or explicit unavailable result |
| Draft ready | Check claims and proposed next step | Assigned reviewer | Decision bound to proposal revision |
| Approved | Submit permitted handoff | Execution service owner | Stable action ID and acknowledged result |
| Accepted | Receive and continue work | Receiving team | Acceptance or a reason for rejection |
| Recovery | Reconcile failed or uncertain work | Service operator and case owner | Corrected state with remaining work identified |

The table distinguishes software operation from human answerability. One person can hold several roles, but each responsibility remains explicit. A service operator can restart a process without having authority to reinterpret finance policy.

## Fit, misfit and responses

The first rehearsal reveals that some legitimate complaints have no receipt ID. A mandatory field blocks them. Removing the field entirely weakens later review. Harbour chooses a `pending_evidence` route with a named owner and expiry/escalation rule. This addresses data and control misfit together.

A second rehearsal reveals that reviewers cannot open warehouse records. More explanatory text in the draft will not fix the role/access mismatch. Harbour grants appropriately scoped evidence access and provides a correction route. The arrangement now connects the feature with the actor's ability to use it.

The [enterprise systems review](../../reference/research/04-implementation.md) helps compare process change, configuration, extension and bounded workarounds. Generic capability is the starting point for local fit, not proof of it.

## Capacity and value calculation

Assume 400 eligible cases a month and 60% actual use, or 240 assisted cases. Preparation saves six minutes; additional review and repair consume two. Net effort saving is 16 hours. At £30 an hour, capacity value is £480. If operating expense is £250, the ongoing difference is £230 before implementation cost and any separately justified quality benefit.

These figures are teaching assumptions. Harbour also measures waiting: if the finance queue remains the main delay, the pilot may save effort without improving resolution time. A useful decision can still follow, but it must state which outcome changed.

## Implementation proceeds through learning

Before launch, test states, permissions, source versions and failure paths. During stabilisation, review incomplete cases daily and adjust workload and evidence presentation. After repeated use, examine whether the intended routine is actually forming and which repairs happen outside the system. Later changes to models or policy repeat the relevant checks.

This lifecycle connects installation, use and outcome without treating them as interchangeable. It also gives employee feedback a route to design owners. A recurring workaround can reveal a legitimate misfit rather than employee resistance.

## Reach the pilot decision

Harbour approves a read-only drafting pilot with a structured-intake comparator, explicit stop conditions for unsupported commitments, and a recovery owner. It retains an ordinary manual route. It will consider external actions only after the smaller contribution and receiving arrangement have evidence of usefulness.

**Worked challenge:** The pilot lowers preparation effort but creates a growing evidence-pending queue. The next decision is to examine missing-source causes, ownership and capacity, then change the arrangement. Increasing the agent's step limit without addressing those dependencies is unlikely to clear the queue responsibly.

## Read the organisational connection

A bounded pilot connects scope, roles, evidence and measures before claiming improvement. The research chapter explains [the worked implementation choice](../../reference/research/04-implementation.md#a-worked-implementation-choice).

The research chapter also explains [who can authorise and carry out a remedy](../../reference/research/08-governance-and-accountability.md#worked-arrangement-govern-a-remedy-rather-than-a-button).

## What to remember

Each case status should tell someone what to do next. Acceptance, escalation and recovery need named owners and capacity to act.

## What this means for the business process

Set a pilot intake limit the review team can handle and retain a route for work outside scope. Compare actual queues and follow-up with the current process before claiming the design improved resolution.

For the research behind this design choice, read [A worked implementation choice](../../reference/research/04-implementation.md#a-worked-implementation-choice).

## Next lesson

The next lesson makes the fallback concrete by examining what to do when a run stops and its effects are uncertain. [Lesson 8.7: Make failures terminal, visible and recoverable](07-failures-and-queues.md).
