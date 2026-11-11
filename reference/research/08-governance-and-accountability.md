# Research chapter 8: Governing AI decisions and making them answerable

[Research reading guide](../literature-guide.md) · [Previous: infrastructure](07-infrastructure-and-standards.md) · [Next: process architecture](09-process-architecture.md)

## A recorded approval can still leave responsibility unresolved

**Fictional Harbour case.** An assistant recommends a credit for a disputed delivery. A service colleague approves it. Finance later discovers that a replacement shipment was already arranged, so the customer received two remedies. The log identifies a reviewer, a tool call and a transaction. It does not explain who was expected to check for an existing remedy, who could change that rule or who must answer the complaint about the failure.

Harbour's customer service, warehouse, transport and finance activities depend on one another. The AI service sits inside those relationships. [The business case](../../HARBOUR.md) supplies the company context. This chapter separates governance, decision rights, control and accountability, then uses the distinctions to design a review arrangement. All Harbour proposals are fictional teaching applications.

## Four terms that answer different questions

**Governance** concerns how an organisation establishes and exercises the right to direct work. For Harbour, that means deciding who can set the assistant’s scope, change the rules for issuing credits and settle disputes about those rules. A right is legitimate when it is recognised under the relevant organisational rules and obligations.

**Decision rights** specify who may decide particular matters. They need an object and conditions: for example, authority to approve a specified credit for an eligible case, within a stated limit. “Owns AI” leaves too much unspecified.

**Control** concerns efforts to guide conduct or results. A control arrangement links a target or standard to observation, comparison and a response. At Harbour, a duplicate-remedy check compares a proposed credit with earlier remedies and blocks or refers a possible duplicate for investigation. A system can record a target without anyone being able to intervene when it is missed.

