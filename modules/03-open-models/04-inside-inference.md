# Lesson 3.4: Follow numbers through a small language model

[Download the matching notebook](/downloads/03-04-inside-inference.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next: inspect a real inference interface](05-source-walkthrough.md)

## Business context: Harbour

An attention calculation helps explain how input representations are combined; its weights are not a ranking of Harbour’s organisational authority.

[Company and supply-chain context](../../HARBOUR.md) · [Module 3 business situation](../../reference/harbour-learning-journey.md#module-3)

## Identifiers become representations

A token ID is an address in a vocabulary. Its numerical size does not describe its meaning: token 900 is not necessarily more important than token 90. An **embedding layer** looks up a learned vector, a list of numerical values, for each ID. Position information also enters the computation so that ordering matters.

Imagine three input tokens, each represented by four values. The sequence becomes a three-by-four table. Real models use larger tables, but the principle is the same. The batch dimension adds another level: two such sequences have shape `[2, 3, 4]`. Shape describes arrangement, not meaning or quality.

## Attention changes a token's representation using context

In a transformer, **attention** calculates how positions should draw on other available positions. Consider “The customer disputed the record because it was incomplete.” Resolving what “it” refers to needs relationships across the sequence. Learned attention operations contribute to contextual representations, alongside other transformations.

Attention is not a human explanation of reasoning. A large attention weight does not by itself identify the causal reason for an answer. Nor is attention the same as verifying a claim against the outside world.

A decoder-only language model normally uses a **causal mask**: a position cannot use future tokens while predicting the next one. The padding mask introduced earlier addresses a different issue, which positions are placeholders. During training, target labels determine which predictions are graded. Three kinds of masking can therefore have different jobs.

## Scores become a continuation

The model's output for each position includes scores over vocabulary tokens, called **logits**. A probability transformation and generation rule select the next token. The sequence grows and the process repeats. A key/value cache stores intermediate attention information that can avoid recomputing parts of the prefix. Longer sequences still require resources, even if weights are unchanged.

Here is a small library exercise using randomly initialised weights. It requires `torch` and `transformers`, but downloads no model or tokenizer and calls no service. It demonstrates shapes, not learned language ability.

```python
import torch
from transformers import GPT2Config, GPT2LMHeadModel

torch.manual_seed(7)
configuration = GPT2Config(
    vocab_size=16, n_positions=32, n_embd=16,
    n_layer=1, n_head=2, bos_token_id=1,
    eos_token_id=15, pad_token_id=0,
)
model = GPT2LMHeadModel(configuration).eval()
ids = torch.tensor([[1, 2, 3]])
with torch.no_grad():
    result = model(input_ids=ids)
print(tuple(ids.shape), tuple(result.logits.shape))
assert tuple(result.logits.shape) == (1, 3, 16)
```

`GPT2Config` defines a tiny architecture. Constructing the model from that configuration creates weights locally; it does not retrieve a pretrained system. `eval()` changes training-sensitive behaviour such as dropout. `no_grad()` avoids recording differentiation information. Neither operation trains or verifies the model.

The output shape means one sequence, three positions and sixteen candidate-token scores per position. The last position's scores can guide the next token. They are not sixteen possible business decisions. The vocabulary definition and application determine how token sequences become text and then a usable answer.

**Worked check:** Why would increasing the vocabulary to 32 change the last output dimension but not make the model twice as knowledgeable? It changes the number of token scores the architecture produces. Knowledge-like behaviour depends on learned parameters, data and use, not the dimension alone.

**Technical reference:** [Transformers GPT-2 model documentation](https://huggingface.co/docs/transformers/model_doc/gpt2). The local neural implementation is explained in the next lesson.

## Read the organisational connection

A numerical inference trace supports a technical claim within its tested scope. The research chapter explains [the evidence path](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).

## Practical activity: Calculate a small attention-weighted combination by hand and in code.



A comprehension constructs a new collection from an existing one. Read `[expression for item in items if condition]` as: visit each item, keep those meeting the condition, and calculate the expression. `zip` pairs corresponding items from sequences. It stops at the shortest input, so paired evaluation needs an explicit equal-length condition.

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

Which source value receives the larger weight?

```python
import math
scores = [1.0, 0.0]
weights = [math.exp(s) / sum(math.exp(x) for x in scores) for s in scores]
values = [10.0, 2.0]
combined = sum(w * value for w, value in zip(weights, values))
print("Weights:", weights, "Weighted value:", combined)
assert weights[0] > weights[1]
```

Ten receives the larger weight because its score is larger. This arithmetic illustrates attention weighting, not how the full transformer learns its scores.

### Complete the exercise

Write the prediction before consulting the worked answer: Which source value receives the larger weight?

**Worked answer.** Ten receives the larger weight because its score is larger. This arithmetic illustrates attention weighting, not how the full transformer learns its scores.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
