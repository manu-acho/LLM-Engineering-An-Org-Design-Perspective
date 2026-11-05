# Use the live models: setup, first request and troubleshooting

[Start here](../START-HERE.md) · [Glossary](glossary.md) · [Verification](verification.md)

Live exercises are a recommended part of the implementation route. They show actual generation, embeddings, tool proposals, specialist contributions and measured evaluation. The local examples remain useful for seeing arithmetic and control flow without a model obscuring them. Both routes contribute to understanding the service.

## Prepare the local configuration

Open the course folder in VS Code. The file `.env` holds configuration for this checkout. The dot is part of its filename. `.env.example` is a template intended for sharing; real credentials belong only in `.env`.

Add the following names, with a real key on the first line:

```text
OPENAI_API_KEY=replace-with-your-local-key
OPENAI_MODEL=gpt-6-luna
COURSE_LIVE_MODE=1
```

Save the file with Cmd+S on macOS or Ctrl+S on Windows/Linux. An unsaved editor buffer is not the on-disk configuration read by Python. Do not put a real key into a notebook or its output. The course setup preserves existing keys and keeps `.env` outside Git and the downloadable workspace.

An **API key** is a credential allowing the client to use a provider account. A **model token** is a unit of model input or output. They share a word but have different meanings. `COURSE_LIVE_MODE` is a local switch for the recommended live cells; it is not a provider credential or a spending limit.

The default model is GPT-6 Luna, with reasoning effort set to `none` in the course helper. Another supported model can be selected through `OPENAI_MODEL`, but settings, availability and results need checking. The earlier GPT-4.1 Mini development runs are retained as observations, not a recommendation to start a new project on a deprecated model. Check the [current model documentation](https://developers.openai.com/api/docs/models/gpt-6-luna) when setting up an account.

## Check the environment before paying for a request

From the course folder:

```sh
python3 scripts/setup.py
uv run --locked python scripts/check_environment.py
```

The first command installs the locked environment and notebook kernel, preserves credentials and adds missing blank settings. The second reports readiness and whether a key is present without printing its value. These commands do not send a model request.

Select the project's `.venv` kernel in the notebook. Restart that kernel after changing configuration, especially if a previous session loaded another value. Existing nonempty terminal environment variables take precedence over the local file. The setup cell displays whether live mode is enabled.

## Make the first request

The following is a complete small exercise:

```python
from ai_orgdesign.provider import Gateway

session = Gateway(max_requests=1, max_output_tokens=200)
result = session.generate(
    "An order records 12 boxes. The customer reports 10. "
    "State the difference and what remains unknown."
)
print(result.text)
print(result.record)
```

`Gateway` is a course helper around the official Python client. Creating a session stores settings; calling `generate` sends the request. The named arguments set an attempt ceiling and an output-token ceiling. The returned object keeps the generated text separate from the execution record. Its implementation is included in `src/ai_orgdesign/provider.py`.

Read the answer against the prompt. Twelve minus ten is two. Neither quantity establishes actual receipt. The model could still infer a cause or turn an order into a shipment record; the [worked experiments](worked-model-experiments.md) show an actual example of that failure.

## Understand the response record

| Field | Meaning |
|---|---|
| `model` | Model identity returned by the provider, which may identify a more specific snapshot than the requested alias |
| `response_id` | Provider identifier useful for correlating the request with an account record |
| `status` | Whether the provider reports completion or another outcome |
| `input_tokens` and `output_tokens` | Returned usage counts; missing usage stays unknown |
| `cached_input_tokens` / `reasoning_output_tokens` | Additional returned categories where supplied; missing values remain unknown |
| `elapsed_seconds` | Measured local request duration, including network waiting |

A completed response is an execution outcome. It does not certify factual support. A schema-conforming brief still passes through case, quantity, source and uncertainty checks. Those checks are deliberately narrow and do not prove every sentence in a free-text summary.

## Run the recommended lesson activities

Marked cells use the fictional data printed or included in the lesson. They execute when live mode is enabled. A notebook normally has a ceiling of twelve gateway attempts, each with at most one thousand output tokens. A framework comparison also uses its stated SDK turn limits and shows SDK usage separately. These are execution limits, not a guaranteed monetary cap.

Run the relevant cells once, inspect the result and then vary one condition. Restarting a session also resets its local request counter. Repeated `Run All` operations can therefore make additional paid requests. The ordinary notebook verifier forces live mode off even if the local `.env` enables it.

The CPU-model exercises have a separate `RUN_DOWNLOAD` switch. They fetch public weights at pinned revisions and run locally; they do not use the paid inference API. Model weights and trained adapters remain outside the public build.

## Estimate cost without inventing an invoice

Use the actual returned usage and rates appropriate to the model, endpoint and processing mode. For example, an explicitly assumed calculation is `input_tokens × input_rate / 1,000,000 + output_tokens × output_rate / 1,000,000`. Cached input, cache writes, regional processing and other usage categories can require different treatment. Embedding usage must use its own price basis.

The course records usage instead of silently filling missing values with zero. Its simple generation estimator uses the supplied rates; it is not the final bill. Check the [official pricing page](https://developers.openai.com/api/docs/pricing) and account usage before claiming an exact expense. A timeout can leave completion or billing uncertain even when no answer was received.

## Read an error as part of the experiment

A **traceback** identifies where Python encountered an exception. Start with its final line for the exception category, then inspect the relevant course line above it. Do not paste credentials or raw request headers into a diagnostic message.

| Result | What to investigate |
|---|---|
| Key missing | Confirm `.env`, exact variable name, saved file and selected kernel |
| Authentication failure | Check that the configured key belongs to the intended provider account |
| Model unavailable | Check `OPENAI_MODEL` and the account's model access |
| Quota or rate limit | Distinguish account allowance from request frequency; use the provider's guidance before retrying |
| Timeout | Keep the attempt and any available usage visible; do not assume the operation cost nothing |
| Incomplete output | Inspect the status and output limit; an empty prefix is not a finished answer |
| Refusal | Inspect the task and returned refusal rather than presenting it as a normal contribution |
| Invalid facts or source IDs | The application rejected the generated contribution; inspect the evidence, prompt and contract |
| Unexpected route | Check retrieval, policy applicability and label meaning before changing the model |

The helper makes no automatic retry. A deliberate retry uses another attempt and can produce a different answer. The [official error guide](https://developers.openai.com/api/docs/guides/error-codes) describes provider error categories; the course adds explanations of their consequences for the exercise.

## Move from answers to tools and services

A tool proposal is returned model content. Application code validates it, checks scope, executes a permitted function and sends the observation back. The [function-calling guide](https://developers.openai.com/api/docs/guides/function-calling) provides the authoritative protocol reference. The full course implementation exposes the actual observations rather than treating a model's completion story as evidence that a task happened.

Later exercises add structured outputs, retrieval, accepted specialist contributions, checkpoints, MCP and a local HTTP service. In every case, distinguish what the model proposed, what the application enforced, what a person accepted and what remains unknown about the business outcome.
