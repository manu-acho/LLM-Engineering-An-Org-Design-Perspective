# Lesson 16.2: Measure a bounded run without inventing usage

[Download the matching notebook](/downloads/16-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

A model result without its inputs, configuration and stopping reason is difficult to investigate. Harbour needs enough execution evidence to diagnose a failed contribution while avoiding a second uncontrolled store of customer information.

The implementation lives in `src/ai_orgdesign/labs/m16.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

harness wraps the bounded loop from Module 9. It hashes a fixed instruction string, measures elapsed time with perf_counter, counts recorded tool calls and preserves the stop reason. It explicitly leaves provider_usage as None because the scripted planner makes no model request. estimate_cost multiplies token counts by assumed prices per million tokens and rejects negative inputs. The resulting number is illustrative arithmetic, not billed cost.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m16 import demo
result = demo()
assert result["trace"]["provider_usage"] is None
assert abs(result["illustrative_cost"] - .0018) < 1e-12
print(result)
```

The supplied loop uses one tool call and stops with final. Elapsed time is measured at runtime and will vary. The assumed cost calculation for one thousand input tokens at one unit per million and two hundred output tokens at four units per million is 0.0018 currency units. No actual provider usage is claimed.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Suppose a run stopped after reading the case but before writing its final response. Decide which trace fields distinguish that failure from a denied tool call and from an unresolved business investigation.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** A step-level record should distinguish requested, authorised, started, completed and failed operations, with bounded identifiers and exception categories. A final loop stop reason is not a full audit trail. An unresolved business case can coexist with a technically successful run; an execution error can coexist with a correct earlier read.

## Consider the alternative

Structured local logs are sufficient for the first experiment. A tracing service can correlate distributed spans and evaluations, but needs retention, access and redaction rules. Recording hidden reasoning is neither required nor an adequate explanation of evidence support.

The [organisation design reading](../../reference/research/05-routines.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
