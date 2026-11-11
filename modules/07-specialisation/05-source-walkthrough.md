# Lesson 7.5: Follow gradients, frozen weights and saved state

[Download the matching notebook](/downloads/07-05-source-walkthrough.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

A gradient indicates how a small change to a learned number would affect the loss. The trainer uses that information to update the adapter, while the frozen base values stay fixed. Locate the adapter in the saved material and the step that reloads it. This distinguishes keeping the training result from doing the training again.

Trace saved weights, adapter identity and reload behaviour before claiming a trained artefact can be reproduced.

[Company and supply-chain context](../../HARBOUR.md) · [Module 7 business situation](../../reference/harbour-learning-journey.md#module-7)

## Practical activity: Train and reload a real text-classification LoRA adapter.


The notebook is the easiest way to run this activity. Its first cell loads the course settings. `ROOT` records where the course files are, and `RUN_LIVE` records whether the optional provider call is enabled. The local steps can be read with live mode off. When running the snippets outside the notebook, use this setup once from a prepared checkout:

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

May the saved adapter be paired with an arbitrary base-model revision?

```python
from ai_orgdesign.text_adaptation import TRAIN, TEST
from ai_orgdesign.model_revisions import BERT_REVISION
assert not set(text for text,label in TRAIN) & set(text for text,label in TEST)
print("Train examples:",len(TRAIN),"Test examples:",len(TEST),"Revision:",BERT_REVISION)
```

### Run the pinned local model

This is a text classifier, not a chat model. Label 0 means finance and label 1 means delivery operations. The pretrained encoder provides representations; a newly initialised classification head learns the two outputs. LoRA updates selected attention transformations while the head is trained and saved with the adapter. The warning about newly initialised classifier weights is expected before task training.

The actual development run and its limits are recorded in the worked experiments.

This optional download route uses no paid inference API. The first run needs a network connection and local storage; later runs use the cached weights. Enable it explicitly in the matching notebook. Inspect the model revision, data split, outputs and limitations.

```python
from ai_orgdesign.text_adaptation import train_adapter
from ai_orgdesign.model_revisions import BERT_REVISION
adaptation = train_adapter(ROOT / "outputs" / "text-adapter", BERT_REVISION)
print(adaptation)
assert adaptation["reload_predictions_equal"]
```

For model provenance and the observed development runs, see [Worked model experiments](../../reference/worked-model-experiments.md).

### Complete the exercise

**Worked answer.** No. The adapter depends on the base architecture and parameters; retain its exact revision and tokenizer.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
