# Lesson 14.7: Connect the interface, feedback and ongoing service

[Module route](README.md) · [Return to the integration plan](04-integration-plan.md)

## What you'll learn and why it matters

Connect visible status, stored work and feedback to the decisions Harbour makes after rollout. Use that distinction to judge whether a service is ready to expand.

“Submitted” on a screen might mean the request was received, while “accepted” should tell the adviser a reviewer has taken responsibility. The backend is the software behind the screen that stores and processes the work. Match each visible status to what the backend knows and give staff a way to report a misleading status.

## The backend and the screen expose different views

The Agents course's final project separates an operating backend from a frontend. Its [read-only API](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/api.py) returns accounts, holdings, market-source status and logs. The engine changes the example account data elsewhere. A dashboard refresh therefore observes selected state; it is not the action itself.

The API also derives values, such as current holdings value, from stored positions and market information. A derived display can change because the source price changes even when no new trade occurs. In a business service, the same issue appears when a case screen combines authoritative records, delayed copies and calculated status.

## Define what a status promises

Harbour distinguishes `draft_saved`, `submission_acknowledged`, `accepted_by_team` and `resolved`. Each status has a source and meaning. The interface shows stale or unavailable observations explicitly. It does not turn a green network response into a claim that the customer problem was solved.

An error shown only in a server console can leave the user facing an old success state. The application needs a visible failure or freshness indicator and a route for unresolved work. Observability includes serving the person waiting, not only helping engineers debug.

## Feedback must identify what should change

A thumbs-down signal can mean wrong source, poor retrieval, misunderstood policy, unsuitable category, inaccessible evidence or unacceptable wording. Store a bounded reason and link it to the relevant case/configuration where appropriate. The response owner can then distinguish source correction, software repair and organisational redesign.

Do not automatically turn every correction into training data. A reviewer may be wrong, a policy may have changed, or a workaround may be temporary. Adjudication and versioning determine whether feedback expresses a new desired target.

## A comparative review over time

| Period | Observation | Inquiry and response |
|---|---|---|
| First week | Many missing-source drafts | Repair source access and intake, retain failed cases |
| Stabilisation | Review queue grows | Examine scope, effort, capacity and escalation |
| Recurrent use | Staff bypass one category | Investigate misfit and actual work before blaming adoption |
| Policy change | Old recommendations reappear | Check source/index/cache/model contracts and reevaluate |
| Expansion | New case types perform unevenly | Establish a new population and comparison |

This is a learning lifecycle, not an assumption that benefits inevitably grow. Some use cases should remain narrow or be withdrawn. A useful service review can recommend a simpler design when maintenance or coordination cost exceeds the contribution.

## Preserve the different levels of evidence

Inspecting a prompt establishes represented design. Testing enabled tools establishes selected configuration. Deployment records establish an installed arrangement. Repeated observation and situated accounts help examine use. Outcome comparisons support claims about consequences under stated conditions. Moving up this chain requires additional evidence.

The [technology and organisation review](../../reference/research/06-technology-in-practice.md) explains why a feature, possibility, actualisation and outcome are distinct. The [implementation review](../../reference/research/04-implementation.md) connects fit and adjustment beyond go-live.

**Worked final judgement:** An agent has run for three months with no process crashes. That is useful availability evidence. To decide whether it should expand, also examine supported work, changed effort, accepted responsibility, recovery, affected actors and business outcomes. The course's technical patterns become valuable through those concrete arrangements, rather than through the label “agentic” alone.

## Read the organisational connection

Continuing evaluation should examine which changes actually account for a service improvement. The research chapter explains [redesign and rival explanations](../../reference/research/06-technology-in-practice.md#a-worked-redesign-and-its-rival-explanations).

## What to remember

A read-only dashboard observes selected records. Draft, acknowledgement, acceptance and resolution each represent different events. Feedback and comparison over time show where the work needs repair.

## What this means for the business process

Tie each customer-facing status to its source event and give advisers a route to challenge stale or misleading states. Before expanding, examine acceptance, review work and customer resolution as well as uptime.

For the research behind this design choice, read [Worked design: extend the boundary of success](../../reference/research/09-process-architecture.md#worked-design-extend-the-boundary-of-success).

## Put it to work

Take the companion workbook into a process of your own. Define what the AI contribution should produce, who accepts it and how you will measure what happens after the handoff. [Companion workbook](../../WORKBOOK.md).
