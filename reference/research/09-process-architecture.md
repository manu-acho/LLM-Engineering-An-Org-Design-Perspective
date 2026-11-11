# Research chapter 9: AI within the business process

[Research reading guide](../literature-guide.md) · [Previous: governance](08-governance-and-accountability.md) · [Study pathways](../research-study-pathways.md)

## A good agent run can end before the business problem does

**Fictional Harbour case.** An agent retrieves delivery records, drafts a response and records a successful run. The customer still needs replacement packaging for tomorrow's production. The warehouse has no confirmed replacement order, transport has no collection instruction and finance is considering a credit. The technical run succeeded within its boundary. The business process remains unresolved.

Harbour distributes packaging through linked purchasing, inventory, order fulfilment, delivery and financial activities. [The business case](../../HARBOUR.md) introduces these dependencies. This chapter explains processes, models and event evidence before examining how an AI workflow fits within a wider process architecture. The cases and proposed measures are teaching examples.

## Process, model, workflow and performed work

A **business process** connects activities that contribute to an outcome. A delivery-discrepancy process may begin with a reported problem and end with an agreed, completed remedy and reconciled records. Choosing those boundaries is an analytical decision: a narrower study might examine only evidence gathering.

A **process model** represents selected activities, decisions, roles or data. Harbour’s diagram might show a step called “check for an earlier remedy”. A **configured workflow** consists of steps and rules set up in software. It could require a reviewer to record that check before the credit service accepts a request. **Performed work** is what people and systems actually do. A reviewer might look for the credit in one system and call the warehouse to confirm whether a replacement was sent. The call can be part of the performed process even when the diagram and workflow omit it.

