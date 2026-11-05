"""Compatibility entry point for the now fully instrumented model tool loop."""

from ai_orgdesign.agent_loop import investigate
from ai_orgdesign.provider import Gateway


def ask(question, tenant="north", *, consent=False, client=None, model=None):
    if not consent:
        raise ValueError("Enable the live exercise explicitly before sending a paid request")
    gateway = Gateway(model=model, client=client, max_requests=3, max_output_tokens=1000)
    result = investigate(gateway, question, tenant=tenant, max_rounds=3, max_tools=2)
    return {**result, "usage": gateway.ledger()}
