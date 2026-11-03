# Module 3: Open models and inference

[Previous module](02-conversation-and-tools.md) · [Guide index](../README.md) · [Next module](04-evaluation-and-code-generation.md)

## What you should be able to do

Describe the tokenizer–model–decoder sequence; explain tensors, devices and chat templates; trace the local probability visualizer; compare hosting arrangements; and design a meeting-notes pipeline that preserves evidence and uncertainty.

**Course walkthrough:** [day 1](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week3/day1.ipynb) introduces Colab; [day 2](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week3/day2.ipynb) links a pipelines lesson; [day 3](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week3/day3.ipynb) links tokenizers; [day 4](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week3/day4.ipynb) links models; [day 5](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week3/day5.ipynb) links the meeting-minutes project and invokes the local [visualizer](https://github.com/ed-donner/llm_engineering/blob/103f4bf045180f3b8b7721fd55b7897305a72672/week3/visualizer.py).

**External lesson unavailable:** Most substantive week 3 cells live in linked Colab notebooks. A remote notebook exposed only a sign-in link to the web reader. The walkthrough below distinguishes inspected local code from original teaching examples; it does not claim to reconstruct the exact remote lessons.

## 1. Concepts: from a hosted service to model components

A hosted API hides loading and hardware management. Running an open model makes those responsibilities visible. You obtain compatible weights and a tokenizer, prepare input tensors, select a device and precision, run generation, and decode output IDs.

“Open” needs precision: available weights, source code, training data transparency and permission to use commercially are separate questions. A model with downloadable weights is not automatically unrestricted. Inspect the particular model's licence and model card before choosing it for a client.

The main components are:

| Component | What it contributes | What it does not establish |
|---|---|---|
| Tokenizer | Maps text to IDs and back | Meaning or truth of the output |
| Model weights | Learned numerical parameters | Current access to organisational records |
| Configuration | Architecture and generation-related settings | Suitability for your operating problem |
| Runtime and device | Execute tensor operations | Privacy of surrounding logs and services |
| Prompt/template | Encodes the intended task and conversation | Guaranteed compliance with that intent |

A **tensor** is a multidimensional array. Token IDs for one prompt commonly have shape `[1, sequence_length]`: one batch element and a sequence of IDs. An **attention mask** indicates which positions should be treated as real input rather than padding. A **device** is the execution location, such as CPU or GPU; tensors and the relevant model operations must be compatible with that placement.

Parameter memory is only part of the resource requirement. Loading, intermediate activations and the attention key/value cache also occupy memory. A rough weight-only estimate is parameter count × bytes per parameter; it is a lower-bound planning aid, not a fit guarantee. Lower precision reduces storage, but hardware/runtime support and measured quality determine whether it is useful.

Base models continue text. Instruction-tuned models have additional training for instruction following. Chat-tuned models often require specific control tokens around roles and turns. The **chat template** converts structured messages into the sequence expected by that model; arbitrary role labels pasted into a string need not work equivalently. [Hugging Face chat-template documentation](https://huggingface.co/docs/transformers/en/chat_templating).

## 2. What the locally available code does

### The notebook's local entry point

Day 5 creates `TokenPredictor(model_name)`, calls `predict_tokens(message)`, builds a directed graph and draws it. This gives three separate responsibilities: obtaining predictions, constructing a graph representation, and rendering that representation.

### `TokenPredictor.predict_tokens`

The method requests streaming output with log probabilities and a small number of alternative next tokens. It loops over text-bearing chunks and reads the alternatives from the response object. `math.exp(logprob)` converts a natural-log probability to a probability.

For each observed token it stores a dictionary with the generated token, its probability and two alternatives. A list of these dictionaries becomes the output. A class instance holds the client and chosen model, while the method's local `predictions` list holds this particular run.

Read this visualisation carefully. It shows alternatives conditional on the prefix actually generated. It does not generate a full tree of alternative sentences, and it does not estimate the factual correctness of those sentences. A highly likely next token can continue a false claim.

The implementation assumes a close relationship between a streamed text delta and a token logprob entry. Treat that as an API-specific assumption to verify. A robust adapter would handle missing probabilities and a chunk containing multiple token entries explicitly. Likewise, the graph's labelled END node is a rendering convention, not evidence of a measured 100% end-of-sequence probability.

### `create_token_graph` and `visualize_predictions`

`nx.DiGraph()` creates a directed graph. Main-path nodes receive stable IDs such as `t0`; alternative nodes get suffixes. Edges connect a token's prefix to its main or alternative continuation. Display labels, colours and sizes live as node attributes.

The renderer then creates a position dictionary and draws nodes, edges and labels with matplotlib. This separation is useful beyond AI: you can change the display without changing the underlying prediction records.

## 3. Learn the inference pattern

**Enrichment: integration sketch, not a remote course cell.** It requires PyTorch, Transformers and an accessible compatible model. `model_id` is deliberately supplied by the caller; no model is downloaded by this guide.

```python
def generate_continuation(model_id, prompt):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    model.eval()
    inputs = tokenizer(prompt, return_tensors="pt")
    input_length = inputs["input_ids"].shape[1]
    with torch.no_grad():
        output = model.generate(
            **inputs, max_new_tokens=40, do_sample=False
        )
    continuation = output[0, input_length:]
    return tokenizer.decode(continuation, skip_special_tokens=True)
```

Read it in stages. The `Auto...` classes choose implementations from model metadata. The tokenizer returns a dictionary of tensors. `**inputs` expands that dictionary into named arguments. `model.eval()` selects evaluation behaviour; `torch.no_grad()` suppresses gradient recording. They serve different purposes. For a decoder-only model, slicing after the original input length removes the echoed prompt. This simple CPU sketch reloads everything per call; an application would usually load once and reuse the objects. See [Hugging Face generation guidance](https://huggingface.co/docs/transformers/en/llm_tutorial).

For a chat-tuned model, first apply its chat template rather than assuming this plain completion prompt is appropriate. For GPU inference, move inputs and model consistently or follow the serving runtime's device-placement scheme. `device_map="auto"` can distribute a model; it is not a universal substitute for understanding placement.

Patterns here include **factory loading**, **batch dimensions**, **explicit resource lifecycle**, **configuration-driven behaviour** and **separation of data/model/presentation**.

| Approach | Why choose it? | Main responsibility you retain |
|---|---|---|
| Hosted model API | Fast route to a capability | Data handling, task evaluation and provider integration |
| Transformers pipeline | Convenient task-level prototype | Choosing compatible components and inspecting defaults |
| Direct model/tokenizer use | Detailed control or experiments | Input formatting, memory, batching and generation settings |
| Local model server | Reusable service interface on controlled hardware | Capacity, access and runtime operations |
| Managed private endpoint | Dedicated deployment without owning all hardware operations | Configuration, isolation and end-to-end evaluation |

Local execution can reduce external transmission, but privacy depends on the entire pipeline. A local model with cloud transcription, external telemetry or shared logs is not a fully local system.

## 4. Business application: meeting notes as a chain of transformations

**Enrichment based on the lesson topic:** For Harbour's handoff meetings, a plausible workflow is audio → transcript → speaker/turn information → candidate decisions and actions → human-confirmed notes. The local lesson title establishes a meeting-minutes project; these design details are added here rather than attributed to unseen Colab cells.

Each stage loses or changes information. Transcription can mishear negation, names and numbers. Speaker attribution can confuse who accepted responsibility. Summarisation can turn “we could” into “we will”. Preserve transcript spans and timestamps behind important claims.

An action record needs more than a sentence: proposed owner, requested action, due date if stated, evidence span and confirmation status. Distinguish a participant's suggestion, an agreed decision and a formal authorisation. Models should not silently collapse these categories.

From an organisation design perspective, minutes help constitute the official account of a meeting. The ability to edit, challenge or approve them therefore matters. Decide who confirms commitments and how a dissenting interpretation remains visible.

Evaluate transcription and summarisation separately. A summary cannot fairly be blamed for every upstream transcription error, but the complete system remains responsible for the delivered record. Test names, cross-talk, uncertainty, objections and corrections, not just clean monologues.

## 5. Experiment, diagnose and reflect

**Exercise without audio or a GPU:** Write a synthetic transcript with one suggestion, one confirmed decision and one withdrawn action. Implement a deterministic extractor for explicit markers such as `DECISION:`. Compare that baseline with an LLM draft, if you later choose to run one. Require evidence spans and count false commitments.

**Technical extension:** Run a small approved model in an appropriate environment. Print input shape, generated shape and decoded continuation. Compare plain text and the model's chat template. Change one generation setting and record the effect without assuming that variability means quality.

**Common failures:** out-of-memory errors require examining model, context, batch and precision; nonsensical chat often points to formatting mismatch; repeated prompt text suggests output slicing; missing libraries or a fresh Colab runtime indicate environment state rather than conceptual failure.

**Check your understanding:** Why are tokenizer and model a pair? Why does `no_grad()` differ from `eval()`? What does a token probability tell you? Who has authority to confirm a meeting commitment?

**Answer cues:** IDs must match learned representations; gradient recording and evaluation behaviour differ; the probability concerns a token continuation, not a factual claim; confirmation belongs to the agreed accountable participants or process owner.

**Decision note:** Compare two deployment arrangements for meeting notes, including quality, data path, operating effort and the process for correcting records.
