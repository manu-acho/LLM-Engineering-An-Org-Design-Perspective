"""Optional paid model tool loop. Never called by default notebooks or tests."""

import json
import os

from ai_orgdesign.business import dispatch
from ai_orgdesign.workspace import load_local_environment, require_api_key

TOOL = {
    "type": "function",
    "name": "lookup_case",
    "description": "Read a fictional delivery case in the caller's scope.",
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {"case_id": {"type": "string"}},
        "required": ["case_id"],
        "additionalProperties": False,
    },
}


def ask(question, tenant="north", *, consent=False, client=None, model=None):
    if not consent:
        raise ValueError("Explicit consent required for a potentially paid network call")
    if client is None:
        from openai import OpenAI

        load_local_environment()
        model = model or os.environ.get("OPENAI_MODEL", "").strip()
        if not model:
            raise ValueError("Set OPENAI_MODEL to a supported model available to the account")
        client = OpenAI(api_key=require_api_key("OPENAI_API_KEY"), timeout=20, max_retries=0)
    if not model:
        raise ValueError("Explicit model required")
    history = [{"role": "user", "content": question}]
    calls_used = 0
    for _ in range(3):
        response = client.responses.create(
            model=model,
            input=history,
            instructions="Investigate fictional delivery records. Do not authorise a remedy. Preserve uncertainty.",
            tools=[TOOL],
            parallel_tool_calls=False,
            max_output_tokens=300,
            store=False,
        )
        calls = [item for item in response.output if item.type == "function_call"]
        history.extend(response.output)
        if not calls:
            return {"text": response.output_text, "tool_calls": calls_used}
        for call in calls:
            if calls_used >= 2:
                raise RuntimeError("Tool budget exhausted")
            arguments = json.loads(call.arguments)
            if not isinstance(arguments, dict):
                raise ValueError("Tool arguments must be an object")
            value = dispatch(call.name, arguments, tenant)
            history.append(
                {
                    "type": "function_call_output",
                    "call_id": call.call_id,
                    "output": json.dumps(value),
                }
            )
            calls_used += 1
    raise RuntimeError("Model round budget exhausted")