Curtis, Kellner and Over (1992) distinguish perspectives on process modelling. The **functional** perspective asks what work is done. The **behavioural** perspective asks how activities are ordered and under which conditions. The **organisational** perspective examines who participates and how responsibility is arranged. The **informational** perspective examines the information used and produced. Dumas et al. (2018) provide a broader business-process-management treatment. Together they help explain why a flow diagram alone is insufficient: it may show order while omitting responsibility or information meaning. [Curtis et al. (1992)](#curtis-et-al-1992) · [Dumas et al. (2018)](#dumas-et-al-2018)

An agent workflow can be drawn as a **graph**, with steps shown as nodes and connections shown as edges. Harbour’s graph might run from retrieving records to generating a brief. A successful run shows that the graph reached its specified end. The business process continues if another team must accept the brief, check for an earlier remedy or confirm that the customer received the replacement.

## Activities, events, roles and objects

An **activity** is a piece of work, such as checking delivery evidence. An **event** records or denotes something that happened, such as a delivery scan being received. An event named “delivery complete” may express a system status rather than independently verified completion.

An **actor** is a particular person or system participating in work. A **role** groups responsibilities or expected contributions, such as remedy approver. The same person can hold several roles; a role label does not prove that the holder has time, knowledge or authority to fulfil it.

A **business object** is something the work concerns, such as an order, shipment, complaint or invoice. Its **state** is a selected condition, such as disputed, approved or settled. State changes must have clear meaning. Closing a complaint record should not silently mean that an invoice was corrected.

| Object | Possible state change | Separate question |
|---|---|---|
| Complaint | Open to response sent | Did the customer accept the response? |
| Shipment | Planned to delivered | What evidence supports receipt? |
| Remedy proposal | Draft to approved | Is approval still valid for this version? |
| Credit | Requested to posted | Was a duplicate remedy prevented? |
| Case | Investigating to resolved | Are operational and financial issues reconciled? |

These are illustrative states, not a claim that the existing lab implements every object. Their purpose is to make missing relationships visible before software is extended.

## A model needs a purpose and a chosen level of detail

A **modelling purpose** states what the representation is intended to help examine. A high-level customer journey can orient managers. It cannot specify every execution condition. A detailed tool-call flow can support testing while obscuring the full service outcome.

**Granularity** is the level of detail. “Resolve complaint” is coarse. “Read scan”, “compare quantity” and “request recount” are finer. Combining both levels without indicating the distinction can make a diagram misleading.

Mendling, Reijers and van der Aalst (2010) propose guidelines for understandable process models. Their contribution concerns model quality; a readable model still requires evaluation of whether it represents the relevant work. [Mendling et al. (2010)](#mendling-et-al-2010)

A **notation** is a set of symbols and rules for representing something, such as activities and decisions in a process diagram. Three questions help assess a model.

**Syntactic quality** concerns compliance with the chosen notation. **Semantic quality** concerns whether it represents the relevant domain adequately. **Pragmatic quality** concerns whether intended readers can understand and use it.

For Harbour, the diagram may use valid symbols yet omit the second shipment that changes the remedy decision. It then has a semantic problem. A diagram that represents the relevant work but is unintelligible to its intended readers has a pragmatic problem. Here pragmatic concerns usability of the model. Chapter 2 uses pragmatic knowledge boundary to discuss differences in interests across groups.

A model should therefore state its boundary, audience, assumptions and omitted cases. At Harbour, a normal-delivery model must not be presented as a complete remedy process if it excludes damaged goods, split shipments and disputed receipts.

## Process architecture connects the processes

A **process architecture** describes relationships among multiple processes, rather than the steps of only one. Dijkman, Vanderfeesten and Reijers (2016) review approaches to designing these architectures. The perspective helps connect local improvement to shared objects and responsibilities across the organisation. [Dijkman et al. (2016)](#dijkman-et-al-2016)

Harbour's shortage investigation depends on order fulfilment and delivery evidence. Its remedy may initiate a new shipment, affect inventory and require financial reconciliation. **Procurement**, the work of arranging purchases from suppliers, enters when replacement stock is unavailable. **Financial reconciliation** checks that related delivery, invoice and remedy records agree or that their differences are explained. An agent that optimises only complaint drafting may move work into each of these processes.

This changes evaluation. Draft completion, customer resolution, warehouse rework and financial correction measure different things. A local time saving can coexist with greater total work. Conversely, extra evidence preparation may reduce downstream disputes. A process architecture helps specify what needs comparison; it does not establish the direction of the result.

**Business process management**, or BPM, concerns the continuing identification, analysis, redesign, implementation and monitoring of processes. Dumas et al. (2018) organise these activities as a lifecycle. Vom Brocke et al. (2014) emphasise principles including context and continuity. BPM therefore extends beyond drawing a process once or installing a workflow tool. [Dumas et al. (2018)](#dumas-et-al-2018) · [Vom Brocke et al. (2014)](#vom-brocke-et-al-2014)

## What event logs can reveal

**Process mining** uses recorded events to study processes. Van der Aalst (2013) distinguishes three uses. **Discovery** builds a process model from recorded events. **Conformance checking** compares recorded behaviour with a selected model. **Enhancement** uses event evidence to add information to, or improve, an existing model, for example by showing where recorded waiting occurs. **Conformance** means correspondence with the selected model, not proof that the model expresses good policy. [Van der Aalst (2013)](#van-der-aalst-2013)

An **event log** is a collection of records of selected events. A conventional log links an activity and a **timestamp**, the recorded date and time, to a **case identifier**, the key used to group events into one process instance. An instance is one occurrence of the process, such as handling a particular complaint. Choosing that identifier matters. A complaint can concern several shipments; one shipment can contain items from several orders. An invoice may cover several deliveries. Treating one order as one case can duplicate, fragment or omit important relationships.

At Harbour, an agent run identifier groups technical operations. It cannot automatically serve as the identifier for the customer problem. Reopening the same complaint may create another run. One run may examine several orders. Interpretation requires an explicit mapping between these objects. **Case correlation** is the work of linking events to the cases and business objects they concern. It may require complaint, shipment and invoice references together, rather than assuming that one identifier groups all the relevant work.

Logs are selective observations. Offline phone calls, delayed scans and informal clarification may not appear. Timestamps may reflect recording time rather than when work happened. A discovered sequence should therefore be investigated alongside record definitions and accounts of work. Missing events do not prove missing work.

## Variation is not automatically a defect

A **variant** is a different observed path through a process. An **exception** is a situation that falls outside a specified ordinary arrangement. Neither word establishes whether the difference is beneficial or harmful.

A recount before a credit may be a sensible response to conflicting evidence. Repeating the recount because an attachment was lost may be avoidable rework. The same activity sequence can arise for different reasons. A frequency chart alone cannot distinguish them.

Fahland and van der Aalst (2015) examine process-model repair using observed behaviour. Repair can improve correspondence between a model and recorded activity. The organisational decision remains whether the observed practice ought to be retained, changed or prohibited. Matching a model to an unsafe workaround would improve one kind of fit while preserving a problem. [Fahland and van der Aalst (2015)](#fahland-and-van-der-aalst-2015)

This is where [routines research](05-routines.md) adds something that process conformance cannot supply alone: inquiry into participants' understandings, recurrent performances and reasons for variation.

## What language models add to process work

Vidgof, Bachhofner and Mendling (2023) discuss opportunities and challenges for language models across BPM activities. Their paper is a research agenda, not evidence that an LLM can autonomously redesign a business process reliably. [Vidgof et al. (2023)](../bibliography.md#vidgof-et-al-2023)

For example, Harbour could give a language model its complaint procedure and ask for a draft process description. The output could help staff spot missing questions about split deliveries or credit reversals. It could also invent a handoff, omit a step or assign credit authority to the wrong role. A draft that records its sources and marks unresolved questions gives the warehouse and finance teams specific points to check.

A format check can show that the generated description uses valid diagram symbols. Comparing the draft with the procedure and records can reveal whether it represents the intended steps and decisions. Observing cases can show whether staff can follow those steps and what they do when the evidence conflicts. These checks address different claims about the same process.

## Worked design: extend the boundary of success

Harbour proposes recording three points in the remedy process. **Evidence ready** means the next team has enough information to investigate. **Remedy authorised** means the designated person approved the specified action. **Remedy completed** means the action occurred and the related operational and financial records were reconciled. The service can report a successful run at the first point while the customer’s case is still open.

Consider a complaint about two missing boxes. The service prepares a brief but finds a possible split shipment. The case remains awaiting clarification. After transport confirms the second shipment, the proposed remedy changes from credit to delivery confirmation. Finance checks that no earlier remedy needs reversal. Customer service closes the case only under an agreed resolution rule.

Measures should reflect those distinctions. Evidence-preparation time excludes later waiting. End-to-end resolution time uses a defined start and end, including unresolved cases rather than dropping them. Duplicate-remedy incidents require a business definition across credits and replacements. Warehouse investigation effort includes work outside the AI interface. These are proposed measures, not reported performance figures.

A meaningful comparison would examine **case mix**, the proportions of different kinds and difficulties of case, alongside exception rates, staffing and changes in recording practice. Ten straightforward delivery queries and ten disputed shortages can require very different amounts of work. When recording practice changes, apparent performance can change even if the underlying work does not.

## Exercise: draw two boundaries

Describe the boundary of an agent run and the boundary of a customer remedy. Identify one successful technical event that is insufficient for the business outcome, and one business activity that may be absent from the technical trace.

**Worked response.** The run begins with a request and ends with a prepared brief. A remedy begins with a reported discrepancy and ends under a defined operational and financial resolution rule. “Brief generated” establishes an output, not resolution. A transport colleague's phone confirmation may be essential work absent from the run trace. The design needs a way to represent its source and uncertainty without pretending the original trace contained it.

## Advanced inquiry: compare traces with performed work

Select a small, explicitly bounded sample of ordinary and disputed cases. Compare the prescribed process, configured workflow, event records and observed activity. Ask whether exceptions restore necessary coordination or compensate for avoidable design problems. Consider missing or late records as rival explanations before attributing a delay to staff behaviour.

The resulting study can connect process design to [coordination](02-coordination.md), [shared infrastructure](07-infrastructure-and-standards.md) and [accountability](08-governance-and-accountability.md). Its contribution is a reasoned account of how local AI activity enters a wider service, with boundaries that permit the claims to be checked.

## References

The [project bibliography](../bibliography.md) includes these publications, additional literature and source-access notes.

### Curtis et al. (1992)
Curtis, B., Kellner, M. I., and Over, J. (1992). Process modeling. *Communications of the ACM, 35*(9), 75–90. [Publication](https://doi.org/10.1145/130994.130998).

### Dumas et al. (2018)
Dumas, M., La Rosa, M., Mendling, J., and Reijers, H. A. (2018). *Fundamentals of Business Process Management* (2nd ed.). Springer. [Publication](https://doi.org/10.1007/978-3-662-56509-4).

### Mendling et al. (2010)
Mendling, J., Reijers, H. A., and van der Aalst, W. M. P. (2010). Seven process modeling guidelines (7PMG). *Information and Software Technology, 52*(2), 127–136. [Publication](https://doi.org/10.1016/j.infsof.2009.08.004).

### Dijkman et al. (2016)
Dijkman, R., Vanderfeesten, I., and Reijers, H. A. (2016). Business process architectures: Overview, comparison and framework. *Enterprise Information Systems, 10*(2), 129–158. [Publication](https://doi.org/10.1080/17517575.2014.928951).

### Vom Brocke et al. (2014)
Vom Brocke, J., Schmiedel, T., Recker, J., Trkman, P., Mertens, W., and Viaene, S. (2014). Ten principles of good business process management. *Business Process Management Journal, 20*(4), 530–548. [Publication](https://doi.org/10.1108/BPMJ-06-2013-0074).

### Van der Aalst (2013)
Van der Aalst, W. M. P. (2013). Business process management: A comprehensive survey. *ISRN Software Engineering, 2013*, Article 507984. [Publication](https://doi.org/10.1155/2013/507984).

### Fahland and van der Aalst (2015)
Fahland, D., and van der Aalst, W. M. P. (2015). Model repair: Aligning process models to reality. *Information Systems, 47*, 220–243. [Publication](https://doi.org/10.1016/j.is.2013.12.007).
