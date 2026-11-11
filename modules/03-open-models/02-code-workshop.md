# Lesson 3.2: Encode, generate, decode

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

The miniature vocabulary below gives a number to each word. Encode “delivery was”, add one supplied number, then decode only the added piece. A real model chooses the new numbers itself. Keep the miniature exercise separate from the later code that shows how to load and use a real model.

[Open the companion workshop notebook](../../notebooks/03-open-models.ipynb).

## A miniature representation exercise

Real tokenizers handle large vocabularies, subword fragments and special tokens. We will use a tiny invented word vocabulary to make the representation changes visible. This is not a language model and does not demonstrate learning.

```python
vocabulary = {"delivery": 1, "was": 2, "late": 3, "confirmed": 4}
reverse_vocabulary = {number: word for word, number in vocabulary.items()}

def encode_words(text):
    return [vocabulary[word] for word in text.split()]

def decode_words(ids):
    return " ".join(reverse_vocabulary[number] for number in ids)

input_ids = encode_words("delivery was")
output_ids = input_ids + [3]
new_ids = output_ids[len(input_ids):]
answer = decode_words(new_ids)
```

`vocabulary.items()` supplies key/value pairs. The dictionary comprehension reverses them, producing number-to-word lookup. `text.split()` separates the input at whitespace. The list comprehension replaces each word with its ID. The input becomes `[1, 2]`.

`input_ids + [3]` appends a predetermined ID in a new list. This imitates the shape of decoder-only generation output, not its computation. The full sequence is `[1, 2, 3]`. `len(input_ids)` returns 2. The slice `[2:]` keeps positions starting at index 2, so `new_ids` is `[3]`. Decoding returns `late`.

Why remove the input prefix? Some generation interfaces return the prompt together with the continuation. If you display the whole sequence as the “answer”, the user sees the prompt echoed. Knowing the representation lets you fix the actual problem rather than changing the prompt randomly.

## A real interface, read without running

The following is an integration example. It requires installed libraries and a compatible accessible model and may download weights if executed. It is provided for code reading; no download or model call was made for this curriculum.

```python
def continue_text(model_id, prompt):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    model.eval()
    inputs = tokenizer(prompt, return_tensors="pt")
    prefix_length = inputs["input_ids"].shape[1]
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=20, do_sample=False)
    return tokenizer.decode(outputs[0, prefix_length:], skip_special_tokens=True)
```

Imports inside the function make the required libraries available when it runs. `from_pretrained` loads components associated with the supplied identifier. `Auto` means the library selects a compatible implementation from configuration. It does not mean the library chooses your business model for you.

`return_tensors="pt"` asks for PyTorch tensors. `inputs` is a dictionary, commonly including token IDs and an attention mask. `.shape[1]` reads the second dimension, sequence length, for this single input. `**inputs` expands the dictionary into named arguments for `generate`.

`model.eval()` selects evaluation behaviour for relevant model components. `torch.no_grad()` prevents recording the computations needed to calculate training gradients. These serve different purposes. We are generating, not updating parameters.

`max_new_tokens=20` caps newly generated tokens. `do_sample=False` selects a non-sampling decoding path in this example. It does not promise factual accuracy or identical results under every environment change. Finally, the output slice removes the input prefix and `decode` returns readable text. This example assumes an appropriate decoder-only model and a plain completion prompt; chat models need their expected template. See the [generation guide](https://huggingface.co/docs/transformers/en/llm_tutorial).

Loading inside the function makes the lifecycle visible but is inefficient for repeated requests. A service would usually load once, reuse the objects and manage concurrency and memory. The original week 8 serving code demonstrates that later pattern.

## What the local week 3 code adds

Most week 3 lessons link to Colab notebooks whose remote cells were not available during authoring. The local [visualizer.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week3/visualizer.py) can still be inspected. It asks an API for token log probabilities, turns them into probabilities and stores alternative tokens in records. A graph function then draws the sequence and alternatives.

A log probability is a logarithmic representation of a probability; applying the exponential function reverses that transformation. You need not calculate one manually to understand the display. You do need to know that it concerns token continuation, not confidence that a business claim is true.

The graph's alternatives branch from the prefix actually generated. It does not explore every possible complete answer. Display structure can therefore suggest more coverage than the underlying calculation provides unless explained carefully.

## Alternatives and a diagnostic exercise

A task-level library pipeline hides some steps for convenience. Direct tokenizer/model code makes them visible and configurable. A local model server hides loading behind an API so several applications can reuse it. Each approach moves responsibility; none eliminates it.

Change the toy input to `delivery confirmed`. Then try an unknown word. Predict where the error occurs.

**What the example shows:** Known words encode, although our fake continuation is still hard-coded and may be nonsensical. An unknown word raises a lookup error. Real tokenizers usually have ways to handle unfamiliar strings, but that does not mean they understand those strings. The exercise distinguishes coverage of representation from appropriateness of output.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Encoding and decoding are inspectable transformations whose organisational effects need further evidence. The research chapter explains [materiality in digital systems](../../reference/research/06-technology-in-practice.md#materiality-in-digital-systems).
