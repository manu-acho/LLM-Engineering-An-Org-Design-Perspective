# Lesson 7.2: Prepare the answer without leaking it into the question

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

## What you'll learn and why it matters

Separate the question supplied at use time from the answer supplied during training. Trace which pieces count towards loss so Harbour can tell what behaviour the training rewards.

A training example can contain a question and the answer the model is supposed to learn to give. When the system later asks for an answer, it supplies only the question. In the workshop, follow which pieces are used as context and which pieces the training calculation counts when it judges a prediction.

[Open the companion workshop notebook](../../notebooks/07-specialisation.ipynb).

## A training record has two roles

The course prepares product-price examples. To keep the mechanism visible, our teaching example uses a synthetic category target instead. We will create prompt/completion records and then illustrate loss labels using invented token IDs. No model is trained.

```python
def make_example(description, category):
    return {
        "prompt": "Classify this request:\n" + description + "\nCategory: ",
        "completion": category,
    }

example = make_example("Warehouse recount needed", "operations")
inference_prompt = example["prompt"]
training_text = example["prompt"] + example["completion"]
```

`example` stores the question and target separately. A training pipeline may combine them to compute a prediction objective. An inference request should receive the prompt without the answer. If you evaluate by supplying `training_text`, a model could appear correct simply because the target is visible.

The literal string `Category: ` is part of the contract. Change it unexpectedly between training and serving and you change the input pattern the adapted model sees.

## Illustrate loss masking

```python
def labels_for_completion(input_ids, prompt_length):
    if not 0 <= prompt_length <= len(input_ids):
        raise ValueError("Prompt boundary is outside the sequence")
    return [-100] * prompt_length + input_ids[prompt_length:]

input_ids = [10, 11, 12, 20, 21]
labels = labels_for_completion(input_ids, prompt_length=3)
```

The first three invented IDs represent prompt tokens; the final two represent completion tokens. `[-100] * 3` repeats the ignore marker three times. The slice retains target IDs after the prompt boundary. The result is `[-100, -100, -100, 20, 21]`.

Many relevant training losses use `-100` to mark ignored target positions. The input still contains all five IDs. The model can use prompt information while the training objective grades completion positions. This example explains one convention; a real trainer must use the convention its loss expects.

Do not calculate boundaries casually by separately encoding text pieces. A tokenizer can treat joined text differently at a boundary. Use a supported preparation/collation path and inspect the actual batch. A **collator** takes examples and constructs batched arrays, often including padding, attention masks and target labels. See [TRL's supervised fine-tuning documentation](https://huggingface.co/docs/trl/en/sft_trainer).

## Trace the actual local preparation

Open [week7/pricer/items.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week7/pricer/items.py). `count_tokens` encodes the summary. `make_prompts` limits its length, creates a prompt ending with the fixed price prefix and stores a completion. Training/validation examples can use rounded targets; test examples retain an original price representation.

`to_datapoint` converts an object into a two-field dictionary. `push_prompts_to_hub` packages records into dataset splits. The split called `val` there differs from the earlier item dataset's `validation`. Reading the actual keys avoids a misleading “dataset missing” diagnosis.

The week 6 and week 7 folders both contain a package named `pricer`, with different `Item` definitions. Python imports the one found through its current import path and may keep it cached. If a method seems absent, inspect the imported module's file and restart the notebook kernel if needed. A changed class file is not automatically re-imported into an existing process.

## Saving is not the end of the experiment

A training run may save an adapter. The later [pricer_service2.py](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week8/pricer_service2.py) loads a base model and tokenizer, attaches a pinned adapter and reconstructs the price prompt before generation.

The service illustrates a compatibility contract across preparation, training and inference. Retain model IDs and revisions, tokenizer/template, preprocessing, target format and parser. Test reloading in a fresh process so that hidden notebook state cannot supply missing configuration.

A successful save only establishes that files were written. A successful reload establishes more about compatibility. A successful held-out task evaluation is a further step. Keep those claims separate.

## Alternatives and practice

Prompt examples can sometimes establish the desired format without training. A deterministic classifier may suit explicit categories. Retrieval can supply policy facts. Adapt only when comparison shows that the remaining problem justifies it.

Create one ambiguous request and two defensible category interpretations. Then write the rule that would resolve it. If you cannot state that rule or identify an adjudicator, identify the organisational uncertainty before generating more training examples.

**What the example shows:** More examples of inconsistent labels can teach inconsistency. The programming pipeline can validate fields and still carry a conceptually unresolved target. Label validity belongs alongside code correctness in the experiment design.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

The separation of question and answer determines which evidence is legitimately available at prediction time. The research chapter explains [decision premises](../../reference/research/03-decisions.md#decision-premises).

## What to remember

The training example contains a prompt and a completion. The inference prompt leaves out the answer. Loss masking can exclude prompt positions from the training score.

## What this means for the business process

Ask the routing or drafting owner to inspect representative completions before training. A wrong boundary can change what the model learns, while a wrong target can teach behaviour Harbour did not intend.

For the research behind this design choice, read [Select controls for the work that can actually be assessed](../../reference/research/08-governance-and-accountability.md#select-controls-for-the-work-that-can-actually-be-assessed).

## Next lesson

Next examine who can question the categories that an adaptation has learned, even when its saved state is sound. [Lesson 7.3: A specialised model still needs people to question its categories](03-business-and-organisation.md).
