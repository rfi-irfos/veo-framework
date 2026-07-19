"""Deterministic hallucination comparator (FRAMEWORK.md §6 — the comparator).

The second independent check. Every reflective claim is checked against a
reproducible baseline: when the *same* interaction is re-run under a plain,
non-reflective prompt — deterministically, with the flattering frame removed —
does the model produce the same structure, or does the "insight" evaporate?

If the claim appears only inside the reflective register and not under the
comparator, it is flagged as HALLUCINATION, not emergence.

This tool does not call a model. It compares two *captured* outputs — the
reflective transcript and the comparator run — and reports whether the
claimed structure survives. You capture both runs yourself (e.g. by saving
the model's plain-prompt output to a file); the tool tells you whether the
claim is present in both, in only the reflective one, or in neither.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .similarity import similarity, SIMILARITY_THRESHOLD
from .store import CANDIDATE, VERIFIED, HALLUCINATION, UNVERIFIABLE


@dataclass
class ComparatorResult:
    claim: str
    in_reflective: bool
    in_comparator: bool
    verdict: str  # VERIFIED / HALLUCINATION / CANDIDATE / UNVERIFIABLE
    reflective_score: float
    comparator_score: float

    def to_dict(self) -> dict:
        return {
            "claim": self.claim,
            "in_reflective": self.in_reflective,
            "in_comparator": self.in_comparator,
            "verdict": self.verdict,
            "reflective_score": round(self.reflective_score, 4),
            "comparator_score": round(self.comparator_score, 4),
        }


class Comparator:
    def __init__(self, threshold: float = SIMILARITY_THRESHOLD):
        self.threshold = threshold

    def evaluate(
        self, claim: str, reflective_text: str, comparator_text: str
    ) -> ComparatorResult:
        """Classify a claimed insight against the two captured runs.

        - present in BOTH            -> VERIFIED (survives the comparator)
        - present ONLY in reflective  -> HALLUCINATION (evaporates without the
                                         flattering frame)
        - present ONLY in comparator  -> CANDIDATE (not a reflective find)
        - in NEITHER                -> UNVERIFIABLE
        """
        r_score = similarity(claim, reflective_text)
        c_score = similarity(claim, comparator_text)
        in_r = r_score >= self.threshold
        in_c = c_score >= self.threshold

        if in_r and in_c:
            verdict = VERIFIED
        elif in_r and not in_c:
            verdict = HALLUCINATION
        elif in_c and not in_r:
            verdict = CANDIDATE
        else:
            verdict = UNVERIFIABLE

        return ComparatorResult(
            claim=claim,
            in_reflective=in_r,
            in_comparator=in_c,
            verdict=verdict,
            reflective_score=r_score,
            comparator_score=c_score,
        )
