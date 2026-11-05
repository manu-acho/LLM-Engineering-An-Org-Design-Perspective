# Lesson 3.2: Inspect a real neural forward pass

[Download the matching notebook](/downloads/03-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Choosing local inference changes who operates the model, where data travels and which resources are needed. It does not settle whether the output is accurate enough to enter a meeting record or resolve a case.

The implementation lives in `src/ai_orgdesign/labs/m03.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

GPT2Config specifies a tiny decoder architecture: eight vocabulary entries, sixteen positions, sixteen representation dimensions, one layer and two attention heads. GPT2LMHeadModel creates actual neural parameters from that configuration. torch.tensor constructs a batch with three token identifiers. eval disables training-specific behaviour, while no_grad avoids recording gradient calculations. The last-position logits contain one score for each vocabulary entry. softmax turns those eight scores into a distribution. These weights are random; the computation is real inference but the model has not learned language.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m03 import local_inference
result = local_inference()
assert result["shape"] == [1, 8]
assert abs(sum(result["probabilities"]) - 1) < 1e-5
print(result)
```

The logits have shape [1, 8]: one sequence and eight candidate tokens. The eight probabilities sum approximately to one. The notebook reports the parameter count and CPU device from the actual model. Neither a fluent sentence nor business knowledge should be expected.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Explain why replacing the random model with downloaded pretrained weights changes the source of its behaviour, while leaving the need to inspect context, scope and record ownership.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** Pretrained weights contain relationships estimated from prior training. Random weights do not. Both produce scores through a forward pass. A pretrained continuation still requires task evaluation and cannot establish who has authority to approve a meeting record. Hosting a model locally also does not confer a licence to redistribute its weights.

## Consider the alternative

A hosted API transfers model serving to a provider; local inference retains more operating responsibility. A pretrained open model provides a meaningful language baseline only after its access, licence and hardware requirements have been checked. The optional download exercise uses a tiny test model for loading mechanics, not a recommended business model.

The [organisation design reading](../../reference/research/06-technology-in-practice.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
