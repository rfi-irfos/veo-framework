"""Lightweight text similarity — dependency-free.

Used by the recurrence check (FRAMEWORK.md §6.1) to decide whether two
observations are "the same pattern". We deliberately use a transparent,
reproducible Jaccard-over-character-shingles metric rather than an opaque
embedding model: the bar for "the same pattern" is fixed and stated, and
anyone can recompute it by hand.
"""

from __future__ import annotations

import re
from typing import Iterable

# FRAMEWORK.md §6.1: "Set a real bar for 'the same pattern' — semantic
# similarity above a fixed, stated threshold, checked the same way every
# time." This is that fixed, stated threshold.
SIMILARITY_THRESHOLD = 0.5

_STOP = {
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "for",
    "with", "is", "are", "was", "were", "be", "this", "that", "it", "as",
    "at", "by", "from", "we", "you", "i", "my", "your", "not", "no", "do",
    "does", "did", "so", "if", "into", "than", "then", "they", "their",
    "what", "which", "who", "how", "why", "when", "more", "most", "some",
    "can", "could", "should", "would", "will", "may", "might", "about",
    "around", "one", "two", "three",
}


def tokenize(text: str, shingle: int = 3) -> set[str]:
    """Stopword-filtered word tokens (primary) plus character shingles.

    Word tokens carry most of the semantic weight; character shingles only
    add a little robustness to small spelling/wording drift. The same
    ``shingle`` length must be used every time the comparator runs — that
    is part of "checked the same way every time".
    """
    text = (text or "").lower()
    words = [w for w in re.findall(r"[a-z0-9]+", text) if w not in _STOP]
    chars = re.sub(r"[^a-z0-9]+", "", text)

    toks: set[str] = set(words)
    if len(chars) >= shingle:
        for i in range(len(chars) - shingle + 1):
            toks.add("~" + chars[i : i + shingle])  # prefix keeps shingles distinct from words
    return toks


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = a & b
    union = a | b
    # Word tokens (no '~' prefix) are weighted 3x over character shingles
    # so semantic overlap dominates the score, not incidental letter n-grams.
    w_inter = sum(3 if not t.startswith("~") else 1 for t in inter)
    w_union = sum(3 if not t.startswith("~") else 1 for t in union)
    return w_inter / w_union


def containment(a: set[str], b: set[str]) -> float:
    """Fraction of ``a``'s tokens that are also in ``b`` (a ⊆ b style).

    Useful when comparing a short claim against a long source: we want to
    know how much of the claim is *contained* in the source, not how much
    of the source the claim covers (which Jaccard would unfairly penalise).
    """
    if not a:
        return 0.0
    inter = a & b
    w_inter = sum(3 if not t.startswith("~") else 1 for t in inter)
    w_a = sum(3 if not t.startswith("~") else 1 for t in a)
    return w_inter / w_a


def similarity(a: str, b: str, shingle: int = 3) -> float:
    """Symmetric similarity in [0, 1] between two observation texts.

    Uses the max of Jaccard and containment so that (a) two similarly-sized
    near-paraphrases score high (Jaccard), and (b) a short claim fully
    contained in a longer source also scores high (containment).
    """
    ta, tb = tokenize(a, shingle), tokenize(b, shingle)
    return max(jaccard(ta, tb), containment(ta, tb))
