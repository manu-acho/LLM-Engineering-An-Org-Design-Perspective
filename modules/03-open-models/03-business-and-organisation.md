# Lesson 3.3: When meeting notes become an organisational record

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## What you'll learn and why it matters

Trace how spoken words become an organisational record. Identify where a suggestion can turn into an apparent assignment and who needs to correct it.

“We could review the backlog on Friday” is a suggestion in a meeting. In notes, “Warehouse will review the backlog on Friday” gives a team an apparent commitment. Follow who said the original words, how the draft changed them and who can accept or correct the final record. A shorter sentence can assign work that nobody agreed to take.

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

The research chapter also explains [how shared records acquire consistent meanings](../../reference/research/07-infrastructure-and-standards.md#standards-make-comparison-possible-and-require-continuing-work).

## What to remember

A recording, transcript, draft summary and accepted record serve different purposes. Compressing a tentative statement can make it sound like a commitment.

## What this means for the business process

Have the meeting owner confirm assignments with the people who will carry them out and provide a correction route. A shared note helps coordination when readers can tell what was agreed, by whom and with what authority.

For the research behind this design choice, read [Shared data and shared meaning](../../reference/research/02-coordination.md#shared-data-and-shared-meaning).

## Next lesson

Having seen what a fluent summary can change, next trace how a model's numerical representations produce that text. [Lesson 3.4: Follow numbers through a small language model](04-inside-inference.md).
