# Lesson 7.1: What fine-tuning changes, and what it cannot settle

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## What you'll learn and why it matters

Compare changing the prompt, supplying better evidence and adapting the model through training. Harbour needs to match the intervention to the cause of the failure.

Harbour can show the model one example of a good brief in each request, find the current policy for that request, or train it further on examples of the desired brief. Fine-tuning is the third option: it changes learned values in the model or adds trainable values used alongside it. First diagnose whether the failure is a missing fact or a repeated behaviour before choosing what to change.

## When a repeated behaviour remains weak

Harbour has clarified a stable set of request categories. A general model still confuses two categories despite clear instructions and sufficient evidence. The team has representative, reviewed examples. This is a plausible reason to investigate fine-tuning, further training intended to adapt behaviour.

It is not evidence that fine-tuning will help. Compare it with simpler interventions and preserve an independent evaluation set. The decision is about a remaining, measured failure, not enthusiasm for training a proprietary model.

## Prompting, retrieval and fine-tuning

Prompting changes instructions or examples supplied at inference time. Retrieval changes which evidence is supplied. Fine-tuning changes learned parameters in the model or an attached adaptation.

Three failures suggest different repairs. If the brief has the right facts but omits the requested headings, try making the instruction clearer. If it uses an expired rule, fix which policy is supplied. If the desired writing behaviour remains unreliable across many correctly supplied examples, further training may be worth comparing. In all three cases, reuse the same test cases so the comparison shows which failure changed.

If the current credit threshold changes every month, retrieval or a business tool usually gives a clearer evidence/update route than trying to encode each value in parameters. If the model repeatedly struggles to apply a stable classification scheme, adaptation may be worth testing. These are diagnostic tendencies, not universal rules.

## Full updates and smaller updates

**Full fine-tuning** updates the model's existing parameters. Large models can require substantial memory for weights, training intermediates, gradients and optimizer state. Memory is therefore not simply the size of the downloaded file.

**Parameter-efficient fine-tuning**, or PEFT, adjusts a smaller parameter set. A common method is **LoRA**, low-rank adaptation. It adds a constrained update to selected model transformations while the original weights can remain frozen.

To understand the idea without prior matrix algebra, imagine a layer as a table of numerical relationships between inputs and outputs. A four-by-four table contains sixteen entries. A restricted update can be represented through two smaller tables, four-by-one and one-by-four, containing eight entries in total. Multiplying the smaller tables produces a four-by-four update, but not every possible update can be expressed at that size.

The restriction reduces trainable parameters. It also limits the form of adaptation. The **rank** controls part of that capacity. This miniature count illustrates the mechanism; it is not a memory estimate for a real model. The [LoRA reference](https://huggingface.co/docs/peft/en/package_reference/lora) gives the technical configuration.

## Why QLoRA includes quantization

**QLoRA** combines adaptation with a frozen base represented using reduced precision. The original method uses four-bit NormalFloat, double quantization and paged optimizers to reduce memory requirements. The low-rank adapters remain trainable. See the [QLoRA paper](https://arxiv.org/abs/2305.14314).

This does not mean the model becomes universally cheap to train or that every numerical operation uses four bits. Hardware support, sequence lengths, batch size and implementation still matter. The important conceptual separation is between the stored base, the added trainable update and the computations used during training.

## What the model is taught to predict

A supervised language-model example can contain a **prompt** and a desired **completion**. For the price task, the prompt ends with `Price is $`, and the completion supplies the expected number. During inference, the answer must not already be included.

Training generally asks the model to predict target tokens. If you want to supervise only the completion, prompt positions can be excluded from the loss while remaining available as input. This is **loss masking**. An **attention mask**, introduced in Module 3, instead marks usable input versus padding positions. The two answer different questions.

The distinction is crucial: “do not grade the model on reproducing the question” is not the same as “prevent the model from reading the question”.

## Settings and artifacts

Learning rate controls the scale of updates. Batch size controls how many examples contribute to a step or accumulated update. Epoch count controls passes through the data. These settings influence learning and overfitting; copying a notebook value does not justify it for another task.

The output artifact may be an adapter rather than a complete standalone model. To use it later, retain the compatible base, tokenizer, prompt/template and configuration. An adapter trained against one base revision should not be assumed compatible with another just because their names look similar.

The local week 7 notebooks refer to remote training lessons whose cells were unavailable during authoring. The new explanation teaches the mechanism using inspected local preparation/serving code and identified technical references; it does not claim to reproduce unseen training instructions.

**Check:** Explain why a lower training loss does not settle whether Harbour's routing improved. A strong answer distinguishes the token objective from the operational target, training cases from new cases, and successful imitation from a legitimate category definition.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Model specialisation cannot by itself settle whether its categories suit the work. The research chapter explains [fit and misfit](../../reference/research/04-implementation.md#six-kinds-of-misfit).

## What to remember

Prompting changes instructions at use time. Retrieval changes the evidence available. Fine-tuning changes learned values in the model or an attached adaptation.

## What this means for the business process

Diagnose the failure before funding training. An obsolete policy calls for a source fix. A recurring failure to follow a well-specified format on correctly supplied cases may warrant comparing an adaptation with a simpler prompt change.

For the research behind this design choice, read [Six kinds of misfit](../../reference/research/04-implementation.md#six-kinds-of-misfit).

## Next lesson

Next look at the training record itself. You will separate the answer used in training from the input supplied when asking the model to predict. [Lesson 7.2: Prepare the answer without leaking it into the question](02-code-workshop.md).
