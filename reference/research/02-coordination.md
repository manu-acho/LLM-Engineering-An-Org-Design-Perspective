# Research chapter 2: Coordinating people, teams and AI systems

[Research reading guide](../literature-guide.md) · [Previous: organisation design](01-organisation-design.md) · [Next: decisions](03-decisions.md)

Read [Meet Harbour](../../HARBOUR.md) for the shared fictional company. In this chapter, its delivery-investigation work illustrates the dependencies between source collection, investigation, review and settlement. The case is an application of the research concepts, not evidence for the original studies.

## A handoff can arrive without becoming usable

**Fictional teaching case.** Harbour's assistant sends a shortage brief to operations. The software records a successful delivery. Operations returns the case: the brief has an order number but no distinction between the customer's report and the warehouse's shipment count. Sales regards the handoff as complete. Operations regards it as unusable.

The transport worked. The dependency remains unresolved. A receiving activity needs a contribution with particular content, meaning and timing, not merely a message that has arrived.

This chapter begins with that dependency, then asks how mechanisms support coordination, why shared data can leave meanings unresolved, and why expertise and repair remain important. The examples apply the literature to AI-supported work. They are not reports of observed deployments.

## Identify what depends on what

Malone and Crowston (1994) frame coordination as managing dependencies among activities. Their interdisciplinary framework directs attention to what connects tasks and to alternative ways of managing those connections. It does not make every technical connection an organisational coordination mechanism. [Malone and Crowston (1994)](#malone-and-crowston-1994)

A dependency can involve the flow of an output, competition for a resource or the need for contributions to fit together. These distinctions reveal different problems. A reviewer needs a draft before reviewing it. Several drafts may compete for the same reviewer. Separately produced sections may disagree about what “confirmed” means. One application can contain all three problems.

| Dependency in the fictional service | Possible response | What still needs checking |
|---|---|---|
| Operations needs shipment evidence | An evidence requirement and acceptance check | Whether the source is current and understood |
| Cases compete for reviewer attention | A queue, priority rule and allocated capacity | Whether priorities are suitable and waiting is acceptable |
| Customer and warehouse accounts must be reconciled | A shared case record and clarification process | Whether disagreement can be expressed and resolved |
| A specialist contribution must reach a suitable recipient | Named routing and an acceptance response | Whether the recipient is available and accepts the work |

The table is a teaching application of dependency reasoning, not a reproduction of one author's complete taxonomy. Its purpose is to make a design choice assessable. “Add orchestration” is too vague until the dependency and intended response are named.

## Mechanisms and conditions

A **coordination mechanism** is an arrangement intended to connect interdependent work. Plans, meetings, roles, routines and shared representations are examples. Okhuysen and Bechky (2009) distinguish such mechanisms from three **integrative conditions**: accountability, predictability and common understanding. [Okhuysen and Bechky (2009)](#okhuysen-and-bechky-2009)

Accountability in this coordination framework concerns making contributions and responsibilities identifiable. Predictability concerns anticipating how connected work will proceed. Common understanding concerns a sufficient shared interpretation of the work. These conditions help explain what a mechanism is intended to accomplish; the presence of a mechanism does not prove that the condition exists.

At Harbour, a named recipient makes intended assignment visible. It does not establish accepted ownership or an answerability relationship with consequences. A response deadline specifies an expectation. It does not establish that the receiving team can meet it. A shared brief offers a common reference. It does not establish common understanding.

**Application to code:** a function that places a case in a queue implements a routing operation. An acknowledgement records receipt. A separate acceptance state can record that the receiving service has accepted work against defined conditions. None of these records, alone, establishes that a person understood the case or that the problem was resolved. The distinction helps select useful states without making the log carry a stronger claim than it can support.

## Shared data and shared meaning

A common format helps exchange information, but different groups may interpret the same content differently. Carlile (2004) distinguishes syntactic, semantic and pragmatic knowledge boundaries, with transfer, translation and transformation as progressively more demanding responses. [Carlile (2004)](#carlile-2004)

A **syntactic boundary** concerns compatible representations. If both systems use the same order identifier and field structure, records can be transferred. A **semantic boundary** concerns different meanings. “Delivered” might mean that goods left the warehouse to one team and that the customer accepted them to another. Translation requires making these meanings explicit.

A **pragmatic boundary** involves different interests as well as knowledge. Sales may want to preserve the relationship quickly; operations may need to avoid accepting an unsupported shortage; finance may need defensible credit evidence. A common definition can leave these interests unresolved. Transformation can require changing the working arrangement or shared representation through negotiation.

An AI summary can make the boundary harder to see if it chooses one meaning and writes it fluently. A better summary can preserve the competing accounts, but it cannot itself establish an agreed resolution. This is a theoretical application to a fictional case, not a finding that language models necessarily create semantic conflict.

For technical design, distinguish schema validation from agreement about meaning. A JSON response can be structurally valid while its `status` field carries incompatible interpretations. The schema should document meanings and uncertainty; the organisational arrangement must provide a route to dispute or revise them.

## Bringing expertise into the work

Routing a task to a specialist label is insufficient if the necessary expertise cannot be mobilised. Faraj and Sproull (2000) connect expertise coordination with knowing where expertise is needed and located and bringing it into the work. Their study concerns software development teams; it does not establish the effectiveness of AI specialist agents. [Faraj and Sproull (2000)](#faraj-and-sproull-2000)

The practical distinction is between possessing a resource and being able to use it in time. A company may employ a policy expert who is not available to the case team. A model may have access to a policy document whose relevant exception is hard to interpret. In either situation, listing the resource does not settle the dependency.

Gittell (2002) adds relationships and communication: shared goals, shared knowledge, mutual respect and communication that supports problem solving. The healthcare setting of the original study limits direct transfer. For AI integration, the reasonable use is to investigate whether the surrounding human relationships support coordination, not to claim that an interface contains mutual respect. [Gittell (2002)](#gittell-2002)

## Coordination continues after configuration

Practice research treats coordination as work that participants keep accomplishing and modifying. Jarzabkowski, Lê and Feldman (2012) examine how coordination mechanisms emerge and change through disruption and stabilisation. [Jarzabkowski et al. (2012)](#jarzabkowski-l-and-feldman-2012)

**Illustrative application:** a new complaint type arrives with photographs that the brief cannot represent. Staff telephone the warehouse and add a note outside the usual form. This could be useful repair, an unsafe workaround or a symptom of unsuitable intake. The deviation alone does not decide which explanation is right. Observation should establish what problem staff encountered, what they changed and what happened downstream.

This matters for agent frameworks. A graph can specify an escalation edge. Actual coordination also depends on someone noticing the escalation, understanding the case and having a practical route to respond. Retry logic can repeat a request; it cannot make an unavailable specialist available or settle disputed ownership.

## Expertise, dialogue and the limits of a standard path

Expertise coordination has two connected demands. The organisation needs to recognise what knowledge a situation requires, and it needs to bring that knowledge into the work. A directory of specialists addresses only part of the problem. An investigator may know who understands a shipment discrepancy but be unable to obtain their contribution before the customer needs a response. The same distinction applies to an agent architecture: a named specialist component is useful only if its contribution addresses the actual knowledge requirement. [Faraj and Sproull (2000)](#faraj-and-sproull-2000)

Faraj and Xiao (2006) examine coordination in a trauma centre, where uncertainty and time pressure make both expertise and dialogue consequential. Their account includes practices for coordinating expertise and practices such as contesting knowledge claims and making sense of a situation together. The setting matters: this is not evidence that every business exception should be handled like an emergency. It shows why some uncertain work requires more than compliance with a prescribed sequence. [Faraj and Xiao (2006)](#faraj-and-xiao-2006)

**Fictional AI application.** An assistant classifies a customer complaint as a shortage. The warehouse specialist suspects a split shipment; the adviser suspects that the customer is counting inner packs rather than boxes. All three accounts can use the same quantities while referring to different objects. The next useful contribution is a clarification of what was counted. Generating a longer recommendation before that clarification may amplify the original ambiguity.

A dialogic arrangement allows participants to challenge the problem definition as well as add missing facts. The application can preserve competing accounts, identify their sources and support a clarification request. The organisation still needs to determine who can convene the discussion and what counts as sufficient resolution. A shared record can support that work without resolving it by itself.

## Four questions for a usable contribution

A handoff can be assessed through content, meaning, timing and ownership. **Content** concerns whether the requested material is present. **Meaning** concerns whether the recipient can interpret it adequately. **Timing** concerns whether the contribution is available when the dependent activity needs it. **Ownership** concerns who accepts the next task and handles a return. This is a practical synthesis of dependency and coordination reasoning, not a separate taxonomy attributed to one author.

These questions help distinguish failure modes that otherwise look like a generic agent error. A valid response may omit a source, use an ambiguous status, arrive too late or reach a team that cannot accept the task. Each failure calls for a different response. Structural validation can check required fields. Clarification can address meaning. Scheduling and capacity can address timing. Acceptance and escalation arrangements can address ownership.

The distinction also improves evaluation. A delivery receipt tests transport. A successful schema check tests structure. Neither establishes that the receiving contribution was useful. A case-level examination can follow what the recipient did next, which clarification was required and how responsibility became settled. Such evidence connects a mechanism to the condition it was intended to support.

## A worked handoff design

Harbour's proposed handoff contract includes a case identifier, source identifiers and versions, reported versus confirmed quantities, unresolved questions, proposed recipient and requested response. “Accepted” means operations has enough information to begin the named investigation. It does not mean the shortage is confirmed.

The receiver can accept, return for a specified missing item, or redirect with a reason. A named service owner investigates cases that remain unaccepted. The design also reserves a conversation route for conflicts that cannot be reduced to missing fields. These are proposed mechanisms and responsibilities, not established benefits.

Useful pilot measures include time to acceptance, returns for missing evidence, repeated clarification, queue age and resolution quality. A rise in explicit returns may initially reflect better visibility of an existing problem. It should not automatically be read as worsening coordination. Conversely, fewer returns may reflect discouraged challenge rather than better evidence.

## Study pause: diagnose the dependency

A team proposes five agents that all send drafts to one reviewer. Identify two dependencies and one alternative arrangement.

**Worked response:** The drafts depend on review, and they compete for the same capacity. They may also need reconciliation if their claims overlap. Alternatives include fewer contributions, explicit acceptance criteria, automated structural checks before review, or separating review by expertise. The choice depends on the source of delay and error; adding reviewers without diagnosing the work is not enough.

## Continue with the course

Apply these concepts to [the pilot's worked business design](../../modules/01-standalone-foundations/06-business-design.md) and [the exercises](../../modules/01-standalone-foundations/07-assessment.md). The [standalone curriculum](../../CURRICULUM.md) identifies how later planned modules will develop the technical and organisational questions together.

## References

### Malone and Crowston (1994)

Malone, T. W., and Crowston, K. (1994). The interdisciplinary study of coordination. *ACM Computing Surveys, 26*(1), 87–119. [Publication](https://doi.org/10.1145/174666.174668) · [MIT author-hosted version](https://ccs.mit.edu/papers/CCSWP157.html).

### Okhuysen and Bechky (2009)

Okhuysen, G. A., and Bechky, B. A. (2009). Coordination in organizations: An integrative perspective. *Academy of Management Annals, 3*(1), 463–502. [Publisher record](https://doi.org/10.1080/19416520903047533).

### Carlile (2004)

Carlile, P. R. (2004). Transferring, translating, and transforming: An integrative framework for managing knowledge across boundaries. *Organization Science, 15*(5), 555–568. [Publication](https://doi.org/10.1287/orsc.1040.0094).

### Faraj and Sproull (2000)

Faraj, S., and Sproull, L. (2000). Coordinating expertise in software development teams. *Management Science, 46*(12), 1554–1568. [Publication](https://doi.org/10.1287/mnsc.46.12.1554.12072).

### Gittell (2002)

Gittell, J. H. (2002). Coordinating mechanisms in care provider groups: Relational coordination as a mediator and input uncertainty as a moderator of performance effects. *Management Science, 48*(11), 1408–1426. [Publication](https://doi.org/10.1287/mnsc.48.11.1408.268).

### Jarzabkowski, Lê and Feldman (2012)

Jarzabkowski, P. A., Lê, J. K., and Feldman, M. S. (2012). Toward a theory of coordinating: Creating coordinating mechanisms in practice. *Organization Science, 23*(4), 907–927. [Publication](https://doi.org/10.1287/orsc.1110.0693).

### Faraj and Xiao (2006)

Faraj, S., and Xiao, Y. (2006). Coordination in fast-response organizations. *Management Science, 52*(8), 1155–1169. [Publication](https://doi.org/10.1287/mnsc.1060.0526).
