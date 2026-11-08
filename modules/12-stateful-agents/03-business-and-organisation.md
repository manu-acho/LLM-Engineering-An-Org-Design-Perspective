# Lesson 12.3: A pause creates work for somebody

[Download the matching notebook](/downloads/12-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## Business context: Harbour

Consider whether the reviewer has the time, evidence and ability to disagree with the proposal.

[Company and supply-chain context](../../HARBOUR.md) · [Module 12 business situation](../../reference/harbour-learning-journey.md#module-12)

## Human review becomes a queue

**Fictional case.** Harbour adds approval interrupts before customer commitments. The system pauses correctly, but cases accumulate. Finance receives no protected review time. Some reviewers approve quickly to clear the queue; others ask account managers to investigate outside the system.

The technical pause is working. The proposed control arrangement is incomplete. A human-in-the-loop feature becomes useful only when someone can perform the work that the loop assigns to them.

## Formal rights and practical influence

The [decision-theory review](../../reference/research/03-decisions.md) distinguishes permission from accepted authority and the practical conditions of choice. A reviewer needs access to the evidence, relevant expertise, time and the ability to reject or request a change.

The exact proposal version matters too. If an assistant revises a draft after approval, the reviewer has not necessarily authorised the revised commitment. Binding the approval to the proposal is a technical implementation of an organisational distinction: what, exactly, did this person agree to?

Discretion can move to the people who define which actions interrupt, which changes invalidate approval and which categories permit automatic treatment. Those choices deserve an owner and a challenge route, even when frontline approval remains visible.

## Waiting and escalation are coordination arrangements

The [coordination review](../../reference/research/02-coordination.md) asks what one activity needs from another. A paused case depends on a response from a reviewer. Define when the response is due, how absence is handled and who owns the case while it waits.

An “awaiting review” status can improve predictability if staff understand and monitor it. It can also become a parking place with no effective owner. An elapsed-time alert is useful only if someone has both responsibility and capacity to act on it.

Separate ordinary delay, missing evidence and a substantive policy dispute. They may need different queues and escalation paths. Treating every unresolved case as a retry can burden the same unavailable person repeatedly.

## Saved state represents work selectively

The [routines review](../../reference/research/05-routines.md) helps interpret checkpoints. A saved state may contain source IDs, a proposed action and a status. It may omit the conversation in which a warehouse specialist qualified the record or the informal agreement that an urgent customer needs a call.

The state is an artefact supporting work, not the whole routine. Investigate what people do between recorded transitions. If important coordination consistently occurs outside the application, decide whether it should be represented, linked or left outside with an explicit boundary.

Do not assume every workaround is misuse. It might repair a genuine mismatch between the formal route and the task. It might also weaken an important control. The response requires case evidence rather than a general verdict about resistance.

## Recovery needs an accountable role

The [enterprise-systems review](../../reference/research/04-implementation.md) treats implementation as a process extending beyond launch. Paused cases may reveal missing reviewer roles, unsuitable categories, source-access problems or records that become stale overnight.

Define who can repair each kind of failure. A service operator may restart a process but lack authority to renew an expired credit proposal. A process owner may revise the approval rule but need engineering support to migrate saved state. A reviewer may correct one case while being unable to resolve a recurring design defect.

A business continuity plan needs more than a backup database. It should explain how staff identify unresolved cases, avoid duplicate effects, restore a usable view and communicate uncertainty during recovery.

## Availability, actual use and benefit

The [technology-and-organisation review](../../reference/research/06-technology-in-practice.md) gives us a way to examine the approval feature. It may offer a possibility of meaningful review to one role and only a compulsory confirmation step to another. The difference depends on access, knowledge, workload and authority.

Observe review over time: which passages are opened, which disagreements lead to changes, how rejected cases are resolved and what happens when the reviewer is absent. These actions help investigate actualisation. An approval count alone cannot distinguish effective checking from hurried compliance.

A lower error rate might reflect the approval design, better intake introduced alongside it, or a temporary change in case mix. Connect outcome comparisons to evidence of the process.

## Apply the idea

Suppose interruptions reduce duplicate credits but double resolution time. Would you remove review, add capacity, narrow the interrupted category or improve the evidence presentation?

There is no universal answer. Identify which cases need judgement, which checks can be deterministic and where waiting occurs. A low-risk category with stable criteria may support bounded automatic processing. A disputed policy question may need a clearer decision forum rather than faster clicking.

**Try it:** Design a review service, not just a button. Specify the reviewed object and version, reviewer's evidence and rights, expected response time, absence cover, rejection route and recovery owner. Include one metric for decision quality and one for the effort imposed on the people doing the review.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A pause creates a dependency on reviewer attention and capacity. The research chapter explains [shared-resource dependencies](../../reference/research/02-coordination.md#identify-what-depends-on-what).

## Practical activity: Relate review capacity to incoming prepared work.





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

What is the backlog growth under these steady illustrative rates?

```python
arrivals_per_hour=30
review_capacity_per_hour=20
print("Illustrative backlog growth per hour:",arrivals_per_hour-review_capacity_per_hour)
```

Ten cases per hour. This is not a stable queue to which a steady-state waiting-time calculation should be applied without further conditions.

### Complete the exercise

Write the prediction before consulting the worked answer: What is the backlog growth under these steady illustrative rates?

**Worked answer.** Ten cases per hour. This is not a stable queue to which a steady-state waiting-time calculation should be applied without further conditions.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

A Harbour case can wait for a recount, carrier information or a reviewer who is unavailable. During that wait, the case or policy may change. Resuming yesterday’s proposed decision against today’s record would confuse durable storage with current authority.

**Task:** Specify a paused case’s owner, awaited contribution, expiry or review conditions and safe resumption checks.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Save the contribution and its source/version identity. Keep an owner for waiting work, revisit stale facts and revalidate policy before committing. A stored model draft can be reused where suitable; a changed business situation may need a new investigation.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.

## Research extension: examine the wider arrangement

[Governance and accountability](../../reference/research/08-governance-and-accountability.md#worked-arrangement-govern-a-remedy-rather-than-a-button). Link approval to a specified proposal version. Distinguish a technical stale-version refusal from evidence that a reviewer can obtain a timely corrected decision.
