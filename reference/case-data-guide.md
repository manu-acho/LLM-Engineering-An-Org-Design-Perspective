# Follow the cases, records and learning artefacts

[Curriculum](../CURRICULUM.md) · [Workbook](../WORKBOOK.md)

Harbour is a fictional distributor used to connect technical choices with the organisation of work. An investigation case is not the same object as its order, policy or model run.

| Identifier or artefact | Meaning |
|---|---|
| H-17 | The continuing investigation case: order twelve, customer report ten |
| O-17 | The order discussed in conversation examples; an order identifier, not a second case |
| order-17 / customer-17 | Source identifiers for the respective evidence |
| P-2 / P-4 | Current permitted policy passages in the extended case fixtures |
| H-19 | Equal quantities with damaged goods; quantity agreement does not settle condition |
| H-20 | An invoice/tax issue requiring the relevant routing rule |
| H-21 | Missing receipt information, requiring more evidence |
| H-22 | A report containing instruction-like text, used to examine trust boundaries |
| H-23–H-26 | Separate teaching comparison cases; their public reference labels are not confidential enterprise test evidence |
| H-18 | A south-region case used to examine denied north-region access |
| meeting-1 | A separate meeting-note illustration about suggestions and accepted commitments |

The small Module 1 lab and the later packaged implementation use the same H-17 case identifier. The standalone two-file lab deliberately has fewer fields. The extended fixtures in `src/ai_orgdesign/case_data.py` add policy, categories and contrasting cases. A case's `expected` reference label is held by the evaluator and removed by `get_case` before preparing model context.

The meeting-note and historical routing examples are additional applications, not new facts about H-17. They ask how commitments or categories become organisational records. Their organisational questions connect with the delivery case without pretending they share the same data.

## Keep the artefacts separate

A source record supplies a recorded or reported value. A retrieved passage is a selected representation of a source. A generated brief is a proposed contribution. An accepted handoff records that a recipient can use it. A review decision records an authorised next step. A run trace describes selected execution events. None substitutes for all the others.

The notebooks progressively construct these artefacts and show the relevant fields. When an example changes a quantity or category, it is a new fictional experiment. Preserve that distinction in the workbook instead of treating every output as part of one consistent real-world history.

## Use the splits honestly

Development cases support diagnosis and iteration. The teaching confirmation split supports learning a comparison procedure. Both are public, small, invented and inspected during course development. Their scores are not estimates of enterprise performance or evidence of an untouched scientific benchmark. A real deployment needs an appropriately governed evaluation population, source and label review, and a comparison with the surrounding work.

## Define the teaching routes before scoring them

`needs_evidence` means that the customer-reported quantity itself is missing. `investigate` means that supplied order and reported quantities disagree. `review` covers qualitative conditions such as damaged goods when quantities agree. `finance` routes the invoice/tax issues defined by the supplied policy. All four still involve accountable work; none is a remedy approval.

Actual receipt remains unverified across these fixtures. That common uncertainty must not collapse every category into `needs_evidence`. A development run exposed precisely that ambiguity. The clarified `grounded-v3` instruction profile makes the categories' operational meanings explicit before comparison. In a real service, disagreement about such meanings requires a task and policy decision, not merely another training run.
