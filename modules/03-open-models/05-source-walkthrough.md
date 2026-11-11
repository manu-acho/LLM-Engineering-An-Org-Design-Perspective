# Lesson 3.5: Load weights, inspect shapes and diagnose inference

[Download the matching notebook](/downloads/03-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

Loading a model means bringing its learned numbers into memory so the computer can use them. Generation then repeats the calculation for possible next pieces as the reply grows. In the lab, separate a failure to load the model from an unhelpful answer after it has loaded. Changing the instruction cannot fix a missing file or a model too large to load.

Identify the inference path and source of model weights before attributing a result to the company’s evidence.

[Company and supply-chain context](../../HARBOUR.md) · [Module 3 business situation](../../reference/harbour-learning-journey.md#module-3)

## Practical activity: Run a small instruction-following open model on CPU.


### Predict and follow the values

Do trained weights eliminate the need to check evidence support?

```python
from ai_orgdesign.model_revisions import SMOL_REVISION
print("Pinned SmolLM2 revision:", SMOL_REVISION)
print("The download exercise below loads trained weights, unlike the random forward-pass exercise.")
```

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

**Worked answer.** No. They make useful language behaviour possible but do not verify a particular customer record.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
