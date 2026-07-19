"""Durable storage of reflective exchanges and their extracted observations.

An *observation* is one reflective claim pulled out of a session — e.g.
"this line of questioning tends to produce X". It starts life as a
**candidate** and only earns a stronger status through one of the two
independent checks in FRAMEWORK.md §6:

  1. cross-session recurrence (a pattern, seen again in a different session)
  2. mechanical fact-checking (a checkable claim, verified against a source)

Storage is a single JSONL file so the recurrence check can be run across
sessions over time. No database, no network.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Observation:
    """One reflective claim extracted from a session.

    ``times_seen`` counts how many *distinct* sessions it has recurred in
    (including the originating one). ``verified`` is set by a mechanical
    fact-check. ``status`` is derived (see ``status_from_counts``).
    """

    id: str
    text: str
    session_id: str
    kind: str = "pattern"  # "pattern" or "fact"
    created_at: str = field(default_factory=_now)
    times_seen: int = 1
    verified: bool = False
    source: Optional[str] = None  # for fact-kind: the canonical source text

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Observation":
        return cls(
            id=d["id"],
            text=d["text"],
            session_id=d["session_id"],
            kind=d.get("kind", "pattern"),
            created_at=d.get("created_at", _now()),
            times_seen=d.get("times_seen", 1),
            verified=bool(d.get("verified", False)),
            source=d.get("source"),
        )


@dataclass
class Exchange:
    """A logged reflective session: raw turns plus extracted observations."""

    session_id: str
    turns: list[dict] = field(default_factory=list)
    observations: list[Observation] = field(default_factory=list)
    created_at: str = field(default_factory=_now)

    def to_dict(self) -> dict:
        return {
            "session_id": self.session_id,
            "created_at": self.created_at,
            "turns": self.turns,
            "observations": [o.to_dict() for o in self.observations],
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Exchange":
        return cls(
            session_id=d["session_id"],
            turns=d.get("turns", []),
            observations=[Observation.from_dict(o) for o in d.get("observations", [])],
            created_at=d.get("created_at", _now()),
        )


# Status vocabulary — mirrors FRAMEWORK.md §6's three-plus-one states.
CANDIDATE = "candidate"
VERIFIED = "verified"
UNVERIFIABLE = "unverifiable"
HALLUCINATION = "hallucination"


def status_from_counts(times_seen: int, verified: bool, kind: str) -> str:
    """Derive an observation's status from its checks.

    - fact + verified                          -> verified
    - fact + not verified                      -> unverifiable
    - pattern + recurred in >= 2 distinct ses -> verified
    - pattern + recurred fewer than that       -> candidate
    """
    if kind == "fact":
        return VERIFIED if verified else UNVERIFIABLE
    # pattern
    return VERIFIED if times_seen >= 2 else CANDIDATE


# REPEAT_THRESHOLD enforces FRAMEWORK.md §6.1: "promote to verified once it
# has recurred ... more than once" — i.e. at least two distinct sessions.
REPEAT_THRESHOLD = 2


class ExchangeStore:
    """Append-only JSONL store of exchanges, one JSON object per line."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def add(self, exchange: Exchange) -> None:
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(exchange.to_dict(), ensure_ascii=False) + "\n")

    def all(self) -> list[Exchange]:
        if not self.path.exists():
            return []
        out: list[Exchange] = []
        with self.path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(Exchange.from_dict(json.loads(line)))
                except json.JSONDecodeError:
                    # Skip corrupt lines rather than crash the whole run.
                    continue
        return out

    def sessions_with_observation(self, text: str, min_sim: float) -> list[str]:
        """Return the set of session ids whose observations are similar to ``text``."""
        from .similarity import similarity

        sessions: set[str] = set()
        for ex in self.all():
            for o in ex.observations:
                if similarity(o.text, text) >= min_sim:
                    sessions.add(ex.session_id)
        return sorted(sessions)

    def merge_recurrence(self, text: str, min_sim: float) -> int:
        """Fold all similar observations into the most recent one.

        Returns the new ``times_seen`` for that observation. Used to keep a
        running recurrence count as new sessions come in.
        """
        sessions = self.sessions_with_observation(text, min_sim)
        if not sessions:
            return 1
        # Bump the existing observation that best matches.
        best: Observation | None = None
        best_sim = -1.0
        for ex in self.all():
            for o in ex.observations:
                s = similarity(o.text, text)
                if s >= min_sim and s > best_sim:
                    best, best_sim = o, s
        if best is not None:
            best.times_seen = len(sessions)
        return len(sessions)
