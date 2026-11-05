"""Conversation state, validated tools and streaming without a provider."""

import json

from ai_orgdesign.business import dispatch


def conversation(case_id="H-17", tenant="north"):
    history = [{"role": "user", "content": f"Inspect {case_id}"}]
    call = {"id": "call-1", "name": "lookup_case", "arguments": {"case_id": case_id}}
    # This call is scripted, not inferred by a model. The same dispatcher validates either.
    result = dispatch(call["name"], call["arguments"], tenant)
    history.append({"role": "tool", "call_id": call["id"], "content": json.dumps(result)})
    return {"history": history, "case": result, "state": {"selected_case": case_id}}


def stream_words(text):
    for word in text.split():
        yield word + " "


def demo():
    result = conversation()
    result["stream"] = list(stream_words("Evidence awaits review"))
    return result
