# Lesson 3.5: Load weights, inspect shapes and diagnose inference

[Download the matching notebook](/downloads/03-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Identify the inference path and source of model weights before attributing a result to the company’s evidence.

[Company and supply-chain context](../../HARBOUR.md) · [Module 3 business situation](../../reference/harbour-learning-journey.md#module-3)

## Practical activity: Run a small instruction-following open model on CPU.





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

Do trained weights eliminate the need to check evidence support?

```python
from ai_orgdesign.model_revisions import SMOL_REVISION
print("Pinned SmolLM2 revision:", SMOL_REVISION)
print("The download exercise below loads trained weights, unlike the random forward-pass exercise.")
```

No. They make useful language behaviour possible but do not verify a particular customer record.

### Run the pinned local model

This optional download route uses no paid inference API. The first run needs a network connection and local storage; later runs use the cached weights. Enable it explicitly in the matching notebook. Inspect the model revision, data split, outputs and limitations.

```python
from ai_orgdesign.labs.m03 import instruct_inference
from ai_orgdesign.model_revisions import SMOL_REVISION
local_answer = instruct_inference("An order records 12 boxes; a customer reports 10. State what is unknown.", SMOL_REVISION)
print(local_answer)
```

For model provenance and the observed development runs, see [Worked model experiments](../../reference/worked-model-experiments.md).

### Complete the exercise

Write the prediction before consulting the worked answer: Do trained weights eliminate the need to check evidence support?

**Worked answer.** No. They make useful language behaviour possible but do not verify a particular customer record.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
