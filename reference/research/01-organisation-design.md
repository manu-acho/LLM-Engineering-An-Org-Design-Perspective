# Research chapter 1: Designing work around AI

[Research reading guide](../literature-guide.md) · [Next: coordination](02-coordination.md)

Read [Meet Harbour](../../HARBOUR.md) for the shared fictional company. In this chapter, its delivery-investigation work illustrates the division of work and the integration needed between customer service, warehouse, transport and finance. The case is an application of the research concepts, not evidence for the original studies.

## A faster answer can leave the work unfinished

**Fictional teaching case.** Harbour distributes packaging materials. A customer reports receiving ten boxes after ordering twelve. An AI assistant collects the complaint and shipment record, then produces a concise brief. Preparation is faster. The case still waits because sales expects the warehouse to investigate, while the warehouse expects sales to obtain a recount.

The brief has improved one contribution without resolving how the contributions connect. This is an organisation design problem: how work is divided, who receives each part, what information and authority accompany it, and how the parts come together. The answer requires more than an organisation chart.

The chapter moves from division of work to dependencies, then to information requirements and the fit among design choices. It ends by comparing three ways Harbour could handle the same complaint. The theory provides questions for AI integration; the Harbour story supplies illustrations, not evidence of business results.

## Division creates a need for integration

**Differentiation** means dividing work into specialised tasks, roles or units. **Integration** means bringing those contributions together so that the organisation can accomplish a shared purpose. Once customer service, warehouse and finance each handle part of a complaint, their separate contributions must become a coherent response to the customer.

An **arrangement** is a way of organising a particular piece of work. It includes who does each task, what information and tools they use, who can make decisions and how the work passes between people or teams. A **proposed arrangement** describes how those pieces would work together if the organisation adopted the design. For example, Harbour could ask an AI assistant to prepare a brief, assign the warehouse to check shipment evidence and give finance the authority to approve a credit. This describes a plan. To assess how it works in practice, Harbour would need to see how staff handle actual complaints under that plan.

**Structure** gives that division a relatively stable pattern. It specifies how tasks are grouped, who is assigned to roles or units, and where authority and reporting relationships sit. At Harbour, assigning shipment investigation to the warehouse and credit approval to finance is a structural choice. An organisation chart shows some of this structure, but usually leaves many task boundaries and responsibilities unstated.

**Coordination** concerns how teams manage their reliance on one another after the work is divided. A **handoff** passes work or information to another contributor. **Acceptance conditions** specify what the recipient needs before taking on the next task. For instance, the warehouse might agree to begin an investigation once it has the shipment reference and can tell which quantities came from the customer and which came from warehouse records. A shared record, an agreement about when to start and a conversation about conflicting quantities help the teams bring their work together.

These concepts connect two questions. How is work divided and allocated? How are the resulting contributions made to work together? Structural choices help answer the first, while coordination arrangements help answer the second. They overlap in practice. Assigning a case coordinator, for example, creates a role in the structure specifically to connect other people's work.

