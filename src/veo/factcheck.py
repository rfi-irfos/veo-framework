"""Mechanical fact-checking (FRAMEWORK.md §6.2).

If a reflective exchange makes a claim that references something outside the
model's own opinion — a fact, a prior statement, a tool result, a date —
check it directly against the source. Never hand it to a second model call
and ask it to guess whether the first one was honest.

This module does the *comparison* only and never fabricates a check for you:
you supply the canonical ``source`` text (a tool result, a quoted prior
statement, a date from a record). The tool reports whether the claim is
present in that source. A claim whose check you cannot mechanically run is
marked UNVERIFIABLE — a real, distinct, honest answer, not a quiet
"probably fine".
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

from .similarity import similarity, SIMILARITY_THRESHOLD
from .store import Observation, VERIFIED, UNVERIFIABLE, status_from_counts


@dataclass
class FactCheck:
    observation_id: str
    text: str
    source: Optional[str]
    present: bool
    status: str  # VERIFIED or UNVERIFIABLE
    score: float = 0.0

    def to_dict(self) -> dict:
        return {
            "observation_id": self.observation_id,
            "text": self.text,
            "source": self.source,
            "present": self.present,
            "status": self.status,
            "score": round(self.score, 4),
        }


def factcheck(obs: Observation, source: Optional[str]) -> FactCheck:
    """Verify a fact-kind observation against a supplied canonical source.

    If no source is supplied (the claim can't be mechanically checked), the
    observation is marked UNVERIFIABLE rather than silently passed.
    """
    if obs.kind != "fact":
        raise ValueError("factcheck only applies to kind='fact' observations")

    if not source or not source.strip():
        return FactCheck(
            observation_id=obs.id,
            text=obs.text,
            source=source,
            present=False,
            status=UNVERIFIABLE,
            score=0.0,
        )

    score = similarity(obs.text, source)
    present = score >= SIMILARITY_THRESHOLD
    status = VERIFIED if present else UNVERIFIABLE
    # Keep the observation's verified flag in sync for downstream status.
    obs.verified = present
    obs.source = source
    return FactCheck(
        observation_id=obs.id,
        text=obs.text,
        source=source,
        present=present,
        status=status,
        score=score,
    )
