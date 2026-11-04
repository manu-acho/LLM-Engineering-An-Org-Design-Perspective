# Lesson 13.3: A common interface does not create a common organisation

[Previous lesson](02-code-workshop.md) · [Module route](README.md) · [Framework tour](04-framework-tour.md)

## Several teams connect their assistants

**Fictional case.** Harbour's regional teams have built assistants with different frameworks. Headquarters proposes a shared task board and a common result format. Management expects the assistants to become interchangeable and move cases between regions automatically.

The technical interfaces can become more consistent while the work remains different. One region uses “complete” to mean a draft exists. Another means finance has approved it. A third means the customer has acknowledged the response. Converting all three results into one field would erase a consequential distinction.

## Standards help with some boundaries

The [coordination review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_02_Coordination_Theory_Detailed_Review.md), drawing on Carlile, distinguishes representation, meaning and interests. Shared schemas help information cross a representation boundary. A common field called `accepted` does not settle who accepts what or why.

Ask the teams to describe the same real or fictional case. At which point does responsibility move? Which evidence is mandatory? Which exceptions require negotiation? These questions reveal differences that a technical adapter cannot resolve by renaming fields.

A shared protocol can make a request possible across systems. A service agreement must still state what the receiving unit undertakes to do, under which conditions and with what recourse if it fails.

## Shared infrastructure brings shared maintenance work

The [enterprise-systems review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_04_Enterprise_Systems_Implementation_Transformation_Detailed_Review.md) helps examine the tension between common capability and local fit. A shared board can reduce integration effort and improve visibility. It can also impose categories that fit one unit poorly or concentrate change authority in a central technical team.

Separate what must be common from what may vary. Case identity, versioning and evidence references may need stable contracts. A region's internal staffing sequence may not. Standardising the interface is often more useful than insisting every team use the same framework, but only if the agreed semantics are strong enough for the work.

Someone must own schema changes, version compatibility, access rules and deprecation. Without that work, “interoperability” can become a growing collection of fragile adapters maintained through personal goodwill.

## A task board distributes visibility and attention

The [organisation-design review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_01_Organisation_Design_Detailed_Review.md) asks how information and authority fit together. A central board may make delays visible to managers while adding reporting work for staff. The status design can make some activities count and leave informal repair invisible.

The workshop's distinction between `reported_done` and acceptance is an example of a category with organisational consequences. If incentives reward only the former, workers or agents may finish their local steps while leaving unusable outputs for others.

Decide which measures describe local activity and which describe accepted service outcomes. Both can be useful. Confusing them creates an evaluation problem and may reward the wrong behaviour.

## Interoperability can move discretion

The [decision-theory review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_03_Decision_Theory_Detailed_Review.md) directs attention to who defines the common categories and exceptions. An adapter that converts a regional classification into a global one is applying a decision premise. Its mapping can alter routing and authority even if it is described as routine data transformation.

Treat disputed mappings as business decisions. Record who approved them, what evidence informed them and who can challenge the result. Technical ownership of the integration should not silently become policy ownership.

## What must be observed after connection?

The [routines review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_05_Organisational_Routines_Detailed_Review.md) reminds us that standard interfaces are artefacts. Staff may continue calling trusted contacts to resolve difficult cases. That may be essential repair work rather than evidence that the integration is irrelevant.

The [technology-and-organisation review](https://github.com/manu-acho/org-design-as-code/blob/4e40b3b65360140d89e9581e4e668ef38ab77482/Enterprise-Software-as-Organisation/literature/Stream_06_Technology_Materiality_Organisation_Detailed_Review.md) adds the question of possibilities for particular roles. Shared visibility may enable a coordinator to identify stalled work, but only if they have authority to obtain a response. A new route to another team's agent may be available without being understood or trusted.

Observe accepted transfers, corrections, unresolved ownership and manual reconciliation over time. Then compare service outcomes and effort across roles. A successful protocol test establishes less than a successful organisational integration.

## Apply the idea

Harbour's shared board reduces duplicate data entry but increases rejected cross-region handoffs. Would you standardise all frameworks, clarify completion meanings, change the mandatory evidence or leave some cases local?

A useful answer investigates which differences matter to the rejected cases. Framework consistency might help maintenance but do little for a disagreement about what counts as sufficient evidence. A better interface contract may solve the immediate coordination problem without replacing every runtime.

**Try it:** Write a common task-result contract with separate fields for produced output, checked evidence, review status and recipient acceptance. Name the owner of each field's meaning and the process for changing it. Include one example that must not be converted automatically between regions.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.
