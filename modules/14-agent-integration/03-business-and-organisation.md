# Lesson 14.3: A reusable agent capability needs a service owner

[Download the matching notebook](/downloads/14-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md) · [Integration plan](04-integration-plan.md)

## What you'll learn and why it matters

Define the promise and owner of a reusable business capability. Learn what consuming teams need if a response changes or the service fails.

## Business context: Harbour

Several assistants might rely on the same case lookup. When a field changes, those teams need someone to explain the change and respond if their work breaks. Name the service owner and describe what the lookup promises, who may use it and how that promise is maintained.

Assign responsibility for capability scope, source quality and recipients of failed results.

[Company and supply-chain context](../../HARBOUR.md) · [Module 14 business situation](../../reference/harbour-learning-journey.md#module-14)

## The interface becomes shared infrastructure

**Fictional case.** Harbour publishes internal tools for case lookup, policy retrieval and handoff preparation. Several departments connect their assistants. The technical team celebrates reuse. A month later, a source field changes, one assistant uses an old interpretation and nobody is sure who owns the resulting customer error.

The interface has become part of how work is coordinated. Its meanings, permissions and changes need an operating arrangement, not only an endpoint.

## Decide what each capability promises

The [coordination review](../../reference/research/02-coordination.md) helps specify the dependency. A consumer needs more than a response shaped as JSON. Does `read_case` return the current operational record, a delayed copy or a partial view? Does `prepare_handoff` create a draft or submit work to another team? What does an error mean for the waiting case?

Write those semantics into a service contract. Include source status, required inputs, expected result, failure conditions and receiving ownership. A common protocol can carry this contract's data, but it cannot decide the contract for the organisation.

Where meanings or interests differ, negotiation may be necessary. Finance may require stronger evidence than customer service considers sufficient. A generated summary cannot settle that disagreement by producing one confident recommendation.

## Technical access and business authority

The [decision-theory review](../../reference/research/03-decisions.md) directs attention to authority and the premises behind actions. A service account may be authenticated while lacking a mandate to act for a particular customer or department. A transport credential is not a universal business permission.

Separate capability visibility, operation permission, record scope and decision authority. The workshop shows why a discovery filter is insufficient. Enforcement belongs where the action occurs, with trusted evidence about the caller, case and current policy.

Also ask who can redefine the tool. Changing “draft” into “submit” expands its effect even if the function name stays the same. That is a governance change, not merely an implementation detail.

## Fit includes ownership and maintenance

The [enterprise-systems review](../../reference/research/04-implementation.md) explains why generic capability must be examined in its local setting. A technically available tool may require information frontline staff cannot provide. A default record category may fit one department and misroute another's work.

Name the business owner of the meaning, the technical owner of the service and the process owner of the end-to-end result. In a small organisation, one person may hold several roles. Keeping the responsibilities distinct still helps when a change or failure needs a decision.

Define a supported change process: announce a schema revision, test consumers, maintain compatibility where appropriate and retire old behaviour deliberately. Otherwise every new consumer inherits assumptions no one can explain or safely revise.

## Memory and records participate in routines

The [routines review](../../reference/research/05-routines.md) helps interpret a shared memory or tool log. A stored strategy may represent an intended approach rather than actual practice. A completed transaction record captures selected events while omitting discussion and manual repair.

Decide which information is an authoritative business record and which is a temporary model aid. A remembered interpretation should not silently become policy for later cases. Give staff a route to challenge, correct and trace the source of recurring claims.

The course's separation of researcher tools, account resources and action tools is useful for asking these questions. It is an inspectable software arrangement, not evidence that an equivalent business operating model has been established.

## Integration changes possibilities unevenly

The [technology-and-organisation review](../../reference/research/06-technology-in-practice.md) encourages actor-specific analysis. A shared case tool may enable a service adviser to find current status. It may enable a coordinator to compare delays. It may constrain a regional specialist if required fields cannot express a legitimate exception.

Investigate these relations through actual cases. Availability, use and benefit are different claims. A connector deployed successfully can coexist with duplicated work, unclear ownership or increased review effort.

The [organisation-design review](../../reference/research/01-organisation-design.md) brings the choices together: work division, information access, coordination mechanisms and authority must fit. Interoperability is useful when it supports that arrangement, not merely when more assistants can connect.

## Apply the idea

Harbour's tools are being called frequently, yet staff distrust the resulting drafts. Would you add more context, retrain a model, improve source versioning, clarify tool semantics or change review ownership?

Follow a disputed draft back to its sources and transformations. The cause may be a stale resource, an ambiguous capability name, insufficient access, a missing policy decision or a model inference. Different causes require different changes.

**Try it:** Write a one-page capability contract for `prepare_handoff`. State what it does, what it cannot authorise, who may use it, which evidence it requires, what result proves completion and who handles a disputed result. Then name the person or role who can change that contract.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A reusable service needs ownership for change, support and recovery after launch. The research chapter explains [implementation beyond launch](../../reference/research/04-implementation.md#implementation-extends-beyond-launch).

## Practical activity: Identify who owns a failed or disputed shared capability.


### Predict and follow the values

Who maintains the shared capability in this proposal?

```python
service={"capability":"read_case","service_owner":"case platform","data_owner":"operations records","consumer":"investigation assistant"}
print(service)
```

### Complete the exercise

**Worked answer.** case platform is the named service owner; source corrections remain a separate responsibility.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour wants tools that different assistants can discover and use consistently. A case lookup and policy search could be exposed through MCP, but discovering a tool does not grant a regional user new access or authorise a financial action.

**Task:** Document one capability’s owner, allowed inputs, scope, output meaning, failure contract and support route.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Expose a bounded read with server-side scope and source identity. An unavailable result should remain unavailable rather than becoming invented evidence. The local teaching MCP connection does not establish remote authentication or a production finance integration.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.

## Research extension: examine the wider arrangement

[Process architecture](../../reference/research/09-process-architecture.md#activities-events-roles-and-objects). Separate the agent-run identifier from complaint, order, shipment and invoice identifiers. Explain which relationships are needed to reconstruct a disputed remedy.

[Infrastructure and standards](../../reference/research/07-infrastructure-and-standards.md#worked-design-a-quantity-agreement). A shared schema needs agreed meaning and a correction owner. Use the proposed quantity agreement as a design exercise, without assuming the lab implements every provision.

## What to remember

An interface becomes shared infrastructure when other teams rely on it. Its owner needs to maintain field meanings, access rules and change notices.

## What this means for the business process

Give consuming teams a known support route and a way to test proposed changes against their tasks. When the case lookup changes a field, its owner must account for downstream decisions that use it.

For the research behind this design choice, read [Infrastructure is a relationship with organised work](../../reference/research/07-infrastructure-and-standards.md#infrastructure-is-a-relationship-with-organised-work).

## Next lesson

Next put the capability and its owners into a plan that starts with a specific problem in Harbour's work. [Lesson 14.4: Build an AI integration plan around the work](04-integration-plan.md).
