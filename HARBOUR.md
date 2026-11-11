# Meet Harbour: the business case used in this course

[Start here](START-HERE.md) · [Companion curriculum](README.md) · [Workbook](WORKBOOK.md)

## A customer waiting for packaging

A small manufacturer has finished making a customer's order. Its dispatch team needs boxes to pack the goods and send them out. Harbour, its packaging supplier, has delivered an order. The customer's receiving team reports ten boxes, although the order and shipment records each show twelve.

Two boxes may sound like a small problem. The customer may have to interrupt packing, count stock again, buy substitutes or ask Harbour for a replacement. Harbour must respond without assuming what happened. Its records could be wrong; the customer could have counted differently; the delivery could be incomplete. The discrepancy opens an investigation, not a finding against a particular team.

This is case **H-17**, the thread running through the course. The company, customer situation and all operational examples are fictional. The fuller company background below is a teaching design, not a report about an actual business. Prices, volumes and timings introduced in exercises are separate labelled assumptions rather than established company performance.

## What Harbour does

Harbour is a business-to-business distributor of packaging materials. It buys items such as boxes, protective packaging and packing supplies from manufacturers, holds stock and sells them to business customers. Its customers include manufacturers, retailers and businesses preparing goods for dispatch. These customers need the right materials in usable condition and at a useful time, with accurate commercial records.

A **distributor** connects producers with customers who may need smaller quantities, mixed orders, local availability or delivery arrangements. Harbour does not simply move a parcel. It coordinates purchasing, stock availability, order commitments, warehouse work, delivery and account settlement. In this fictional business, some transport is supplied by delivery partners, creating a boundary between Harbour's internal work and another organisation's records and responsibilities.

Harbour earns revenue by selling packaging. The difference between sales revenue and the cost of goods must also support storage, handling, delivery, service and other operating expenses. A replacement shipment can protect a customer relationship while adding cost and consuming stock needed elsewhere. Rejecting an unsupported claim can protect margin while damaging trust if the investigation is slow or unfair. The business needs evidence and judgement about both service and cost.

Cash timing matters alongside margin. Harbour may pay for stock before the customer pays its invoice. Holding extra stock can support availability while tying up funds and storage capacity. A delayed dispute can also leave an invoice unsettled. Finance therefore participates in the operating design, rather than appearing only after the physical work is finished.

No particular company size, software vendor, national tax regime or measured financial result is assumed. The operational setting is sufficiently specific to explain the work while leaving these additional implementation choices open.

## Follow the supply chain

A **supply chain** is the connected work through which organisations obtain materials and deliver goods or services to customers. At Harbour, the teaching picture is:

**Suppliers → inbound receipt → stored inventory → customer order → picking and packing → dispatch and transport → customer receipt**

Information, decisions and money connect these physical activities. A customer order moves upstream to guide fulfilment. Availability information moves back to the customer. An invoice requests payment; a dispute can interrupt settlement. A return, replacement or credit can create work in the opposite direction to the original delivery.

| Stage | Work and information | A dependency that can cause trouble |
|---|---|---|
| Purchasing and replenishment | Agree supply, monitor availability and arrange incoming stock | Sales promises depend on stock and supplier commitments that may change |
| Inbound receipt and inventory | Receive supplies, identify items and record usable quantities | A receipt entry or stock count can differ from the physical goods |
| Customer order and commitment | Record items, quantities, delivery needs and agreed terms | A requested date is not automatically a feasible delivery promise |
| Warehouse fulfilment | Allocate stock, pick, pack and record dispatch | A system entry does not establish everything that occurred on the warehouse floor |
| Transport and delivery | Hand goods to a carrier and obtain delivery information | Dispatch, carrier events and customer receipt describe different moments |
| Customer service and investigation | Clarify reports, assemble evidence and coordinate follow-up | Several teams can own records while no one accepts the unresolved case |
| Finance and settlement | Invoice, review account discrepancies and process authorised adjustments | A delivery investigation and an invoice correction may require different evidence and authority |

**Picking** means selecting the ordered items from storage. **Packing** prepares them for transport; **dispatch** hands them into the delivery process. **Inventory** means stock held for use or sale. **Replenishment** means arranging more stock to meet future needs. A **credit** reduces an amount charged to a customer; it is distinct from shipping replacement goods or making a payment. These distinctions matter because each action changes a different part of the business.

