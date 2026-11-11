# Lesson 1.4: From a probability to a service response

[Module route](README.md) · [Next: follow the full pipeline](05-source-walkthrough.md)

## What you'll learn and why it matters

Trace a model request across preparation, generation and response handling. Learn to tell which failures come from the service exchange and which come from the claims in the answer.

When a model suggests the next piece of text, several pieces could fit. A probability gives each possible piece a share of the chance of being selected under the model's calculation. Follow one choice, add it to the text and see how it affects the next choice. Then follow the same reply through the application that presents it.

## What is being selected?

Suppose a toy model gives three possible next tokens these probabilities: `confirmed` 0.6, `reported` 0.3 and `disputed` 0.1. These numbers concern continuations of a particular input. They are not a confidence assessment of the delivery evidence.

**Greedy decoding** selects the highest-scoring token, here `confirmed`. **Sampling** draws from the distribution, so another token can be selected. The next distribution is then calculated using the selected token as part of the input. Early choices affect later wording. A language model is therefore generating a sequence, not selecting one prewritten answer from a menu.

**Temperature** can change how concentrated the sampling distribution is. Lower values generally concentrate it; higher values spread it. A particular model or API may not expose that setting. Even a deterministic-looking setting does not turn a generation system into a source-verification procedure. Keep the input evidence and evaluation cases fixed when investigating settings.

**Top-p sampling** limits selection to a set whose cumulative probability reaches a specified threshold. In our invented distribution, a threshold of 0.8 requires the first two candidates, whose probabilities total 0.9. This is a selection rule, not an instruction to be 80% factually correct. Token limits are different again: they bound generation length and can cut off a response.

## A request crosses several boundaries

An API is an agreed interface through which programs request operations. HTTP is a request/response communication protocol often used to reach that interface. JSON is a text representation of structured values. These names describe different parts of the same interaction.

```text
Python dictionaries → request serialization → network service
→ model execution → response data → Python object → displayed answer
```

Authentication establishes the calling account. It does not verify the delivery complaint. A successful HTTP response says the service handled the request at that level; the generated answer still needs checking. A timeout leaves uncertainty about whether the remote service processed the request. Retrying a read-only model call can incur a second charge even when no business record changes.

## Read a response before extracting its text

A response may contain identifiers, output items, usage counts and a termination reason. The display string is only one part. When an answer appears incomplete, inspect whether generation stopped because of a length limit rather than rewriting the prompt immediately. When nothing is displayed, distinguish a refusal, non-text output, extraction error and failed request.

The original course uses Chat Completions response access. New examples may use Responses. Preserve the interface distinction: `choices[0].message.content` and `output_text` belong to different response objects. An adapter can hide this difference from the rest of an application.

## A small experiment with a clear interpretation

Use a fictional complaint with two established quantities and one disputed explanation. Prepare five identical requests under each supported generation setting. Record whether each answer preserves “customer reports”, invents a cause, retains the order ID and finishes completely. Compare claim-level behaviour, not just how varied the wording sounds.

If all ten outputs invent a warehouse failure, investigate the question and evidence before choosing a temperature. If only some outputs omit a qualification, keep the failure cases and test an explicit output structure. The experiment can support a limited statement about those cases; it cannot establish a universal reliability rate.

**Worked check:** Would lowering temperature resolve two contradictory source records? No. It changes selection behaviour. The application still needs a rule for representing disagreement and a person or process that can resolve the underlying issue.

**Further reading:** [OpenAI text generation](https://developers.openai.com/api/docs/guides/text), alongside the pinned source in the next lesson. Settings must be checked for the selected model.

## Read the organisational connection

Generating a response and verifying a business fact are different operations. The research chapter explains [distinct acts in a workflow](../../reference/research/03-decisions.md#distinct-acts-in-one-workflow).

## What to remember

Next-token probabilities guide text selection. The service response also carries information about how the request ended. Extracting text alone can hide an incomplete run.

## What this means for the business process

Keep the completion status with the draft and show when an adviser needs to check or repeat the request. Assess the claims against evidence separately from whether the service returned a usable response.

For the research behind this design choice, read [An evidence path without skipped steps](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).

## Next lesson

Next follow a real example from Ed Donner's course, starting where the summariser obtains its evidence and prepares a request. [Lesson 1.5: Walk the original summariser and multi-page builder](05-source-walkthrough.md).
