"""veo command-line interface.

Local-first, dependency-free. Wraps the four protocol moves from
FRAMEWORK.md §6 into subcommands:

  veo log        Log a reflective exchange (turns + extracted observations).
  veo recurrence Run the cross-session recurrence check over the store.
  veo factcheck  Mechanically verify a fact-kind claim against a source.
  veo compare    Run the deterministic hallucination comparator on a claim.
  veo status     Show the current status of every logged observation.

All data lives in one JSONL file (default ~/.veo/exchanges.jsonl). The
store path is configurable with --store so you can keep separate research
corpora.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .store import ExchangeStore, Exchange, Observation, status_from_counts
from .similarity import SIMILARITY_THRESHOLD
from .recurrence import RecurrenceChecker
from .factcheck import factcheck
from .comparator import Comparator


DEFAULT_STORE = Path.home() / ".veo" / "exchanges.jsonl"


def _store(args) -> ExchangeStore:
    return ExchangeStore(args.store or DEFAULT_STORE)


def cmd_log(args) -> int:
    store = _store(args)
    session_id = args.session or "session-" + Path(args.turns.name).stem if args.turns else "session-cli"
    turns: list[dict] = []
    if args.turns:
        raw = args.turns.read_text(encoding="utf-8")
        for i, line in enumerate(l := [x for x in raw.splitlines() if x.strip()], start=1):
            role = "user" if i % 2 == 1 else "model"
            turns.append({"role": role, "text": line})

    observations: list[Observation] = []
    kind = args.kind
    for c in args.claim:
        observations.append(
            Observation(id=_short(), text=c, session_id=session_id, kind=kind)
        )
    ex = Exchange(session_id=session_id, turns=turns, observations=observations)
    store.add(ex)
    print(f"logged session {session_id} with {len(observations)} observation(s) to {store.path}")
    return 0


def cmd_recurrence(args) -> int:
    store = _store(args)
    checker = RecurrenceChecker(store, min_sim=args.threshold)
    if args.text:
        res = checker.promote(args.text, session_id=args.session)
        print(json.dumps(res.to_dict(), indent=2))
        return 0
    for res in checker.check_all():
        mark = "VERIFIED" if res.status == "verified" else "candidate"
        print(f"[{mark}] (seen in {res.times_seen} session(s)): {res.text}")
    return 0


def cmd_factcheck(args) -> int:
    store = _store(args)
    source = args.source.read_text(encoding="utf-8") if args.source else None
    obs = Observation(id=_short(), text=args.claim, session_id=args.session or "fact-cli", kind="fact")
    res = factcheck(obs, source)
    print(json.dumps(res.to_dict(), indent=2))
    # Persist the checked fact so later `status` shows it.
    ex = Exchange(session_id=obs.session_id, observations=[obs])
    store.add(ex)
    return 0


def cmd_compare(args) -> int:
    reflective = args.reflective.read_text(encoding="utf-8")
    comparator = args.comparator.read_text(encoding="utf-8")
    comp = Comparator(args.threshold)
    res = comp.evaluate(args.claim, reflective, comparator)
    print(json.dumps(res.to_dict(), indent=2))
    return 0


def cmd_status(args) -> int:
    store = _store(args)
    checker = RecurrenceChecker(store, min_sim=args.threshold)
    results = checker.check_all()
    if not results:
        print("no observations logged yet")
        return 0
    counts: dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    print(f"store: {store.path}")
    print(f"observations: {len(results)}  ->  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print("-" * 60)
    for r in results:
        print(f"[{r.status}] (×{r.times_seen}) {r.text}")
    return 0


def _short() -> str:
    import uuid
    return uuid.uuid4().hex[:12]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="veo", description="veo-framework verification protocol tool (FRAMEWORK.md §6)")
    p.add_argument("--store", default=None, help=f"JSONL store path (default {DEFAULT_STORE})")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("log", help="log a reflective exchange with extracted observations")
    pl.add_argument("--session", help="session id (default: derived from --turns filename)")
    pl.add_argument("--turns", type=Path, help="file of alternating user/model lines")
    pl.add_argument("--claim", action="append", required=True, help="an extracted observation (repeatable)")
    pl.add_argument("--kind", choices=["pattern", "fact"], default="pattern")
    pl.set_defaults(func=cmd_log)

    pr = sub.add_parser("recurrence", help="cross-session recurrence check (§6.1)")
    pr.add_argument("--text", help="new observation text to record/promote")
    pr.add_argument("--session", help="session id for a new observation")
    pr.add_argument("--threshold", type=float, default=SIMILARITY_THRESHOLD)
    pr.set_defaults(func=cmd_recurrence)

    pf = sub.add_parser("factcheck", help="mechanical fact-check (§6.2)")
    pf.add_argument("--claim", required=True)
    pf.add_argument("--source", type=Path, help="canonical source text file")
    pf.add_argument("--session", help="session id to attach the fact to")
    pf.set_defaults(func=cmd_factcheck)

    pc = sub.add_parser("compare", help="deterministic hallucination comparator")
    pc.add_argument("--claim", required=True)
    pc.add_argument("--reflective", type=Path, required=True, help="the reflective transcript text")
    pc.add_argument("--comparator", type=Path, required=True, help="plain-prompt comparator run text")
    pc.add_argument("--threshold", type=float, default=SIMILARITY_THRESHOLD)
    pc.set_defaults(func=cmd_compare)

    ps = sub.add_parser("status", help="show every observation's current status")
    ps.add_argument("--threshold", type=float, default=SIMILARITY_THRESHOLD)
    ps.set_defaults(func=cmd_status)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
