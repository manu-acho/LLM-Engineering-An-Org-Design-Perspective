# Lesson 13.6: Design interoperability across teams, meanings and maintenance

[Download the matching notebook](/downloads/13-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: implement a common result contract](07-common-contracts.md)

## Business context: Harbour

For another team to use a service, it needs to know what to send, what a response establishes and who will fix it when it breaks. An acceptance contract describes what the receiver can rely on. Write those conditions before choosing whether a central team or individual teams maintain the shared service.

Define what interoperability requires beyond two outputs being valid JSON.

[Company and supply-chain context](../../HARBOUR.md) · [Module 13 business situation](../../reference/harbour-learning-journey.md#module-13)

## Connection solves only part of the boundary

**Fictional case.** Harbour's regional teams use different agent runtimes. Each can return JSON and write to a common task board. One team marks `done` when a draft exists; another uses it when a reviewer accepts the result. The board appears integrated while its central status has two meanings.

A common schema is useful for syntactic coordination. Agreeing what `done` means is semantic work. Deciding who carries rework cost and who may reject a contribution can involve conflicting interests. Carlile's syntactic, semantic and pragmatic boundaries help distinguish these tasks.

## Complete an acceptance contract

Harbour adopts four separate states: `in_progress`, `reported_done`, `validated` and `accepted`. A worker may report its result. An automated validator may check file identity and required fields. A receiving owner accepts the contribution for the intended use. Those transitions retain evidence and actor identity.

The common contract includes task ID, input revision, output identity, source references, status and error category. A timed-out worker cannot be silently converted to success because its framework returned a final message earlier.

## Compare governance arrangements

| Arrangement | Benefit to investigate | Maintenance responsibility |
|---|---|---|
| One shared runtime | Fewer compatibility boundaries | Central platform team and participating process owners |
| Several runtimes behind adapters | Local choice with a common application contract | Platform contract owner plus runtime owners |
| Independent services linked by a protocol | Separate deployment and ownership | Service agreements, identity, versions and failure handling |

Harbour selects adapters for two existing runtimes and avoids adding new frameworks without a specific need. A common protocol may help later service boundaries, but it does not replace the agreed meanings or acceptance process.

## Modularity changes integration work

Separate runtimes can make local changes easier while increasing testing across interfaces. The organisation design review treats modularity as contingent. If tasks are highly reciprocal, standard interfaces may need a route for repeated clarification rather than pretending every interaction is a clean handoff.

Harbour maintains a shared contract test set and a regular process-owner review for disputed meanings. Engineers own compatibility failures. Process owners own what counts as an acceptable business contribution. Neither can discharge the other's responsibility merely by approving a schema.

## Trace one cross-team failure

Region A returns an output against policy version three. Region B now operates under version four. The adapter preserves the input revision, so acceptance rejects the stale contribution and requests revision. If the adapter had discarded version metadata, the inconsistency might appear as a mysterious business error after technical success.

This illustrates why interoperability can move discretion. The adapter designer chooses which distinctions survive conversion. A field mapping that collapses several statuses into `done` makes an organisational judgement, even if written as an ordinary utility function.

## Evaluate the arrangement

Measure accepted contributions, rework, cross-team clarification, version failures and recovery time. Include maintainers' effort, not just model latency. Also observe whether teams share an understanding of ownership and can resolve disagreements without bypassing the board.

**Worked decision:** A new framework produces faster outputs but loses source identity during conversion. It should not pass the common acceptance test until that contract is preserved or an explicitly justified new contract is agreed. Faster incompatible output can increase coordination work.

**Research basis:** [Organisation design](../../reference/research/01-organisation-design.md), [coordination](../../reference/research/02-coordination.md) and [decision theory](../../reference/research/03-decisions.md).

## Read the organisational connection

Interoperability requires attention to interpretation and interests alongside schemas. The research chapter explains [knowledge boundaries](../../reference/research/02-coordination.md#shared-data-and-shared-meaning).

## Practical activity: Choose a runtime against actual operating requirements.


### Predict and follow the values

Is a remote worker required by this particular task?

```python
requirements={"durable_review":"required","remote_worker":"not required","source_trace":"required"}
print(requirements)
assert requirements["remote_worker"]=="not required"
```

### Complete the exercise

**Worked answer.** No. Choosing one would add a service boundary that needs its own justification and controls.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
