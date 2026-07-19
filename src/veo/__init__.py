"""veo — a local-first tool for applying the veo-framework verification protocol.

Implements FRAMEWORK.md §6: a concrete, runnable separation of
routine output / verified emergence / hallucination, instead of a static
"take it with a grain of salt" disclaimer.

This is methodology-with-teeth: log reflective exchanges durably, run the
cross-session recurrence check, and run the deterministic hallucination
comparator. No network, no API key, no dependencies beyond the Python
standard library.
"""

from .store import ExchangeStore, Exchange, Observation, status_from_counts
from .similarity import (
    tokenize,
    jaccard,
    similarity,
    SIMILARITY_THRESHOLD,
)
from .recurrence import RecurrenceChecker, RecurrenceResult
from .factcheck import FactCheck, factcheck
from .comparator import Comparator, ComparatorResult
from .cli import main

__all__ = [
    "ExchangeStore",
    "Exchange",
    "Observation",
    "status_from_counts",
    "tokenize",
    "jaccard",
    "similarity",
    "SIMILARITY_THRESHOLD",
    "RecurrenceChecker",
    "RecurrenceResult",
    "FactCheck",
    "factcheck",
    "Comparator",
    "ComparatorResult",
    "main",
]
