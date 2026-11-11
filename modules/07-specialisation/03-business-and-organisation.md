# Lesson 7.3: A specialised model still needs people to question its categories

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## What you'll learn and why it matters

Explain why a specialised model still needs a route for challenging its categories. Harbour needs to recognise cases that no approved label describes well.

If Harbour teaches a model to classify “late” and “missing”, a new kind of partly delivered order may fit neither label. Specialisation improves performance for the chosen task and examples; it does not settle how the business should classify cases. Look for who can flag a bad category, revise the examples and change the routing practice.

## A specialised model becomes difficult to question

**Fictional case.** Harbour fine-tunes a request classifier. It matches the approved examples well. Six months later a service redesign changes exception ownership, but the classifier continues routing cases according to old labels. Users assume the specialised model “knows our process”.

The problem is partly model maintenance and partly the authority attached to a learned category. Specialisation can make an arrangement easier to reproduce without making it appropriate forever.

## Where judgement moved

Research chapter 3 asks where decision premises originate and who can revise them. In this case, judgement entered through category definitions, selected examples, annotation decisions, the training objective, validation criteria and deployment rules. The model's output is downstream of those choices.

Calling the result automatic does not remove that judgement. It can move it away from the frontline user to people who curate data and approve versions. Whether this improves or worsens the work depends on the arrangement and evidence; the review does not justify a universal claim that automation removes discretion.

The organisation should know who owns the category scheme, who can challenge a classification and what triggers retraining or a rules change. A technical model owner and a process owner have related but different responsibilities.

## Routines can change through performance

Research chapter 5 examines how routines change through repeated work. This **routine-dynamics** perspective helps explain why a task can change even when no formal redesign has been announced. Repeated exceptions, local learning and new connections among teams can produce adjustments. Stable performance need not mean an identical sequence every time.

A model trained on recorded history sees only what was represented in that history. It may not see the conversation that made an unusual routing appropriate. Treating every later departure as an error can suppress useful variation. Treating every departure as innovation can conceal poor practice. Investigate the actual cases.

This is a reason to keep disagreement and override records, with context. They are potential evidence about changing work, not merely negative feedback to be eliminated.

## Consistency is a conditional benefit

Standardisation can help when common categories and stable responsibilities support coordination. It can impose a poor fit when local requirements differ. Research chapter 4's implementation perspective asks whether a generic capability fits particular roles, controls and knowledge requirements.

A specialist model deployed across several clients may carry the first client's categories into another setting. Fine-tuning creates a technical adaptation, but local organisational adaptation is still needed. Do not describe similarity of industry as evidence that decision rights and exception practices are the same.

## Specialisation is consequential through a changing arrangement

A pinned adapter, a category vocabulary and an override button are inspectable technical properties. Their relation to useful action depends on who uses them, which task they face and how revisions become legitimate. A specialised model is not the whole arrangement.

For a case worker, an override may make a legitimate exception possible. For a process owner, accumulated override reasons may support identifying an obsolete category. Those possibilities require usable reasons, review capacity and a path to change the deployed rules. An unused override log actualises neither merely by existing.

Research chapter 6's practice lens also suggests asking how recurrent use changes the significance of the model. A team may treat it as an authoritative route selector or as a first suggestion checked against local expertise. Neither can be inferred from the model's validation score.

Extend the category-governance memo with an account of who can act on override evidence and how that action changes later work. This is a teaching application of [Research chapter 6](../../reference/research/06-technology-in-practice.md), not a finding that adaptation necessarily improves or constrains discretion.

## Apply the idea

Overrides are increasing. Would you retrain immediately, restrict overrides, change the categories or investigate a sample first? Consider three recorded reasons: an obsolete category, missing evidence and an apparently correct label rejected because of local workload.

**Worked response:** The reasons point to different interventions. An obsolete category needs a process/taxonomy decision. Missing evidence may require improved intake or retrieval. Workload-driven reassignment may require capacity allocation rather than changing the meaning of the original label. Investigate before combining every override into a new target.

**Rival explanation:** Users may be learning the system's intended category definition, so early overrides could decline without any model change. Observe use over time to distinguish people learning the system from a better model or a changing process.

A careful update process needs agreed label definitions, compatible model files and a fixed comparison set. It also needs checks on new cases, someone to review overrides, and a way to restore the earlier version if the update causes problems. These are practical consequences of the theory, not guarantees of success.

## Try it

Prepare a category-governance memo: who defines, labels, approves, challenges and revises categories; what evidence each role sees; and how changes reach the deployed application. Add a statement about the kinds of practice not visible in the training data.

For research, a model's agreement with a coding scheme does not independently validate the scheme. The model may reproduce the researcher's interpretation consistently. That consistency alone does not show that the interpretation explains the evidence well.

**Research basis:** [Research chapter 3](../../reference/research/03-decisions.md), [Research chapter 4](../../reference/research/04-implementation.md) and [Research chapter 5](../../reference/research/05-routines.md). See the [literature foundation](../../reference/literature-guide.md) for the research perspectives and evidence boundaries.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

The right to revise a category matters alongside the right to override one prediction. The research chapter explains [where discretion moves](../../reference/research/03-decisions.md#where-discretion-moves).

The research chapter also explains [the organisational effects of categories](../../reference/research/07-infrastructure-and-standards.md#classification-changes-what-an-organisation-can-see).

## What to remember

Training can make an existing classification more consistent. New or disputed work can still expose a problem with the categories themselves.

## What this means for the business process

Have advisers log cases that do not fit and let the routing owner decide whether to revise categories and examples. Keep the reason for the change, because changing a category can redistribute attention and work.

For the research behind this design choice, read [Classification changes what an organisation can see](../../reference/research/07-infrastructure-and-standards.md#classification-changes-what-an-organisation-can-see).

## Next lesson

The next lesson shows how chosen examples and scoring rules turn that category design into a numerical training task. [Lesson 7.4: Understand an adapter, a training batch and a loss](04-adaptation-mechanics.md).
