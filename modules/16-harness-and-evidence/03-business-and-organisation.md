# Lesson 16.3: Design the work, responsibility and learning

[Download the matching notebook](/downloads/16-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md)

## Business context: Harbour

Balance operational visibility with confidentiality and an investigator’s need to challenge an output.

[Company and supply-chain context](../../HARBOUR.md) · [Module 16 business situation](../../reference/harbour-learning-journey.md#module-16)

## A trace is an artefact about work

A run log records selected events. It does not contain the whole activity. Harbour's investigator may telephone a warehouse, interpret an ambiguous note and negotiate an exception without those actions appearing in a model trace. The technical record remains useful, but its scope must be stated.

Feldman and Pentland (2003) distinguish the general understanding of a routine from its particular performances. Prompts, forms and logs are artefacts associated with the work; they should not be substituted for the routine itself. The [routines chapter](../../reference/research/05-routines.md) develops these distinctions and the related arguments about designing artefacts while expecting coordinated action to follow automatically.

## Give each observation an operational use

Suppose an investigator says a draft omitted the difference between reported and verified receipt. A useful trace can identify the source version, retrieved context, instruction version and returned contribution. It can help determine whether the defect began in the source, retrieval, transformation or generation. A simple thumbs-down without these links cannot locate the intervention.

The service review should distinguish a model defect from an ownership problem. If investigators agree that the draft is faithful but no team accepts the exception, changing the model prompt addresses the wrong mechanism. If the policy source is obsolete, retraining a model may preserve rather than correct the underlying error.

## Design the feedback route

Operations receives the case-level concern and decides whether immediate investigation is needed. A source owner handles incorrect or obsolete evidence. The engineering owner investigates execution and transformation errors. A service manager considers changes to scope and responsibility. These are proposed roles for the fictional case, not a universally optimal organisation chart.

Feedback needs enough context to support that allocation, but should not become an unrestricted copy of confidential case data. Retention, redaction and access are part of the logging arrangement. A technically convenient full transcript may be a poor organisational choice if it gives an unnecessarily broad audience access to sensitive records.

## Compare time, cost and contribution together

Assume a candidate produces a draft faster but doubles review time because source labels are hard to inspect. A lower model latency does not establish improved case preparation. The comparison should record the complete task boundary and the people doing the added work.

A different interpretation remains possible: early review time may reflect learning a new interface rather than a permanent burden. Observe repeated use, retain the time period and examine whether the work changes. Do not label every initial difficulty a design failure or every later improvement a model effect.

## Worked operational review

For a bounded sample, the service manager requests configuration identity, stop categories, missing-source frequency, case-level rework reasons and end-to-end elapsed time. The report separates assumed token costs from observed usage. It includes cases where the service refused or failed, rather than analysing only successful drafts.

The judgement asks whether a specific correction is warranted and who can carry it out. A new dashboard is not the conclusion unless it supplies information someone can use. The [technology-in-practice chapter](../../reference/research/06-technology-in-practice.md) supports the distinction between a technical possibility and its realisation by particular actors under particular conditions.

## Practical activity: Route feedback to the intervention it actually requires.





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

Who investigates the execution failure in this proposal?

```python
feedback={"wrong source":"record owner","execution failure":"engineering owner","unaccepted handoff":"service owner"}
print(feedback)
```

engineering owner. A prompt edit should not be the automatic response to every kind of feedback.

### Complete the exercise

Write the prediction before consulting the worked answer: Who investigates the execution failure in this proposal?

**Worked answer.** engineering owner. A prompt edit should not be the automatic response to every kind of feedback.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

When an investigation draft is wrong, Harbour needs to know which evidence and instructions produced it. Operations needs enough information to correct the work; technical support needs enough to diagnose execution. Keeping every customer detail in unrestricted logs would create another problem.

**Task:** Design an incident record linking execution identity, affected cases, business owner, technical owner and correction status.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Retain permitted source and configuration identities, status and relevant usage, with access and retention rules. Technical repair restores execution; the case owner still checks whether customers received an unsuitable answer or whether work needs to be repeated.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.
