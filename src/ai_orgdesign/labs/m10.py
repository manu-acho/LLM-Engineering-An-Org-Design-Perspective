"""Typed specialist results and explicit acceptance conditions."""

from pydantic import BaseModel, ConfigDict, Field


class Contribution(BaseModel):
    model_config = ConfigDict(extra="forbid")
    case_id: str
    sources: list[str] = Field(min_length=1)
    conclusion: str
    unresolved: list[str] = Field(min_length=1)


def accept(payload, expected_case="H-17", allowed_sources=None):
    result = Contribution.model_validate(payload)
    allowed_sources = {"order-17", "customer-17"} if allowed_sources is None else allowed_sources
    if result.case_id != expected_case or not set(result.sources) <= allowed_sources:
        raise ValueError("Wrong case or unsupported source")
    return {"state": "accepted_for_review", **result.model_dump()}


def demo():
    return accept(
        {
            "case_id": "H-17",
            "sources": ["order-17", "customer-17"],
            "conclusion": "Quantities disagree",
            "unresolved": ["actual receipt"],
        }
    )
