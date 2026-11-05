# Lesson 7.5: Follow gradients, frozen weights and saved state

[Download the matching notebook](/downloads/07-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m07.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

LowRank keeps a two-by-two identity matrix as a frozen buffer. Two trainable matrices, a and b, produce an additive update b @ a. The @ operator means matrix multiplication, so a two-by-one matrix multiplied by a one-by-two matrix produces a two-by-two update with rank at most one. adapt evaluates an initial mean squared error, performs 120 Adam steps against four supplied input-target pairs, saves the state dictionary, constructs a fresh model and reloads it. The base matrix never enters the optimiser parameters. This is a linear demonstration of low-rank adaptation, not an implementation of full transformer LoRA or QLoRA.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Explain why matching the saved outputs proves neither successful business adaptation nor the quality of a quantized language model. Identify what additional artefacts would be needed to reproduce a real adapter deployment.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m07 import LowRank
model = LowRank()
print({name: list(value.shape) for name, value in model.named_parameters()})
print("Frozen base:", model.base.tolist())
```

**Interpretation.** Reload equality checks artefact reconstruction. A business task also needs representative held-out evaluation, correct labels and a comparison with prompting and retrieval. A real language-model adapter requires the exact base revision, tokenizer, adapter configuration, training data identity, package versions and serving settings. Quantization introduces another numerical approximation that this unquantized lab does not test.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The final training loss should be substantially below the initial loss. Reloading should reproduce the trained outputs, and the frozen base should equal the identity matrix. The test checks these properties rather than requiring platform-identical final decimal digits. There is no held-out generalisation claim from this four-pair training exercise.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. Prompt changes are inexpensive to reverse, retrieval can supply current evidence and parameter adaptation can shape repeated behaviour. These mechanisms can be combined, but each creates a different maintenance obligation. Smaller low-rank updates reduce trainable parameter count; they do not by themselves establish lower total service cost.

The [research connection](../../reference/research/05-routines.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
