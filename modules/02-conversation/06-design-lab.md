# Lesson 2.6: Allocate discretion across a conversational service

[Module route](README.md) · [Next module](../03-open-models/README.md)

A service that drafts replies can give advisers freedom to reword a message while keeping the rules for credit approval fixed. Discretion is the room someone has to choose how to act within their role. Compare who can change a draft, choose evidence and approve a credit. Those choices do not have to be assigned to the same person or program.

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

The research chapter also explains [what makes review practical](../../reference/research/08-governance-and-accountability.md#meaningful-review-needs-resources-and-a-practical-alternative).
