# Lesson 11.3: An agent team needs integration, not just role names

[Download the matching notebook](/downloads/11-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## Harbour draws an organisation chart of agents

**Fictional case.** Harbour replaces one general assistant with an evidence researcher, policy analyst, service manager and quality reviewer. The diagram resembles a department. Early demonstrations look more thorough because every case produces several reports.

But report length is not the operating goal. The important questions are whether the contributions are useful, whether contradictions are resolved and whether someone can act on the result. A team of prompts can reproduce a poorly integrated process as easily as a well-designed one.

## Differentiation creates an integration problem

The [organisation-design review](../../reference/research/01-organisation-design.md) explains differentiation, dividing work into specialised contributions, and integration, reconnecting them. Specialisation is useful when the differences matter: a policy task may need a different source set and output contract from an evidence-comparison task.

Each new boundary also needs an integration mechanism. How does the policy analyst see an unresolved factual conflict? Can the researcher revise a source interpretation after feedback? Who decides when the available evidence is insufficient? A strictly one-way sequence may be suitable for straightforward cases but poorly suited to repeated clarification.

This is why agent count is a weak design measure. Four agents do not imply four independent competencies or four accountable organisational roles. Describe what each contributes, which information it can inspect and how the result is checked.

## Technical hierarchy and accepted authority differ

The [decision-theory review](../../reference/research/03-decisions.md) helps examine the manager agent. Its instructions and tools may let it allocate tasks and select an output. That is technical control within a process. Whether the organisation should accept that selection is another question.

Define the manager's authority narrowly. It might request another search, reject a malformed draft or route a case to a human reviewer. It should not acquire the ability to change policy simply because its prompt says “senior manager”. The person or body accountable for the policy remains relevant.

A hierarchical runtime can be appropriate without imitating the employer's hierarchy. A sequential runtime can support work spanning several departments. Match the software process to dependencies rather than assuming that agent labels should mirror the organisation chart.

## A reviewer is not automatically independent

If the drafter and reviewer use the same source summary, both can miss the qualification removed during collection. If they use the same model and similar prompts, their errors may be correlated. A review agent can add useful criticism without supplying independent confirmation.

Define the evidence the reviewer receives. To challenge a factual claim, it may need original passages, source dates and counterexamples, not merely the final report. Separate factual support, policy compliance, communication quality and authority to act. One global “quality” score can hide which of these was actually assessed.

A business reviewer may also need authority to stop a case, request a correction and change a recurring bad rule. Without those rights, review risks becoming a repeated confirmation step.

## Task settings can stabilise a way of working

The [routines review](../../reference/research/05-routines.md) treats task templates and software outputs as artefacts that influence, but do not fully determine, recurrent work. A YAML task description can encode assumptions about what counts as complete, whose input is needed and which exceptions deserve attention.

When staff repair unusual cases outside the crew, those actions belong to the work. Investigate whether the formal task design should change, whether a bounded exception route is appropriate or whether the task is unsuitable for automated treatment. Do not train away every exception without understanding what it accomplishes.

The [enterprise-systems review](../../reference/research/04-implementation.md) adds the issue of local fit. A reusable crew may carry one department's categories into another. Reusing a framework can save engineering effort while still requiring changes to roles, source access and acceptance criteria.

## Make the relation between a feature and a useful action explicit

A source-bearing task output may enable a reviewer to check a claim, if that reviewer can open and interpret the sources. A required final report may help a receiving team, or it may obstruct urgent escalation when the evidence is incomplete. The [technology-and-organisation review](../../reference/research/06-technology-in-practice.md) directs attention to the actor, goal and conditions behind these possibilities.

The task graph is evidence of the represented design. Configured tools show selected capabilities. Repeated cases reveal whether people actually rely on the reports, repair them or bypass the process. Outcome comparisons are still needed before claiming improved service.

## Apply the idea

Suppose the new crew increases agreement between its drafter and reviewer, but staff make more corrections after customer contact. What would you investigate?

One explanation is that the internal checks are rewarding a shared interpretation rather than checking it against evidence. Another is that the crew is now handling harder cases. Compare case difficulty and examine the correction trail before deciding that another reviewer agent is the solution.

**Try it:** Build a contribution table for the four agents. For each, state its input, output, evidence access, rejection rights and human owner. Remove one agent and explain what would be lost. If the answer is only “another opinion”, specify what would make that opinion informative.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Separating contributions creates a need for reintegration even when all roles use software. The research chapter explains [division and integration](../../reference/research/01-organisation-design.md#division-creates-a-need-for-integration).
