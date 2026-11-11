# Lesson 3.3: When meeting notes become an organisational record

[Download the matching notebook](/downloads/03-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## Business context: Harbour

“We could review the backlog on Friday” is a suggestion in a meeting. In notes, “Warehouse will review the backlog on Friday” gives a team an apparent commitment. Follow who said the original words, how the draft changed them and who can accept or correct the final record. A shorter sentence can assign work that nobody agreed to take.

A meeting-note example tests whether a proposed follow-up becomes an invented commitment. Apply that distinction to investigation ownership without adding the meeting to H-17.

[Company and supply-chain context](../../HARBOUR.md) · [Module 3 business situation](../../reference/harbour-learning-journey.md#module-3)

## A sentence becomes a commitment

**Fictional case.** In Harbour's meeting, an account manager says, “If the recount confirms the shortage, finance could consider a credit.” An AI note says, “Finance will issue a credit.” The note is clear and concise. It also removes a condition, changes a possibility into a commitment and reallocates responsibility.

This is not merely a writing-quality issue. A meeting note can become the record on which later work depends. We need to examine both how the note was produced and how the organisation adopts it.

## Follow the transformations

An audio-to-notes system can contain recording, transcription, speaker attribution, summarisation and action extraction. Each stage can change meaning. A transcription error may miss “not”; a speaker label may assign a statement to the wrong person; a summary may compress disagreement; an action extractor may infer an owner that nobody accepted.

An end-to-end assessment should identify where a disputed claim first appeared. Preserve links to transcript passages and, where appropriate, audio times. That supports correction and helps separate upstream errors from later transformations.

Do not promise that a local model resolves the organisational problem. Local inference changes one part of the technical arrangement. Who confirms the note remains an organisational design choice.

## Shared text and shared meaning

Research chapter 2's knowledge-boundary discussion explains why a common representation can coexist with different meanings. Sales may hear “resolution” as a promise to preserve the customer relationship. Finance may hear it as completion of evidence and authorisation requirements. A summary that says “resolution agreed” can conceal that difference.

Carlile distinguishes three kinds of knowledge boundary. A **syntactic boundary** concerns how information is represented: common fields or formats may help. A **semantic boundary** concerns meaning: teams need to explain what their terms mean. A **pragmatic boundary** involves different interests: teams may need to negotiate what should happen, even when they understand each other. An LLM may assist with identifying and articulating these differences. Generating a smooth paragraph does not establish agreement.

The practical design is to distinguish a proposal, a question, a conditional commitment, an agreed action and an objection. An unresolved statement should remain unresolved in the record.

## Artefact, understanding and performance

The routines review distinguishes the note as an artefact from participants' understandings and subsequent actions. Participants may refer to the note as the official account while relying on private follow-ups to make the work possible. A repeated pattern of those activities requires evidence across meetings and later work, not just one document.

Feldman and Pentland distinguish the **ostensive** aspect of a routine, how people understand it, from its **performative** aspect, what people do on particular occasions. Here that means asking both how participants describe meeting follow-up and how they actually carry it out. The note may influence both, but it is not either by itself.

If staff routinely correct an AI note after circulation, the correction task is part of the work created by the application. It belongs in the benefit assessment, even if the original transcription took only a minute.

## Fit includes roles and controls

Research chapter 4 broadens fit beyond functionality. A note generator can perform its technical function while fitting roles or controls poorly. Perhaps the person expected to confirm notes lacks access to the source meeting. Perhaps a team uses discussion as exploration and finds premature action extraction disruptive.

These are design issues to investigate rather than evidence that all automated notes are unsuitable. Options include a draft-only mode, participant confirmation, a separate decision register or limiting extraction to explicitly agreed markers.

## Editable text and a contestable record are different possibilities

An editable AI note is a feature. The possibility for a participant to correct a commitment depends on more: access, time to review, knowledge that the note exists and a process recognising corrections. Research chapter 6 calls attention to this relation between an actor, an arrangement and a goal.

For the meeting chair, a confirmation field may support maintaining an agreed action record. For a specialist absent when the note circulates, it may not supply a workable opportunity to contest an assigned action. The technical property is the same; the relevant action conditions differ.

Examine the material details too. A label saying “confirmed” and a link to the supporting passage make different claims from an unlabeled generated action. Hosting the model locally changes a data path; it does not establish these review and correction arrangements.

For the exercise below, trace a disputed note from draft through correction to the version another team actually uses. That sequence helps investigate **actualisation**, the process through which a possibility is realised over time. The interpretation draws on [Research chapter 6](../../reference/research/06-technology-in-practice.md) and remains a fictional teaching application.

## Apply the idea

Return to the conditional credit sentence above. A second person at the meeting adds, “I disagree until the warehouse has checked.” Design three fields for an action record and decide who could confirm them.

**Worked response:** A useful record may contain the exact proposed action with its condition, the proposed owner and acceptance status, and supporting transcript spans including the objection. A due date should be absent unless stated or separately agreed. An incomplete field is preferable to invented certainty.

**Alternative:** A facilitated decision log completed during the meeting may be better for commitments, while AI notes assist with general discussion summaries. The correct choice depends on the meeting's purpose and the cost of confirmation.

Measure false commitments, missing conditions, wrong ownership, correction effort and whether participants can contest the record before others act on it. Shorter notes alone do not show improved coordination.

**Research basis:** [Research chapter 2](../../reference/research/02-coordination.md) on knowledge boundaries; [Research chapter 4](../../reference/research/04-implementation.md) on multidimensional fit; [Research chapter 5](../../reference/research/05-routines.md) on artefacts and recurrent work. The applications are illustrative transfers, with the [evidence distinctions](../../reference/literature-guide.md) retained.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

A generated meeting record is an artefact, distinct from participants' accounts and actions. The research chapter explains [understandings and performances](../../reference/research/05-routines.md#understandings-and-performances).

## Practical activity: Preserve the difference between a suggestion and a confirmed commitment.


The notebook is the easiest way to run this activity. Its first cell loads the course settings. `ROOT` records where the course files are, and `RUN_LIVE` records whether the optional provider call is enabled. The local steps can be read with live mode off. When running the snippets outside the notebook, use this setup once from a prepared checkout:

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

Does this source establish an accepted owner?

```python
meeting = {"source_id":"meeting-1","statement":"Sara suggests checking on Friday.","confirmed_owner":None}
assert meeting["confirmed_owner"] is None
print(meeting)
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    answer = gateway.generate("Source meeting-1: Sara suggests checking on Friday. Prepare one note and list what needs confirmation. Do not convert a suggestion into a commitment.")
    print(answer.text)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. A suggestion does not establish that Sara accepted responsibility or that Friday became a deadline.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour is considering how to obtain model capability for internal investigation notes. Hosting locally may change where data is processed, but it also creates responsibility for model files, updates and support. A separate meeting-note illustration examines whether a suggestion can be mistaken for an accepted commitment; it is not additional delivery evidence.

**Task:** Compare a local model and a provider service for Harbour’s preparation task, including data access, technical support and fallback.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Local execution can give direct control over model files and processing location, but someone must maintain the environment and investigate bad outputs. A provider reduces some hosting work while adding service and data-handling dependencies. Neither supplies record authority or business approval.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.
