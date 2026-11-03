# Module 7: Open-model fine-tuning and QLoRA

[Previous module](06-data-baselines-and-adaptation.md) · [Guide index](../README.md) · [Next module](08-agents-and-operations.md)

## What you should be able to do

Explain full fine-tuning, LoRA and QLoRA; trace prompt/completion preparation; distinguish loss masking from attention masking; understand the train–save–reload lifecycle; and specify a specialisation experiment with credible comparison criteria.

**Course walkthrough:** [day 1](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week7/day1.ipynb), [day 2](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week7/day2.ipynb), [days 3–4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week7/day3%20and%204.ipynb), [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week7/day5.ipynb), the week-specific [Item implementation](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week7/pricer/items.py), and [evaluation utility](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week7/util.py). A later [deployment implementation](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/pricer_service2.py) demonstrates loading the base model and trained adapter.

**External lesson unavailable:** Day 1 and days 3–5 rely on Colab links. The training link could not be read through the web reader and remained on a loading screen in the browser. The training explanation below is enrichment based on the local preparation/serving code and primary technical references, not a claim about the inaccessible training cells or their exact settings.

## 1. Concepts: what gets trained?

**Full fine-tuning** updates a model's existing parameters for a task. It requires resources not only for weights but also for gradients and optimizer state.

**Parameter-efficient fine-tuning (PEFT)** updates a smaller set of added or selected parameters. In **LoRA**, a layer's weight update is expressed using two low-rank matrices. For a weight matrix `W` with dimensions `d_out × d_in`, write an adapted transformation as `Wx + sBAx`, where `A` has shape `r × d_in`, `B` has shape `d_out × r`, and `r` is relatively small. The added parameter count is `r(d_in + d_out)` rather than `d_in × d_out`. The scale `s` depends on the adapter configuration. This reduces the trainable parameter footprint without promising equal quality for every task. [PEFT LoRA reference](https://huggingface.co/docs/peft/en/package_reference/lora).

