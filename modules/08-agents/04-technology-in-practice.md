# Lesson 8.4: From an AI feature to a way of working

[Module route](README.md) · [Literature foundation](../../reference/literature-guide.md)

## What you'll learn and why it matters

Explain how a feature becomes usable for a particular person in practice. Use the approval panel to identify what an adviser or reviewer can actually do.

The approval screen may exist, but if staff cannot see the carrier record there, they may approve from email instead. An affordance is a possibility for action in relation to a person and their circumstances. Ask who can actually inspect the record or correct the status on this screen. The feature list alone does not answer that question.

## The approval panel that nobody uses

**Fictional continuing case.** Harbour adds an evidence panel to the credit-review screen. It displays the order, complaint and policy extracts beside an AI recommendation. The project team describes this as “transparent AI review”. Three weeks after launch, reviewers still ask account managers to send screenshots by email.

Several explanations are possible. The panel may contain incomplete records, use unfamiliar labels or be unavailable to an important reviewer. Reviewers may trust the email sender more than the indexed source. Their allotted review time may be too short. Or they may not yet have learned that the panel supplies the necessary evidence.

The feature exists. Its relation to the work is still a question. Research chapter 6 gives us a vocabulary for investigating that relation without assuming either that the feature determines practice or that its technical design is irrelevant.

## Materiality: digital arrangements can make a concrete difference

**Materiality** concerns the properties and arrangements through which a technology makes actions possible, difficult, visible, durable or unavailable. Digital systems have material consequences even though their records are not sheets of paper. A mandatory field can block submission. A permission check can deny a lookup. A missing source ID can make an answer harder to verify.

Connect this to the code you have read. Module 2's dispatcher checks permitted order IDs before performing a lookup. Module 5's retrieval function excludes records outside scope. Module 8's simulator refuses an unapproved action. These are inspectable technical operations. Describing them does not yet tell us whether people regard the restrictions as legitimate, whether they have alternatives or how work proceeds after a block.

Treating software as consequential does not require treating it as an autonomous organisational cause. A blocked transaction is a technical event; its contribution to delay, better control or off-system work needs further evidence.

## Affordance: a possibility for someone to do something

An **affordance** is a relational possibility for action involving an actor, an arrangement, a goal and relevant conditions. Start with four ordinary questions: Who is trying to do what? Which arrangement could help? Under what conditions could they use it? What might prevent that?

The evidence panel contains links. That is a feature description. For a finance reviewer who has access, understands the records and has time to compare them, it may afford checking the recommendation against source evidence. For an account manager without policy-source access, the same panel may not offer that possibility. Naming the feature alone would miss the difference.

State the possibility and its conditions separately. For example: “The panel may help finance reviewers compare a recommendation with current policy. They need access to the passages, the ability to interpret them, and a way to act when they disagree.” This is a proposal to investigate, not proof that checking happens.

## Constraints depend on goals too

Suppose submission requires a complete delivery-receipt ID. The requirement can support a controller's consistent checking. For an intake worker handling a customer whose receipt is unavailable, it can prevent a valid issue from entering the workflow.

The same rule can enable one activity and constrain another. Do not label every constraint a harm or every removed constraint an improvement. Investigate the goals and consequences. Possible designs include a documented exception state, a pending-evidence route or a different minimum-evidence rule. Removing the field may solve intake while weakening later checks; leaving it unchanged may move valid work into email.

## Actualisation: the work between availability and outcome

**Affordance actualisation** concerns actions through which a possibility is realised in an organisational setting over time. It may involve learning the panel, repairing source links, adjusting review responsibilities, negotiating response times and revising exception handling.

Actualisation is not the same as switching the feature on. Nor does an increased click count prove that meaningful checking happened. To study it, follow cases: which sources were consulted, what differences were noticed, who could correct a record and how the result affected the next activity. Inspect change over time and the work that remains outside the application.

The source review discusses affordance actualisation through work including a longitudinal electronic-health-record study. Here we use its conceptual questions to design an AI inquiry. We do not transfer its detailed stages or findings as established facts about Harbour.

