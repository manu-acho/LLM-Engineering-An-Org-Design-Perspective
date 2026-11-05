"""Reproducible classification baseline with train-only text preprocessing."""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

TRAIN = [
    ("invoice tax", "finance"),
    ("billing invoice", "finance"),
    ("payment tax", "finance"),
    ("delivery missing", "operations"),
    ("shipment delay", "operations"),
    ("delivery damaged", "operations"),
]
TEST = [
    ("invoice payment", "finance"),
    ("delivery delay", "operations"),
    ("shipment damaged", "operations"),
]


def fit_baseline():
    pipeline = make_pipeline(CountVectorizer(), LogisticRegression(random_state=7))
    pipeline.fit([row[0] for row in TRAIN], [row[1] for row in TRAIN])
    return pipeline


def demo():
    model = fit_baseline()
    predicted = model.predict([row[0] for row in TEST]).tolist()
    return {
        "predicted": predicted,
        "accuracy": accuracy_score([row[1] for row in TEST], predicted),
        "test_n": len(TEST),
        "classes": model.classes_.tolist(),
        "boundary": "A tiny invented split tests mechanics, not deployment generalisation",
    }
