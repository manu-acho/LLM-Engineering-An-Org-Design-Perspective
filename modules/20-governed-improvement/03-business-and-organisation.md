# Lesson 20.3: Design the work, responsibility and learning

[Download the matching notebook](/downloads/20-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

## Business context: Harbour

Assess the effect on coordination, decision rights, routines and customer-facing work.

[Company and supply-chain context](../../HARBOUR.md) · [Module 20 business situation](../../reference/harbour-learning-journey.md#module-20)

## A score is evidence for a decision, not the decision itself

Harbour's improvement proposal reduces unsupported conclusions on the development cases. Before promoting it, the service manager asks whether it changes retrieval, drafting, review effort or the population of cases accepted. The same score change can arise from different mechanisms, some of which may be undesirable.

For example, a candidate can reduce unsafe approvals by referring almost every case. That may be appropriate when the previous system exceeded its competence, but it changes review workload. A promotion decision should examine that burden and the service's purpose rather than treating a higher safety score as a complete operating design.

## Keep the organisation in the improvement loop

Feldman (2000) examines change through responses to the outcomes of repeated performances. Applying that reasoning to AI services means asking who notices a problem, how it is interpreted and which change is retained. A feedback button alone does not establish organisational learning. The [routines chapter](../../reference/research/05-routines.md) provides the argument and its limits, with a link to the publication.

An improver that edits prompts can only change the artefacts it is allowed to edit. If the problem is obsolete policy, contested categories or missing review capacity, prompt edits may compensate temporarily or make the defect less visible. Improvement governance must allow the conclusion that a source, process or responsibility arrangement needs to change.

## Defend an evaluation rather than display a verdict

The final proposal should identify the evaluation population, exclusions, reference decisions, evidence available to each route, failure categories and observation period. Explain how the candidate was selected and which cases were reserved for confirmation. A larger number of test runs does not make the population representative automatically.

Retain rival explanations. A shorter resolution time may reflect easier cases, extra staffing, a clearer intake form or an unrelated policy change. A technical evaluation can isolate some behaviours in controlled examples. Claims about organisational outcomes require a design and evidence appropriate to those outcomes.

## Preserve contestability after promotion

A released version needs a route for staff and affected customers to challenge an unsuitable conclusion or category. An override should identify a reason and responsible reviewer without automatically becoming a new training label. Corrections can concern facts, policy, implementation or the legitimacy of a category itself.

The [organisation design chapter](../../reference/research/01-organisation-design.md) connects contribution, integration and fit. The [technology-in-practice chapter](../../reference/research/06-technology-in-practice.md) distinguishes a designed capability from its situated realisation. Together they support a final judgement that examines the whole arrangement while preserving differences among those theories.

## Worked capstone decision

The proposed release prepares evidence-linked drafts, leaves unresolved facts visible and keeps remedy authority with an authorised manager. It uses versioned state, bounded capabilities, explicit acceptance and idempotent local decisions. Its tests support selected local behaviours. No real insurer, customer, payment provider or cloud service has been exercised.

A defensible next step is a controlled service study with an appropriate population, review capacity, monitoring and correction route. Expansion is conditional on that evidence. If a simpler record view performs equally well with less burden, selecting it is a successful design conclusion rather than a failed AI project.

## Practical activity: Route a discovered problem to the change that could address it.





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

Should every failure automatically lead to a prompt change?

```python
failures={"crushed-box policy not retrieved":"retrieval query or index","unsupported quantity":"evidence transformation or generation","review backlog":"capacity or task design"}
print(failures)
```

No. The intervention should address the mechanism supported by the evidence.

### Complete the exercise

Write the prediction before consulting the worked answer: Should every failure automatically lead to a prompt change?

**Worked answer.** No. The intervention should address the mechanism supported by the evidence.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour’s final decision concerns a proposed business arrangement as well as a software configuration. A candidate can match more route references while consuming more resources or increasing review work. The company must weigh those trade-offs and retain the option to simplify, defer or withdraw the capability.

**Task:** Produce a final business and organisation design proposal joining customer outcome, goods and information flows, finance authority, service ownership and measured technical evidence.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Limit assistance to justified contributions; retain functional source owners and accountable investigation. Explain accepted handoffs, capacity, remedy authority and correction. State what actual checks establish, compare with simpler arrangements, and define conditions for expansion, revision or withdrawal.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.
