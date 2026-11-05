# Lesson 7.2: Train and reconstruct a low-rank update

[Download the matching notebook](/downloads/07-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Fine-tuning changes numerical parameters, while retrieval changes the supplied evidence. This module exposes a real parameter update on a small enough task that every trained quantity and saved artefact can be inspected.

The implementation lives in `src/ai_orgdesign/labs/m07.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

LowRank keeps a two-by-two identity matrix as a frozen buffer. Two trainable matrices, a and b, produce an additive update b @ a. The @ operator means matrix multiplication, so a two-by-one matrix multiplied by a one-by-two matrix produces a two-by-two update with rank at most one. adapt evaluates an initial mean squared error, performs 120 Adam steps against four supplied input-target pairs, saves the state dictionary, constructs a fresh model and reloads it. The base matrix never enters the optimiser parameters. This is a linear demonstration of low-rank adaptation, not an implementation of full transformer LoRA or QLoRA.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m07 import demo
result = demo()
assert result["loss_after"] < result["loss_before"] / 10
assert result["base_unchanged"] and result["reload_equal"]
print(result)
```

The final training loss should be substantially below the initial loss. Reloading should reproduce the trained outputs, and the frozen base should equal the identity matrix. The test checks these properties rather than requiring platform-identical final decimal digits. There is no held-out generalisation claim from this four-pair training exercise.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Explain why matching the saved outputs proves neither successful business adaptation nor the quality of a quantized language model. Identify what additional artefacts would be needed to reproduce a real adapter deployment.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** Reload equality checks artefact reconstruction. A business task also needs representative held-out evaluation, correct labels and a comparison with prompting and retrieval. A real language-model adapter requires the exact base revision, tokenizer, adapter configuration, training data identity, package versions and serving settings. Quantization introduces another numerical approximation that this unquantized lab does not test.

## Consider the alternative

Prompt changes are inexpensive to reverse, retrieval can supply current evidence and parameter adaptation can shape repeated behaviour. These mechanisms can be combined, but each creates a different maintenance obligation. Smaller low-rank updates reduce trainable parameter count; they do not by themselves establish lower total service cost.

The [organisation design reading](../../reference/research/05-routines.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