**QLoRA** combines a frozen quantized base model with trainable low-rank adapters. The original method includes 4-bit NormalFloat, double quantization and paged optimizers. Quantized storage does not mean that every operation or trainable parameter uses four bits. The point is to reduce memory requirements while still learning a useful adaptation. [QLoRA paper](https://arxiv.org/abs/2305.14314).

Rank controls adapter capacity and parameter count. Learning rate controls update size. Batch size controls how many examples contribute per optimizer update; gradient accumulation can combine several smaller steps before an update. Epochs count passes through the training data. None should be selected solely because a notebook used a particular value.

Fine-tuning can improve repeated task behaviour, formatting or domain-specific distinctions. It is not the natural first tool for injecting frequently changing facts, enforcing permissions or resolving disputed label definitions. Those require evidence and application design.

## 2. What the available code does

### Day 2: construct a stable prompt/completion contract

The notebook loads train, validation and test items, loads a tokenizer for its base model, counts summary tokens and inspects the truncation distribution. `CUTOFF = 110` is a chosen experiment parameter, not a universally suitable length.

The **week 7** `pricer/items.py` adds methods not present in the simpler week 6 version:

- `count_tokens` encodes the summary without added special tokens.
- `make_prompts` truncates the summary at a token budget and constructs a prompt ending in `Price is $`.
- It stores the expected numeric answer separately in `completion`.
- `count_prompt_tokens` measures prompt plus completion.
- `to_datapoint` returns a two-field dictionary suitable for a dataset.
- `push_prompts_to_hub` serialises split-specific prompt/completion records.

Training and validation completions are rounded to whole dollars and formatted with `.00`; test completions retain the original price string. This is a meaningful target/evaluation choice: training encourages a rounded answer while test error can still be measured against original prices.

The prompt does not contain the answer when passed to generation. During training, the completion supplies the supervised target. Mixing these two roles leaks the answer into an evaluation request.

There is also a split naming distinction. `Item.from_hub` expects `validation` for the earlier item dataset, whereas `push_prompts_to_hub` writes `val` for prompt datasets. Inspect dataset keys at the boundary rather than assuming all dataset revisions use identical names.

Week-specific imports matter. `from pricer.items import Item` can resolve to a different file depending on the working directory and Python import path. When a method seems missing, inspect `pricer.items.__file__` and restart the kernel if an earlier module remains cached.

### Evaluation utility: compare numeric predictions consistently

`util.Tester` accepts a predictor, iterates over prompt/completion records, parses predictions and compares them with `float(datapoint['completion'])`. It plots absolute error and predicted-versus-actual values.

This differs from week 6's evaluator, which takes `Item` objects. Passing the wrong representation to a helper is an interface mismatch. Do not patch symptoms before checking what each function expects.

The regex parser again converts unparseable outputs to zero. For a serious experiment, distinguish invalid output from a valid numeric estimate and report both coverage and error among valid predictions.

### Later serving code: reconstruct a trained system

`week8/pricer_service2.py` defines a 4-bit configuration, loads the tokenizer and base model, and attaches an adapter using `PeftModel.from_pretrained`. The adapter revision is pinned. A usable artifact is therefore more than an adapter file: it includes the compatible base model, tokenizer, prompt format, configuration and output interpretation.

The serving method constructs the same question/prefix pattern, tokenizes, generates a few tokens without gradients, decodes and parses a number. This exposes how a train/serve mismatch could appear: changed prompt wording, missing prefix, different tokenizer or an incompatible adapter/base pair.

## 3. Understand the training sequence

**Enrichment: lifecycle sketch, not executable code or a remote notebook transcription:**

```text
freeze data splits and baseline
→ load compatible base model and tokenizer
→ prepare quantized model for adaptation
→ attach configured adapters
→ encode prompt/completion examples
→ check labels, padding and loss mask
→ train on training split; select using validation split
→ save adapter, tokenizer and experiment manifest
→ reload into a fresh process
→ evaluate against the frozen baseline and holdout
```

PEFT's preparation step accounts for details needed when adapting quantized models; do not assume that an inference-only quantized load is ready for training. [PEFT quantization guidance](https://huggingface.co/docs/peft/en/developer_guides/quantization).

**Loss masking** specifies which target tokens contribute to the loss. For completion-only training, prompt positions are ignored in the target labels. The model can still attend to that prompt. An attention mask instead indicates usable/padded input positions. Confusing the two can remove information or train the wrong objective.

**Teaching example: dependency-free illustration of labels, using already tokenized IDs:**

```python
def completion_labels(input_ids, prompt_length):
    if not 0 <= prompt_length <= len(input_ids):
        raise ValueError("Invalid prompt boundary")
    return [-100] * prompt_length + input_ids[prompt_length:]

ids = [11, 12, 13, 21, 22]
labels = completion_labels(ids, prompt_length=3)
# [-100, -100, -100, 21, 22]
```

`-100` is the conventional ignore label in many PyTorch language-model training losses. In real tokenization, separately encoding prompt and completion may not give a safe concatenation boundary; use the trainer's supported dataset/masking path and inspect actual batches. Causal language-model implementations typically shift token targets internally. Do not manually shift them a second time without checking the loss implementation. [TRL supervised fine-tuning documentation](https://huggingface.co/docs/trl/en/sft_trainer).

The **data collator** converts examples into batches, including padding and labels. The trainer coordinates updates and evaluation. These abstractions remove boilerplate, but you still need to inspect a batch to establish that the intended supervision reaches the loss.

## 4. Patterns and alternatives

| Pattern | Why it matters | Alternative |
|---|---|---|
| Prompt/completion contract | Makes task supervision explicit | Chat-formatted examples for a compatible chat model |
| Frozen base plus adapter | Separates shared capability from task-specific changes | Full fine-tuning when justified and feasible |
| Token-budget preparation | Controls sequence cost and truncation | Section-aware compression or shorter task inputs |
| Validation-based selection | Keeps test evidence separate from tuning | Cross-validation where dataset size and task permit |
| Versioned artifact manifest | Allows compatible reload and rollback | A single bundled export, still with provenance |
| Fresh-process reload check | Finds hidden dependence on notebook state | A clean serving-environment smoke check |

Before adaptation, compare a better prompt, retrieval, a stronger task-appropriate model and a simpler classifier/regressor. Fine-tuning is useful only if it improves the chosen outcome enough to justify annotation, training, serving and maintenance.

A model can lower language-model loss while failing to improve the business metric. Training predicts tokens; the application needs a correct classification, price or structured record. Evaluate both the training signal and the actual task.

## 5. Business application and organisation design

For Harbour, consider a stable taxonomy of request types after the discovery work has clarified categories. Fine-tuning might help distinguish recurring ambiguous request patterns. It should not decide policy ownership simply because the historic team assignments are easy to learn.

Specify who defines labels, adjudicates disagreement and approves taxonomy changes. A new category or process redesign can invalidate the old training distribution. Plan how evidence of drift reaches those owners and how revised labels become a new model version.

For research coding, a model trained on your coding scheme can assist with consistent application. Agreement with your past labels is not independent evidence that the scheme is theoretically valid. Preserve disagreements and novel cases rather than forcing every passage into existing categories.

## 6. Experiment, diagnose and reflect

**Exercise without a GPU:** Create five prompt/completion pairs for a synthetic stable task. Check that test prompts contain no answers, specify token budgets, and identify examples where truncation removes decisive information. Write a dataset manifest with split names and label definitions.

**Optional training experiment:** In a suitable environment, use a small dataset and fixed baseline, then compare validation-selected adaptation with the baseline on the same untouched holdout. Record invalid outputs, per-category failures, inference effort and reload success. Do not choose hyperparameters using the final test set.

**Common failures:** incompatible tokenizer/base/adapter; all labels ignored; target truncated away; validation split name mismatch; prompt echo mistaken for output; a method missing because Python imported week 6's helper; good loss paired with weak operational results.

**Check your understanding:** Which weights does LoRA change? How do attention and loss masks differ? Why reload in a fresh process? When should RAG precede fine-tuning?

**Answer cues:** added low-rank adapter weights in the usual frozen-base setup; accessible input versus supervised target positions; it exposes hidden state and compatibility gaps; changing factual knowledge often belongs in retrieval.

**Decision note:** Define the remaining baseline failure, the stable behaviour you want to teach, annotation ownership, comparison metrics, resource budget and stop criteria.
