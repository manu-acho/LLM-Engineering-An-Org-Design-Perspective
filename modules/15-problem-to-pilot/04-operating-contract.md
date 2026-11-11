# Lesson 15.4: Make the operating contract inspectable

[Download the matching notebook](/downloads/15-04-operating-contract.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Read what a pilot accepts, returns and refuses, and trace a difficult input through those rules. This gives Harbour a concrete agreement for using generated code in the service.

## Business context: Harbour

An operating contract sets out what the service accepts, what it returns and who acts on it. Read the example for the rules that separate a usable brief from one that must be returned for correction. Trace a discrepancy case with a missing source through the rules instead of relying on the draft's fluency.

Choose the smallest service slice that can test the proposed contribution.

[Company and supply-chain context](../../HARBOUR.md) · [Module 15 business situation](../../reference/harbour-learning-journey.md#module-15)

## Start with a concrete contribution

Harbour wants to reduce the effort of investigating delivery discrepancies. That is a business problem, not yet a requirement for an agent. A useful pilot tests a bounded contribution against an explicit alternative and preserves the case owner's ability to investigate exceptions.

An operating contract states what information is required, what contribution is promised, what counts as acceptance and who owns the next step. It also names refusal and failure outcomes. A contract is useful when another person can apply it to a case without guessing what a success label means.

## Follow the included implementation

REQUIREMENTS pairs three cases with expected outcomes and named owners. route applies scope before evidence checks, then distinguishes a discrepancy from an apparently matching record. demo constructs the three inputs, evaluates them and computes a hash of the exact input data. The hash identifies the examples; it does not validate their quality. Keeping the expected outcomes separate from route makes it possible to detect an implementation that disagrees with the specification.

Open `src/ai_orgdesign/labs/m15.py` and follow each call into its supporting function. Ordinary Python functions receive values and return values; a class groups state and operations; a context manager controls a resource's lifetime. The [programming reference](../../reference/python-patterns.md) explains these patterns with small examples, and the [technical foundations](../../reference/technical-foundations.md) introduces transactions, concurrency and neural calculations before their use.

## Write acceptance and rejection conditions

The three demonstrated outcomes are `review`, `deny` and `needs_evidence`; `matches` is true for those supplied examples. The function also returns `compare_policy` when quantities agree, so the demonstration does not exercise every possible output. In this small requirements exercise, `review` means a discrepancy needs human investigation. It is not the narrower damaged-goods label used by the extended four-route task. Agreement between quantities produces `compare_policy` rather than automatic closure. This deliberately avoids using numerical agreement as sufficient evidence that the customer problem is resolved.

Acceptance conditions should be observable. “The system handles errors” is too vague. Specify which input is refused, whether the attempt changes state, what the caller sees and who receives unresolved work. A failed test is useful information about the contract; suppressing an exception merely to obtain a successful notebook run destroys that information.

## Compare another arrangement

An intake form, a record-comparison script or a better source feed may solve the first problem without generation. A coding agent can help implement the agreed slice, but its proposed code must face the same acceptance cases and review as manually written code.

Compare the alternatives on the same task boundary. Include work transferred to another person or service, information that becomes unavailable and new maintenance obligations. A component-level speed gain can be real while the complete service remains slower or harder to investigate.

## Exercise and worked answer

Add an acceptance example with equal quantities but a damaged box. Identify which missing input and policy rule are needed before the pilot can handle that case.

**Worked answer.** Quantity comparison cannot recognise condition or contractual remedy. The pilot needs an explicit damage report, supporting evidence and an agreed review route. Expanding the schema and examples changes scope; changing a prompt alone would hide that change. Keep damaged-goods cases outside automated handling until the revised specification is tested.

Carry that answer into the design record: required input, permitted contribution, acceptance owner, escalation trigger, recovery route and evidence for any benefit claim. The design record describes who will do the work and what rules they will follow. Observing actual cases shows whether those roles and rules work as planned.

## Practical activity: Inspect generated code before allowing a restricted execution.


### Predict and follow the values

Does this restricted exercise permit arbitrary generated Python?

```python
from ai_orgdesign.code_generation import compile_routing
try:
    compile_routing("def route_case(case):\n    return open('private.txt')")
except ValueError:
    print("File access is outside the exercise subset")
else:
    raise AssertionError("Disallowed code accepted")
```

### Complete the exercise

**Worked answer.** No. Calls, imports, attributes, loops and mutation are refused. This is not a general-purpose sandbox.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## Interpret this exercise’s route

The local requirements exercise uses `review` for discrepancy investigation and also has a `compare_policy` outcome for matching quantities. The extended four-route brief uses `investigate` for a discrepancy and a narrower `review` label for qualitative concerns. The [routing crosswalk](../../reference/case-data-guide.md#routing-vocabulary-belongs-to-a-task) keeps these contracts distinct.

## What to remember

A quantity rule cannot resolve a damage report on its own. The contract specifies the evidence, the response and what the next person must do.

## What this means for the business process

Put missing evidence and damaged deliveries into the acceptance examples, and send them to an investigator with a clear reason. Have that receiving role check the criteria before treating the contract as ready.

For the research behind this design choice, read [Four questions for a usable contribution](../../reference/research/02-coordination.md#four-questions-for-a-usable-contribution).

## Next lesson

The next workshop inspects model-proposed code and uses those acceptance cases to decide whether it behaves as required. [Lesson 15.5: Trace scope, evidence and discrepancy rules](05-source-walkthrough.md).
