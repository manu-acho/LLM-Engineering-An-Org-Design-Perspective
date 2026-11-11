# Lesson 19.6: Complete a defensible service decision

[Download the matching notebook](/downloads/19-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Research chapter](../../reference/research/04-implementation.md)

## What you'll learn and why it matters

Write a service decision and an incident handover that another person can act on. Explain who owns customer recovery while technical support restores the service.

## Business context: Harbour

A successful local run shows that Harbour can exercise a path through the service. Decide what else is needed before relying on it during ordinary work: an owner, a way to detect failures and a route for recovery or manual work. Work through the difficult case before recommending a release.

Prepare a release plan that includes user communication, recovery and a viable manual route.

[Company and supply-chain context](../../HARBOUR.md) · [Module 19 business situation](../../reference/harbour-learning-journey.md#module-19)

## Prepare the decision record

The fictional Harbour case is an opportunity to connect an executable pattern with the organisation around it. The technical walkthrough supplies the mechanism. This exercise asks what contribution should be accepted, by whom and under which conditions.

Write a one-page decision record with a stated population and exclusions, the proposed contribution, authoritative sources, the people or services involved, acceptance conditions, refusal conditions, recovery and a comparison against an alternative. Keep unsupported assumptions visible. Do not fill a missing business rule by quietly turning a convenient software default into policy.

## Work the difficult case first

Identify what must be added before the local token-based teaching application can be offered to several organisations on the public internet. Distinguish those requirements from the fact that a local endpoint returned HTTP 200.

Before running a variation, predict the result and its business implication. An exception is not necessarily a defect: denying a forbidden read or rejecting a stale approval can be the intended behaviour. Explain which distinction matters in this case.

**Worked reasoning.** The deployment needs an appropriate identity provider and credential lifecycle, HTTPS termination, persistent storage with backup and restore tests, least-privilege networking, secret management, monitoring, quotas, updates and accountable support. Multi-tenant isolation needs broader tests than these two fictional scopes. A successful local request proves only the exercised route, not the full deployment design.

## Separate the technical claim from the service claim

The public health route reports teaching simulation. An unauthenticated case read receives 401. A correctly authenticated north caller can read H-17. Readers cannot approve, a stale decision receives a conflict response, and an extra actor field is rejected by schema validation. No payment or external customer integration is included.

The code checks support that local claim under the supplied fictional inputs. A service-level claim needs a defined comparison population, an observation period, a reference process and evidence about the surrounding work. Record failed and referred cases as well as successful ones. Omitting them can change both the denominator and the apparent benefit.

## Worked choice among alternatives

A single-host service is a useful first operating boundary. A managed container or serverless platform changes scaling, timeout and persistence assumptions. Static Netlify hosting serves the course notes; it does not operate the Python application. Cloud deployment is optional and must not be presented as tested when only local execution was observed.

A defensible decision can retain the simpler alternative, narrow the contribution, request more evidence or authorise a bounded pilot. It need not select the most technically elaborate arrangement. The reason should connect observed difficulties with an intervention that can plausibly address them.

## Check the completed explanation

A strong response defines unfamiliar terms, names the relevant owner rather than a vague human-in-the-loop, explains what the code establishes and identifies at least one rival explanation for a favourable result. It should also state what new evidence could change the decision. The linked research chapter supplies the theoretical argument and scholarly references; the case here is an application, not a finding from that literature.

## Practical activity: Define an incident handover that someone else can act on.


### Predict and follow the values

Who owns the unresolved business case during a technical incident?

```python
handover={"purpose":"evidence preparation","exclusions":["payments","real customer data"],"failure_owner":"engineering","pending_case_owner":"operations","recovery":"inspect current state before retry"}
print(handover)
```

### Complete the exercise

**Worked answer.** operations retains that responsibility; fixing a process does not itself resolve the customer problem.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A local run demonstrates a tested path. An incident involves detecting the fault, restoring capability and dealing with the cases affected.

## What this means for the business process

Assign engineering the technical recovery and operations the review of unresolved cases. Require a handover with affected cases and next actions so restoring the process does not leave customer work unassigned.

For the research behind this design choice, read [Connected routines and hidden work](../../reference/research/05-routines.md#connected-routines-and-hidden-work).

## Next lesson

Module 20 asks how Harbour can change the live service deliberately, test the change and restore an earlier version if needed. [Lesson 20.1: Governed improvement and integration capstone](../20-governed-improvement/01-concepts.md).
