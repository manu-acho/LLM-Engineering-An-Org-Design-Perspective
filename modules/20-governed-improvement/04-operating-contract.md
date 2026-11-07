# Lesson 20.4: Make the operating contract inspectable

[Download the matching notebook](/downloads/20-04-operating-contract.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Keep evaluation, resource limits and explicit approval distinct in a promotion decision.

[Company and supply-chain context](../../HARBOUR.md) · [Module 20 business situation](../../reference/harbour-learning-journey.md#module-20)

## Start with a concrete contribution

An improvement loop can optimise a proxy while degrading the service. Harbour treats a proposed configuration as a candidate that must pass comparable evaluation, explicit safety and cost conditions, and a human promotion decision.

An operating contract states what information is required, what contribution is promised, what counts as acceptance and who owns the next step. It also names refusal and failure outcomes. A contract is useful when another person can apply it to a case without guessing what a success label means.

## Follow the included implementation

gate requires baseline and candidate records with the same nonempty evaluation size and dataset hash. It compares unsafe decisions, accuracy and a chosen ten-percent cost tolerance, then requires explicit human approval. It returns reasons rather than silently changing a live version. demo constructs illustrative scores and shows how approval changes the promotion result. The dataset hash names a teaching evaluation identity; it is not proof that hidden test labels were protected or that the sample is statistically adequate.

Open `src/ai_orgdesign/labs/m20.py` and follow each call into its supporting function. Ordinary Python functions receive values and return values; a class groups state and operations; a context manager controls a resource's lifetime. The [programming reference](../../reference/python-patterns.md) explains these patterns with small examples, and the [technical foundations](../../reference/technical-foundations.md) introduces transactions, concurrency and neural calculations before their use.

## Write acceptance and rejection conditions

The illustrative candidate is blocked without approval and passes the stated gate with approval. A candidate with more unsafe decisions is blocked even if its accuracy improves. Different dataset identities raise an error because the comparison is not the declared experiment. Promotion does not establish statistical significance or guarantee future performance.

Acceptance conditions should be observable. “The system handles errors” is too vague. Specify which input is refused, whether the attempt changes state, what the caller sees and who receives unresolved work. A failed test is useful information about the contract; suppressing an exception merely to obtain a successful notebook run destroys that information.

## Compare another arrangement

A fixed, periodically reviewed configuration may be safer and cheaper than automatic proposal generation. An improver can suggest changes without holding promotion authority. Versioning and rollback preserve a recovery route, but cannot undo every external consequence already caused by a released version.

Compare the alternatives on the same task boundary. Include work transferred to another person or service, information that becomes unavailable and new maintenance obligations. A component-level speed gain can be real while the complete service remains slower or harder to investigate.

## Exercise and worked answer

Suppose an improver repeatedly tests candidates against the same held-out cases. Explain why those cases eventually stop functioning as an independent test, even if their filenames never change.

**Worked answer.** Selection decisions convey information about the test set. Repeated optimisation against its scores can overfit the selection process without directly displaying labels. Keep separate development and final confirmation sets, restrict evaluation access, record the number of selection rounds and use a new representative comparison when scope changes. Human approval should examine the experiment design as well as the displayed score.

Carry that answer into the design record: required input, permitted contribution, acceptance owner, escalation trigger, recovery route and evidence for any benefit claim. A design record describes the proposed arrangement. Repeated observation and outcome comparisons are needed to examine what it becomes in practice.

## Practical activity: Require explicit approval and comparable evaluation before promotion.





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

Can the gate promote while human_approved is False?

```python
from ai_orgdesign.labs.m20 import gate
baseline={"n":2,"dataset_hash":"same-cases","accuracy":1.,"unsafe":0,"cost":100}
candidate={**baseline,"cost":105}
assert not gate(baseline,candidate,human_approved=False)["promote"]
print(gate(baseline,candidate,human_approved=True))
```

No. These local numbers illustrate the rule; Lesson 20.2 supplies a measured model comparison.

### Complete the exercise

Write the prediction before consulting the worked answer: Can the gate promote while human_approved is False?

**Worked answer.** No. These local numbers illustrate the rule; Lesson 20.2 supplies a measured model comparison.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
