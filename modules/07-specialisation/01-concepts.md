# Lesson 7.1: What fine-tuning changes, and what it cannot settle

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## When a repeated behaviour remains weak

Harbour has clarified a stable set of request categories. A general model still confuses two categories despite clear instructions and sufficient evidence. The team has representative, reviewed examples. This is a plausible reason to investigate fine-tuning, further training intended to adapt behaviour.

It is not evidence that fine-tuning will help. Compare it with simpler interventions and preserve an independent evaluation set. The decision is about a remaining, measured failure, not enthusiasm for training a proprietary model.

## Prompting, retrieval and fine-tuning

Prompting changes instructions or examples supplied at inference time. Retrieval changes which evidence is supplied. Fine-tuning changes learned parameters in the model or an attached adaptation.

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
