# Lesson 3.1: What changes when you run a model yourself?

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## What you'll learn and why it matters

Identify what a hosted service handles and what Harbour would need to handle to run a model itself. This makes the hosting choice a question of capability and support as well as computing.

With a hosted model, the application sends a request to a service that runs the model elsewhere. To run a model locally, the computer needs a way to turn text into numbers, the learned numbers that define the model, and software to carry out the calculations. The lesson calls these the tokenizer, weights and runtime. Follow the same short input through each before comparing computer memory requirements.

## From a service request to visible components

A hosted model service hides much of the machinery. You send a request and receive a response. Someone else loads the model, operates the computing equipment and handles some capacity problems. Running a model yourself makes those responsibilities visible.

For Harbour's meeting-note application, the distinction is practical. A founder might prefer local processing for control over sensitive discussion. The choice also requires checking the entire audio, transcription, generation and storage path. A local text model does not make cloud transcription local.

## Weights, tokenizer and runtime

**Weights** are learned numerical parameters. A model's architecture specifies how operations connect; the weights specify learned values used in those operations. A saved model is not simply a document of facts. Its parameters support distributed learned behaviour.

Consider a much smaller calculation: a programme that takes a quantity and doubles it. The instruction to multiply specifies the operation; the number two is a value used in the operation. This is an analogy for the difference between a model's design and its weights. In a language model there are many operations and learned values. The tokenizer first represents the input as identifiers, and the runtime carries out those operations. Loading the weights supplies the values; it does not itself answer a question.

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

## What to remember

Local inference needs a tokenizer, learned weights, software to run the operations and suitable hardware. Those parts have to work together before a model can answer.

## What this means for the business process

Before choosing local hosting, name who owns model updates, compatibility checks and recovery when the machine cannot run the model. Include those continuing responsibilities in the comparison with hosted service.

For the research behind this design choice, read [Implementation extends beyond launch](../../reference/research/04-implementation.md#implementation-extends-beyond-launch).

## Next lesson

Next encode and decode a tiny example by hand so you can identify what the tokenizer and model would each supply in a real run. [Lesson 3.2: Encode, generate, decode](02-code-workshop.md).
