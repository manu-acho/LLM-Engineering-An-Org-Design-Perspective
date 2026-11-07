# Lesson 3.6: Design the meeting record and its correction process

[Download the matching notebook](/downloads/03-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../04-evaluation/README.md)

## Business context: Harbour

Choose a hosting arrangement with named support and update responsibilities as well as data-handling requirements.

[Company and supply-chain context](../../HARBOUR.md) · [Module 3 business situation](../../reference/harbour-learning-journey.md#module-3)

## Begin with the work the record must support

**Fictional case.** Harbour's weekly meeting produces notes that sales uses for customer communication, finance uses for control and operations uses for follow-up. The teams disagree about what “agreed” means. An automatic note generator could make this disagreement less visible by producing one smooth account.

Carlile's knowledge-boundary argument helps separate three problems. Different formats create a syntactic boundary. Different meanings of “agreed” create a semantic boundary. Different interests in speed and financial exposure create a pragmatic boundary. A common document can help the first while leaving the other two unresolved.

## Compare three records

| Record design | Useful contribution | Work still required |
|---|---|---|
| Free-text summary | Fast orientation | Locate original statements and check inferred commitments |
| Evidence-linked draft | Inspect claims beside transcript spans | Confirm source interpretation and proposed owner |
| Confirmed action register | Support follow-up on accepted actions | Negotiate unresolved commitments and maintain corrections |

Harbour selects a draft plus confirmed register. An automatically extracted action remains `proposed` until the named owner confirms or rejects it. Confirmation concerns the action and its conditions; it is not approval of every sentence in the summary.

## Work one statement through the design

The transcript contains: “If the warehouse confirms two missing boxes, finance could review a credit on Thursday.” The draft creates these fields:

| Field | Value |
|---|---|
| Evidence | Transcript span T-44, speaker finance representative |
| Proposed activity | Review possible credit |
| Condition | Warehouse confirms shortage |
| Proposed timing | Thursday |
| Status | Unconfirmed proposal |

Operations corrects the expected recount date to Friday. The action owner then accepts review after Friday's result. The register keeps a revision and the confirming actor. The earlier draft is retained as a draft, not silently rewritten into evidence that Thursday was ever an agreed commitment.

This is a material design choice: status, version and source fields change what can be recorded. Whether participants actually use the correction route requires observation. A visible edit button alone does not establish that a junior employee can challenge a senior manager's account.

## Follow the routine over three meetings

At the first meeting, staff correct many owner assignments. At the second, they begin saying proposed owners explicitly. At the third, one team moves difficult discussion into a separate call to avoid premature recording. The note generator has entered a changing routine.

Feldman and Pentland's ostensive/performative distinction helps interpret this. Participants' understandings guide performances; performances can maintain or alter those understandings. The register is a separate artefact participating in the relationship. Off-system calls may represent useful specialist adjustment, a control problem or both. Their meaning cannot be inferred from their absence in the log.

## Make the operating choice explicit

Sales gains a clearer basis for communication after confirmation. Finance retains the right to correct a misrepresented condition. Operations owns recount evidence. The meeting chair owns unresolved assignments, while the source owner handles transcript corrections. Store only the recording and transcript needed for the agreed purpose and retention arrangement; a technical preference for “more context” does not define that purpose.

The pilot compares omitted conditions, incorrect owners, time spent confirming notes and subsequent clarification. If confirmation takes longer but prevents consequential wrong commitments, the decision requires weighing those outcomes. A note count or a shorter summary is insufficient.

**Worked decision:** Staff stop using confirmation because they cannot open transcript spans. Address access, presentation and review time first. This is a misfit between the feature and the role's conditions, rather than immediate evidence that local models or employees are the problem.

**Research basis:** [Coordination](../../reference/research/02-coordination.md), [routines](../../reference/research/05-routines.md) and [technology in practice](../../reference/research/06-technology-in-practice.md).

## Read the organisational connection

A correction interface needs to connect to the recurring work of confirming and using the record. The research chapter explains [artefacts and patterns of action](../../reference/research/05-routines.md#designing-an-artefact-and-designing-a-pattern).

## Practical activity: Compare hosting decisions using a specified data path.





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

Which listed path sends text to a model provider?

```python
paths = {"hosted_text":["local record","provider","local review"],"local_text":["local record","local model","local review"]}
for name, path in paths.items():
    print(name, " -> ".join(path))
```

hosted_text does. A local text model would not make a separate cloud transcription stage local.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

```python
if RUN_LIVE:
    answer = gateway.generate("Describe one advantage and one operating responsibility of hosting a language model locally. Keep the answer specific to a fictional meeting-note service.")
    print(answer.text)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

Write the prediction before consulting the worked answer: Which listed path sends text to a model provider?

**Worked answer.** hosted_text does. A local text model would not make a separate cloud transcription stage local.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
