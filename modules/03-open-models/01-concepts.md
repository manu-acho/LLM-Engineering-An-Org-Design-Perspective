# Lesson 3.1: What changes when you run a model yourself?

[Download the matching notebook](/downloads/03-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## From a service request to visible components

A hosted model service hides much of the machinery. You send a request and receive a response. Someone else loads the model, operates the computing equipment and handles some capacity problems. Running a model yourself makes those responsibilities visible.

For Harbour's meeting-note application, the distinction is practical. A founder might prefer local processing for control over sensitive discussion. The choice also requires checking the entire audio, transcription, generation and storage path. A local text model does not make cloud transcription local.

## Weights, tokenizer and runtime

**Weights** are learned numerical parameters. A model's architecture specifies how operations connect; the weights specify learned values used in those operations. A saved model is not simply a document of facts. Its parameters support distributed learned behaviour.

A **tokenizer** turns text into token IDs and back. Those IDs must match the model's learned vocabulary. The numerical ID 42 means whatever that tokenizer assigns to it; a different tokenizer can assign 42 to another unit. This is why the tokenizer is not an interchangeable cosmetic accessory.

A **runtime** executes the model's operations. Libraries such as Transformers provide code to load compatible components and request generation. A **pipeline**, in the library sense, can bundle preparation, inference and output conversion for a task. This is a particular implementation of the more general pipeline idea introduced earlier.

## Devices and memory

A CPU is a general-purpose processor. A GPU is designed to perform many suitable numerical operations in parallel. Some model computations benefit greatly from GPUs, but a particular model must still fit the available memory and use supported software.

A **tensor** is a numerical array with dimensions. A single list of token IDs might have 20 positions. A batch of three equally sized sequences can be represented with dimensions `[3, 20]`. A dimension says how the values are arranged; it is not another name for a token.

Sequences often have different lengths. **Padding** adds placeholder positions so they can be processed in a rectangular batch. An **attention mask** marks which positions are genuine input and which are padding. The mask prevents the placeholder from being treated like ordinary task evidence in the relevant operations.

Memory holds more than weights: intermediate values and stored information used during generation occupy space too. A model fitting at a short prompt does not prove that a much longer prompt or larger batch will fit. “Number of parameters” is therefore only one resource indicator.

## Precision and quantization

A stored number can use more or fewer bits. Fewer bits can reduce memory consumption but represent values less precisely. **Quantization** uses a reduced-precision representation for selected numerical values. It can make deployment practical, but the quality and speed consequences depend on the model, hardware and implementation.

Do not interpret a four-bit model as a program in which every calculation occurs at four-bit precision. Storage formats, computation formats and added trainable parameters can differ. Module 7 returns to this distinction when explaining QLoRA.

## Base, instruction and chat models

A base language model learns to continue text. An instruction-tuned model has additional training intended to help it respond to instructions. A chat model expects turns encoded in a particular format. These are distinctions of training and interface, not guarantees that one model will solve your task.

A **chat template** inserts the model-specific markers for roles and turn boundaries. A dictionary containing a system message must eventually become a token sequence. Using the wrong markers can make a well-written request ineffective. The [official chat-template guide](https://huggingface.co/docs/transformers/en/chat_templating) explains this interface boundary.

## What does “open” buy you?

Available weights can allow different hosting and adaptation arrangements. They do not automatically supply unrestricted licensing, training-data transparency, application security or operational capability. Ask separately what is available, what use is permitted and what you are capable of operating.

Self-hosting may be appropriate for control or specialised requirements. A hosted service may be appropriate when it meets the data and performance requirements and operating a model would add unnecessary work. Neither follows from a universal rule that one form is always cheaper, safer or more capable.

**Explain it back:** A colleague says, “We downloaded the model, so the meeting-notes system is private and ready.” Identify the missing questions. Your answer should include licensing, the full data path, hardware/runtime compatibility, task quality, storage and access, rather than discussing weights alone.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Running the model locally creates continuing maintenance and support work. The research chapter explains [implementation beyond launch](../../reference/research/04-implementation.md#implementation-extends-beyond-launch).

## Practical activity: Estimate weight storage separately from context and other runtime memory.





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

How many decimal megabytes do these illustrative FP32 weights occupy?

```python
parameters = 135_000_000
bytes_per_parameter = 4
weight_bytes = parameters * bytes_per_parameter
print("Illustrative FP32 weight MB:", weight_bytes / 1_000_000)
assert weight_bytes == 540_000_000
```

540 MB for weights alone. Actual checkpoint precision, activations, caches and runtime overhead change the memory requirement.

### Complete the exercise

Write the prediction before consulting the worked answer: How many decimal megabytes do these illustrative FP32 weights occupy?

**Worked answer.** 540 MB for weights alone. Actual checkpoint precision, activations, caches and runtime overhead change the memory requirement.

The notebook includes a place for an independent attempt. The solution is labelled separately. A successful assertion checks its stated example; it does not grade the whole business design. Complete the module's organisational case with a named recipient, acceptance conditions, authority, correction and a comparison with another arrangement.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
