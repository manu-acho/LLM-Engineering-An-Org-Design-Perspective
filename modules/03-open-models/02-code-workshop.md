# Lesson 3.2: Inspect a real neural forward pass

[Download the matching notebook](/downloads/03-02-code-workshop.ipynb) · [Module route](README.md) · [Glossary](../../reference/glossary.md)

## What you'll learn and why it matters

Read the dimensions printed by one neural forward pass. This helps Harbour distinguish a check that the model ran from evidence that it handled a business case correctly.

## Business context: Harbour

A forward pass takes one input through a model to calculate an output without training it. Think of a row of tokens, or pieces of text, where each position gets scores for possible next pieces. A shape lists the sizes of the axes in that table. In the lab, match each printed size to what it counts before trying to interpret the values.

The local neural example demonstrates computation. Random weights do not supply Harbour’s operating knowledge or a correct customer answer.

[Company and supply-chain context](../../HARBOUR.md) · [Module 3 business situation](../../reference/harbour-learning-journey.md#module-3)

## Practical activity: Read dimensions from a real neural forward pass.

A tensor is a numerical array. Its shape identifies the size of each dimension. A logit is a model score before conversion into probabilities.


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

How many candidate-token scores does the last position contain?

```python
from ai_orgdesign.labs.m03 import local_inference
result = local_inference()
print(result)
assert result["shape"] == [1, 8]
assert abs(sum(result["probabilities"]) - 1) < 1e-5
```

### Use the live model

After [API setup](../../reference/live-model-guide.md), live mode sends an actual request with the exercise’s fictional data. With live mode off, this block reports that it skipped the request. When a result is returned, read its status and any facts separately from the wording.

```python
if RUN_LIVE:
    answer = gateway.generate("Explain why random neural weights do not supply learned business knowledge, in two sentences.")
    print(answer.text)
else:
    print("Live exercise not run. Set COURSE_LIVE_MODE=1 in the local .env when ready.")
```

A failed or incomplete result must remain visible. The [live-model guide](../../reference/live-model-guide.md) explains authentication, quota, timeout, refusal and response-format problems, with the offline verification route kept separate.

### Complete the exercise

**Worked answer.** Eight. One input sequence by eight vocabulary entries is not an evaluation of eight business cases.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.


The [further learning guide](../../reference/further-learning.md) offers optional alternative explanations. The full shared implementation is included in the checkout; no source course is needed to run this lesson.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.

## What to remember

A forward pass calculates scores for token positions and vocabulary entries. An axis of eight vocabulary entries does not represent eight evaluated deliveries.

## What this means for the business process

Use output dimensions to diagnose an integration problem such as an unexpected model result. Keep a separate test that checks the claims in a Harbour brief against its sources. The two tests support different conclusions.

For the research behind this design choice, read [An evidence path without skipped steps](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).

## Next lesson

The next lesson applies that distinction to meeting notes, where a technically successful run can still change the meaning of a commitment. [Lesson 3.3: When meeting notes become an organisational record](03-business-and-organisation.md).
