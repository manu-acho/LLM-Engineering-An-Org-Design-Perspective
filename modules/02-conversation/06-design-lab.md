# Lesson 2.6: Allocate discretion across a conversational service

[Download the matching notebook](/downloads/02-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../03-open-models/README.md)

## What you'll learn and why it matters

Compare ways of assigning discretion across a conversational service. Explain who should be able to change wording, select evidence or approve a credit, and why.

## Business context: Harbour

A service that drafts replies can give advisers freedom to reword a message while keeping the rules for credit approval fixed. Discretion is the room someone has to choose how to act within their role. Compare who can change a draft, choose evidence and approve a credit. Those choices do not have to be assigned to the same person or program.

A conversation becomes a usable handoff only when an investigator accepts the contribution and next responsibility.

[Company and supply-chain context](../../HARBOUR.md) · [Module 2 business situation](../../reference/harbour-learning-journey.md#module-2)

## Put the decision on the table

**Fictional worked case.** Harbour wants its assistant to resolve small disputed credits. The proposal gives the assistant an order lookup and a credit tool. An operations manager argues that anything below £50 should be automatic. Finance argues that every credit needs review. Both positions hide several decisions.

Separate identifying a case, gathering records, interpreting the discrepancy, recommending a remedy, approving it and executing it. The same actor need not perform all six. A tool's availability answers only whether a software path exists.

## Who chooses the premises?

Simon treats organisational decisions as shaped by premises: the starting points people accept when deciding. A threshold of £50 is one premise. Others include what counts as proof of delivery, whether repeated claims are grouped and whether customer statements override shipment scans. Automating the final button can leave the most consequential judgement in those earlier choices.

**Bounded rationality** recognises limits on attention, knowledge and calculation. A reviewer cannot inspect every fact in unlimited detail. **Satisficing** means searching for an acceptable solution under criteria and limits, rather than calculating an all-knowing optimum. A review form can support judgement by showing relevant evidence; it can also narrow attention to whatever the form happens to contain.

The [decision theory review](../../reference/research/03-decisions.md) distinguishes technical permission, responsibility, approval rights and accountability. Simon's acceptance-based authority and formal-versus-real authority are related questions with different theoretical origins. Neither reduces to an access-control flag.

## Compare two coherent arrangements

| Design choice | Central specialist review | Bounded frontline resolution |
|---|---|---|
| Routine evidence gathering | Assistant retrieves permitted records | Same |
| Remedy | Finance selects or approves | Frontline staff select within explicit policy |
| Exceptions | Finance investigates | Routed to finance with case ownership retained |
| Learning route | Finance revises recurring rules | Frontline overrides inform policy-owner review |
| Main capacity concern | Specialist queue | Training, consistency and exception escalation |

Either can work under appropriate conditions. The frontline arrangement requires usable policy, relevant competence, source access and a manageable scope. The central arrangement requires sufficient specialist capacity and clear response expectations. A company cannot select the first merely by removing a permission check, or the second merely by adding an approval screen.

## Calculate the queue implication

Suppose 60 cases arrive daily and finance has two hours for review. At three minutes per case, capacity is 40. The backlog grows by about 20 cases per day before variation and rework. A faster draft can increase submissions without increasing this capacity.

Harbour chooses frontline resolution for a narrowly defined category with consistent evidence, while uncertain cases remain specialist work. If 30 daily cases qualify, finance receives 30 rather than 60. This is a design hypothesis, not a measured result. Cases must actually meet the rule; labelling difficult work “routine” to reduce the queue would undermine it.

## Connect the design to the code

The dispatcher derives scope from trusted identity. Lookup remains read-only. A proposed credit carries a case ID, amount, policy version and proposal version. Execution checks the relevant role and current case state. The interface distinguishes “draft”, “approved” and “acknowledged”. A recurrent exception reaches the policy owner instead of being treated forever as individual error.

The pilot measures correct remedies, specialist waiting, frontline effort and reversals. It also checks whether staff feel able to challenge a suggested category and whether that challenge reaches somebody who can change it. These actor-specific conditions come from the [technology and organisation review](../../reference/research/06-technology-in-practice.md).

**Worked decision:** If finance rejects many apparently eligible cases because shipment scans are unreliable, change the evidence rule and investigate the source. Do not assume that adding another reviewer model repairs the premise. The useful redesign may involve data ownership and frontline authority as much as conversation quality.

## Read the organisational connection

Task framing, rule configuration and exception handling locate judgement at different points. The research chapter explains [where discretion moves](../../reference/research/03-decisions.md#where-discretion-moves).

## Practical activity: Write an acceptance contract that assigns the next step.


`None` means an absent value. It is different from zero, an empty string and `False`. Keeping that distinction prevents missing evidence from becoming an invented quantity.

### Predict and follow the values

After acceptance, which role owns further investigation in this case?

```python
contract = {"contribution":"source-labelled draft","recipient":"investigator","accepted":False,"next_owner":None}
contract["accepted"] = True
contract["next_owner"] = "investigator"
print(contract)
```

### Complete the exercise

**Worked answer.** The investigator owns it. A delivered chat message does not automatically establish that acceptance.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A service can give advisers room to tailor wording while requiring the same approval conditions. Rules and defaults shape choices before a person sees the result.

## What this means for the business process

Set the allowed evidence and approval conditions explicitly, and leave room for advisers to challenge an unsuitable draft. A standard path changes where judgement happens. Give the person who sees an exception a practical way to raise it.

For the research behind this design choice, read [Where discretion moves](../../reference/research/03-decisions.md#where-discretion-moves).

## Next lesson

Module 3 changes where the model runs. You will compare that technical choice with the work of maintaining the model and its surrounding service. [Lesson 3.1: What changes when you run a model yourself?](../03-open-models/01-concepts.md).
