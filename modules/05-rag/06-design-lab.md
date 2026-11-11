# Lesson 5.6: Build an organisational knowledge service

[Download the matching notebook](/downloads/05-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../06-data/README.md)

## Business context: Harbour

A shared folder does not tell an adviser which policy is current or who can correct it. A source registry is a list that names the records a service may use and identifies who owns them, when they apply and what they establish. Make one entry for a policy and one for a dispatch record. They are useful for different reasons and should not settle the same questions.

Design a route for missing, conflicting or superseded policy evidence.

[Company and supply-chain context](../../HARBOUR.md) · [Module 5 business situation](../../reference/harbour-learning-journey.md#module-5)

## Resolve what “knowledge” means for this task

**Fictional case.** Harbour has three documents: a finance policy, an operations procedure and an account-manager interview. The first defines authority, the second describes a prescribed sequence, and the third describes how one person says small complaints are usually handled. A search index can hold all three. It should not turn them into one undifferentiated source of instruction.

The service has two modes. Operational guidance foregrounds current authoritative policy and exposes unresolved conflicts. Inquiry mode helps analysts compare formal rules with situated accounts. The same retrieved passage can have a different evidential role in the two tasks.

## Complete a source registry

| Source | Owner | Status and scope | Correction route |
|---|---|---|---|
| Credit policy P-3 | Finance policy owner | Approved, effective date, all service teams | Policy change request |
| Delivery procedure D-2 | Operations process owner | Current prescribed verification steps | Procedure review |
| Interview I-7 | Research custodian | Situated account, approved research use | Clarification or analytic note, not silent editing |

The registry separates content maintenance from application maintenance. An engineer can rebuild an index without having authority to revise finance policy. A policy owner can approve a rule without controlling the embedding service. Both need a route for changes to reach the deployed arrangement.

## Work a conflict to a decision

The assistant retrieves “finance approves disputed credits” and an interview describing informal account-manager resolution. Here the policy refers to an authorised finance manager, rather than every finance user; the remedy decision and processing of an account adjustment remain separate. It returns both with their source types. The frontline user asks for permission to act. The application reports the approved rule, records the conflicting account as a matter for investigation and supplies an escalation route. It does not invent a new exception.

The policy owner then examines repeated cases. Some informal resolutions are legitimate exceptions that were poorly documented; others reflect avoidable waiting. A revised policy defines a narrow frontline category and a pending-evidence state. The new version enters the registry, is indexed, and is tested against old and new cases before switching the service.

This sequence connects retrieval to organisational learning. Correction becomes a change to a governed source and operating process, rather than a growing list of hidden prompt patches.

## Transfer, translation and negotiation

Carlile's framework explains why a better search result can be only the first step. Common fields transfer information across a syntactic boundary. Explaining that “complete” means shipment recorded to one group and customer issue resolved to another translates meaning. Disagreement about who bears review effort may require negotiation across a pragmatic boundary.

The assistant can display the disagreement and assemble evidence. A cross-functional owner must decide the operating settlement. No similarity score establishes that settlement's legitimacy.

Relational coordination adds shared goals, knowledge of others' work, mutual respect and timely problem-solving communication. Harbour therefore pairs the source service with a short route for specialists to clarify an exceptional case. The intervention is a combination of information access and working relationships.

## Evaluate the complete service

Suppose the pilot answers 90 of 100 questions with correct source references. Staff still escalate 40 because the underlying policies conflict. Citation correctness is encouraging technical evidence. It does not establish that organisational uncertainty was resolved.

Measure retrieval coverage, supported claims and appropriate abstention alongside conflict resolution, policy-update turnaround, review effort and useful completion. Observe whether frontline staff can actually open the sources and obtain an answer from the policy owner. Those conditions turn a feature into a usable possibility for particular actors.

**Worked choice:** Should Harbour fine-tune a model on the 40 conflicting answers? First decide which interpretations should govern and why. Training on unresolved disagreement can reproduce it with greater consistency. A source-governance intervention may be the necessary next step.

**Research basis:** [Coordination](../../reference/research/02-coordination.md), [decision theory](../../reference/research/03-decisions.md) and [routines](../../reference/research/05-routines.md).

## Read the organisational connection

A knowledge service needs routes for translation and contestation as well as document transfer. The research chapter explains [knowledge boundaries](../../reference/research/02-coordination.md#shared-data-and-shared-meaning).

## Practical activity: Design what happens when no permitted evidence is found.


### Predict and follow the values

Which status preserves the missing-evidence condition?

```python
from ai_orgdesign.labs.m05 import retrieve
from ai_orgdesign.case_data import POLICIES
hits = retrieve("delivery", tenant="unknown", documents=POLICIES)
response = {"status":"needs_evidence","next_owner":"knowledge service owner"} if not hits else {"status":"ready"}
print(response)
```

### Complete the exercise

**Worked answer.** needs_evidence. It does not assert that no relevant policy exists anywhere.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Keep the policy and the role separate

The policy vignette places remedy approval with an authorised finance manager. It does not grant all finance users that authority or change the live exercise’s role checks. Describe a different arrangement explicitly before evaluating it.
