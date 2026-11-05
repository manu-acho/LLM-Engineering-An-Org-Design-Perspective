"""A harness records bounded execution, instruction identity and assumed costs."""

import math
import time

from ai_orgdesign.business import fingerprint
from ai_orgdesign.labs.m09 import run, scripted_planner


def estimate_cost(input_tokens, output_tokens, input_per_million, output_per_million):
    values = [input_tokens, output_tokens, input_per_million, output_per_million]
    if any(
        type(value) not in (int, float) or not math.isfinite(value) or value < 0 for value in values
    ):
        raise ValueError("Usage and prices must be nonnegative")
    return (input_tokens * input_per_million + output_tokens * output_per_million) / 1_000_000


def harness(planner=scripted_planner):
    instructions = "Prepare evidence; never authorise a remedy."
    started = time.perf_counter()
    result = run(planner, budget=2)
    return {
        "run_id": "teaching-run",
        "instruction_hash": fingerprint(instructions),
        "elapsed_seconds": time.perf_counter() - started,
        "tool_calls": len(result["observations"]),
        "stop": result["stop"],
        "provider_usage": None,
        "sensitive_text_logged": False,
    }


def demo():
    return {
        "trace": harness(),
        "illustrative_cost": estimate_cost(1000, 200, 1, 4),
        "price_basis": "Chosen numbers for arithmetic, not provider prices or billed usage",
    }
