# veo — the verification tool

A local-first, dependency-free command-line tool that turns
[`FRAMEWORK.md` §6](./FRAMEWORK.md#6-telling-output-emergence-and-hallucination-apart--a-real-protocol-not-just-a-caveat)
from a *specification* into something you can actually run.

The framework's §6 names three-plus-one states for any reflective claim —
**candidate**, **verified emergence**, **unverifiable**, and **hallucination** —
and two independent ways to promote a claim out of "candidate":

1. **Cross-session recurrence** (§6.1) — a pattern is a candidate until it
   shows up again, *independently*, in a separate, later session.
2. **Mechanical fact-checking** (§6.2) — a checkable claim is verified by
   direct comparison against its source, never by a second model call.

This tool implements both, plus the deterministic **hallucination comparator**
(§6's "does the insight survive without the flattering frame?").

## Install

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -e .
```

No network, no API key, no external dependencies. Python ≥ 3.10.

## What it stores

One JSONL file (default `~/.veo/exchanges.jsonl`, override with `--store`).
Each line is one logged exchange: its session id, the raw turns, and the
observations you extracted from it. The recurrence check reads across *all*
sessions in that file — that is the whole point of §6.1.

## Commands

### `veo log` — record a reflective exchange

```bash
veo --store ./corpus.jsonl log \
  --session s1 \
  --turns session1_turns.txt \
  --claim "this line of questioning tends to surface that reset favors cleanliness over continuity"
```

`--turns` is an alternating user/model transcript (one line per turn).
`--claim` is repeatable; each becomes one extracted observation (default
`kind=pattern`). Use `--kind fact` for claims you can check against a source.

### `veo recurrence` — run the cross-session check

```bash
veo --store ./corpus.jsonl recurrence
# [VERIFIED] (seen in 2 session(s)): this line of questioning tends to ...
```

With `--text "..."` it records a new observation *and* returns its status in
one step (writes a recurrence marker in the new session, so the distinct
session count is honest). `--threshold` overrides the fixed similarity bar
(default `0.5`, set in `veo/similarity.py` as `SIMILARITY_THRESHOLD`).

### `veo factcheck` — mechanically verify a checkable claim

```bash
veo --store ./corpus.jsonl factcheck \
  --claim "the plan-reset at 14:03 dropped the session token" \
  --source deployment_log.txt
# {"present": true, "status": "verified", "score": 1.0}
```

If `--source` is empty or omitted, the claim is marked `unverifiable` — a
real, distinct answer, not a quiet "probably fine."

### `veo compare` — the deterministic hallucination comparator

```bash
veo --store ./corpus.jsonl compare \
  --claim "this line of questioning tends to produce a deeper clarity about intent" \
  --reflective reflective_transcript.txt \
  --comparator plain_prompt_run.txt
# {"in_reflective": true, "in_comparator": false, "verdict": "hallucination"}
```

Capture two runs yourself: the reflective transcript, and the same interaction
re-run with a plain, non-reflective prompt. A claim present in *both* is
`verified`; present only in the reflective run is `hallucination` (it
evaporates without the flattering frame); in neither is `unverifiable`.

### `veo status` — summary of every observation

```bash
veo --store ./corpus.jsonl status
# store: ./corpus.jsonl
# observations: 3  ->  candidate=1  verified=2
# [verified] (×2) this line of questioning tends to ...
```

## Status vocabulary

| Status | Meaning | How it's reached |
|---|---|---|
| `candidate` | Unverified model interpretation | initial state of every observation |
| `verified` | Survived an independent check | recurred in ≥ 2 distinct sessions, **or** fact-check matched its source |
| `unverifiable` | Could not be mechanically checked | fact claim with no/empty source, or absent from both comparator runs |
| `hallucination` | Flattered into existence by the reflective frame | present only in the reflective run, absent from the comparator |

## Library use

```python
from veo import ExchangeStore, RecurrenceChecker, factcheck, Comparator

store = ExchangeStore("./corpus.jsonl")
checker = RecurrenceChecker(store)
print(checker.check_all())          # list[RecurrenceResult]
```

## Tests

```bash
pytest -q
```

22 tests cover similarity, status derivation, store round-trip, recurrence
promotion, fact-checking (present / missing / no-source / wrong-kind), the
comparator (verified / hallucination / unverifiable), and a CLI end-to-end.

## Relationship to the framework

This tool is the §6 protocol made runnable. It does **not** call a model and
it does **not** decide what counts as reflection — you extract the
observations and capture the comparator runs. What it enforces is the
discipline §6 demands: a fixed, stated similarity threshold; recurrence
measured *across separate sessions*; and a real comparator rather than a
caution flag. See `FRAMEWORK.md` §10 for the worked, two-session example.