Burton and Obel (2018) explain organisation design through the **fit** between structure and coordination, meaning how well the division of work and the means of connecting it suit one another and the task. Their argument also includes information, decisions and **incentives**, the rewards or pressures that influence what contributors prioritise. Rewarding speed while expecting careful investigation can pull the same role in different directions. If specialised teams often receive conflicting evidence, they need time and a clear route to resolve disputes before passing a case on. [Burton and Obel (2018)](#burton-and-obel-2018)

To assess fit in Harbour's complaint process, first identify which part of the work an AI tool would change. Puranam, Alexy and Reitzig (2014) distinguish four organising problems. **Task division** asks what pieces of work need doing. **Task allocation** asks who or what should do each piece. **Information provision** asks what each contributor needs to know to do the work. **Reward provision** asks what encourages people to make the desired contributions. Their framework helps explain which organising problems a design addresses. Its application to Harbour is a teaching example. Assessing an AI team in practice would require evidence of how it works. [Puranam et al. (2014)](#puranam-alexy-and-reitzig-2014)

Suppose Harbour separates preparing a complaint brief from deciding whether to issue a credit. That is **task division**. Assigning the brief to an AI summariser, a tool that condenses the complaint and shipment records, is **task allocation**. The brief serves **information provision** when it gives the warehouse the shipment reference, shows where each quantity came from and identifies what is still disputed. The warehouse can then decide whether it has enough evidence to begin investigating.

A routing model serves a different purpose. It proposes which team should receive a case. If Harbour allows it to send a suspected delivery shortage directly to the warehouse, the software helps allocate that case to a team. The warehouse still needs a way to return the case for clarification if the evidence is incomplete. Sending the case and taking responsibility for investigating it are separate steps.

A dashboard for the AI-assisted service might count closed cases directly from service records. This changes what managers can see. If Harbour uses those counts to reward staff, it also changes **reward provision**. Staff may then have a reason to close cases quickly even when a delivery dispute needs further investigation. A measure of completed work can influence how staff handle the cases behind it.

The summariser and routing tool could use the same language model. Each creates a different dependency for the warehouse. The brief must carry usable evidence, and the routing decision must deliver the case to a team that can act on it. These dependencies explain why a faster draft can still leave a complaint waiting.

## Dependencies before departments

**Interdependence** means that activities rely on one another. Thompson's distinction among pooled, sequential and reciprocal interdependence helps identify the pattern of reliance. The distinction concerns the relationship among activities, rather than the department names on an organisation chart. [Thompson (1967)](#thompson-1967)

| Pattern | Plain-language explanation | AI-related illustration |
|---|---|---|
| Pooled | Contributions support a common whole without each directly feeding the next | Several service teams depend on a common knowledge service and its maintenance |
| Sequential | One activity supplies an input needed by another | A prepared complaint brief becomes an investigator's input |
| Reciprocal | Contributions must be adjusted in response to one another | Sales and the warehouse revise the case account as new evidence arrives |

These patterns can coexist in one service. They are aids to diagnosis, not labels that determine a single correct technology. A stable handoff may benefit from a standard brief. A disputed interpretation may require repeated discussion. Adding more detail to the brief cannot by itself settle who should accept a disputed claim.

Mintzberg's **coordinating mechanisms** are ways of managing those dependencies. **Standardisation** establishes common expectations in advance. It can specify a process, such as a required evidence check, an output, such as the contents of an accepted brief, or skills, such as training in shipment investigation. **Direct supervision** gives someone responsibility for directing others' work. **Mutual adjustment** allows contributors to adapt their actions through communication, as when customer service and the warehouse discuss a disputed count. Harbour could use a checklist for routine cases, ask a supervisor to settle disputed assignments and bring in a specialist when a quantity needs explanation. [Mintzberg (1979)](#mintzberg-1979)

## Information demand and capacity

**Uncertainty** arises when the information needed to perform the work exceeds what is already available. **Information processing** here means obtaining, interpreting and exchanging information so that connected activities can proceed. It includes people discussing a case as well as software handling records. Galbraith's information-processing view asks how an organisation responds to that gap. Two broad responses are to reduce information requirements and to increase the capacity to process information. Requirements concern the information and clarification the work calls for. Capacity concerns the time, expertise, relationships and technical means available to handle that demand. [Galbraith (1973, 1977)](#galbraith-1973-and-1977)

At Harbour, requiring an order identifier when an adviser first logs the complaint, a step called **intake**, can reduce repeated clarification. Giving one team responsibility for an entire bounded case can reduce some cross-team exchanges. Shared evidence and a well-prepared brief can increase the capacity to handle information that still needs to travel. Reducing demand and increasing capacity may therefore complement each other.

This does not mean that uncertainty should be concealed. Replacing “customer reports ten boxes” with “ten boxes delivered” produces apparent certainty by changing the claim. The representation is simpler, but the organisation may now be working from an unsupported premise. Information processing includes preserving distinctions that matter to later action.

The engineering connection is concrete. Input selection determines what the model can consider. A prompt defines the preparation task. **Truncation** shortens an input by cutting material out, potentially removing a qualification that a reviewer needs. A generated brief rearranges what becomes prominent. Each operation should be examined for its effect on the recipient's ability to understand and act, not only the readability of the output.

## Fit is a relationship among choices

A **configuration** is a set of design choices whose effects depend on one another. For AI integration, these choices include task scope, source access, reviewer capacity, escalation rights, maintenance responsibilities and performance measures. Burton and Obel's fit argument provides the general foundation; the specific AI configuration below is a teaching interpretation. [Burton and Obel (2018)](#burton-and-obel-2018)

Consider a reviewer who is responsible for detecting unsupported claims but cannot open the shipment record. Responsibility and access do not fit. Consider a team rewarded for the number of cases submitted while the receiving team needs careful evidence. Incentives and handoff quality pull in different directions. A stronger prompt cannot fully repair either mismatch.

Three questions help keep the claim precise. **Architectural coherence** asks whether the designed elements are consistent. **Implementation fit** asks whether the selected roles, rules and software settings suit a particular organisation. **Enacted fit** asks whether actual work meets its coordination and information requirements. This three-part distinction provides a way to organise the analysis in this course. It is not a single validated measurement scale.

An architecture diagram can support the first inquiry. Local requirements, configured permissions and assigned responsibilities support the second. Repeated observation and performance evidence are needed for the third. A design may be coherent and still work poorly in its setting.

## When more agents create more integration work

**Modularity** means dividing a system into parts with relatively limited interaction across their boundaries. **Decomposition** is the act of breaking a larger task or system into smaller parts. Ethiraj and Levinthal (2004) examine the trade-offs of decomposition in a simulation model. Their contribution is a warning against treating ever finer division as automatically beneficial. Both excessive integration and excessive fragmentation can create difficulties. [Ethiraj and Levinthal (2004)](#ethiraj-and-levinthal-2004)

**AI application, not a finding from that study:** a researcher agent, writer agent and reviewer agent may create useful separation when they bring different evidence, capabilities or checks. If all three repeatedly reinterpret the same ambiguous case, decomposition may instead multiply handoffs and reconciliation. A technical boundary is not evidence that the work is organisationally independent.

Before splitting an agent, identify what can be completed within the boundary and what must still be negotiated across it. A shared model does not remove that question. Nor does using different models answer it.

## Complementarity, compensation and alternative designs

The effect of a design choice can change when another choice changes. Two design choices are **complementary** when one becomes more useful in the presence of the other. Source access and review expertise offer a simple illustration: access is more valuable when the reviewer can interpret the material, while expertise is easier to exercise when the evidence is available. This example applies configurational reasoning; it is not a measured result from an AI deployment.

Rivkin and Siggelkow (2003) examine interdependencies among hierarchy, incentives, decision decomposition and processing limits in an **agent-based model**, a simulation of interacting decision-makers under specified rules. Here, agent names a simulated decision-maker, a different use from a language-model agent in an application. Their analysis concerns a balance between searching for better arrangements and retaining a useful arrangement once found. It provides a reason to examine combinations of choices rather than assume that a single feature has a stable effect everywhere.

A **hierarchy**, an arrangement of levels of authority, can support integration by settling a disputed handoff. It can also delay work if every minor clarification must move up those levels. Which effect dominates depends on the wider configuration. [Rivkin and Siggelkow (2003)](#rivkin-and-siggelkow-2003)

**Compensation** occurs when one design choice offsets a limitation of another. A specialist conversation may compensate for what a standard complaint form cannot express. That does not make the form unnecessary. The combination may handle routine cases economically while retaining a way to investigate unusual ones. If the conversation becomes necessary for almost every case, however, the supposed exception route may be concealing a poor normal design.

**Formal arrangements** are officially specified roles, rules and reporting relationships. **Informal arrangements** are relationships and ways of working that develop beyond those specifications, such as knowing which warehouse colleague can quickly explain an unusual scan. The two can interact. Gulati and Puranam (2009) argue that inconsistency between them can support renewal under particular conditions, including a sufficiently strong pre-existing informal organisation and substantial gains from pursuing different demands. Their argument does not license a general recommendation to create inconsistent rules. For an AI service, it prompts investigation of whether informal expert contacts sustain useful work, conceal weaknesses or exclude less-connected staff. [Gulati and Puranam (2009)](#gulati-and-puranam-2009)

Different configurations may accomplish similar purposes. This possibility is called **equifinality**. One organisation might keep investigation and response in one team; another might use specialised teams with a reliable handoff. The existence of both options does not demonstrate equal performance. Their suitability depends on case volume, expertise, uncertainty and evidence about outcomes. The appropriate comparison concerns the whole arrangement, including the integration work each option requires.

At Harbour, a single case team could reduce repeated transfers while requiring broader expertise within that team. A specialist structure could preserve deep expertise while requiring clear acceptance conditions and time for clarification. Adding an assistant changes the preparation contribution in either design. It does not settle which structure is preferable. The design decision remains a comparison of capabilities, dependencies and costs under particular conditions.

## A worked comparison at Harbour

Harbour considers three designs. Structured intake and direct record lookup suit cases with standard questions and accessible records. An AI brief that identifies the records behind its claims may help with complaints written in the customer’s own words. A specialist conversation may remain necessary when records and customer accounts conflict. This is a choice among ways of organising contributions, not a contest to maximise AI use.

For the brief option, sales obtains the identifier and customer account. The application prepares a draft that preserves source labels. An investigator can inspect records, request clarification and reject the draft. The warehouse confirms shipment evidence. A named service owner investigates stalled handoffs. Harbour would need a trial to see whether this division of responsibilities and these handoffs work as planned.

Suppose a draft saves five preparation minutes but adds three checking minutes. The net staff saving is two minutes for each case actually using it. At 200 uses a month, this is 400 minutes, or six hours and forty minutes. These are illustrative assumptions. They do not establish cash savings, shorter waiting time or higher quality. If the investigator's queue remains unchanged, customer resolution may be no faster.

The comparison should therefore include preparation, checking, clarification, waiting, errors and the distribution of work across roles. A structured-intake comparator matters because the benefit may come partly from better intake rather than generation.

## Study pause: draw the missing connection

Choose a proposed AI assistant. Write down its output, the recipient, the evidence needed to accept it and the action that follows. Then identify a dependency that the assistant does not resolve.

**Worked response:** A complaint assistant prepares a brief for operations. Operations needs the current shipment record and a distinction between reports and confirmed facts. It can begin an investigation, but the brief cannot make the warehouse accept ownership of a disputed recount. Harbour still needs to assign responsibility for obtaining the recount and identify who can settle a disputed assignment.

## Continue with the course

Apply these concepts to [the pilot's worked business design](../../modules/01-standalone-foundations/06-business-design.md) and [the exercises](../../modules/01-standalone-foundations/07-assessment.md). The [course curriculum](../../CURRICULUM.md) connects these questions to the later modules on agents, service operation and business implementation.

## AI research extension: automation and augmentation can reshape each other

**Automation** transfers specified work to a machine. **Augmentation** changes what a person can do with assistance. The terms describe an arrangement of work, not a permanent property of a model. The same assistant can automate initial sorting while augmenting investigation of an unusual case.

Raisch and Krakowski (2021) develop a conceptual argument about tensions and connections between automation and augmentation. Their framework challenges the assumption that the two are independent choices with stable consequences. It is a theoretical contribution, not a measured estimate of employment or productivity effects. [Raisch and Krakowski (2021)](../bibliography.md#raisch-and-krakowski-2021)

**Harbour application.** Automating a first evidence brief can change the cases that reach an experienced investigator. The remaining work may become more unusual and demanding. A team that measures only average drafting time can miss this change in task mix. Conversely, the investigator's corrections may help redesign what can later be automated. Neither trajectory follows inevitably from adopting AI.

This sharpens the earlier discussion of interdependence. The unit of design is more than one person's task. It includes how work is allocated, how competence develops and how neighbouring teams absorb changed outputs. Removing routine cases may free attention while also removing opportunities through which new colleagues learn. That is a proposition to investigate, not a universal objection to automation.

**Study exercise.** Draw a before-and-after account of evidence preparation, exception investigation and approval. Identify who encounters ordinary cases, who encounters exceptions and how a new colleague learns each. A worked answer should distinguish a shorter preparation task from a changed learning arrangement. Evidence would include case allocation, observed work and accounts of skill development over time, rather than a single demonstration.

For deeper analysis, compare the design's promised labour saving with its effects on [coordination](02-coordination.md) and [process-wide work](09-process-architecture.md). A design may improve both, worsen both or trade one against the other. The framework supplies questions for that comparison, not its answer.

## References

The [project bibliography](../bibliography.md) brings together the chapter references and additional AI research, with source-access notes.

### Burton and Obel (2018)

Burton, R. M., and Obel, B. (2018). The science of organizational design: Fit between structure and coordination. *Journal of Organization Design, 7*, article 5. [Publication](https://doi.org/10.1186/s41469-018-0029-2).

### Puranam, Alexy and Reitzig (2014)

Puranam, P., Alexy, O., and Reitzig, M. (2014). What's “new” about new forms of organizing? *Academy of Management Review, 39*(2), 162–180. [Publication](https://doi.org/10.5465/amr.2011.0436).

### Thompson (1967)

Thompson, J. D. (1967). *Organizations in Action: Social Science Bases of Administrative Theory*. McGraw-Hill.

### Mintzberg (1979)

Mintzberg, H. (1979). *The Structuring of Organizations: A Synthesis of the Research*. Prentice-Hall.

### Galbraith (1973 and 1977)

Galbraith, J. R. (1973). *Designing Complex Organizations*. Addison-Wesley. Galbraith, J. R. (1977). *Organization Design*. Addison-Wesley.

### Ethiraj and Levinthal (2004)

Ethiraj, S. K., and Levinthal, D. (2004). Modularity and innovation in complex systems. *Management Science, 50*(2), 159–173. [Publication](https://doi.org/10.1287/mnsc.1030.0145).

### Rivkin and Siggelkow (2003)

Rivkin, J. W., and Siggelkow, N. (2003). Balancing search and stability: Interdependencies among elements of organizational design. *Management Science, 49*(3), 290–311. [Publication](https://doi.org/10.1287/mnsc.49.3.290.12740).

### Gulati and Puranam (2009)

Gulati, R., and Puranam, P. (2009). Renewal through reorganization: The value of inconsistencies between formal and informal organization. *Organization Science, 20*(2), 422–440. [Publication](https://doi.org/10.1287/orsc.1090.0421).
