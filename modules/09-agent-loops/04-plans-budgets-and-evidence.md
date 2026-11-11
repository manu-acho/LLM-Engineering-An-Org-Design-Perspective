# Lesson 9.4: Turn a plan into a bounded investigation

[Download the matching notebook](/downloads/09-04-plans-budgets-and-evidence.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: inspect the digital twin](05-source-walkthrough.md)

## Business context: Harbour

A plan might say to check dispatch, then ask the carrier if the first check leaves a gap. Define the evidence required to finish, as well as limits on attempts, time or spending. A budget is a limit on one of those resources. The application can stop the loop because a limit was reached while the investigation itself remains incomplete.

Inspect ceilings on rounds and tool calls as local execution boundaries rather than a service guarantee.

[Company and supply-chain context](../../HARBOUR.md) · [Module 9 business situation](../../reference/harbour-learning-journey.md#module-9)

## A plan changes the next question

An assistant investigating a disputed delivery might propose: find the order, compare quantities, obtain policy, then draft a response. A fixed application can encode those steps directly. A model-selected loop becomes useful when the next evidence need depends on what was found. A missing receipt might require clarification before policy lookup is meaningful.

The plan is a representation of intended work. Execution records establish which steps ran. A success check compares the resulting evidence with the defined task. Keep these objects separate, because a model can write a complete checklist without obtaining the necessary records.

## Specify completion before launching the loop

For Harbour's read-only investigation, completion means an identified order, current permitted policy, a clear account of agreement or conflict and a referenced draft. “The model stopped requesting tools” is a runtime termination condition, not the complete business criterion.

Possible terminal states include `draft_ready`, `missing_evidence`, `scope_denied`, `budget_exhausted` and `service_failure`. These states tell the next actor what remains. Treating all of them as one final answer string makes unresolved work harder to identify.

## Use more than one budget

A turn limit bounds model iterations. A tool-call limit bounds proposed operations. A time limit bounds waiting. A spending limit bounds a resource exposure. One turn containing five tool calls consumes those budgets differently from five turns containing one call each.

Suppose an investigation allows four model turns, six reads and 30 seconds. The first turn requests three reads; one takes 25 seconds. The second turn has less than five seconds left, even though most turns remain. An application needs to check the remaining deadline before starting another operation, rather than resetting the full timeout at every step.

## Design for partial information

If the order record arrives but policy is unavailable, a useful result can state the factual discrepancy while refusing to infer a remedy. This is a partial evidence product with a visible boundary. It is different from silently omitting policy and returning a normal-looking recommendation.

Keep source version, operation identity, result status and observation time with each result. A value such as `2` without its source can mean reported shortage, verified shortage or a model calculation. A more explicit record supports later checking:

```python
observation = {
    "operation_id": "read-17-1",
    "source_id": "order-17:v3",
    "status": "found",
    "claim_type": "customer_reported_difference",
    "value": 2,
}
assert observation["claim_type"] != "verified_shortage"
```

## Compare a loop with a form

If every request contains an order ID and always needs the same two records, a fixed lookup-and-draft route may be clearer. If users describe uncertain situations and the next useful evidence varies, model selection may reduce rigid branching. The comparison should use the same completion criteria, sources and cases.

**Worked failure:** A model repeatedly requests an unavailable source and exhausts its budget. The application should retain the evidence already gathered, expose the unresolved source and assign a next owner. Increasing the budget is appropriate only if more permitted work could reasonably change the result. Persistence cannot create a source that the organisation has not made available.

The [coordination review](../../reference/research/02-coordination.md) helps distinguish a missing contribution from a scheduling problem. The loop's next step and the organisation's next responsibility must connect.

## Read the organisational connection

Budgets and stopping rules structure search without proving that the first acceptable answer is adequate. The research chapter explains [bounded rationality](../../reference/research/03-decisions.md#bounded-rationality).

## Practical activity: Track the difference between a planned and completed step.


### Predict and follow the values

How many steps have completion evidence here?

```python
steps = [{"activity":"read case","state":"completed","receipt":"case-H-17"},{"activity":"verify receipt","state":"planned","receipt":None}]
completed = [step["activity"] for step in steps if step["state"] == "completed"]
print(completed)
```

### Complete the exercise

**Worked answer.** One. A written plan for receipt verification is not a verified delivery.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
