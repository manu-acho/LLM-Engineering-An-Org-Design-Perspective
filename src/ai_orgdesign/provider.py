"""Inspectable OpenAI calls for fictional course exercises.

No request is made on import. Offline tests inject a transport or a gateway.
"""

import json
import math
import os
import threading
import time
from dataclasses import asdict, dataclass

from ai_orgdesign.workspace import load_local_environment, require_api_key


class ModelRunError(RuntimeError):
    """A model response is unavailable, incomplete, refused or unusable."""


@dataclass
class RunRecord:
    operation: str
    model: str
    response_id: str | None
    status: str
    input_tokens: int | None
    output_tokens: int | None
    elapsed_seconds: float
    cached_input_tokens: int | None = None
    reasoning_output_tokens: int | None = None


@dataclass
class TextResult:
    text: str
    record: RunRecord
    value: dict | None = None


class Gateway:
    """A short-lived exercise session with request and output limits.

    max_requests counts attempts, including failed requests. The usage ledger
    records observed usage, not a claim about the final provider invoice.
    """

    def __init__(self, model=None, *, client=None, max_requests=12, max_output_tokens=1000):
        load_local_environment()
        self.model = model or os.environ.get("OPENAI_MODEL") or "gpt-6-luna"
        if type(max_requests) is not int or max_requests < 1:
            raise ValueError("max_requests must be a positive integer")
        if type(max_output_tokens) is not int or max_output_tokens < 1:
            raise ValueError("max_output_tokens must be a positive integer")
        self.max_requests = max_requests
        self.max_output_tokens = max_output_tokens
        self.attempts = 0
        self.records: list[RunRecord] = []
        self._lock = threading.Lock()
        if client is None:
            from openai import OpenAI

            client = OpenAI(api_key=require_api_key("OPENAI_API_KEY"), timeout=45, max_retries=0)
        self.client = client

    def _reserve(self):
        with self._lock:
            if self.attempts >= self.max_requests:
                raise ModelRunError(
                    "Exercise request limit reached. Inspect the ledger before starting another session."
                )
            self.attempts += 1

    def _record(self, response, operation, elapsed):
        usage = getattr(response, "usage", None)
        record = RunRecord(
            operation,
            getattr(response, "model", self.model),
            getattr(response, "id", None),
            getattr(response, "status", "unknown"),
            getattr(usage, "input_tokens", None),
            getattr(usage, "output_tokens", None),
            elapsed,
        )
        record.cached_input_tokens = getattr(
            getattr(usage, "input_tokens_details", None), "cached_tokens", None
        )
        record.reasoning_output_tokens = getattr(
            getattr(usage, "output_tokens_details", None), "reasoning_tokens", None
        )
        with self._lock:
            self.records.append(record)
        return record

    def request(self, messages, *, instructions, tools=None, schema=None, operation="generate"):
        self._reserve()
        kwargs = dict(
            model=self.model,
            input=messages,
            instructions=instructions,
            store=False,
            max_output_tokens=self.max_output_tokens,
        )
        if self.model.startswith("gpt-6"):
            kwargs["reasoning"] = {"effort": "none"}
        if tools:
            kwargs.update(tools=tools, parallel_tool_calls=False)
        if schema:
            kwargs["text"] = {
                "format": {
                    "type": "json_schema",
                    "name": "course_result",
                    "strict": True,
                    "schema": schema,
                }
            }
        started = time.perf_counter()
        try:
            response = self.client.responses.create(**kwargs)
        except Exception as error:
            # Do not echo a raw HTTP body, headers or credential-bearing exception.
            name = type(error).__name__
            with self._lock:
                self.records.append(
                    RunRecord(
                        operation,
                        self.model,
                        getattr(error, "request_id", None),
                        "api_error:" + name,
                        None,
                        None,
                        time.perf_counter() - started,
                    )
                )
            hints = {
                "AuthenticationError": "Check OPENAI_API_KEY in the local .env.",
                "RateLimitError": "Check account quota and retry after the provider's indicated delay.",
                "NotFoundError": "Check OPENAI_MODEL and account access.",
                "APITimeoutError": "The request timed out; inspect usage before retrying.",
                "BadRequestError": "Check model support and the request schema.",
            }
            raise ModelRunError(
                f"{name}: {hints.get(name, 'Inspect the request settings and provider status. No automatic retry was made.')}"
            ) from None
        record = self._record(response, operation, time.perf_counter() - started)
        if record.status != "completed":
            raise ModelRunError(
                f"Response status was {record.status}; no completed answer was accepted. Usage remains in gateway.records."
            )
        for item in response.output:
            for part in getattr(item, "content", []):
                if getattr(part, "type", "") == "refusal":
                    raise ModelRunError(
                        "The model refused this request; inspect the task rather than treating it as an answer."
                    )
        return response, record

    def generate(
        self,
        prompt,
        *,
        instructions="Use supplied evidence; preserve uncertainty.",
        schema=None,
        messages=None,
    ):
        messages = [*(messages or []), {"role": "user", "content": prompt}]
        response, record = self.request(messages, instructions=instructions, schema=schema)
        text = response.output_text
        if not text or not text.strip():
            raise ModelRunError("The completed response contained no answer text.")
        value = None
        if schema:
            try:
                value = json.loads(text)
            except json.JSONDecodeError:
                raise ModelRunError("The response was not usable JSON.") from None
        return TextResult(text, record, value)

    def stream(self, prompt):
        """Yield text deltas; validate the terminal response before marking completion."""
        self._reserve()
        started = time.perf_counter()
        terminal = None
        try:
            settings = {"reasoning": {"effort": "none"}} if self.model.startswith("gpt-6") else {}
            stream = self.client.responses.create(
                model=self.model,
                input=prompt,
                store=False,
                max_output_tokens=self.max_output_tokens,
                stream=True,
                **settings,
            )
            try:
                for event in stream:
                    if event.type == "response.output_text.delta":
                        yield event.delta
                    elif event.type in {
                        "response.completed",
                        "response.incomplete",
                        "response.failed",
                    }:
                        terminal = event.response
                    elif event.type == "error":
                        raise ModelRunError(
                            "Provider reported a stream error; partial text is not a completed answer."
                        )
            finally:
                stream.close()
        except ModelRunError:
            raise
        except Exception:
            raise ModelRunError(
                "Stream interrupted. Retain the partial-result status and inspect before retrying."
            ) from None
        if terminal is None:
            raise ModelRunError("Stream ended without a completion record.")
        record = self._record(terminal, "stream", time.perf_counter() - started)
        if record.status != "completed" or not terminal.output_text.strip():
            raise ModelRunError("Stream did not produce a completed nonempty answer.")

    def embed(self, texts, model="text-embedding-3-small"):
        if not texts or any(not isinstance(t, str) or not t.strip() for t in texts):
            raise ValueError("Supply a nonempty list of nonempty texts")
        self._reserve()
        started = time.perf_counter()
        response = self.client.embeddings.create(model=model, input=texts)
        rows = sorted(response.data, key=lambda row: row.index)
        if [row.index for row in rows] != list(range(len(texts))):
            raise ModelRunError("Embedding response did not match the submitted inputs")
        dimensions = {len(row.embedding) for row in rows}
        if (
            len(dimensions) != 1
            or not next(iter(dimensions))
            or not all(math.isfinite(value) for row in rows for value in row.embedding)
        ):
            raise ModelRunError("Invalid embedding dimensions or values")
        with self._lock:
            self.records.append(
                RunRecord(
                    "embed",
                    model,
                    None,
                    "completed",
                    response.usage.prompt_tokens,
                    0,
                    time.perf_counter() - started,
                )
            )
        return [row.embedding for row in rows]

    def ledger(self):
        return [asdict(record) for record in self.records]


def estimated_cost(records, input_per_million, output_per_million):
    for value in [input_per_million, output_per_million]:
        if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
            raise ValueError("Prices must be finite nonnegative numbers")
    if any(
        record.input_tokens is None or record.output_tokens is None or record.operation == "embed"
        for record in records
    ):
        raise ValueError(
            "A complete generation-only usage ledger is required; price embedding usage separately"
        )
    return (
        sum(
            record.input_tokens * input_per_million + record.output_tokens * output_per_million
            for record in records
        )
        / 1_000_000
    )
