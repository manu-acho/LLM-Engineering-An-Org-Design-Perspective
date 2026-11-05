# Lesson 3.5: Load weights, inspect shapes and diagnose inference

[Download the matching notebook](/downloads/03-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m03.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

GPT2Config specifies a tiny decoder architecture: eight vocabulary entries, sixteen positions, sixteen representation dimensions, one layer and two attention heads. GPT2LMHeadModel creates actual neural parameters from that configuration. torch.tensor constructs a batch with three token identifiers. eval disables training-specific behaviour, while no_grad avoids recording gradient calculations. The last-position logits contain one score for each vocabulary entry. softmax turns those eight scores into a distribution. These weights are random; the computation is real inference but the model has not learned language.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Explain why replacing the random model with downloaded pretrained weights changes the source of its behaviour, while leaving the need to inspect context, scope and record ownership.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m03 import VOCAB
assert len(VOCAB) == 8
print(dict(enumerate(VOCAB)))
print("These custom token IDs are not a pretrained tokenizer.")
```

**Interpretation.** Pretrained weights contain relationships estimated from prior training. Random weights do not. Both produce scores through a forward pass. A pretrained continuation still requires task evaluation and cannot establish who has authority to approve a meeting record. Hosting a model locally also does not confer a licence to redistribute its weights.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The logits have shape [1, 8]: one sequence and eight candidate tokens. The eight probabilities sum approximately to one. The notebook reports the parameter count and CPU device from the actual model. Neither a fluent sentence nor business knowledge should be expected.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A hosted API transfers model serving to a provider; local inference retains more operating responsibility. A pretrained open model provides a meaningful language baseline only after its access, licence and hardware requirements have been checked. The optional download exercise uses a tiny test model for loading mechanics, not a recommended business model.

The [research connection](../../reference/research/06-technology-in-practice.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
