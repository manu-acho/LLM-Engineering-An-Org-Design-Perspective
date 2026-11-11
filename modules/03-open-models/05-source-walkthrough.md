# Lesson 3.5: Load, encode, generate and diagnose

[Module route](README.md) · [Next: design a trustworthy meeting record](06-design-lab.md)

## What you'll learn and why it matters

Trace model loading, encoding, generation and decoding through the inference function. Use its execution record to distinguish a load failure from an unsuitable meeting note.

A local inference program loads a tokenizer and the learned model, converts the question into identifiers, then asks the model to extend that sequence. Trace where the program removes the original question before displaying the new text. A failed load and an unhelpful answer occur at different stages and need different checks.

[Open the companion workshop notebook](../../notebooks/03-open-models.ipynb).

## Separate local and remote source material

Ed Donner's [Week 3 notebooks](https://github.com/ed-donner/llm_engineering/tree/103f4bf045180f3b8b7721fd55b7897305a72672/week3) point to Colab lessons for pipelines, tokenizers, model inference and meeting minutes. The linked Colab contents were not accessible for inspection in preparing this expansion. The walkthrough below is an independent teaching lab, not a reconstruction of unseen cells.

The local [visualizer](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week3/visualizer.py) does provide an inspectable source path. It requests token alternatives, converts log probabilities with `math.exp`, constructs prediction records and draws a graph. Those alternatives are conditional on the generated prefix. The picture is not a fully explored tree of alternative answers or a truth-probability map.

## A complete inference function with visible boundaries

This optional integration lab needs `torch`, `transformers` and a compatible pretrained causal language model already stored locally. `local_files_only=True` prevents fetching missing weights. Loading can still require substantial memory. Set the directory in the calling environment and use synthetic input. No pretrained inference was executed while authoring this lesson.

```python
def answer_locally(model_directory, question, max_new_tokens=40):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(
        model_directory, local_files_only=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_directory, local_files_only=True
    ).eval()
    messages = [{"role": "user", "content": question}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    batch = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
    prefix_length = batch["input_ids"].shape[1]
    with torch.no_grad():
        generated = model.generate(
            **batch, max_new_tokens=max_new_tokens, do_sample=False
        )
    continuation = generated[0, prefix_length:]
    return {
        "text": tokenizer.decode(continuation, skip_special_tokens=True),
        "input_tokens": prefix_length,
        "output_tokens": len(continuation),
    }
```

The function deliberately loads once per call to keep the example self-contained. A service would normally load compatible components during startup and reuse them, while managing concurrent requests. Otherwise repeated loading can dominate latency.

`apply_chat_template` turns role-labelled messages into model-specific text. The later tokenizer call creates tensors. Avoid adding a second set of special tokens after applying a template that already includes them. `**batch` expands input IDs and masks into named arguments. Slicing removes the prompt prefix from decoder-only output before decoding the continuation.

This example stays on the default device. Moving a model to a GPU also requires inputs on a compatible device and adequate memory. Automatically selecting a device is convenient only when the resulting placement is understood. A CPU lab may be slower but easier to diagnose.

## Keep an execution record

Before interpreting quality, record model and tokenizer revisions, template, input length, generation settings, device, output and termination behaviour. The same model name can refer to changing files. A run that stops at its output limit can be incomplete even when returned text is grammatical.

| Observation | First boundary to inspect | Why |
|---|---|---|
| Missing-file error | Local model directory | The lab intentionally refuses downloads |
| Template error | Tokenizer configuration and model type | Not every pretrained model is a chat model |
| Memory failure | Weights, context, device and batch | A short successful request does not establish long-input capacity |
| Prompt repeated in answer | Prefix slicing and model architecture | Some interfaces return prompt plus continuation |
| Fluent invented commitment | Evidence and task evaluation | Correct loading does not establish factual support |

## Extend the meeting application in stages

First use a short, synthetic transcript. Generate structured notes containing claim, speaker, evidence span, condition and proposed owner. Compare notes with a manually prepared reference. Only after this works should audio transcription be added. Then transcription errors can be assessed separately from summary errors.

Speaker attribution, recording permission, storage and access are additional application concerns. Running the final text model locally does not make an upstream transcription service local. Map the entire data path before making a privacy or operating claim.

**Worked exercise:** The transcript says “finance could approve after recount”; the note says “finance approved”. Even if every model-loading and tensor-shape check passes, the note fails a claim-preservation test. Add a case specifically checking modality and conditions rather than increasing the hardware allocation.

## Read the organisational connection

A successful load-and-generate path does not establish that the surrounding service works well. The research chapter explains [capability, configuration, practice and outcome](../../reference/research/04-implementation.md#capability-configuration-practice-and-outcome).

## What to remember

The tokenizer represents the question numerically. The model generates new identifiers and the application decodes them after the input. Local and remote source material have different setup boundaries.

## What this means for the business process

Record the model revision and the stage that failed. Assign loading and compatibility problems to technical support, and give the meeting owner a separate route to correct an unsupported assignment.

For the research behind this design choice, read [Six kinds of misfit](../../reference/research/04-implementation.md#six-kinds-of-misfit).

## Next lesson

You can now distinguish model operation from evidence quality. Next design who reviews the generated meeting record and how colleagues correct it. [Lesson 3.6: Design the meeting record and its correction process](06-design-lab.md).
