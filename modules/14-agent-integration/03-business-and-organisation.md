# Lesson 14.3: A reusable agent capability needs a service owner

[Download the matching notebook](/downloads/14-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md) · [Integration plan](04-integration-plan.md)

## Business context: Harbour

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

Who maintains the shared capability in this proposal?

```python
service={"capability":"read_case","service_owner":"case platform","data_owner":"operations records","consumer":"investigation assistant"}
print(service)
```

case platform is the named service owner; source corrections remain a separate responsibility.

### Complete the exercise

Write the prediction before consulting the worked answer: Who maintains the shared capability in this proposal?

**Worked answer.** case platform is the named service owner; source corrections remain a separate responsibility.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour wants tools that different assistants can discover and use consistently. A case lookup and policy search could be exposed through MCP, but discovering a tool does not grant a regional user new access or authorise a financial action.

**Task:** Document one capability’s owner, allowed inputs, scope, output meaning, failure contract and support route.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Expose a bounded read with server-side scope and source identity. An unavailable result should remain unavailable rather than becoming invented evidence. The local teaching MCP connection does not establish remote authentication or a production finance integration.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.
