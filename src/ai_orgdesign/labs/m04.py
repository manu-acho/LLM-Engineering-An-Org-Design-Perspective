"""Task evaluation with explicit denominators and rejection costs."""


def score(truth, predictions, false_approval_cost=20):
    if not truth or len(truth) != len(predictions):
        raise ValueError("Paired nonempty records required")
    labels = {"review", "clear"}
    if not set(truth + predictions) <= labels:
        raise ValueError("Unknown outcome label")
    correct = sum(t == p for t, p in zip(truth, predictions))
    unsafe = sum(t == "review" and p == "clear" for t, p in zip(truth, predictions))
    unnecessary = sum(t == "clear" and p == "review" for t, p in zip(truth, predictions))
    return {
        "n": len(truth),
        "accuracy": correct / len(truth),
        "unsafe_clearances": unsafe,
        "unnecessary_reviews": unnecessary,
        "illustrative_loss": unsafe * false_approval_cost + unnecessary,
    }


def demo():
    truth = ["review", "review", "clear", "clear"]
    return {
        "always_clear": score(truth, ["clear"] * 4),
        "conservative": score(truth, ["review", "review", "review", "clear"]),
        "boundary": "Fictional cases and chosen costs, not measured business benefit",
    }
