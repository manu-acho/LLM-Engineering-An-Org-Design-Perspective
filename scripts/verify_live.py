"""Explicitly requested, bounded provider checks using fictional course data."""

import argparse
import json
from datetime import datetime, timezone

from ai_orgdesign.workspace import project_root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--confirm-live", action="store_true", help="Send paid API requests")
    parser.add_argument("--scenario", choices=["smoke", "capstone"], default="smoke")
    args = parser.parse_args()
    if not args.confirm_live:
        parser.error("No requests sent. Add --confirm-live to authorise this paid run.")
    from ai_orgdesign.provider import Gateway

    gateway = Gateway(max_requests=6, max_output_tokens=1000)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    folder = project_root() / "outputs" / f"live-check-{stamp}"
    folder.mkdir(parents=True)
    result = {"scenario": args.scenario, "model_requested": gateway.model}
    try:
        if args.scenario == "smoke":
            from ai_orgdesign.investigation import draft

            result["draft"] = draft(gateway)
            result["streamed_text"] = "".join(
                gateway.stream("Explain in two sentences why an order does not verify delivery.")
            )
        else:
            from ai_orgdesign.capstone import run_live

            result["capstone"] = run_live(gateway, folder / "service.db")
        result["execution"] = "completed; inspect answer quality separately"
    except Exception as error:
        # Raw provider error bodies may contain request data. Save only the type.
        result["execution"] = "failed"
        result["error_type"] = type(error).__name__
        raise
    finally:
        result["gateway_usage"] = gateway.ledger()
        (folder / "result.json").write_text(json.dumps(result, indent=2))
        print(f"Local fictional-case results: {folder / 'result.json'}")
        print("No live business outcome or general reliability claim follows from this check.")


if __name__ == "__main__":
    main()
