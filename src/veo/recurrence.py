"""Cross-session recurrence check (FRAMEWORK.md §6.1).

A reflective observation is a *candidate*, not a finding, until the same
pattern shows up again, *independently*, in a separate, later conversation —
not merely repeated within one exchange. (A model agreeing with its own
earlier framing later in the same session is not independent confirmation.)
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Iterable

from .similarity import similarity, SIMILARITY_THRESHOLD
from .store import (
    ExchangeStore,
    Observation,
    REPEAT_THRESHOLD,
    status_from_counts,
    CANDIDATE,
    VERIFIED,
)


@dataclass
class RecurrenceResult:
    observation_id: str
    text: str
    sessions_seen: list[str]
    times_seen: int
    status: str  # CANDIDATE or VERIFIED
    threshold: int = REPEAT_THRESHOLD

    def to_dict(self) -> dict:
        return {
            "observation_id": self.observation_id,
            "text": self.text,
            "sessions_seen": self.sessions_seen,
            "times_seen": self.times_seen,
            "status": self.status,
            "threshold": self.threshold,
        }


class RecurrenceChecker:
    def __init__(self, store: ExchangeStore, min_sim: float = SIMILARITY_THRESHOLD):
        self.store = store
        self.min_sim = min_sim

    def check(self, observation: Observation) -> RecurrenceResult:
        # Recurrence is computed live from the store, not from a persisted
        # counter — the store is append-only, so we re-derive the distinct
        # session count every time rather than trusting a mutated field.
        sessions = self.store.sessions_with_observation(observation.text, self.min_sim)
        times = max(observation.times_seen, len(sessions))
        status = status_from_counts(times, observation.verified, observation.kind)
        return RecurrenceResult(
            observation_id=observation.id,
            text=observation.text,
            sessions_seen=sessions,
            times_seen=times,
            status=status,
        )

    def check_all(self) -> list[RecurrenceResult]:
        # Dedup by similarity so recurrence markers (same text, new session)
        # collapse into one reported result.
        kept: list[Observation] = []
        for ex in self.store.all():
            for o in ex.observations:
                if any(similarity(o.text, k.text) >= self.min_sim for k in kept):
                    continue
                kept.append(o)
        return [self.check(o) for o in kept]

    def promote(self, text: str, session_id: str | None = None) -> RecurrenceResult:
        """Record a new observation (or add a recurrence marker for an existing
        similar one) and return its recurrence status.

        Write path used by the logger. If a similar observation already exists
        in the store, we still log this session as a *recurrence marker* — a
        fresh observation with the same text but the new session id — so the
        distinct-session count is accurate (the whole point of FRAMEWORK.md
        §6.1 is that recurrence must be measured *across separate sessions*).
        ``check_all`` then dedupes them by similarity when reporting status.
        """
        sid = session_id or "unknown"
        existing = self.store.sessions_with_observation(text, self.min_sim)
        # Always log this session. If a similar observation exists, this entry
        # acts as the recurrence marker; otherwise it is the first candidate.
        oid = uuid.uuid4().hex[:12]
        new_obs = Observation(
            id=oid,
            text=text,
            session_id=sid,
            kind="pattern",
            times_seen=1,
        )
        ex = Exchange(session_id=sid)
        ex.observations.append(new_obs)
        self.store.add(ex)
        # Report status from the best-matching observation across the store.
        best: Observation | None = None
        best_sim = -1.0
        for e in self.store.all():
            for o in e.observations:
                s = similarity(o.text, text)
                if s >= self.min_sim and s > best_sim:
                    best, best_sim = o, s
        return self.check(best if best is not None else new_obs)


# local import kept at bottom to avoid a circular import at module load
from .store import Exchange  # noqa: E402
