# Lesson 6.6: Redesign a routing task before learning its labels

[Download the matching notebook](/downloads/06-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../07-specialisation/README.md)

## Business context: Harbour

Define invoice and delivery boundaries and a referral route for mixed or unclear requests.

[Company and supply-chain context](../../HARBOUR.md) · [Module 6 business situation](../../reference/harbour-learning-journey.md#module-6)

## A clear column can contain an unclear task

**Fictional case.** Harbour exports old complaints with an `assigned_team` column. Staff want a classifier to reproduce it. Examination reveals that the value sometimes means the first contacted team, sometimes the final owner and sometimes the only team available that day.

The problem is not simply noisy text. Several organisational decisions have been compressed into one field. Training faithfully on that field could preserve precisely the confusion the proposed system is meant to reduce.

## Separate contribution from ownership

Harbour replaces one target with three questions: what evidence is needed next, which team can supply it, and who retains responsibility for the customer case? A delivery recount can be operations work while account management retains case ownership. A later finance decision does not mean finance should have received the first enquiry.

This is differentiation and integration applied to the dataset. Technical labels now correspond to explicit contributions rather than an accidental history of assignment.

## Complete an annotation rule

| Situation in the initial message | First contribution label | Case ownership |
|---|---|---|
| Missing receipt or disputed quantity | Delivery evidence | Account management retains until accepted transfer |
| Verified discrepancy with remedy question | Policy/remedy review | Named case owner retains during finance review |
| Contradictory or insufficient information | Clarification required | Intake owner obtains missing evidence |

Two reviewers label a development sample independently. They retain disagreement and explain its cause. The policy owner adjudicates the rule, then revises the annotation guide. The held-out set is prepared separately after the task definition is stable. This is governance of the target, not merely cleaning spelling.

## Diagnose misfit and compare responses

Strong and Volkoff's fit/misfit perspective, discussed in the [enterprise systems review](../../reference/research/04-implementation.md), directs attention to data, functionality, roles and controls. Harbour's one-column history contains data and role misfit. A model extension alone cannot resolve it.

Options include changing the process, adding fields, configuring routing rules, using a classifier for ambiguous language or declining automation for certain categories. Harbour chooses rules for explicit order-status requests and a classifier that recommends the next contribution for free-text cases. Uncertain cases enter clarification rather than being forced into a wrong team.

## Measure the new task

Suppose a majority baseline routes 85% of cases to operations and scores 85% overall. It misses every finance-first case. The proposed classifier scores 88%, but that three-point gain is not enough information. Examine category-level precision and recall, missed consequential cases, clarification use, repeated transfers and accepted ownership.

A classifier that correctly predicts “finance” but abandons customer ownership can still harm service. Pair the prediction with the receiving arrangement. A notification does not establish acceptance.

## Learning from actual use

For the first month, staff record why recommendations were overridden: missing evidence, category ambiguity, source error, workload or model interpretation. The label owner reviews recurring patterns. A temporary workload workaround should not automatically become the target for future training.

The [routines review](../../reference/research/05-routines.md) helps explain why recorded performance is a selective representation of work. Informal repairs may be absent from the export. Treat observation and staff accounts as additional evidence, while preserving their own limits.

**Worked decision:** Override rates rise after a policy change. Before retraining, determine whether the label definition changed, the new rule reached the application and the current evaluation still represents the task. New data can help only after the organisation knows what behaviour it wants to learn.

## Read the organisational connection

A routing category can create role or data mismatches even when prediction accuracy is high. The research chapter explains [six kinds of misfit](../../reference/research/04-implementation.md#six-kinds-of-misfit).

## Practical activity: Compare a learned baseline with a model-labelled route on new text.





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

Does a single correct prediction establish generalisation?

```python
from ai_orgdesign.labs.m06 import fit_baseline
message = "invoice tax question"
print("Classical baseline:", fit_baseline().predict([message]).tolist())
```

No. It is one observation; evaluate representative cases and meaningful error categories.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

```python
if RUN_LIVE:
    schema = {"type":"object","additionalProperties":False,"properties":{"label":{"type":"string","enum":["finance","operations"]}},"required":["label"]}
    result = gateway.generate(message, instructions="Classify a fictional request into finance or operations. Invoice and tax queries go to finance; delivery issues to operations.", schema=schema)
    print("Live label:", result.value)
    print(result.record)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

Write the prediction before consulting the worked answer: Does a single correct prediction establish generalisation?

**Worked answer.** No. It is one observation; evaluate representative cases and meaningful error categories.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Interpret the returned label

This activity uses two receiving functions, `finance` and `operations`. Later four-route briefs distinguish investigation and qualitative review as separate case routes. Those outputs answer different questions. See the [routing crosswalk](../../reference/case-data-guide.md#routing-vocabulary-belongs-to-a-task) before translating between them.
