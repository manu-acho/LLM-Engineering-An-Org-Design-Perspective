# Research chapter 7: The shared foundations beneath an AI service

[Research reading guide](../literature-guide.md) · [Previous: technology in practice](06-technology-in-practice.md) · [Next: governance](08-governance-and-accountability.md)

## The assistant that counted the wrong thing

**Fictional Harbour case.** A customer reports that two cases of packaging are missing. The order system records cases, the warehouse records boxes and a supplier catalogue describes packs. An assistant retrieves all three records and drafts a confident shortage explanation. Each record exists. The quantities still cannot safely be compared.

Harbour is a packaging distributor. It buys goods, holds inventory, fulfils customer orders and reconciles delivery discrepancies with financial records. Its AI assistant depends on shared product identifiers, quantity definitions, customer records and permissions across those activities. [The business case](../../HARBOUR.md) introduces the company; [the case-data guide](../case-data-guide.md) distinguishes the teaching fixtures from broader fictional illustrations.

This chapter follows those shared foundations. It starts with infrastructure and its history, then examines standards and classification. The closing case shows how apparently minor data choices distribute work and responsibility. The proposed designs are teaching interpretations, not findings from an operating business.

## Infrastructure is a relationship with organised work

**Infrastructure** is an arrangement that supports other activities and becomes embedded in how those activities are performed. It includes more than a server, database or network. A stock record becomes useful through definitions, access arrangements, recording practices and people who maintain it.

