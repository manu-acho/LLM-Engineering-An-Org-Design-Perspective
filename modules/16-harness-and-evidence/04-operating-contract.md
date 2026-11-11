# Lesson 16.4: Make the operating contract inspectable

[Download the matching notebook](/downloads/16-04-operating-contract.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Read an operating record and calculate a cost under explicit price assumptions. Learn to distinguish a complete run from one with insufficient evidence for comparison.

## Business context: Harbour

To compare two runs, Harbour needs to know what instructions were used and whether each run actually finished. Follow the supplied example from the request to its recorded outcome. Specify which details are required before treating a run as evidence about speed, quality or cost.

Define evidence retention and incident ownership across business and technical support.

[Company and supply-chain context](../../HARBOUR.md) · [Module 16 business situation](../../reference/harbour-learning-journey.md#module-16)

## Start with a concrete contribution

A model result without its inputs, configuration and stopping reason is difficult to investigate. Harbour needs enough execution evidence to diagnose a failed contribution while avoiding a second uncontrolled store of customer information.

An operating contract states what information is required, what contribution is promised, what counts as acceptance and who owns the next step. It also names refusal and failure outcomes. A contract is useful when another person can apply it to a case without guessing what a success label means.

## Follow the included implementation

harness wraps the bounded loop from Module 9. It hashes a fixed instruction string, measures elapsed time with perf_counter, counts recorded tool calls and preserves the stop reason. It explicitly leaves provider_usage as None because the scripted planner makes no model request. estimate_cost multiplies token counts by assumed prices per million tokens and rejects negative inputs. The resulting number is illustrative arithmetic, not billed cost.

Open `src/ai_orgdesign/labs/m16.py` and follow each call into its supporting function. Ordinary Python functions receive values and return values; a class groups state and operations; a context manager controls a resource's lifetime. The [programming reference](../../reference/python-patterns.md) explains these patterns with small examples, and the [technical foundations](../../reference/technical-foundations.md) introduces transactions, concurrency and neural calculations before their use.

## Write acceptance and rejection conditions

The supplied loop uses one tool call and stops with final. Elapsed time is measured at runtime and will vary. The assumed cost calculation for one thousand input tokens at one unit per million and two hundred output tokens at four units per million is 0.0018 currency units. No actual provider usage is claimed.

Acceptance conditions should be observable. “The system handles errors” is too vague. Specify which input is refused, whether the attempt changes state, what the caller sees and who receives unresolved work. A failed test is useful information about the contract; suppressing an exception merely to obtain a successful notebook run destroys that information.

## Compare another arrangement

Structured local logs are sufficient for the first experiment. A tracing service can correlate distributed spans and evaluations, but needs retention, access and redaction rules. Recording hidden reasoning is neither required nor an adequate explanation of evidence support.

Compare the alternatives on the same task boundary. Include work transferred to another person or service, information that becomes unavailable and new maintenance obligations. A component-level speed gain can be real while the complete service remains slower or harder to investigate.

## Exercise and worked answer

Suppose a run stopped after reading the case but before writing its final response. Decide which trace fields distinguish that failure from a denied tool call and from an unresolved business investigation.

**Worked answer.** A step-level record should distinguish requested, authorised, started, completed and failed operations, with bounded identifiers and exception categories. A final loop stop reason is not a full audit trail. An unresolved business case can coexist with a technically successful run; an execution error can coexist with a correct earlier read.

Carry that answer into the design record: required input, permitted contribution, acceptance owner, escalation trigger, recovery route and evidence for any benefit claim. The design record describes who will do the work and what rules they will follow. Observing actual cases shows whether those roles and rules work as planned.

## Practical activity: Calculate an explicitly assumed token cost and reject invalid values.


### Predict and follow the values

Is 0.0018 an observed provider invoice?

```python
from ai_orgdesign.labs.m16 import estimate_cost
amount=estimate_cost(1000,200,1,4)
print("Assumed currency cost:",amount)
assert abs(amount-.0018)<1e-12
try:
    estimate_cost(float("nan"),200,1,4)
except ValueError:
    print("Non-finite input rejected")
```

### Complete the exercise

**Worked answer.** No. The counts and rates in this arithmetic example are assumptions.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A run record needs a stable identity, timing and an outcome. The cost calculation depends on valid counts and assumed prices. A failed run can still use resources.

## What this means for the business process

Agree which run outcomes count in the comparison and preserve missing fields. Have the service owner separate measured usage, price assumptions and the work that continues outside the model call.

For the research behind this design choice, read [An evidence path without skipped steps](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).

## Next lesson

Next inspect an incomplete reply and see why its usage may belong in the record even when the answer is refused. [Lesson 16.5: Trace instruction identity, time and assumed cost](05-source-walkthrough.md).
