# Lesson 3.4: Follow numbers through a small language model

[Module route](README.md) · [Next: inspect a real inference interface](05-source-walkthrough.md)

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

**Technical reference:** [Transformers GPT-2 model documentation](https://huggingface.co/docs/transformers/model_doc/gpt2). This independent exercise supplements the source course's remotely hosted lessons.

## Read the organisational connection

A numerical inference trace supports a technical claim within its tested scope. The research chapter explains [the evidence path](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).
