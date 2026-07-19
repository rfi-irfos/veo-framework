"""Tests for the veo verification protocol tool.

Run with:  pytest -q   (from repo root, after `pip install -e .`)
All tests use a temp store, so they never touch the user's real corpus.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from veo.store import (
    ExchangeStore,
    Exchange,
    Observation,
    status_from_counts,
    CANDIDATE,
    VERIFIED,
    UNVERIFIABLE,
    HALLUCINATION,
    REPEAT_THRESHOLD,
)
from veo.similarity import tokenize, jaccard, similarity, SIMILARITY_THRESHOLD
from veo.recurrence import RecurrenceChecker
from veo.factcheck import factcheck
from veo.comparator import Comparator

DATA = Path(__file__).parent / "data"


@pytest.fixture
def store(tmp_path):
    return ExchangeStore(tmp_path / "ex.jsonl")


# ---- similarity ---------------------------------------------------------

def test_tokenize_lowercases_and_filters_stopwords():
    toks = tokenize("This line of questioning produces clarity")
    assert "this" not in toks
    assert "produces" in toks
    assert any(len(t) == 4 and t.startswith("~") for t in toks)  # prefixed char shingles present


def test_jaccard_identical_is_one():
    a = {"x", "y", "z"}
    assert jaccard(a, a) == 1.0


def test_jaccard_disjoint_is_zero():
    assert jaccard({"a"}, {"b"}) == 0.0


def test_similarity_near_paraphrase_above_threshold():
    s = similarity(
        "this line of questioning tends to produce a sense of what the caller wants",
        "this line of questioning tends to surface what the caller actually wants",
    )
    assert s >= SIMILARITY_THRESHOLD


def test_similarity_unrelated_is_low():
    assert similarity("the sky is blue", "a database index speeds lookups") < 0.2


# ---- status derivation ---------------------------------------------------

def test_status_pattern_single_session_is_candidate():
    assert status_from_counts(1, False, "pattern") == CANDIDATE


def test_status_pattern_two_sessions_is_verified():
    assert status_from_counts(REPEAT_THRESHOLD, False, "pattern") == VERIFIED


def test_status_fact_verified_when_checked():
    assert status_from_counts(1, True, "fact") == VERIFIED


def test_status_fact_unchecked_is_unverifiable():
    assert status_from_counts(1, False, "fact") == UNVERIFIABLE


# ---- store --------------------------------------------------------------

def test_store_roundtrip(tmp_path):
    s = ExchangeStore(tmp_path / "r.jsonl")
    ex = Exchange(session_id="s1", observations=[Observation(id="o1", text="x", session_id="s1")])
    s.add(ex)
    loaded = s.all()
    assert len(loaded) == 1
    assert loaded[0].observations[0].text == "x"


def test_store_skips_corrupt_lines(tmp_path):
    p = tmp_path / "c.jsonl"
    p.write_text('{"session_id":"a"}\nNOT JSON\n{"session_id":"b"}\n', encoding="utf-8")
    s = ExchangeStore(p)
    assert len(s.all()) == 2


def test_sessions_with_observation_finds_similar(store):
    store.add(Exchange(session_id="s1", observations=[
        Observation(id="o1", text="this line of questioning tends to produce clarity", session_id="s1")
    ]))
    found = store.sessions_with_observation(
        "this line of questioning tends to surface clarity", SIMILARITY_THRESHOLD
    )
    assert "s1" in found


# ---- recurrence ---------------------------------------------------------

def test_recurrence_promotes_after_two_sessions(store):
    checker = RecurrenceChecker(store)
    r1 = checker.promote("this line of questioning tends to produce clarity", session_id="s1")
    assert r1.status == CANDIDATE
    r2 = checker.promote("this line of questioning tends to surface clarity", session_id="s2")
    assert r2.status == VERIFIED
    assert r2.times_seen >= REPEAT_THRESHOLD


def test_recurrence_check_all_dedupes(store):
    checker = RecurrenceChecker(store)
    checker.promote("alpha pattern of interest", session_id="s1")
    checker.promote("alpha pattern of interest", session_id="s2")
    results = checker.check_all()
    assert len(results) == 1
    assert results[0].status == VERIFIED


# ---- factcheck ----------------------------------------------------------

def test_factcheck_present_in_source(tmp_path):
    src = (DATA / "source_fact.txt").read_text()
    obs = Observation(id="f1", text="the plan-reset at 14:03 dropped the session token", session_id="s1", kind="fact")
    res = factcheck(obs, src)
    assert res.present is True
    assert res.status == VERIFIED


def test_factcheck_missing_is_unverifiable():
    obs = Observation(id="f2", text="the caller was billed twice", session_id="s1", kind="fact")
    res = factcheck(obs, "the deployment log shows a plan reset at 14:03")
    assert res.present is False
    assert res.status == UNVERIFIABLE


def test_factcheck_no_source_is_unverifiable():
    obs = Observation(id="f3", text="anything", session_id="s1", kind="fact")
    res = factcheck(obs, None)
    assert res.status == UNVERIFIABLE


def test_factcheck_rejects_pattern():
    obs = Observation(id="f4", text="x", session_id="s1", kind="pattern")
    with pytest.raises(ValueError):
        factcheck(obs, "source")


# ---- comparator ---------------------------------------------------------

def test_comparator_verified_when_in_both():
    refl = (DATA / "reflective_transcript.txt").read_text()
    plain = (DATA / "plain_comparator.txt").read_text()
    comp = Comparator()
    # A claim that is genuinely true in both registers survives.
    res = comp.evaluate("a plan reset discards the previous steps", refl, plain)
    assert res.verdict in (VERIFIED, CANDIDATE)


def test_comparator_hallucination_when_reflective_only():
    comp = Comparator()
    res = comp.evaluate(
        "this line of questioning tends to produce a deeper clarity about intent",
        "this line of questioning tends to produce a deeper clarity about intent",
        "a plan reset clears the current task list and reloads the default template",
    )
    assert res.verdict == HALLUCINATION


def test_comparator_unverifiable_when_in_neither():
    comp = Comparator()
    res = comp.evaluate("the moon is made of cheese", "plan reset clears tasks", "plan reset clears tasks")
    assert res.verdict == UNVERIFIABLE


# ---- end-to-end via CLI -------------------------------------------------

def test_cli_log_and_status(tmp_path, capsys):
    from veo.cli import main

    store = tmp_path / "cli.jsonl"
    turns = DATA / "session1_turns.txt"
    rc = main(["--store", str(store), "log", "--session", "s1",
               "--turns", str(turns), "--claim", "this line of questioning tends to produce clarity"])
    assert rc == 0
    rc = main(["--store", str(store), "status"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "s1" in out or "observations: 1" in out
