"""TF-IDF retrieval fitted only on permitted active records."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ai_orgdesign.business import DOCUMENTS


def retrieve(query, tenant="north", k=2, documents=None):
    if not query.strip() or type(k) is not int or k < 1:
        raise ValueError("Nonempty query and positive integer k required")
    allowed = [
        dict(d)
        for d in (DOCUMENTS if documents is None else documents)
        if d["tenant"] == tenant and d["active"]
    ]
    if not allowed:
        return []
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform([d["text"] for d in allowed])
    scores = cosine_similarity(vectorizer.transform([query]), matrix)[0]
    ranked = sorted(zip(allowed, scores), key=lambda pair: (-pair[1], pair[0]["id"]))
    return [{**doc, "score": float(score)} for doc, score in ranked[:k] if score > 0]


def grounded_context(hits):
    return "\n".join(f"[{d['id']} v{d['version']}] {d['text']}" for d in hits)


def demo():
    hits = retrieve("delivery evidence")
    return {
        "hits": hits,
        "context": grounded_context(hits),
        "answer": "No generated answer: evidence context only",
    }