The notebooks implement selected investigation and service mechanisms. They do not implement purchasing, stock planning, carrier integration, a complete warehouse system or an accounting ledger. Those activities supply the business context needed to judge the implemented contribution.

## How work is organised

An **organisation design** concerns how work, responsibilities, decisions and coordination are arranged to achieve an organisation's purposes. A department chart shows part of that arrangement. It does not show whether a customer receives a timely answer when records disagree.

Harbour's case background divides expertise across the following functions. These are functional responsibilities in the fictional setting, rather than a claim that every role has already been implemented in the software.

| Function | Contribution to the business | Boundary that needs coordination |
|---|---|---|
| Sales and customer service | Understand needs, record commitments and communicate with customers | A promise must be connected to available stock and a feasible delivery |
| Planning and purchasing | Coordinate replenishment and supplier questions | Buying more stock is different from resolving a delivery already disputed |
| Warehouse operations | Maintain handling records and investigate picking, packing and stock questions | Its dispatch evidence must be interpreted alongside carrier and customer evidence |
| Transport coordination | Obtain carrier information and arrange delivery follow-up | Another organisation may control a record or the next physical activity |
| Finance | Maintain invoice and account records and process authorised adjustments | It needs an accepted basis for a correction, not just a persuasive customer summary |
| Operations and case investigation | Bring the evidence together and coordinate unresolved delivery work | Assignments and handoffs need acceptance; sending a message does not settle ownership |
| Technology and service support | Maintain the application, access rules and technical recovery | Repairing a failed API request does not resolve the underlying customer dispute |

Specialisation helps each function develop expertise. It also creates **interdependence**: one team's work needs another team's contribution. Customer service cannot finish an evidence-based explanation without operations information. Operations may need a customer recount. Finance may need a remedy decision before changing an account. The work can move back and forth rather than follow a neat one-way sequence.

The [organisation design chapter](reference/research/01-organisation-design.md) explains why dividing work creates an integration problem. The [coordination chapter](reference/research/02-coordination.md) helps distinguish work that shares a resource, follows another task or requires mutual adjustment. Applying those ideas to Harbour is a teaching interpretation, not an empirical finding about a distributor.

## Competing priorities are part of the case

Customer service wants to keep the customer informed. Warehouse staff also need to finish today's dispatches. A carrier contact may be waiting for information from a depot. Finance needs accurate records and an authorised basis for an adjustment. Investigators need enough evidence and time to challenge a premature conclusion.

Each concern is reasonable. Problems arise when local priorities do not combine into a satisfactory service. Fast complaint intake can simply produce a longer investigation queue. Rapid dispatch can coexist with poor evidence about exceptions. Fewer issued credits can coexist with unresolved valid complaints. A metric that looks favourable in one team can shift effort or risk to another.

An **end-to-end outcome** concerns the connected service, such as resolving a disputed delivery with an appropriate explanation and action. A **local measure** concerns one contribution, such as minutes spent drafting a brief. The course uses both, but never treats improvement in the second as proof of improvement in the first.

## What happens in H-17?

The order is **O-17**; the investigation is **H-17**. They are different records about related work. The full teaching case distinguishes three sources:

| Source | What it records | What it does not establish on its own |
|---|---|---|
| `order-17` | Twelve boxes ordered | That twelve were picked, dispatched or received |
| `shipment-17` | Twelve boxes recorded for shipment | That the physical delivery matched the entry or that the customer received twelve |
| `customer-17` | Customer reports receiving ten | A verified final count, the cause or the person responsible |

Subtracting ten from twelve gives a difference of two between the selected quantities. It does not prove a warehouse error, a carrier loss or a customer mistake. The service has to preserve the difference between a recorded value, a reported value and an investigated conclusion.

A plausible investigation involves the following work:

1. Customer service records the report and the customer's practical concern.
2. An investigator checks that the order, shipment and report refer to the same delivery and compatible units.
3. Warehouse and transport contacts examine relevant records; customer service obtains clarification or a recount where appropriate.
4. The investigator reconciles the accounts where possible and states what remains uncertain.
5. An authorised manager considers a proposed remedy. Finance processes an authorised account correction where required; operations coordinates any agreed physical action.
6. Customer service communicates the accepted position and next steps. The case remains open if required work is unfinished.

