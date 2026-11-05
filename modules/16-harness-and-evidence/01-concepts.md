# Lesson 16.1: Agent harnesses and operational evidence

[Download the matching notebook](/downloads/16-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## The model is only one part of a run

A **harness** is the application arrangement that supplies instructions and context, exposes tools, runs the loop, applies limits and records what happened. A model can be capable while a harness supplies the wrong policy, accepts a malformed tool argument or loses a failure. Conversely, a reliable harness cannot turn an unsuitable model into a competent investigator.

At Harbour, a run begins with a case and a permitted scope. It may retrieve policy, compare quantities, draft unresolved questions and return a contribution. The harness must distinguish that execution from the continuing business case. One case may contain many runs, and a run may end successfully while the case remains unresolved.

## Give operational evidence a structure

A **trace** connects observations about steps within an execution. A run identifier groups events; a parent-child relationship can connect a model request to a tool call; a timestamp locates them in time. A **span** usually describes one bounded operation. These are useful representations, but they must be interpreted according to what was actually instrumented.

Record the configuration identity, case reference, step category, duration, result category and stopping reason. Configuration identity should cover the instructions, tool schema, model revision and relevant policy or index version. A hash detects whether supplied bytes changed; it does not explain their meaning or certify that the configuration was approved.

The local harness records the instruction hash, elapsed time, tool-call count and stop reason. It leaves provider usage empty because no provider was called. This absence is part of an honest record. Filling it with an estimate and labelling it actual usage would conflate observation and assumption.

## Measure time carefully

Elapsed time from a monotonic clock measures duration without relying on wall-clock adjustments. It is useful for local performance comparisons. A distributed trace also needs a way to correlate events across machines whose clocks may differ. Avoid interpreting small timestamp differences as a reliable causal ordering unless the instrumentation supports it.

Report waiting and active work separately where possible. A model call taking two seconds may sit inside a case that waits two days for evidence. Improving the call can be worthwhile without materially changing resolution time. Percentiles can reveal a long tail that an average conceals; neither explains its cause by itself.

## Cost needs a declared basis

A token is a model-specific text unit, not necessarily a word. Input and output tokens may have different prices, and some services distinguish cached input or other usage categories. The lab isolates a simple calculation with assumed prices per million tokens. The assumptions are printed beside the result rather than presented as current provider prices.

A service cost comparison should also include retrieval, storage, tracing, maintenance and review work when relevant. A lower price per generated token can coincide with more retries or longer human checking. A spending limit needs enforcement during the run, not merely a report after charges have been incurred.

## Observability creates its own data responsibilities

Observability is the capacity to investigate the service through emitted evidence. More logging is not automatically better observability. Full prompts may contain confidential records, and a long transcript may still omit the policy version needed to explain a decision. Select the smallest record sufficient for investigation, specify retention and control who can inspect it.

Logs describe the instrumented path. A missing event could mean a path was not taken, a process failed before emitting it or logging itself failed. Treat absence cautiously and design reconciliation for important transitions. A trace should support inquiry, not become a decorative picture interpreted as proof of control.

## Practical activity: Give a run a stable identity and retain its instruction version.





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

Does the hash certify the instruction is appropriate?

```python
from ai_orgdesign.business import fingerprint
instructions="Preserve recorded and reported quantities separately."
record={"run":"learning-run","instruction_hash":fingerprint(instructions),"case":"H-17"}
print(record)
```

No. It identifies the supplied bytes; quality and approval need other evidence.

### Complete the exercise

Write the prediction before consulting the worked answer: Does the hash certify the instruction is appropriate?

**Worked answer.** No. It identifies the supplied bytes; quality and approval need other evidence.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
