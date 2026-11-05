# Research chapter 1: Designing work around AI

[Research reading guide](../literature-guide.md) · [Next: coordination](02-coordination.md)

## A faster answer can leave the work unfinished

**Fictional teaching case.** Harbour distributes packaging materials. A customer reports receiving ten boxes after ordering twelve. An AI assistant collects the complaint and shipment record, then produces a concise brief. Preparation is faster. The case still waits because sales expects the warehouse to investigate, while the warehouse expects sales to obtain a recount.

The brief has improved one contribution without resolving how the contributions connect. This is an organisation design problem: how work is divided, who receives each part, what information and authority accompany it, and how the parts come together. The answer requires more than an organisation chart.

The chapter moves from division of work to dependencies, then to information requirements and the fit among design choices. It ends by comparing three arrangements for the same case. The theory provides questions for AI integration; the Harbour story supplies illustrations, not evidence of business results.

## Division creates a need for integration

**Differentiation** means dividing work into specialised tasks, roles or units. **Integration** means connecting those contributions so that they serve a collective purpose. Burton and Obel (2018) explain organisation design through the fit between structure and coordination. Their argument includes information, decisions and incentives, rather than treating reporting relationships as the whole design. [Burton and Obel (2018)](#burton-and-obel-2018)

At Harbour, sales understands the customer relationship, the warehouse holds shipment evidence, and finance controls credit arrangements. These specialisms can be valuable. They also make the response dependent on several contributions. Assigning an AI system the task of preparing the brief adds a contribution to this arrangement. It leaves open who verifies the brief and resolves disagreements.

Puranam, Alexy and Reitzig (2014) distinguish fundamental organising problems involving task division, task allocation, reward provision and information provision. This offers a useful test of an apparently new AI organisation: which of these problems has actually been solved differently? A collection of software agents with job titles does not establish a new organisational form. Their conceptual argument helps classify a proposed arrangement; it is not an empirical test of AI agent teams. [Puranam et al. (2014)](#puranam-alexy-and-reitzig-2014)

**Application to AI:** inspect the contribution, its recipient and its acceptance conditions. A summariser may change information preparation. A routing model may change task allocation. A performance dashboard may change what work receives attention or reward. These are different design changes even when they use the same model.

## Dependencies before departments

**Interdependence** means that activities rely on one another. Thompson's distinction among pooled, sequential and reciprocal interdependence helps identify the pattern of reliance. The distinction concerns the relationship among activities, rather than the department names on an organisation chart. [Thompson (1967)](#thompson-1967)

| Pattern | Plain-language explanation | AI-related illustration |
|---|---|---|
| Pooled | Contributions support a common whole without each directly feeding the next | Several service teams depend on a common knowledge service and its maintenance |
| Sequential | One activity supplies an input needed by another | A prepared complaint brief becomes an investigator's input |
| Reciprocal | Contributions must be adjusted in response to one another | Sales and the warehouse revise the case account as new evidence arrives |

These patterns can coexist in one service. They are aids to diagnosis, not labels that determine a single correct technology. A stable handoff may benefit from a standard brief. A disputed interpretation may require repeated discussion. Adding more detail to the brief cannot by itself settle who should accept a disputed claim.

Mintzberg's coordinating mechanisms supply a complementary question: how is the dependency managed? Standardisation specifies processes, outputs or skills; direct supervision gives an actor a coordinating role; mutual adjustment connects participants through communication. A checklist, supervisor and specialist conversation may all belong in one operating arrangement. [Mintzberg (1979)](#mintzberg-1979)

## Information demand and capacity

Uncertainty creates work because the necessary information is not all available in advance. Galbraith's information-processing view asks how an organisation responds to that gap. Two broad responses are to reduce information requirements and to increase the capacity to process information. [Galbraith (1973, 1977)](#galbraith-1973-and-1977)

At Harbour, requiring an order identifier at intake can reduce repeated clarification. Giving one team responsibility for an entire bounded case can reduce some cross-team exchanges. Shared evidence and a well-prepared brief can increase the capacity to handle information that still needs to travel. Reducing demand and increasing capacity may therefore complement each other.

This does not mean that uncertainty should be concealed. Replacing “customer reports ten boxes” with “ten boxes delivered” produces apparent certainty by changing the claim. The representation is simpler, but the organisation may now be working from an unsupported premise. Information processing includes preserving distinctions that matter to later action.

The engineering connection is concrete. Input selection determines what the model can consider. A prompt defines the preparation task. Truncation removes some material. A generated brief rearranges what becomes prominent. Each operation should be examined for its effect on the recipient's ability to understand and act, not only the readability of the output.

## Fit is a relationship among choices

A **configuration** is a set of design choices whose effects depend on one another. For AI integration, these choices include task scope, source access, reviewer capacity, escalation rights, maintenance responsibilities and performance measures. Burton and Obel's fit argument provides the general foundation; the specific AI configuration below is a teaching interpretation. [Burton and Obel (2018)](#burton-and-obel-2018)

Consider a reviewer who is responsible for detecting unsupported claims but cannot open the shipment record. Responsibility and access do not fit. Consider a team rewarded for the number of cases submitted while the receiving team needs careful evidence. Incentives and handoff quality pull in different directions. A stronger prompt cannot fully repair either mismatch.

Three questions help keep the claim precise. **Architectural coherence** asks whether the designed elements are consistent. **Implementation fit** asks whether the selected arrangement suits a particular organisation. **Enacted fit** asks whether actual work meets its coordination and information requirements. This three-part distinction provides a way to organise the analysis in this course. It is not a single validated measurement scale.

An architecture diagram can support the first inquiry. Local requirements, selected settings and operating arrangements support the second. Repeated observation and performance evidence are needed for the third. A design may be coherent and still work poorly in its setting.

## When more agents create more integration work

**Modularity** means dividing a system into parts with relatively limited interaction across their boundaries. Ethiraj and Levinthal (2004) examine the trade-offs of decomposition in a simulation model. Their contribution is a warning against treating ever finer division as automatically beneficial. Both excessive integration and excessive fragmentation can create difficulties. [Ethiraj and Levinthal (2004)](#ethiraj-and-levinthal-2004)

**AI application, not a finding from that study:** a researcher agent, writer agent and reviewer agent may create useful separation when they bring different evidence, capabilities or checks. If all three repeatedly reinterpret the same ambiguous case, decomposition may instead multiply handoffs and reconciliation. A technical boundary is not evidence that the work is organisationally independent.

Before splitting an agent, identify what can be completed within the boundary and what must still be negotiated across it. A shared model does not remove that question. Nor does using different models answer it.

## Complementarity, compensation and alternative designs

The effect of a design choice can change when another choice changes. Two arrangements are **complementary** when one becomes more useful in the presence of the other. Source access and review expertise offer a simple illustration: access is more valuable when the reviewer can interpret the material, while expertise is easier to exercise when the evidence is available. This example applies configurational reasoning; it is not a measured result from an AI deployment.

Rivkin and Siggelkow (2003) examine interdependencies among hierarchy, incentives, decision decomposition and processing limits in an agent-based model. Their analysis concerns a balance between searching for better arrangements and retaining a useful arrangement once found. It provides a reason to examine combinations of choices rather than assume that a single feature has a stable effect everywhere. A hierarchy can support integration in one configuration and obstruct it in another. [Rivkin and Siggelkow (2003)](#rivkin-and-siggelkow-2003)

**Compensation** is different: one arrangement offsets a limitation of another. A specialist conversation may compensate for what a standard complaint form cannot express. That does not make the form unnecessary. The combination may handle routine cases economically while retaining a way to investigate unusual ones. If the conversation becomes necessary for almost every case, however, the supposed exception route may be concealing a poor normal design.

Formal and informal arrangements can also interact. Gulati and Puranam (2009) argue that inconsistency between them can support renewal under particular conditions, including a sufficiently strong pre-existing informal organisation and substantial gains from pursuing different demands. Their argument does not license a general recommendation to create inconsistent rules. For an AI service, it prompts investigation of whether informal expert contacts sustain useful work, conceal weaknesses or exclude less-connected staff. [Gulati and Puranam (2009)](#gulati-and-puranam-2009)

Different configurations may accomplish similar purposes. This possibility is called **equifinality**. One organisation might keep investigation and response in one team; another might use specialised teams with a reliable handoff. The existence of both options does not demonstrate equal performance. Their suitability depends on case volume, expertise, uncertainty and evidence about outcomes. The appropriate comparison concerns the whole arrangement, including the integration work each option requires.

At Harbour, a single case team could reduce repeated transfers while requiring broader expertise within that team. A specialist structure could preserve deep expertise while requiring clear acceptance conditions and time for clarification. Adding an assistant changes the preparation contribution in either design. It does not settle which structure is preferable. The design decision remains a comparison of capabilities, dependencies and costs under particular conditions.

## A worked comparison at Harbour

Harbour considers three designs. Structured intake and direct record lookup suit cases with standard questions and accessible records. A referenced AI brief may help with long free-text complaints. A specialist conversation may remain necessary when records and customer accounts conflict. This is a choice among ways of organising contributions, not a contest to maximise AI use.

For the brief option, sales obtains the identifier and customer account. The application prepares a draft that preserves source labels. An investigator can inspect records, request clarification and reject the draft. The warehouse confirms shipment evidence. A named service owner investigates stalled handoffs. This arrangement is a proposal to test, not an account of an implemented service.

Suppose a draft saves five preparation minutes but adds three checking minutes. The net staff saving is two minutes for each case actually using it. At 200 uses a month, this is 400 minutes, or six hours and forty minutes. These are illustrative assumptions. They do not establish cash savings, shorter waiting time or higher quality. If the investigator's queue remains unchanged, customer resolution may be no faster.

The comparison should therefore include preparation, checking, clarification, waiting, errors and the distribution of work across roles. A structured-intake comparator matters because the benefit may come partly from better intake rather than generation.

## Study pause: draw the missing connection

Choose a proposed AI assistant. Write down its output, the recipient, the evidence needed to accept it and the action that follows. Then identify a dependency that the assistant does not resolve.

**Worked response:** A complaint assistant prepares a brief for operations. Operations needs the current shipment record and a distinction between reports and confirmed facts. It can begin an investigation, but the brief cannot make the warehouse accept ownership of a disputed recount. A response arrangement and escalation route remain necessary.

## Continue with the lessons

Apply information-processing questions to [Lesson 1.3](../../modules/01-foundations/03-business-and-organisation.md), fit to [Lesson 4.6](../../modules/04-evaluation/06-design-lab.md), and decomposition to [Lesson 11.6](../../modules/11-agent-teams/06-design-lab.md). [Chapter 2](02-coordination.md) examines what a receiving contribution actually needs.

## References

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
