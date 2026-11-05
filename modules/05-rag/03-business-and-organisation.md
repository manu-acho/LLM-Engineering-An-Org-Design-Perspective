# Lesson 5.3: A knowledge assistant is also a design of authority

[Download the matching notebook](/downloads/05-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## Three sources tell different stories

**Fictional case.** Harbour has an approved credit policy, a team procedure and an interview with an experienced account manager. The policy assigns disputed credits to finance. The procedure asks operations to verify delivery first. The account manager says small cases are often resolved informally to preserve customer relationships.

A user asks, “Who approves a small disputed credit?” A single smooth answer could hide three different kinds of source: a formal rule, a prescribed sequence and an account of practice.

## Representations deserve different interpretations

The routines review separates written objects, people's understandings and what they do in particular situations. A policy is evidence of a formal rule. An interview can reveal one person's understanding and experience. It does not independently establish how all cases are handled. Repeated observations and event evidence may establish patterns while still missing off-system conversations.

The assistant should preserve source type rather than treating every sentence as an equivalent fact. A useful answer may say what the approved rule requires, what supporting procedure describes and what an interview suggests should be investigated.

The same distinction matters in research. A retrieved interview passage is evidence for analysis, not a completed theoretical explanation. A generated theme needs examination against counterexamples and the study's method.

## Finding language does not reconcile knowledge

Carlile, discussed in Research chapter 2, helps explain why sharing information can still leave disagreement. Common fields and vocabulary can help with a **syntactic** boundary, a difference in how information is represented. Explaining that “approval” means financial authorisation to one team and customer agreement to another addresses a **semantic** boundary, a difference in meaning. If teams disagree about acceptable risk or response time, they face a **pragmatic** boundary: different interests that may require negotiation.

An assistant can help expose those differences by showing passages side by side. It should not silently transform an unresolved policy dispute into a new policy. That would allocate decision authority through a text-generation step without an agreed mandate.

## The index and prompt influence which claims count

The decision-premise lens from Research chapter 3 applies before the final answer. Which documents are indexed? Which source types rank higher? Does the prompt treat official policy as binding, and how does it handle local exceptions? Who sets the current-version flag?

These are governance choices. A technical team can implement them, but the organisation must own them. A passage can resemble the question closely without being the right authority for an answer. The organisation needs rules about which sources take priority for this task.

A project team can make this practical by creating a source registry during its initial investigation. Record source owner, scope, version rules, status, update mechanism and how users challenge an answer. This also exposes whether the client has a knowledge-governance problem that must be addressed alongside retrieval.

## Design for disagreement and correction

For policy questions, distinguish current authoritative instructions, contextual accounts and unresolved conflicts. For research exploration, permit multiple interpretations and make their origins visible. The same corpus can support different tasks only if the response rules make that distinction clear.

A correction route needs an owner and an expected action. A “thumbs down” is useful feedback only if someone can diagnose whether the problem is a source, access rule, retrieval result or answer. Repeated corrections may reveal a flawed category rather than isolated generation errors.

## Retrieval creates possibilities differently for different actors

The search workshop filters records before returning them. That materially changes what the answer can draw on. It is evidence of a technical boundary, not proof that every authorised user can understand or resolve what they retrieve.

For a policy owner with source access and revision authority, a conflict display may enable correcting inconsistent instructions. For a frontline user, it may enable recognising uncertainty and escalating, while leaving resolution outside their authority. Research chapter 6 calls these **candidate affordances**: proposed possibilities for particular people to act through the system. They remain candidates until the necessary conditions and use are investigated.

A filter can support confidentiality while limiting the evidence available for a case. Keep that trade-off visible. A prompt asking for certainty cannot repair an intentionally unavailable source or confer authority to adjudicate a dispute.

Specify what each user can do after finding conflicting passages. Then trace whether that action occurs and reaches an owner who can respond. This investigates actualisation instead of equating retrieval success with knowledge governance. The transfer is based on [Research chapter 6](../../reference/research/06-technology-in-practice.md).

## Apply the idea

Draft an answer using the three fictional sources. What additional evidence would you need before recommending a change to the process?

**Worked answer:** “The approved policy assigns disputed credits to finance, and the procedure calls for delivery verification by operations first. One account-manager interview describes informal handling of some small cases; this is a reason to investigate practice and authorised exceptions, not evidence that the formal policy has changed.”

The answer is longer than “finance approves”, but its distinctions are useful. If the task is a frontline instruction, the assistant should foreground the current approved rule. If the task is a research memo, the tension itself is analytically important.

**Rival explanation:** Informal resolution may be an accepted exception, a workaround, a reporting misunderstanding or unauthorised action. One interview does not settle which. Identify who to speak with and what cases to examine.

**Try it:** Map which sources have authority for which claims. Then describe two answers, one for operational guidance and one for research analysis. Explain why they should differ.

**Research basis:** [Research chapter 2](../../reference/research/02-coordination.md), [Research chapter 3](../../reference/research/03-decisions.md) and [Research chapter 5](../../reference/research/05-routines.md). The linked chapters explain these perspectives; the fictional case illustrates their application.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Access to a policy passage does not confer authority to settle a disputed interpretation. The research chapter explains [permission and authority](../../reference/research/03-decisions.md#permission-and-authority).