This is an explanatory business workflow. It is not a claim that the application performs every step. In the first prototype, the permitted AI contribution is preparation of an investigation brief. Later exercises examine proposed routing, accepted handoffs and simulated review decisions. No real credit, payment or replacement shipment is executed.

## The initial problem and the design proposal

The recurring problem explored in the case is fragmented evidence and unclear acceptance of work across functions. An adviser can pass on a complaint without knowing whether a warehouse contact has accepted the investigation. An investigator can receive a polished summary that omits a disputed source. A manager can face a remedy request without knowing which facts were checked. These are scenario conditions to examine, not measured rates of failure.

The proposed service brings source-labelled evidence and unresolved questions into a usable brief. The proposal also needs an arrangement for people: an identifiable case owner, source owners who can correct records, recipients who can reject incomplete handoffs, and a route for stalled or disputed cases. A named technical operator handles service defects without being presumed to own commercial judgement.

The existing division of functional expertise is the case background. Assigning clearer case ownership, acceptance conditions and review duties is a design proposal to assess. The story does not assume that those proposed changes are already operating successfully. Later modules compare alternatives and examine where they could fail.

A **decision right** identifies who may make a particular choice. Access to a source, permission to draft, approval of a remedy and execution of an account adjustment are different rights. The [decision chapter](reference/research/03-decisions.md) develops this distinction. A manager label inside model text grants none of them.

## A consistent approval arrangement

Harbour’s default teaching arrangement gives an authorised manager the remedy decision. Finance processes an authorised account change where appropriate, and operations coordinates any agreed physical action. A finance manager may hold the authorised-manager role; membership of the finance team alone does not grant that authority. Some lessons deliberately examine different proposed responsibilities or conflicting sources. They should be read as design alternatives, not silent changes to the implemented permission checks.

A manager role in a simulation expresses a technical permission. Whether the person holding it has suitable expertise, time and organisational authority remains a design question. No example connects that permission to real stock, credit or payment execution.

## Four views of one service

A supply-chain view asks how physical goods, commitments and information connect. A finance view asks what commercial consequences follow and who may authorise an adjustment. A customer view asks whether the response is timely, intelligible and appropriate. A technology view asks whether data access, execution and recovery behave as intended.

Organisation design connects those views. It asks how Harbour can combine specialised contributions, handle disagreement and retain accountability across organisational boundaries. The answer may include better intake, a clearer shared record, changed responsibilities or direct discussion. A language model is one possible contributor.

The [implementation chapter](reference/research/04-implementation.md) explains why a plausible benefit needs a population and comparison. The [routines chapter](reference/research/05-routines.md) examines how actual work can differ from a process diagram. The [technology-in-practice chapter](reference/research/06-technology-in-practice.md) asks how a technical feature becomes a practical possibility for particular actors. These chapters supply the scholarly reasoning used to analyse Harbour.

## How the company develops through the course

In **Part 1**, learners understand the business problem, distinguish sources from claims and compare technical contributions. In **Part 2**, they examine what happens when several components participate: which work can proceed independently, which result needs acceptance, and how a case can pause or recover. The companion concludes with a worked integration proposal that connects technical checks with operating responsibilities.

These are progressively harder design questions, not a report that Harbour adopts every new capability. The company does not need agent teams simply because a module teaches them. A defensible final proposal may retain a simpler lookup, restrict generation to selected cases or stop a capability whose costs outweigh its contribution.

The small workshop examples supply only the records shown in their code. A later exercise may omit the dispatch record or change the case identifier. Treat that as a separate teaching example and use the evidence supplied for it.

## A first design exercise

Before proposing AI, draw the path of the goods, the path of the information and the path of a remedy decision. Mark where work crosses a team or organisational boundary. Identify one place where a participant needs evidence and another where a participant needs a decision from someone else.

**Worked starting point.** Goods move from Harbour's warehouse through a carrier to the customer. The complaint travels back to customer service, then prompts investigation across the warehouse, carrier and customer. The remedy decision follows a separate authority path. An investigator needs access to relevant records, but record access alone does not authorise an adjustment. A finance specialist may correct an invoice issue without deciding what happened in the warehouse.

A strong design record keeps these paths connected without collapsing them into one agent's job. By the end of the course, it should explain how the proposed service fits the business, how responsibilities work in practice, what remains uncertain and what evidence could justify changing the arrangement.
