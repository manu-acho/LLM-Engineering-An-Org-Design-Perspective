# Lesson 7.3: A specialised model still needs people to question its categories

[Download the matching notebook](/downloads/07-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

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

## Practical activity: Distinguish a changed policy from a model mistake.





The exercise code below runs from a prepared course checkout. In the matching notebook, the setup cell already supplies ROOT and RUN_LIVE. If following the code here, run this setup first:

```python
from ai_orgdesign.workspace import project_root, live_mode
ROOT = project_root()
RUN_LIVE = live_mode()
if RUN_LIVE:
    from ai_orgdesign.provider import Gateway
    gateway = Gateway(max_requests=12, max_output_tokens=1000)
print("Live mode:", RUN_LIVE)
```

### Predict and follow the values

Should an obsolete policy be repaired primarily by retraining?

```python
overrides = [{"case":"A","reason":"old policy"},{"case":"B","reason":"missing evidence"},{"case":"C","reason":"misread category"}]
changes = {"old policy":"source correction","missing evidence":"intake or retrieval","misread category":"evaluate model behaviour"}
print([(row["case"],changes[row["reason"]]) for row in overrides])
```

No. Correct the authoritative source and examine affected cases before treating the symptom as a parameter problem.

### Complete the exercise

Write the prediction before consulting the worked answer: Should an obsolete policy be repaired primarily by retraining?

**Worked answer.** No. Correct the authoritative source and examine affected cases before treating the symptom as a parameter problem.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
