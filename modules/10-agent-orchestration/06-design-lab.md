# Lesson 10.6: Compare central coordination with specialist ownership

[Download the matching notebook](/downloads/10-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../11-agent-teams/README.md)

## Two architectures express different working assumptions

**Fictional case.** Harbour considers a central coordinator that gathers specialist advice and composes the response. A second proposal transfers cases to a specialist service that continues the conversation. The code can implement both. The organisation must decide what responsibility each arrangement expresses.

A coordinator is useful when one case owner must integrate bounded contributions. Specialist ownership is useful when the specialist needs sustained interaction and can accept responsibility for that part of the work. A runtime handoff without a receiving arrangement supplies neither reliably.

## Complete the contribution contract

| Boundary | Producer supplies | Consumer must decide |
|---|---|---|
| Order evidence | Record identity, version, quantities, uncertainty | Whether evidence is sufficient for the case |
| Policy advice | Applicable scope, current rule, unresolved interpretation | Whether the proposal follows the rule |
| Draft | Claims tied to sources and missing information | Whether to approve, revise or seek more evidence |
| Specialist transfer | Case, scope, pending work and reference | Whether ownership is accepted and when action is due |

This is producer-consumer coordination. A message can arrive successfully while failing the consumer's need. An acceptance criterion explains what usable completion means; a notification alone does not.

## Parallel reads redistribute effort

Suppose order and policy reads each take four minutes, while integration takes three. A sequential route takes eleven minutes before review. Overlapping the independent reads can reduce that idealised interval to seven. The calculation assumes both begin promptly and neither needs clarification from the other.

If half the cases require policy to interpret the order evidence, the dependency is partly sequential. Launching both immediately may produce rework. Measure actual case types rather than treating concurrency as a universal improvement.

The human system has capacity limits too. Faster evidence gathering can send more drafts into a fixed review window. Harbour schedules review capacity and limits intake to match the pilot. Software overlap and organisational workload are connected but distinct questions.

## A worked allocation choice

Harbour keeps the account manager as case owner. Order and policy specialists provide bounded contributions through tools. Finance accepts sustained ownership only for a defined remedy-review stage, with an explicit acceptance event. The coordinator may compose a draft but cannot infer that acceptance from having called a finance-named agent.

The design records missing contributions and disputed conclusions separately. A source outage goes to the operator and case owner. A disagreement over policy interpretation goes to the policy owner. A model-format failure goes to application maintenance. One generic “agent failed” status would obscure those different responses.

## Investigate whether the arrangement works

The pilot compares supported drafts, clarification loops, accepted transfers, specialist effort and elapsed case time. It also follows several difficult cases through actual conversations. Gittell's relational coordination perspective asks whether specialists share goals, understand one another's contributions and communicate to solve problems. Those conditions cannot be read from an orchestration graph.

If technical handoffs succeed but specialists repeatedly return cases as unusable, improve the contribution contract and receiving arrangement. Another coordinator agent may simply accelerate the same misunderstanding.

**Worked challenge:** A manager wants to call the coordinator “autonomous operations director”. What evidence would justify greater authority? Define the precise decision opportunity, relevant premises, evidence, acceptance and accountability first. A more senior agent name changes none of them.

**Research basis:** [Coordination](../../reference/research/02-coordination.md) and [decision theory](../../reference/research/03-decisions.md).

## Read the organisational connection

Specialist contributions need to justify the coordination work their separation creates. The research chapter explains [decomposition and integration](../../reference/research/01-organisation-design.md#when-more-agents-create-more-integration-work).