Star and Ruhleder (1996) examine infrastructure through its relationship with communities of practice. What operates as a familiar background for one group may remain a difficult object of work for another. Their account directs attention to learning, established practice and breakdown, rather than treating infrastructure simply as a large technical object. [Star and Ruhleder (1996)](#star-and-ruhleder-1996)

At Harbour, customer service may treat product lookup as an immediate capability. Warehouse staff make that lookup dependable by recording substitutions and damaged stock. The assistant's fast answer rests partly on work that its interface does not display. A failure should therefore be investigated beyond the model prompt.

An **installed base** is the existing combination of systems, standards, skills and practices on which a new arrangement must build. Hanseth and Lyytinen (2010) develop design theory for evolving information infrastructures, where new services encounter an already connected world. Replacing a spreadsheet does not replace the customer definitions, supplier conventions or local expertise that surrounded it. [Hanseth and Lyytinen (2010)](#hanseth-and-lyytinen-2010)

This creates path dependence: earlier choices shape later options and switching costs. It does not make change impossible. A research study should identify the actual dependencies, who maintains them and which alternatives have been tried before concluding that a system is locked in.

## Standards make comparison possible and require continuing work

A **standard** is an agreed specification or convention that makes activities or objects sufficiently comparable. A common product identifier helps systems refer to the same item. A unit convention helps distinguish a single box from a case containing several boxes. An interface specification defines what a service must send and accept.

These solve different problems. A syntactically valid message can still name the wrong product. Two services can exchange the number `2` successfully while interpreting its unit differently. Technical compatibility therefore needs semantic agreement, meaning agreement about what the exchanged information represents.

Hanseth, Monteiro and Hatling (1996) examine the tension between standardisation and flexibility. Timmermans and Epstein (2010) show why standards should be studied through their making and use, including the local work they require. These perspectives qualify the promise that one universal definition will remove all coordination problems. [Hanseth et al. (1996)](#hanseth-et-al-1996) · [Timmermans and Epstein (2010)](#timmermans-and-epstein-2010)

For Harbour, one quantity convention can make comparison easier. Yet a supplier may sell a mixed pack that cannot be translated by a single fixed multiplier. Someone must handle that exception and revise the mapping when packaging changes. Flexibility without common rules makes comparison fragile; rigid rules can erase legitimate differences. The design question is which differences must be preserved, who may translate them and how an unresolved difference remains visible.

## Classification changes what an organisation can see

A **classification** groups things into categories. “Delivery shortage”, “damaged goods” and “invoice query” are possible complaint categories. A category becomes organisationally consequential when it changes routing, priority, evidence requirements or available remedies.

Bowker and Star (1999) examine how classification systems organise visibility and carry consequences for people and work. Their argument concerns the choices and exclusions built into categories, not a claim that every classification is intentionally unfair. [Bowker and Star (1999)](#bowker-and-star-1999)

An AI classifier adds another layer: it estimates a category from an input. A technically accurate classifier can reproduce an unsuitable category scheme. Accuracy against historical labels answers whether the model matches those labels, not whether those labels express appropriate policy.

**Harbour illustration.** A customer writes, “The courier left the boxes outside and some are wet.” A single-label system forces this into either delivery or damage. The first category reaches transport, the second warehouse quality. The problem crosses both. A multi-label representation or an explicit cross-functional case can preserve that dependency, provided a person or team owns the resulting investigation.

A residual category such as “other” protects unfamiliar cases from forced classification. It also accumulates work. If no one reviews it, the system preserves uncertainty in a field while abandoning the customer in practice. Category maintenance is an operating responsibility, not an occasional model-training task.

## AI makes the data work more visible, or hides it again

Sambasivan et al. (2021) use interviews with 53 AI practitioners to examine **data cascades**, compounding downstream difficulties arising from data problems and the organisational conditions surrounding them. The study concerns particular high-stakes settings. It does not estimate the prevalence or cost of such problems in every AI deployment. [Sambasivan et al. (2021)](../bibliography.md#sambasivan-et-al-2021)

The useful Harbour question is where a quantity ambiguity travels. A unit mismatch can enter retrieval, a summary, a remedy proposal and a finance record. Improving the final answer prompt may leave the initiating condition untouched. The research interpretation is to investigate the path and the work arrangements that sustain it, rather than assume that data quality belongs solely to a technical team.

Gebru et al. (2021) propose **datasheets for datasets**, structured documentation of matters such as origin, composition, collection, intended uses and maintenance. This is a documentation proposal, not evidence that filling in a form makes data suitable. [Gebru et al. (2021)](../bibliography.md#gebru-et-al-2021)

A Harbour adaptation would document who supplies delivery scans, what a missing scan means, which period is covered and how corrections enter the next version. It would distinguish an absent event from evidence that no delivery occurred. The documentation becomes useful when operating teams can correct it and the service respects its limits.

## A platform can invite development while concentrating control

A **platform** supplies a foundation on which other actors can build services or extensions. Yoo, Henfridsson and Lyytinen (2010) discuss the layered organisation of digital innovation. Plantin et al. (2018) connect platform and infrastructure perspectives, helping explain why a service can be both an innovation foundation and a powerful point of dependence. [Yoo et al. (2010)](#yoo-et-al-2010) · [Plantin et al. (2018)](#plantin-et-al-2018)

For an AI service, extension might mean adding a retrieval connector or an action tool. **Generativity**, the capacity for further development by varied actors, does not imply unrestricted access or distributed authority. A provider may allow many extensions while controlling identity, pricing, model availability or accepted interfaces. Harbour may similarly let teams add assistants while centrally controlling product definitions and finance actions.

The design inquiry should identify control points and practical exit options. Can data and configuration be exported? Can a replacement preserve essential identifiers? Which local modifications will survive an interface change? These are questions for investigation, not a claim that every central dependency is undesirable.

## Growth requires more than an open interface

Henfridsson and Bygstad (2013) examine adoption, innovation and scaling as mechanisms in digital-infrastructure evolution. Their account supports investigating combinations of conditions rather than treating extensibility as a direct measure of successful development. [Henfridsson and Bygstad (2013)](../bibliography.md#henfridsson-and-bygstad-2013)

For an AI service, adoption means actual uptake, innovation concerns new arrangements or uses, and scaling concerns expansion. They need not move together. Many staff might adopt the same narrow assistant without developing new uses. A team might invent a valuable connector that cannot be supported across sites. Expansion might amplify an unresolved classification problem. These Harbour possibilities show why a connector count cannot establish organisational adaptability.

Monteiro et al. (2013) and Edwards et al. (2009) direct attention beyond isolated artefacts toward historically accumulated infrastructures. A one-day demonstration misses dependencies acquired over time. An AI inquiry should retain the versions of prompts, category schemes, evidence sources and interfaces that actually coexisted, rather than combine today's policy with last year's model and call that the deployed arrangement. [Monteiro et al. (2013)](../bibliography.md#monteiro-et-al-2013) · [Edwards et al. (2009)](../bibliography.md#edwards-et-al-2009)

It also helps to name the kind of change. A **configuration** selects an available option; an **extension** adds behaviour; an **integration** connects services and meanings; a **workaround** achieves a purpose outside the prescribed route. None alone establishes that the wider organisation can adapt. At Harbour, changing a prompt, adding a transport connector and asking a colleague to telephone a depot solve different parts of the evidence problem. The inquiry should follow their interaction rather than classify every change as an AI improvement.

## Worked design: a quantity agreement

Harbour proposes a small agreement for the evidence service. An agreement about exchanged fields and their meaning is often called a **data contract**. This teaching example contains five provisions.

| Provision | Example | Responsible work |
|---|---|---|
| Identity | Product and packaging version accompany the quantity | Product-data steward maintains mappings |
| Meaning | Quantity includes unit and effective date | Warehouse and commercial teams agree definitions |
| Translation | A conversion identifies its source and validity period | Service checks an approved mapping |
| Uncertainty | Unknown units block numerical reconciliation | Case owner requests clarification |
| Correction | An amended record retains provenance | Record owner publishes a new version |

Suppose an order records twelve cases and a receipt records ten boxes. No shortage quantity follows until the units are reconciled. Even if an approved conversion establishes a numerical difference, that difference alone does not explain loss or justify a credit. Delivery evidence and remedy authority remain separate questions.

This is deliberately a proposed design, not an assertion that the existing lab already implements a general unit-conversion service. The lab's simpler quantities make other concepts inspectable. Extending the software would require conversion fixtures, tests and explicit version rules.

The arrangement incurs costs: mapping work, delayed responses for ambiguous cases and maintenance of old versions. The comparison should include these costs, customer outcomes and the risks of forcing incompatible evidence into one number. A faster draft is only one part of the service.

## Exercise: inspect an invisible dependency

Choose one AI-supported activity and identify three foundations that its users may take for granted. For each, name its maintainer, an exception and evidence that would establish whether maintenance works.

**Worked Harbour response.** Product identity depends on a steward and supplier updates; mixed packaging challenges the mapping; a sample of changed product records and unresolved cases can test maintenance. Customer identity depends on account administration; merged accounts create exceptions; correction histories reveal how those cases were handled. Delivery-event meaning depends on transport recording practice; offline scans arrive late; observations and timestamp histories help distinguish lateness from a missing event.

## Advanced inquiry: investigate evolution rather than a snapshot

Compare two versions of a category scheme, interface or unit convention. Follow a contested change across at least two teams. A proposition worth testing is that central standardisation reduces some reconciliation work while shifting exception work to local teams. The comparison must allow the proposition to fail: local work may fall, persist for unrelated reasons or improve because the standard exposes a previously hidden problem.

Documents show prescribed meaning; configuration shows selected arrangements; observation and correction histories reveal how people sustain or challenge them. No one source establishes all three. Connect this inquiry to [coordination](02-coordination.md), [technology in practice](06-technology-in-practice.md) and [governance](08-governance-and-accountability.md).

## References

The [project bibliography](../bibliography.md) supplies the wider reading collection and source-access notes. The classic works below support the conceptual synthesis; the AI applications are teaching interpretations.

### Star and Ruhleder (1996)
Star, S. L., and Ruhleder, K. (1996). An ecology of infrastructure: Design and access for large information spaces. *Information Systems Research, 7*(1), 111–134. [Publication](https://doi.org/10.1287/isre.7.1.111).

### Hanseth and Lyytinen (2010)
Hanseth, O., and Lyytinen, K. (2010). Design theory for dynamic complexity in information infrastructures: The case of building internet. *Journal of Information Technology, 25*(1), 1–19. [Publication](https://doi.org/10.1057/jit.2009.19).

### Hanseth et al. (1996)
Hanseth, O., Monteiro, E., and Hatling, M. (1996). Developing information infrastructure: The tension between standardization and flexibility. *Science, Technology, & Human Values, 21*(4), 407–426. [Publication](https://doi.org/10.1177/016224399602100402).

### Timmermans and Epstein (2010)
Timmermans, S., and Epstein, S. (2010). A world of standards but not a standard world: Toward a sociology of standards and standardization. *Annual Review of Sociology, 36*, 69–89. [Publication](https://doi.org/10.1146/annurev.soc.012809.102629).

### Bowker and Star (1999)
Bowker, G. C., and Star, S. L. (1999). *Sorting Things Out: Classification and Its Consequences*. MIT Press.

### Yoo et al. (2010)
Yoo, Y., Henfridsson, O., and Lyytinen, K. (2010). The new organizing logic of digital innovation: An agenda for information systems research. *Information Systems Research, 21*(4), 724–735. [Publication](https://doi.org/10.1287/isre.1100.0322).

### Plantin et al. (2018)
Plantin, J.-C., Lagoze, C., Edwards, P. N., and Sandvig, C. (2018). Infrastructure studies meet platform studies in the age of Google and Facebook. *New Media & Society, 20*(1), 293–310. [Publication](https://doi.org/10.1177/1461444816661553).
