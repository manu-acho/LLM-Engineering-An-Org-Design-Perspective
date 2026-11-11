# Lesson 14.7: Connect the interface, feedback and ongoing service

[Download the matching notebook](/downloads/14-07-service-evaluation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Return to the integration plan](04-integration-plan.md)

## What you'll learn and why it matters

Connect visible status, backend state and feedback to the work that follows. Harbour needs an interface that tells people who is acting and how to raise a problem.

## Business context: Harbour

“Submitted” on a screen might mean the request was received, while “accepted” should tell the adviser a reviewer has taken responsibility. The backend is the software behind the screen that stores and processes the work. Match each visible status to what the backend knows and give staff a way to report a misleading status.

Check integration claims against the actual local protocol and the enterprise controls still required.

[Company and supply-chain context](../../HARBOUR.md) · [Module 14 business situation](../../reference/harbour-learning-journey.md#module-14)

## The backend and the screen expose different views

A service screen and its backend expose different views. In the local Harbour HTTP application, a case read reports stored state while a separate decision route changes it. Refreshing a screen observes a selected state; it is not the business action itself.

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

## Practical activity: Observe changed backend state through a fresh read.


### Predict and follow the values

Does a screen refresh itself perform the decision?

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from ai_orgdesign.business import CaseStore
with TemporaryDirectory() as directory:
    store=CaseStore(Path(directory)/"service.db");store.seed()
    before=store.read("H-17","north")
    store.decide("H-17","north","reviewer","manager",1,"return","observe")
    after=store.read("H-17","north")
    print("Before:",before["status"],"After:",after["status"])
```

### Complete the exercise

**Worked answer.** No. A read observes the state changed by the separate authorised command.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A displayed status should correspond to something the service knows. Feedback is more useful when it identifies the affected case, claim or step.

## What this means for the business process

Define which event justifies showing that a case was accepted, and give advisers a route for reporting a misleading status. Examine actual use after release to see whether the intended feedback path is usable.

For the research behind this design choice, read [Actualisation: from possibility to action](../../reference/research/06-technology-in-practice.md#actualisation-from-possibility-to-action).

## Next lesson

Part 3 begins by taking an observed problem and turning it into a bounded pilot with explicit acceptance conditions. [Lesson 15.1: From a business problem to a pilot](../15-problem-to-pilot/01-concepts.md).
