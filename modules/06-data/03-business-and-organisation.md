# Lesson 6.3: Historical labels contain an operating model

[Download the matching notebook](/downloads/06-03-business-and-organisation.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Previous lesson](02-code-workshop.md) · [Module route](README.md)

## Business context: Harbour

Investigate who defines an ambiguous category and who deals with a wrongly routed case.

[Company and supply-chain context](../../HARBOUR.md) · [Module 6 business situation](../../reference/harbour-learning-journey.md#module-6)

## What did the team column record?

**Fictional case.** Harbour exports two years of request assignments. Most disputed deliveries went to account management. A trained router reproduces that pattern accurately. Operations objects: account managers were absorbing the work because a specialist queue was understaffed. The new operating model is meant to change that arrangement.

The label is historically real but does not necessarily express the desired allocation. Training has made an unresolved organisational decision appear like a technical learning problem.

## Categories become decision premises

Research chapter 3's decision-premise lens helps locate the choice. A category, such as “routine complaint”, determines which process and authority rules apply. Whoever defines that category influences later decisions, even without handling each case.

An annotation guide is therefore a small piece of organisational design. It states what distinctions matter, whose judgement resolves ambiguity and which cases remain exceptions. **Annotation** means assigning labels to examples. It should not be delegated to “the data” as if the correct definition were already present in every historical field.

Invite frontline staff, process owners and relevant control roles to examine ambiguous cases. Agreement is useful, but do not manufacture it by erasing meaningful disagreement. A disputed label may reveal overlapping responsibilities or an exception the formal process never accommodated.

## Practice is not automatically the desired standard

Research chapter 5 shows why recurrent behaviour is more than a stored procedure. People interpret, improvise and repair work. A record of the final assignment may omit the conversations and temporary transfers that made resolution possible.

Learning from that record can preserve a useful adaptation or reproduce a workaround. It can also penalise people whose cases need legitimate variation. The design task is to distinguish those possibilities, not to assume that all deviations are errors or all historical patterns are best practice.

This also limits what a researcher can conclude. A team column shows what someone recorded under a particular rule. It does not show every conversation, transfer or judgement that produced the final assignment.

## Fit can require changing more than the model

Research chapter 4's fit/misfit lens suggests several responses. Harbour might clarify roles, change the intake form, create a specialist exception category, configure different routing rules, build a model for a stable subset or defer automation. A sophisticated classifier is not the only available response to conflicting labels.

Some cases may be suitable for a deterministic rule because the criterion is explicit and stable. Other cases may require interpretation and a recommendation with review. Still others may need negotiation over ownership before any routing system can be evaluated meaningfully.

## A mandatory category can enable and obstruct work

A required team label is a material arrangement: the application can refuse an unclassified request. For a queue manager, it may enable predictable allocation. For an intake worker handling a genuinely cross-team case, it may obstruct accurate submission and encourage an arbitrary choice.

Research chapter 6 treats enabling and constraining relations in terms of actors and goals. The lesson is not that required fields are inherently harmful. It is that data completeness in the interface does not establish a valid classification or a useful handoff.

Compare a compulsory single label with an explicit “uncertain” state, several named task roles, or a route that sends the case to a person who can resolve the disagreement. Each changes both the data and the work. If you introduce an exception route, identify who monitors it; availability alone does not mean it will be used effectively.

Before treating new training records as an improvement, examine how ambiguous cases are entered, corrected and acted upon. This applies [Research chapter 6](../../reference/research/06-technology-in-practice.md) to the annotation problem while preserving the distinction between a configured field and enacted practice.

## Apply the idea

Consider four requests: a simple quantity query, a request for goodwill compensation, an unresolved warehouse discrepancy and an urgent complaint from a strategic customer. What would “correct team” mean for each?

**Worked response:** Separate the first evidence-gathering action from final approval authority and ownership of the customer relationship. The warehouse discrepancy may need operations to investigate while finance retains credit authority and account management communicates with the customer. One team label may be an inadequate representation.

A better target could contain a next action, an accountable role and an exception flag. This changes the prediction task and its evaluation. The extra structure is worthwhile only if the receiving process can use it.

**Rival explanation:** The original team field might already have a precise operational meaning, such as ownership of the next response. Investigate its definition and recording practice before declaring the data defective.

## Try it

Write an annotation guide for a narrow task. Define each category, include ambiguous examples, specify which information is available when the prediction is made, and name who resolves disagreements. State which decisions the labels do not represent.

Before selecting a model, agree how requests should be allocated. An accurate prediction of past assignments does not show that those assignments are suitable for future work.

**Research basis:** [Research chapter 3](../../reference/research/03-decisions.md) on premises and discretion; [Research chapter 4](../../reference/research/04-implementation.md) on adaptation choices; [Research chapter 5](../../reference/research/05-routines.md) on records and practice. The case applies the concepts; it is not a reported empirical finding.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Historical labelling choices can move judgement into the design of the training set. The research chapter explains [where discretion moves](../../reference/research/03-decisions.md#where-discretion-moves).

## Practical activity: Show why one historical label can conceal coordination work.





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

How many specialist contributions are identified here?

```python
annotation = {"message":"invoice for damaged delivery","intake_owner":"customer operations","specialists":["finance","warehouse"],"target_definition":"first accountable recipient"}
print(annotation)
assert len(annotation["specialists"]) == 2
```

Two. That does not require two competing accountable owners for the first response.

### Complete the exercise

Write the prediction before consulting the worked answer: How many specialist contributions are identified here?

**Worked answer.** Two. That does not require two competing accountable owners for the first response.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Independent Harbour design record

Harbour routes delivery discrepancies to investigation and invoice questions to finance. These categories allocate work, so disagreements about labels can become disagreements about responsibility. Historical examples may preserve an old arrangement even when the file is tidy and the classifier trains successfully.

**Task:** Write a routing agreement between customer service, operations and finance, including ambiguous and mixed cases.

Before reading the worked direction, write a short response covering: the affected customer or receiving team; the evidence and work needed across functions; and one condition that would make the proposed arrangement unsuitable. State any additional fictional assumption rather than treating it as a supplied fact. Use the course workbook or a personal copy of this notebook.

### Worked direction for comparison

Finance receives the defined invoice/tax issues; operations investigates recorded-versus-reported delivery differences. Missing information stays visible. The teams agree how to accept, return or jointly examine mixed cases rather than forcing every message into a misleading single label.

Other arrangements can be defensible. Check that the proposal names who accepts the work, preserves unavailable evidence and distinguishes technical execution from a business outcome.