## Six separate claims, six evidence needs

| Claim about Harbour | What could support it | What that evidence does not establish alone |
|---|---|---|
| The design includes evidence links | Versioned interface/specification inspection | That the links were enabled locally |
| Finance has source access in this deployment | Configuration and permission tests | That reviewers have an appropriate working arrangement |
| A review role and procedure are in operation | Deployment, role and procedure evidence | How reviewers perceive or use them |
| Reviewers believe they can challenge the recommendation | Situated accounts and elicitation | That they actually challenge it when needed |
| Reviewers repeatedly compare sources and raise discrepancies | Repeated observation and trace evidence with off-system inquiry | A beneficial outcome merely because checking occurs |
| Incorrect credits or review effort changed | Suitable outcome comparisons linked to process evidence | That the feature alone caused the change |

This is a teaching adaptation of the six-layer synthesis in the linked literature review. It is not a single model taken from one theorist. Keep unsupported layers unknown rather than filling them with a plausible story.

## Further depth: different ways to explain technology in practice

The review uses Orlikowski's practice lens to distinguish a system's capabilities from structures enacted through recurrent use. One team might make the panel its working record. Another might enter minimal information and coordinate through email. These possibilities need observation rather than inference from the interface.

Research chapter 6 also discusses **sociomateriality**. Some accounts argue that people and technology are so bound together in an activity that separating a purely social part from a purely technical part distorts what is happening. This is what **constitutive entanglement** means here.

Other approaches preserve a distinction between people and technical arrangements. **Critical-realist affordance** accounts examine how relations between them make actions possible under particular conditions. **Imbrication** examines how human goals and the effects of material arrangements become interlocked over time. The review records real disagreements between these positions. They are not interchangeable names for “people plus technology”.

For the example here, we examine people, arrangements, goals and evidence separately. We are not claiming that it resolves the philosophical disagreement. For a research paper, choose and justify an approach compatible with the question and method before combining these vocabularies.

## Apply the idea: two people, different conditions

Consider two people using the panel: a finance reviewer with authority but little time, and an operations specialist with expertise but no permission to open the sources. For each person, complete this sentence: “The panel may enable ___ to ___, provided ___; it may constrain ___ when ___.”

**What the example shows:** Finance's formal authority does not supply review time. Operations' expertise does not supply access or authorisation. Appropriate responses may involve role design, limited permitted access, better source presentation or a changed escalation route. Asking the model to explain more confidently does not remedy those missing conditions.

Now suppose the pilot reports an improvement. Could clearer policy or extra reviewer staffing help explain the result? Specify what evidence would distinguish the contribution of those changes from the contribution of the panel. The aim is a stronger explanation, not a predetermined pro- or anti-technology verdict.

## Try it

Extend the capstone operating design with two actor-specific affordance/constraint statements, an account of the actions needed for actualisation and an evidence plan across the six layers. Connect at least one statement to an actual code check or representation from an earlier workshop. This preserves technical precision while asking what the mechanism means for particular work.

**Research basis:** [Research chapter 6](../../reference/research/06-technology-in-practice.md). The chapter explains the concepts, theoretical disagreements and evidence distinctions introduced in this lesson.

## Read the organisational connection

The relevant question names an actor, action, goal and conditions rather than only a feature. The research chapter explains [features, affordances and constraints](../../reference/research/06-technology-in-practice.md#feature-affordance-and-constraint).

## What to remember

The same panel offers different possibilities depending on access, information and working conditions. Observed use is a further step beyond the feature's existence.

## What this means for the business process

Observe a real review task during the pilot. If reviewers still switch to email because carrier evidence is missing from the panel, address access and the correction route before interpreting button use as meaningful review.

For the research behind this design choice, read [Actualisation: from possibility to action](../../reference/research/06-technology-in-practice.md#actualisation-from-possibility-to-action).

## Next lesson

Next follow the original capstone across remote calls, storage and display to identify what can go wrong before the adviser sees a result. [Lesson 8.5: Trace the capstone across models, services and stored work](05-source-walkthrough.md).
