# Lesson 8.6: Complete a pilot operating design

[Download the matching notebook](/downloads/08-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: failures and queues](07-failures-and-queues.md)

## Business context: Harbour

Include the receiving team’s time, source access and return route in the proposed service.

[Company and supply-chain context](../../HARBOUR.md) · [Module 8 business situation](../../reference/harbour-learning-journey.md#module-8)

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

## Practical activity: Place an actual generated contribution inside the operating design.





The exercise code below runs from a prepared course checkout. In the matching notebook, the setup cell already supplies ROOT and RUN_LIVE. If following the code here, run this setup first:

```python
from ai_orgdesign.workspace import project_root, live_mode
ROOT = project_root()
RUN_LIVE = live_mode()
if RUN_LIVE:
    from ai_orgdesign.provider import Gateway
    gateway = Gateway(max_requests=12, max_output_tokens=1000)
print("Live mode:", RUN_LIVE)
```

### Predict and follow the values

Is the generated brief itself a remedy decision?

```python
design = {"contribution":"investigation draft","acceptance_owner":"investigator","remedy_authority":"manager","correction_owner":"record owner"}
print(design)
```

No. It is a contribution awaiting accountable review.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

```python
if RUN_LIVE:
    from ai_orgdesign.investigation import draft
    contribution = draft(gateway)
    print(contribution["brief"])
    print("Acceptance owner:", design["acceptance_owner"])
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

Write the prediction before consulting the worked answer: Is the generated brief itself a remedy decision?

**Worked answer.** No. It is a contribution awaiting accountable review.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
