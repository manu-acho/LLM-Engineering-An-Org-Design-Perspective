# Research chapter 2: Coordinating people, teams and AI systems

[Research reading guide](../literature-guide.md) · [Previous: organisation design](01-organisation-design.md) · [Next: decisions](03-decisions.md)

Read [Meet Harbour](../../HARBOUR.md) for the shared fictional company. In this chapter, its delivery-investigation work illustrates the dependencies between source collection, investigation, review and settlement. The case is an application of the research concepts, not evidence for the original studies.

## A handoff can arrive without becoming usable

**Fictional teaching case.** Harbour's assistant sends a shortage brief to operations. The software records a successful delivery. Operations returns the case: the brief has an order number but no distinction between the customer's report and the warehouse's shipment count. Sales regards the handoff as complete. Operations regards it as unusable.

A **handoff** passes work or information from one contributor to another. Technical delivery of the message worked in this example, but the receiving team still lacked what it needed. A **dependency** exists when one activity relies on something supplied or done elsewhere. Here, investigation depends on usable evidence. Coordination manages that reliance by arranging the content, meaning, timing and responsibility of the handoff.

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

The table is a teaching application of dependency reasoning, not a reproduction of one author's complete classification of dependency types. Its purpose is to make a design choice assessable. “Add orchestration” is too vague until the dependency and intended response are named.

## Mechanisms and conditions

