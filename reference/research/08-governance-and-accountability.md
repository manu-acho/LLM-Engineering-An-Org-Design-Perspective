# Research chapter 8: Governing AI decisions and making them answerable

[Research reading guide](../literature-guide.md) · [Previous: infrastructure](07-infrastructure-and-standards.md) · [Next: process architecture](09-process-architecture.md)

## A recorded approval can still leave responsibility unresolved

**Fictional Harbour case.** An assistant recommends a credit for a disputed delivery. A service colleague approves it. Finance later discovers that a replacement shipment was already arranged, so the customer received two remedies. The log identifies a reviewer, a tool call and a transaction. It does not explain who was expected to check for an existing remedy, who could change that rule or who must answer the complaint about the failure.

Harbour's customer service, warehouse, transport and finance activities depend on one another. The AI service sits inside those relationships. [The business case](../../HARBOUR.md) supplies the company context. This chapter separates governance, decision rights, control and accountability, then uses the distinctions to design a review arrangement. All Harbour proposals are fictional teaching applications.

## Four terms that answer different questions

**Governance** concerns how legitimate rights and responsibilities for directing an arrangement are established and exercised. Here it asks who can set the service's scope, change its policy and resolve disputes over those decisions.

**Decision rights** specify who may decide particular matters. They need an object and conditions: for example, authority to approve a specified credit for an eligible case, within a stated limit. “Owns AI” leaves too much unspecified.

**Control** concerns efforts to guide conduct or results. It can include a target, observation, comparison and intervention. A system can record a target without anyone being able to intervene when it is missed.

