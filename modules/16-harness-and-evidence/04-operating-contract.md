# Lesson 16.4: Make the operating contract inspectable

[Download the matching notebook](/downloads/16-04-operating-contract.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

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

Carry that answer into the design record: required input, permitted contribution, acceptance owner, escalation trigger, recovery route and evidence for any benefit claim. A design record describes the proposed arrangement. Repeated observation and outcome comparisons are needed to examine what it becomes in practice.

## Practical activity: Calculate an explicitly assumed token cost and reject invalid values.





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

No. The counts and rates in this arithmetic example are assumptions.

### Complete the exercise

Write the prediction before consulting the worked answer: Is 0.0018 an observed provider invoice?

**Worked answer.** No. The counts and rates in this arithmetic example are assumptions.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