**Accountability** concerns a relationship in which an actor is obliged to explain conduct to someone entitled to question and judge it. Bovens (2007) distinguishes an actor required to explain conduct from a forum able to question, judge and attach consequences. Lindberg (2013) clarifies accountability as a concept with multiple forms. A public-sector theory should not be transferred wholesale to a private firm, but it supplies a sharper question than whether logs exist. [Bovens (2007)](#bovens-2007) · [Lindberg (2013)](#lindberg-2013)

A **forum** in an accountability relationship is the person or body entitled to hear and judge an explanation. **Answerability** is the actor's obligation to provide that explanation. Harbour's transaction log is potentially evidence for this relationship. A finance review panel with a defined mandate, access to explanations and power to require correction is a possible forum. Its actual operation still needs investigation. Calling a meeting an accountability forum does not establish that it can question anyone or change anything.

## Put decisions near knowledge, while examining the costs

Jensen and Meckling (1995) examine the costs of bringing decision rights and relevant knowledge together. **Specific knowledge** is costly to transfer to another decision-maker. A warehouse colleague may understand why a damaged pallet was recorded under an unusual code, while finance understands the financial consequences of a remedy. [Jensen and Meckling (1995)](#jensen-and-meckling-1995)

**Centralisation** concentrates decision rights in a central role or unit. **Decentralisation** distributes them toward other roles or units. **Delegation** assigns a defined scope of decision-making to another actor. Moving all decisions to a central specialist can lose local knowledge or require expensive communication. Delegation can preserve access to that knowledge while creating work to coordinate decisions and check that they remain within their scope. Neither centralisation nor decentralisation is automatically the answer.

An AI summary changes the means of communication, but its completeness cannot be assumed. A concise account may omit the qualification that makes the warehouse code meaningful. The governance design should establish which decisions need direct consultation, which evidence can travel in structured form and how the receiver can challenge that form.

Aghion and Tirole's (1997) distinction between **formal authority**, a right to decide, and **real authority**, effective influence over the decision, adds a further problem. A manager can retain the final approval while a model or specialist effectively frames every available option. This is an application of the distinction to AI, not a claim that their model analysed modern assistants. [Aghion and Tirole (1997)](#aghion-and-tirole-1997)

## Select controls for the work that can actually be assessed

Ouchi (1979) distinguishes markets, bureaucracies and clans as control mechanisms under different conditions. A market coordinates through exchange and prices; bureaucracy relies on rules and authority; clan control draws on shared values and socialisation. These are **ideal types**, deliberately simplified patterns used to compare arrangements. “Ideal” here does not mean best. **Socialisation** is the process of learning shared expectations through participation, training and interaction. Actual organisations can combine these forms of control. [Ouchi (1979)](#ouchi-1979)

Eisenhardt (1985) examines the relationship between behaviour and outcome control, including the ability to specify conduct and measure outcomes. **Behaviour control** examines how work is performed. **Outcome control** examines its results. Kirsch (1996, 1997) extends attention to **portfolios of controls**, combinations of measures used together. **Formal controls** rely on explicit requirements and assessments. **Informal controls** also work through shared expectations, relationships and self-direction in complex systems work. [Eisenhardt (1985)](#eisenhardt-1985) · [Kirsch (1996, 1997)](#kirsch-1996-and-1997)

At Harbour, **behaviour control** might require reviewers to check for a replacement shipment before approving a credit. **Outcome control** might examine whether customers receive the agreed remedy without a duplicate. Informal expectations can help reviewers feel able to flag missing evidence. Each can fail in use. Reviewers may tick the checklist without opening the shipment record. A closure target may encourage early closure. Team norms can discourage a new colleague from raising a doubt. To assess the controls, examine what reviewers actually check and what happens when they disagree.

A readily counted model output is not necessarily a suitable performance measure. Drafts per hour may increase while warehouse investigation queues grow. A financial control might appropriately block duplicate credits, yet fail to recognise a different form of duplicate remedy. Controls need an explicit scope, operating owner and revision route.

## Documentation and auditing support accountability but do not replace it

Mitchell et al. (2019) propose **model cards**, reports describing intended uses, evaluation conditions and limitations. An **audit** is a structured examination of claims, evidence and practice against specified criteria. Raji et al. (2020) propose an internal auditing framework across AI development. These make questions and artefacts more systematic; neither establishes that a particular organisation has an effective accountability relationship. [Mitchell et al. (2019)](../bibliography.md#mitchell-et-al-2019) · [Raji et al. (2020)](../bibliography.md#raji-et-al-2020)

A model card for Harbour’s assistant could say that it drafts evidence briefs and has been tested on complaints involving split shipments. An audit could inspect selected cases and the deployed permissions to check how the service operates. If the audit finds that credit requests were made outside the approved scope, accountability requires a person to explain what happened to a forum that can demand a response. The model card and audit provide material for that inquiry.

**Provenance** is a record of where an item came from and how it changed. It can support investigation of a recommendation. Provenance alone does not establish truth, authorisation or fairness. Likewise, recording a person's name cannot settle whether that person had enough information or freedom to make the decision.

## Meaningful review needs resources and a practical alternative

A **human review** is meaningful when the reviewer can evaluate and change the proposal under the actual conditions of work. That includes time, relevant knowledge, access to evidence, practical permission to disagree and an alternative route when evidence is insufficient.

Buçinca, Malaya and Gajos (2021) tested interventions intended to reduce overreliance on AI recommendations in a controlled experiment. Some designs requiring additional thought reduced overreliance, while participants' preferences and the distribution of benefits complicated the result. A laboratory result does not show that every extra confirmation screen improves workplace judgement. [Buçinca et al. (2021)](../bibliography.md#bu-inca-et-al-2021)

Harbour could test the experiment’s principle by asking reviewers to identify the conflicting quantity before revealing the suggested remedy. The extra step might prompt a source check. It could also produce mechanical copying or delay urgent cases. A pilot could compare the two review procedures on errors caught, time spent, disagreements raised and customer consequences. Cases where the assistant is wrong are especially informative.

## Worked arrangement: govern a remedy rather than a button

The duplicate remedy in the opening case involves several decisions and records. The evidence brief describes what happened. The remedy proposal recommends a response. Approval authorises a particular version of that proposal. The transaction records what the service actually did. Harbour can use those distinctions to assign responsibility at each step and to identify which record would help explain a duplicate.

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

**Discretion** is the room to interpret a situation or choose among alternatives. **Displaced discretion** means that some of that judgement moves elsewhere, for example from an adviser handling a complaint to the people setting the system's eligibility rules. Bovens and Zouridis (2002) examine how computerisation can shift judgement toward system-level design in public administration. The narrower AI teaching interpretation is to follow choices about categories, evidence and thresholds upstream, rather than attach all responsibility to the final transaction. [Bovens and Zouridis (2002)](../bibliography.md#bovens-and-zouridis-2002)

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