**Accountability** concerns an answerability relationship. Bovens (2007) distinguishes an actor required to explain conduct from a forum able to question, judge and attach consequences. Lindberg (2013) clarifies accountability as a concept with multiple forms. A public-sector theory should not be transferred wholesale to a private firm, but it supplies a sharper question than whether logs exist. [Bovens (2007)](#bovens-2007) · [Lindberg (2013)](#lindberg-2013)

Harbour's transaction log is potentially evidence. A finance review panel with a defined mandate, access to explanations and power to require correction is a possible forum. Its actual operation still needs investigation. Calling a meeting an accountability forum does not establish that it can question anyone or change anything.

## Put decisions near knowledge, while examining the costs

Jensen and Meckling (1995) examine the costs of bringing decision rights and relevant knowledge together. **Specific knowledge** is costly to transfer to another decision-maker. A warehouse colleague may understand why a damaged pallet was recorded under an unusual code, while finance understands the financial consequences of a remedy. [Jensen and Meckling (1995)](#jensen-and-meckling-1995)

Moving all decisions to a central specialist can lose local knowledge or require expensive communication. Delegation can preserve that knowledge while creating coordination and control costs. Neither centralisation nor decentralisation is automatically the answer.

An AI summary changes the means of communication, but its completeness cannot be assumed. A concise account may omit the qualification that makes the warehouse code meaningful. The governance design should establish which decisions need direct consultation, which evidence can travel in structured form and how the receiver can challenge that form.

Aghion and Tirole's (1997) distinction between **formal authority**, a right to decide, and **real authority**, effective influence over the decision, adds a further problem. A manager can retain the final approval while a model or specialist effectively frames every available option. This is an application of the distinction to AI, not a claim that their model analysed modern assistants. [Aghion and Tirole (1997)](#aghion-and-tirole-1997)

## Select controls for the work that can actually be assessed

Ouchi (1979) distinguishes markets, bureaucracies and clans as control mechanisms under different conditions. A market coordinates through exchange and prices; bureaucracy relies on rules and authority; clan control draws on shared values and socialisation. These are analytical ideal types, not three software settings. [Ouchi (1979)](#ouchi-1979)

Eisenhardt (1985) examines the relationship between behaviour and outcome control, including the ability to specify conduct and measure outcomes. **Behaviour control** examines how work is performed. **Outcome control** examines its results. Kirsch (1996, 1997) extends attention to portfolios of formal and informal controls in complex systems work. [Eisenhardt (1985)](#eisenhardt-1985) · [Kirsch (1996, 1997)](#kirsch-1996-and-1997)

For Harbour, an approved evidence checklist is a behaviour control. A target for durable resolution is an outcome control. Shared professional expectations about surfacing uncertainty may support both. The checklist can become ritual; the resolution metric can reward premature closure; shared values can exclude dissent. A portfolio must therefore be examined in use.

A readily counted model output is not necessarily a suitable performance measure. Drafts per hour may increase while warehouse investigation queues grow. A financial control might appropriately block duplicate credits, yet fail to recognise a different form of duplicate remedy. Controls need an explicit scope, operating owner and revision route.

## Documentation and auditing support accountability but do not replace it

Mitchell et al. (2019) propose **model cards**, reports describing intended uses, evaluation conditions and limitations. Raji et al. (2020) propose an internal auditing framework across AI development. These make questions and artefacts more systematic; neither establishes that a particular organisation has an effective accountability relationship. [Mitchell et al. (2019)](../bibliography.md#mitchell-et-al-2019) · [Raji et al. (2020)](../bibliography.md#raji-et-al-2020)

Harbour could document the assistant's permitted uses, test cases, known failure patterns and change history. An audit could compare those claims with selected cases and deployment records. The governance question remains who must respond when the audit identifies a problem, by when, and with what power to change the service.

**Provenance** is a record of where an item came from and how it changed. It can support investigation of a recommendation. Provenance alone does not establish truth, authorisation or fairness. Likewise, recording a person's name cannot settle whether that person had enough information or freedom to make the decision.

## Meaningful review needs resources and a practical alternative

A **human review** is meaningful when the reviewer can evaluate and change the proposal under the actual conditions of work. That includes time, relevant knowledge, access to evidence, practical permission to disagree and an alternative route when evidence is insufficient.

Buçinca, Malaya and Gajos (2021) tested interventions intended to reduce overreliance on AI recommendations in a controlled experiment. Some designs requiring additional thought reduced overreliance, while participants' preferences and the distribution of benefits complicated the result. A laboratory result does not show that every extra confirmation screen improves workplace judgement. [Buçinca et al. (2021)](../bibliography.md#bu-inca-et-al-2021)

Harbour might require a reviewer to identify the conflicting quantity before seeing a suggested remedy. That could support checking; it could also create mechanical copying or delay urgent cases. A pilot should assess error detection, review burden, disagreement and customer consequences, including cases where the assistant is wrong. Counting completed review screens is too narrow.

## Worked arrangement: govern a remedy rather than a button

Harbour separates four objects: the evidence brief, the remedy proposal, approval of a particular proposal version and the transaction resulting from execution. The separation makes responsibility more precise without assuming that each object needs a separate department.

| Decision or obligation | Proposed role | Conditions and evidence |
|---|---|---|
| Maintain delivery evidence | Warehouse or transport record owner | Correction provenance and unresolved discrepancies |
| Prepare a remedy proposal | Service case owner, assisted by AI | Source-linked brief and visible uncertainty |
| Authorise the remedy | Designated business approver | Eligible case, specified version and applicable limits |
| Execute a financial action | Restricted transaction service | Valid authorisation and duplicate-action checks |
| Investigate recurring failure | Cross-functional service review | Cases, rejected proposals, corrections and workload |
| Change policy | Named policy authority | Recorded rationale, consultation and subsequent review |

The table is a design to test, not an implemented feature list. It does not choose Harbour's legal mandates or monetary limits. Those would require an operating policy and jurisdiction-specific advice where relevant.

Consider a changed quantity after approval. The execution service should refuse to treat approval of an old proposal as authority for a new one. That technical check is testable. Whether reviewers understand the refusal and can obtain a timely new decision is an organisational question requiring observation.

The review forum also needs a bounded obligation. It could require the service owner to explain duplicate remedies, direct a correction and revisit the evidence rule. If it receives only aggregate success rates, it may never see the exceptions. If it can question but not require a response, the relationship differs from one with enforceable corrective authority.

## Accountability can redistribute burdens

Controls can protect customers and workers. They can also shift risk downward. If an interface hides decisive evidence while naming the last reviewer in every failure report, traceability can make a person visible without making their conditions of action visible.

Kellogg, Valentine and Christin (2020) review algorithmic control and its contestation. Their synthesis directs attention to how systems direct, evaluate and discipline work, and how workers respond. Applying that lens to Harbour means investigating who is measured, who can challenge a score and who can revise the measurement. It does not imply that every AI assistant exercises all the control mechanisms discussed in the review. [Kellogg et al. (2020)](../bibliography.md#kellogg-et-al-2020)

A further complication is displaced discretion. Bovens and Zouridis (2002) examine how computerisation can shift judgement toward system-level design in public administration. The narrower AI teaching interpretation is to follow choices about categories, evidence and thresholds upstream, rather than attach all responsibility to the final transaction. [Bovens and Zouridis (2002)](../bibliography.md#bovens-and-zouridis-2002)

## Exercise: what would make this answerable?

A service owner claims, “Every action is logged, so the system is accountable.” Identify the missing relationships and propose evidence.

**Worked response.** Name the actor obliged to explain the action, the forum able to question the explanation, the standard used to judge it and the possible consequence. Examine an actual disputed case, the information available to the forum and whether its requested correction occurred. A complete log supports reconstruction; it does not establish that the forum can act or that the reviewer controlled the disputed premises.

## Advanced inquiry: test the gap between formal and effective influence

Follow both accepted and rejected proposals. Compare policy documents, permission settings, observed review and disputed cases. A proposition is that concentrated control over evidence selection can increase effective influence despite decentralised formal approvals. Rival explanations include reviewer expertise, case urgency and limited staffing. A defensible study must examine these rather than infer influence from the approval chart.

Connect the inquiry to [decision premises](03-decisions.md), [repeated practice](05-routines.md) and [process architecture](09-process-architecture.md). Accountability concerns those arrangements together, not an isolated model property.

## References

The [project bibliography](../bibliography.md) supplies complete entries and source-access information for the additional AI literature.

### Bovens (2007)
Bovens, M. (2007). Analysing and assessing accountability: A conceptual framework. *European Law Journal, 13*(4), 447–468. [Publication](https://doi.org/10.1111/j.1468-0386.2007.00378.x).

### Lindberg (2013)
Lindberg, S. I. (2013). Mapping accountability: Core concept and subtypes. *International Review of Administrative Sciences, 79*(2), 202–226. [Publication](https://doi.org/10.1177/0020852313477761).

### Jensen and Meckling (1995)
Jensen, M. C., and Meckling, W. H. (1995). Specific and general knowledge, and organizational structure. *Journal of Applied Corporate Finance, 8*(2), 4–18. [Publication](https://doi.org/10.1111/j.1745-6622.1995.tb00283.x).

### Aghion and Tirole (1997)
Aghion, P., and Tirole, J. (1997). Formal and real authority in organizations. *Journal of Political Economy, 105*(1), 1–29. [Publication](https://doi.org/10.1086/262063).

### Ouchi (1979)
Ouchi, W. G. (1979). A conceptual framework for the design of organizational control mechanisms. *Management Science, 25*(9), 833–848. [Publication](https://doi.org/10.1287/mnsc.25.9.833).

### Eisenhardt (1985)
Eisenhardt, K. M. (1985). Control: Organizational and economic approaches. *Management Science, 31*(2), 134–149. [Publication](https://doi.org/10.1287/mnsc.31.2.134).

### Kirsch (1996 and 1997)
Kirsch, L. J. (1996). The management of complex tasks in organizations: Controlling the systems development process. *Organization Science, 7*(1), 1–21. [Publication](https://doi.org/10.1287/orsc.7.1.1).

Kirsch, L. S. (1997). Portfolios of control modes and IS project management. *Information Systems Research, 8*(3), 215–239. [Publication](https://doi.org/10.1287/isre.8.3.215).