A **coordination mechanism** is a way of managing a dependency between activities. Plans, meetings, roles, routines and shared representations are examples. Okhuysen and Bechky (2009) distinguish such mechanisms from three **integrative conditions**: accountability, predictability and common understanding. [Okhuysen and Bechky (2009)](#okhuysen-and-bechky-2009)

Accountability in this coordination framework concerns making contributions and responsibilities identifiable. Predictability concerns anticipating how connected work will proceed. Common understanding concerns a sufficient shared interpretation of the work. A mechanism is something the organisation puts in place. A condition describes what people need to be able to do together for the work to proceed. A timetable is a mechanism. Being able to anticipate when usable evidence will arrive is predictability. The timetable helps only if the relevant contributors can and do work to it. These conditions help explain what a mechanism is intended to accomplish.

At Harbour, naming an investigator makes responsibility visible, which supports **accountability** in the coordination sense. An agreed time for the brief to arrive supports **predictability** if the teams can meet it. Labelling the customer’s count and the warehouse’s count separately helps the teams develop **common understanding** of what is disputed.

Chapter 8 asks a further question about accountability. If a case stalls, who has to explain what happened, who can question the explanation, and who can require a response? A named investigator gives the inquiry somewhere to start.

The software can make the handoff visible by recording three distinct events. **Routed** records placement in the warehouse’s queue. **Received** records arrival. **Accepted** records the receiving team’s or service’s agreement to take on the investigation under specified conditions. For Harbour, acceptance might require a current shipment reference and separate fields for reported and confirmed quantities. An acceptance record gives the next team evidence that the case can proceed under those rules. Understanding the evidence and resolving the complaint require further work.

## Shared data and shared meaning

A **knowledge boundary** arises where groups have different knowledge, language or interests that affect their ability to work together. A common format can help exchange information across that boundary while leaving differences in meaning or interests unresolved. Carlile (2004) distinguishes syntactic, semantic and pragmatic boundaries. **Transfer** moves information in an already usable form. **Translation** makes differing meanings understandable across groups. **Transformation** changes knowledge or working arrangements where differing interests also have to be negotiated. [Carlile (2004)](#carlile-2004)

A **syntactic boundary** concerns compatible representations. If both systems use the same order identifier and field structure, records can be transferred. A **semantic boundary** concerns different meanings. “Delivered” might mean that goods left the warehouse to one team and that the customer accepted them to another. Translation requires making these meanings explicit.

A **pragmatic boundary** involves different interests as well as knowledge. Sales may want to preserve the relationship quickly; operations may need to avoid accepting an unsupported shortage; finance may need defensible credit evidence. A common definition can leave these interests unresolved. Transformation can require changing the working arrangement or shared representation through negotiation.

An AI summary can make the boundary harder to see if it chooses one meaning and writes it fluently. A better summary can preserve the competing accounts, but it cannot itself establish an agreed resolution. This is a theoretical application to a fictional case, not a finding that language models necessarily create semantic conflict.

For technical design, a **schema** specifies the expected fields and allowed values in a record or message. **Schema validation** checks compliance with that specification. JSON is a text format for representing such data, for example `{"status": "delivered"}`. This record can pass a format check while its `status` field carries incompatible interpretations for two teams. The schema should document meanings and uncertainty; the organisational arrangement must provide a route to dispute or revise them.

## Bringing expertise into the work

Routing a task to a specialist label is insufficient if the necessary expertise cannot be mobilised. Faraj and Sproull (2000) connect expertise coordination with knowing where expertise is needed and located and bringing it into the work. Their study concerns software development teams; it does not establish the effectiveness of AI specialist agents. [Faraj and Sproull (2000)](#faraj-and-sproull-2000)

The practical distinction is between possessing a resource and being able to use it in time. A company may employ a policy expert who is not available to the case team. A model may have access to a policy document whose relevant exception is hard to interpret. In either situation, listing the resource does not settle the dependency.

Gittell (2002) adds relationships and communication: shared goals, shared knowledge, mutual respect and communication that supports problem solving. The healthcare setting of the original study limits direct transfer. For AI integration, the reasonable use is to investigate whether the surrounding human relationships support coordination, not to claim that an interface contains mutual respect. [Gittell (2002)](#gittell-2002)

## Coordination continues after configuration

**Configuration** is the selection of software settings, fields and rules. **Practice** concerns what people and systems actually do in their working circumstances. Practice research treats coordination as work that participants keep accomplishing and modifying after those settings have been selected. Jarzabkowski, Lê and Feldman (2012) examine how coordination mechanisms emerge and change through disruption and stabilisation. [Jarzabkowski et al. (2012)](#jarzabkowski-l-and-feldman-2012)

**Illustrative application:** a new complaint type arrives with photographs that the brief cannot represent. Staff telephone the warehouse and add a note outside the usual form. This could be useful repair, an unsafe workaround or a symptom of unsuitable intake. The deviation alone does not decide which explanation is right. Observation should establish what problem staff encountered, what they changed and what happened downstream.

This matters for agent frameworks. A workflow **graph** represents steps as nodes and connections between them as edges. An **escalation** sends an unresolved issue to someone with additional expertise or authority. A graph can contain an edge for that transfer. Actual coordination also depends on someone noticing the escalation, understanding the case and having a practical route to respond. Retry logic can repeat a request; it cannot make an unavailable specialist available or settle disputed ownership.

## Expertise, dialogue and the limits of a standard path

Expertise coordination has two connected demands. The organisation needs to recognise what knowledge a situation requires, and it needs to bring that knowledge into the work. A directory of specialists addresses only part of the problem. An investigator may know who understands a shipment discrepancy but be unable to obtain their contribution before the customer needs a response. The same distinction applies to an agent architecture: a named specialist component is useful only if its contribution addresses the actual knowledge requirement. [Faraj and Sproull (2000)](#faraj-and-sproull-2000)

Faraj and Xiao (2006) examine coordination in a trauma centre, where uncertainty and time pressure make both expertise and dialogue consequential. Their account includes practices for coordinating expertise and practices such as contesting knowledge claims and making sense of a situation together. The setting matters: this is not evidence that every business exception should be handled like an emergency. It shows why some uncertain work requires more than compliance with a prescribed sequence. [Faraj and Xiao (2006)](#faraj-and-xiao-2006)

**Fictional AI application.** An assistant classifies a customer complaint as a shortage. The warehouse specialist suspects a split shipment; the adviser suspects that the customer is counting inner packs rather than boxes. All three accounts can use the same quantities while referring to different objects. The next useful contribution is a clarification of what was counted. Generating a longer recommendation before that clarification may amplify the original ambiguity.

A **dialogic arrangement** makes room for participants to question and revise the account of a problem together. For Harbour, that means discussing whether the case concerns a shortage, a split shipment or different counting units, as well as collecting additional facts. The application can preserve competing accounts, identify their sources and support a clarification request. The organisation still needs to determine who can convene the discussion and what counts as sufficient resolution. A shared record can support that work without resolving it by itself.

## Four questions for a usable contribution

A handoff can be assessed through content, meaning, timing and ownership. **Content** concerns whether the requested material is present. **Meaning** concerns whether the recipient can interpret it adequately. **Timing** concerns whether the contribution is available when the dependent activity needs it. **Ownership** concerns who accepts the next task and handles a return. This is a practical synthesis of dependency and coordination reasoning, not a separate taxonomy attributed to one author.

These questions help distinguish failure modes that otherwise look like a generic agent error. A valid response may omit a source, use an ambiguous status, arrive too late or reach a team that cannot accept the task. Each failure calls for a different response. Structural validation can check required fields. Clarification can address meaning. Scheduling and capacity can address timing. Acceptance and escalation arrangements can address ownership.

The distinction also improves evaluation. A delivery receipt tests transport. A successful schema check tests structure. Neither establishes that the receiving contribution was useful. A case-level examination can follow what the recipient did next, which clarification was required and how responsibility became settled. Such evidence connects a mechanism to the condition it was intended to support.

## A worked handoff design

Harbour's proposed handoff contract includes a case identifier, source identifiers and versions, reported versus confirmed quantities, unresolved questions, proposed recipient and requested response. Operations marks a case **accepted** once it has enough information to begin the named investigation. Confirming the shortage is part of that investigation.

The receiver can accept, return for a specified missing item, or redirect with a reason. A named service owner investigates cases that remain unaccepted. The design also reserves a conversation route for conflicts that cannot be reduced to missing fields. These are proposed mechanisms and responsibilities, not established benefits.

Useful pilot measures include time to acceptance, returns for missing evidence, repeated clarification, queue age and resolution quality. **Queue age** measures how long a case has been waiting in the queue. A rise in explicit returns may initially reflect better visibility of an existing problem. It should not automatically be read as worsening coordination. Conversely, fewer returns may reflect discouraged challenge rather than better evidence.

## Study pause: diagnose the dependency

A team proposes five agents that all send drafts to one reviewer. Identify two dependencies and one different way to divide or schedule the review work.

**Worked response:** The drafts depend on review, and they compete for the same capacity. They may also need reconciliation if their claims overlap. Alternatives include fewer contributions, explicit acceptance criteria, automated structural checks before review, or separating review by expertise. The choice depends on the source of delay and error; adding reviewers without diagnosing the work is not enough.

## Continue with the course

Apply these concepts to [the pilot's worked business design](../../modules/01-standalone-foundations/06-business-design.md) and [the exercises](../../modules/01-standalone-foundations/07-assessment.md). The [course curriculum](../../CURRICULUM.md) connects these questions to the later modules on agents, service operation and business implementation.

## AI research extension: coordinating when the basis of an answer changes

A **learning algorithm** derives patterns from data rather than relying only on rules written individually by a programmer. Once deployed, such a system may still require a deliberate update to change. The term does not mean that every model continuously learns from every conversation.

Faraj, Pachidi and Sayegh (2018) examine implications of learning algorithms for working and organising, including the difficulty of inspecting how outputs are produced and the politics of how work is represented. Their contribution is a conceptual research agenda. It does not establish that every deployment will deskill workers or reorganise authority in the same way. [Faraj et al. (2018)](../bibliography.md#faraj-et-al-2018)

The coordination problem is that a handoff can remain formally unchanged while its practical basis changes. A receiving team previously trusted a named specialist's brief because it knew how that specialist checked the evidence. An AI-produced brief may look similar while relying on different source selection and assumptions. A familiar document format does not establish common understanding.

Consider the brief’s quantity field. A warehouse investigator may interpret “10” differently depending on whether it came from a scan, was inferred from a customer’s message, or was converted from packs to boxes. **Provenance** records where the information came from and how it changed. A brief can preserve common understanding by showing the original source and any conversion, then identifying who can answer a question about either. A confidence score would need a defined meaning before the investigator could use it for that purpose.

This interpretation extends the chapter's discussion of expertise. Knowing where expertise resides includes knowing who can explain a product mapping, revise an evidence rule or recognise an unusual delivery pattern. A model's fluent answer should not cause those relationships to disappear from the operating design.

**Study exercise.** Compare a source-linked brief with a polished summary that omits provenance. Identify what the receiving actor can verify in each. A defensible answer recognises that provenance helps investigation but does not prove the source correct. It also identifies the colleague or role able to repair a disputed meaning. Follow this question into [shared definitions and infrastructure](07-infrastructure-and-standards.md).

## References

The [project bibliography](../bibliography.md) brings together the chapter references and additional AI research, with source-access notes.

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
