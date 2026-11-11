# Lesson 16.2: Measure a bounded run without inventing usage

[Download the matching notebook](/downloads/16-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

A stopwatch can measure elapsed time. It cannot tell how many tokens the provider counted. In the live lab, read usage from the provider's returned information and preserve any missing value as unknown. Then distinguish what was measured from any cost estimated by applying a price.

Inspect actual response status, model identity, usage and elapsed time.

[Company and supply-chain context](../../HARBOUR.md) · [Module 16 business situation](../../reference/harbour-learning-journey.md#module-16)

## Practical activity: Measure actual provider usage for a live contribution.


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

Are token counts supplied by the provider the same as a complete service cost?

```python
print("The live cell records the returned model, response ID, status, tokens and duration.")
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    answer=gateway.generate("Explain the order-versus-receipt distinction in one sentence.")
    print(answer.text)
    print(answer.record)
    print(gateway.ledger())
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** No. They support an inference-usage calculation, while review, storage and other operating work remain separate.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
