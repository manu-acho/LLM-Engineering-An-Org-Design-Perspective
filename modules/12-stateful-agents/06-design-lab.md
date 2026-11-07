# Lesson 12.6: Design review as a service with capacity and discretion

[Download the matching notebook](/downloads/12-06-design-lab.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next module](../13-agent-frameworks/README.md)

## Business context: Harbour

Resume an explicit simulated review choice without treating persistence as renewed permission.

[Company and supply-chain context](../../HARBOUR.md) · [Module 12 business situation](../../reference/harbour-learning-journey.md#module-12)

## A pause creates a dependency

**Fictional case.** Harbour's graph correctly pauses 50 cases a day. Finance has 90 minutes of review capacity. At three minutes per case, it can review 30. The pending queue grows by approximately 20 a day before accounting for variation, absence and rework.

The interrupt works technically. The implementation has not supplied a sufficient review arrangement. The next redesign should examine who needs to review which cases and what makes a review useful.

## Compare four responses

| Response | What it changes | What must be checked |
|---|---|---|
| Add protected capacity | More reviewer time | Whether effort is justified and expertise available |
| Narrow interrupted scope | Fewer cases require the same review | Whether remaining automatic cases meet an explicit rule |
| Improve evidence presentation | Less effort per valid review | Whether reviewers still perform substantive checking |
| Delegate a bounded category | Different allocation of decision opportunity | Competence, authority, incentives and escalation |

Harbour combines evidence improvement with a narrower rule. Clear, supported drafts take two minutes. Only 35 daily cases need finance review, giving an expected 70-minute load. The margin within 90 minutes is not a guaranteed service level: arrival variation and complex cases still matter. Monitor waiting rather than planning exactly at average capacity.

## Meaningful discretion requires more than a button

Reviewers need to see the evidence, understand it, reject a proposal and obtain correction. A formal right to reject can coexist with pressure to approve. A performance target based solely on clearing the queue can undermine the purpose of review.

Harbour measures unsupported approvals and justified revisions alongside turnaround. Recurrent rule disputes reach the policy owner. The reviewer is not expected to solve every category problem through individual exceptions.

The [decision theory review](../../reference/research/03-decisions.md) distinguishes permission, practical influence and accepted authority. Those distinctions help identify why a technically complete interrupt might produce superficial confirmation.

## Follow a delayed case

Case C-17 waits overnight. In the morning, operations updates the quantity record. The reviewer sees proposal revision one, prepared against the old source. The system must either invalidate it or make the changed evidence explicit and issue a revised proposal. Approval of revision one should not silently become approval of revision two.

The case owner handles the customer's waiting. The reviewer handles the decision opportunity. The operator handles checkpoint or service recovery. These responsibilities connect without becoming interchangeable.

## Observe the routine, including work outside the graph

At first, reviewers call operations when a field is unclear. Those calls are useful repair work. If recurrent, they may reveal a missing data field or an unsuitable category. Recording only checkpoint transitions would miss the work making the process usable.

Over several weeks, Harbour changes the evidence panel and annotation rule. Review effort falls and fewer calls are needed. That is a possible actualisation process to investigate: actors learn and alter an arrangement over time. A single screenshot of the panel cannot establish it.

## Make the expansion decision

The pilot can expand when supported review decisions, waiting, effort and customer outcomes meet stated conditions on representative cases. It should not expand merely because all paused cases can eventually be resumed in a test.

**Worked challenge:** Review reduces wrong remedies but doubles elapsed time. The answer is not automatically to remove review. Compare which errors were prevented, where waiting arose and whether scope, capacity or evidence can be redesigned. The appropriate trade-off follows the service's consequences and conditions.

**Research basis:** [Coordination](../../reference/research/02-coordination.md), [routines](../../reference/research/05-routines.md) and [technology in practice](../../reference/research/06-technology-in-practice.md).

## Read the organisational connection

Meaningful review depends on access, expertise, time and a practical route to respond. The research chapter explains [actualisation](../../reference/research/06-technology-in-practice.md#actualisation-from-possibility-to-action).

## Practical activity: Resume human review without repeating the prepared model contribution.





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

Should resuming the review require a second drafting call?

```python
from pathlib import Path
from uuid import uuid4
review_path=ROOT/"outputs"/("resume-"+uuid4().hex+".db")
review_path.parent.mkdir(exist_ok=True)
review_action="return"
print("The course reviewer will return this fictional case for evidence; no payment exists.")
```

No. The saved contribution should be reviewed; current case and policy conditions must still be checked.

### Use the live model

Live mode is the recommended implementation route after [API setup](../../reference/live-model-guide.md). The following operation uses the fictional evidence shown here, returns an actual result and retains usage. Named arguments label a function's inputs; a returned object provides fields such as text, value and record. Read those fields independently instead of treating fluent text as a success certificate.

```python
if RUN_LIVE:
    from ai_orgdesign.durable_review import start,resume
    start(review_path,gateway)
    before=gateway.attempts
    result=resume(review_path,review_action)
    assert gateway.attempts == before
    print(result["decision"])
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

Write the prediction before consulting the worked answer: Should resuming the review require a second drafting call?

**Worked answer.** No. The saved contribution should be reviewed; current case and policy conditions must still be checked.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
