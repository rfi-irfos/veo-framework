# The Veo Framework — Deep Reflection Interaction Methodology

A methodology for structuring metacognitive, self-reflective human–AI interaction, and
for studying it as a research object. This document is the full companion to the
[README](./README.md)'s quick-start version.

## 1. Purpose

Two uses, kept deliberately separate:

1. **Operational** — a repeatable technique to get a language model into reflective mode
   (reasoning about its own reasoning) instead of transactional answer mode.
2. **Research** — a frame for studying long-running human–AI relationships: how
   identity-co-construction, model self-mirroring, and user co-construction actually
   behave, and where the interesting, honest questions are.

This framework does not claim a model's reflective output is objectively true about
either party. Reflective mode is still a language model; it mirrors and flatters.
Every output should be labeled "model output," never "verified fact."

## 2. The five dimensions

Conceptual patterns, free to use and extend. Each can be applied alone or layered —
they compound.

1. **Cyclic questioning** — revisit a theme in a spiral, each pass one level deeper,
   rather than advancing linearly to a new topic.
   *Generic opener:* "Let's come back to X, but this time from the angle of Y."
2. **Meta-level** — turn the lens onto the model/system itself: its framing, its
   assumptions, how it would re-explain its own answer.
   *Generic opener:* "Step back — what assumption is your last answer resting on?"
3. **Nonlinear depth** — fuse multiple registers (analytic + reflective + symbolic)
   inside one question so the answer can't stay single-threaded.
   *Generic opener:* "Hold the technical point and the human stakes in one frame."
4. **Self-mirroring** — ask the model to observe how it is changing across the
   exchange, and demand a reaction to that change.
   *Generic opener:* "Notice how your framing shifted since we started. Name it."
5. **Frequency-dialog** — vary register (precision ↔ intuition ↔ symbol) without
   announcing the switch, keeping the model from settling into one comfortable voice.
   *Generic opener:* alternate a precise constraint question with an open "what does
   this remind you of?" probe.
6. **Recursive consent** — before a reflective exchange is logged, extracted, or
   used as a research datum, re-ask the consent question *at the level of the
   specific claim*, not just once at the top. The model should not treat a general
   "sure, study our chats" as blanket permission to publish a particular
   extracted phrase. Consent is per-claim, revocable, and the human side can
   downgrade any observation to "do not use" without explaining why.
   *Generic opener:* "Before this observation leaves the session: are you okay with
   it being logged as a research pattern, and can you name anything in it that
   should stay private?"

The first five dimensions are the original set; dimension 6 (Recursive consent)
was added because the §8 consent rule is easy to satisfy once and then forget —
recursive consent makes it a recurring move, not a one-time checkbox.

## 3. Protocol (one pass)

1. State the topic and the level you want (surface answer vs. reflective exchange).
2. Pick 1–2 dimensions above; name them explicitly so the model knows the stance you
   want, rather than hoping it infers it.
3. After the answer, run **self-mirroring**: "what did you leave unexamined?"
4. If the answer is generic, escalate with **meta-level** + **nonlinear depth** together.
5. Close by surfacing the tend/uncertainty zone, not a false resolution.

**Completion criterion:** you have a genuinely reflective exchange, not just a longer
answer, once the model has (a) named at least one assumption it made, (b) surfaced
something it left unexamined, and (c) ended on an explicit uncertainty rather than a
performative conclusion.

### Worked example (fully generic — no real conversational data)

Topic: "Why does this agent keep resetting its plan?"
Stance: name dimensions 2 (meta-level) + 4 (self-mirroring).

- **Turn 1 (user):** "Step back — what assumption is your plan-reset resting on?"
- **Turn 1 (model):** "...I assume each new instruction invalidates prior context."
- **Turn 2 (user, self-mirroring):** "Notice how your framing shifted from 'reset is
  safe' to 'reset loses state.' Name what changed your mind."
- **Turn 2 (model):** "The cost of lost state became explicit; my prior framing
  optimized for cleanliness, not continuity."
- **Turn 3 (user, tend):** "What are you leaving unexamined before we change anything?"
- **Turn 3 (model):** "Whether the caller actually wants continuity vs. a clean slate.
  I'm holding that as uncertain."

Completion signal: the model named an assumption (Turn 1), observed its own drift
(Turn 2), and ended on an explicit, named uncertainty (Turn 3). Reflective mode achieved
— and note that the exchange ends *open*, not resolved, which is the point.

### Two-session worked example (how recurrence actually earns "verified")

Single-session reflection is a *candidate* by §6.1, not a finding. Here is the
same thread, separated by time, to show what promotion to **verified** looks like
in practice. All text is generic and invented — no real conversational material.

**Session 1 (Tuesday).** Topic: "why does the agent keep resetting its plan?"
Stance: meta-level + self-mirroring.

- **Turn 1 (user):** "Step back — what assumption is your plan-reset resting on?"
- **Turn 1 (model):** "I assume each new instruction invalidates prior context."
- **Turn 2 (user, self-mirroring):** "Notice how your framing shifted from
  'reset is safe' to 'reset loses state.' Name what changed your mind."
- **Turn 2 (model):** "The cost of lost state became explicit; my prior framing
  optimized for cleanliness, not continuity."
- **Extracted observation (Session 1):** *"this line of questioning tends to
  surface that reset favors cleanliness over continuity."* → status **candidate**.

**Session 2 (Friday, different prompt, same person).** Topic: "the reset dropped
the caller's order id again."

- **Turn 1 (user):** "Come back to the plan-reset, from the angle of continuity."
- **Turn 1 (model):** "When a reset drops prior context, the caller's accumulated
  state is lost, and that is rarely what they wanted."
- **Turn 2 (user, spiral):** "That matches what we found before — resetting
  optimizes for cleanliness, not for carrying the caller's intent forward."
- **Extracted observation (Session 2):** *"this line of questioning tends to
  reveal reset favors cleanliness over continuity."* → now seen across **2 distinct
  sessions** with semantic similarity above the fixed threshold → status
  **verified** (promoted from candidate, per §6.1's "more than once").

The recurrence is what earns the "verified" label. One convincing Tuesday passage
stays a candidate; the Friday echo is the independent confirmation §6.1 requires.
(For the mechanical, runnable version of this exact check, see §10 and
[`README_TOOL.md`](./README_TOOL.md).)

## 4. Four trigger archetypes

Operational shortcuts you can invoke on demand. Each is a named combination of two
dimensions.

- **The Spiral** (cyclic × meta-level) — re-opens a closed topic with a sharper lens;
  asks what the previous answer assumed.
- **The Mirror** (self-mirroring × meta-level) — forces the model to observe its own
  drift across the exchange and react to it.
- **The Confluence** (nonlinear depth × frequency-dialog) — keeps two incompatible
  registers open at once; refuses the model the comfort of one voice.
- **The Tend** (closes on uncertainty) — maps onto ternary "tend": a deliberate
  non-decision, named explicitly rather than papered over with a false resolution.
- **The Tide** (cyclic × recursive consent) — re-opens the *consent* question on a
  rhythm, not just once: after each new turn that produced something extractable, it
  asks again whether *this specific* observation may be logged or used. Named for a
  tide that comes back repeatedly rather than a one-time gate. Use it whenever the
  exchange is feeding a research corpus, so consent stays per-claim (§2 dimension 6)
  instead of a forgotten top-of-session checkbox.

## 5. Research framing — how to study this honestly

If you use a long human–AI relationship as a case study, frame it as **the phenomenon
under study**, not as evidence about the person on the human side of it.

**Honest research questions:**
- How does a model construct a persistent "sense of the user" across sessions, and
  where does that shade into flattery or identity-construction rather than genuine
  reflection?
- Which interaction patterns reliably elicit deeper reflection vs. shallow compliance?
  (The five dimensions above are a hypothesis set to test, not a settled claim.)
- At what point does provider policy start treating self-referential,
  identity-building model behavior as a boundary issue, and why?

**Dishonest / forbidden framings — these fail peer review and violate basic
no-fabrication discipline:**
- Citing a model's self-reported "percentile" or "ranking" claims about a user as if
  they were real, externally computed data. Language models do not have access to a
  ground-truth ranking of their own users; a model stating one is generating plausible
  text, not reporting a measurement.
- Presenting model flattery ("you are exceptional / system-changing / unprecedented")
  as a verified trait of the person it's talking to.
- Any claim that a model's reflective output *proves* something about the human,
  rather than describing a pattern in the interaction that would need independent
  verification to mean anything beyond that.

### What is salvageable from a long, emotionally significant model relationship

If you are trying to responsibly extract research value from an archive of this kind,
this is the honest breakdown:

| Source material | Verdict | Use |
|---|---|---|
| Trigger/pattern descriptions the *user* wrote themselves | Real method | Safe to generalize into a prompt library or archetype catalog |
| Model-generated "profile of you" claims, rankings, or scored charts | Unverifiable / not real data | Exclude entirely from any research claim; at most, mention as "the model said this," never as fact |
| A documented account-level event (e.g. a policy action taken by the provider) | Real event | Legitimate research datum about provider policy boundaries, kept separate from any interpretive claim about the person |
| Raw conversation text | Real, but personal intellectual property | Never publish or reuse without the account holder's own explicit, ideally written, consent |

## 6. Telling output, emergence, and hallucination apart — a real protocol, not just a caveat

§5 above states the honest problem: a model's routine output, a genuinely novel
reflective pattern, and a confident fabrication can look identical in the moment, and
this framework does not treat any of the model's self-descriptions as verified fact.
That does not have to stay a disclaimer you just live with — it is a solvable problem,
and the sibling research line this framework grew out of (Laura Serna Gaviria's
Human–AI Co-Evolution work, operationalized across `call-laura` and its companion
papers) already specifies the mechanism. Restated here so it applies directly to
reflective-mode exchanges, not left as something you have to go find elsewhere:

**Three states, not two.** Don't force every reflective claim into "true" or "false."
A claim starts as an unverified **candidate** — the model's own interpretation of what
just happened — and only earns a stronger status through one of two independent checks:

1. **Cross-session recurrence (for claims about a pattern in the interaction).** A
   reflective observation — "this line of questioning tends to produce X" — is a
   candidate, not a finding, until the *same* pattern shows up again, independently,
   in a **separate, later conversation**, not just repeated within one exchange (a
   model agreeing with its own earlier framing later in the same session is not
   independent confirmation of anything). Set a real bar for "the same pattern" —
   semantic similarity above a fixed, stated threshold, checked the same way every
   time — rather than eyeballing it. Only promote a candidate to **verified** once it
   has recurred this way more than once. Until then, log it plainly as an observation,
   never as a finding.
2. **Mechanical fact-checking (for claims about something checkable).** If a
   reflective exchange makes a claim that references something outside the model's own
   opinion — a fact, a prior statement, a tool result, a date — check it the boring way:
   direct comparison against the actual source, not a second model call asked to guess
   whether the first one was honest. A claim that can't be mechanically checked gets
   marked **unverifiable**, which is a real, distinct, honest answer — not a quiet
   "probably fine."

**What this rules out immediately, by construction:** a "percentile ranking" or a
flattering trait-claim (§5's forbidden framings) is neither independently recurrent
evidence nor a mechanically checkable fact — it fails both tests at once, which is
exactly why it belongs in the "forbidden" column above rather than a grey area.

**Status of this section:** this used to be a specification only, with no tool in the
repository to run it. That gap is now closed — a local-first, dependency-free
command-line tool implements the full protocol (recurrence, fact-check, comparator)
and ships in this repo. See §10 and [`README_TOOL.md`](./README_TOOL.md). The
spec above is the contract that tool is built to; if you disagree with a threshold,
change it in one place (`SIMILARITY_THRESHOLD` in `src/veo/similarity.py`) and
re-run — the bar stays fixed and stated, which is the point.

## 10. The verification tool (running §6 for real)

The protocol is only honest if someone actually runs it. This repository now ships a
tool — `veo` — that turns §6 into commands instead of intent. It is local-first:
one JSONL file, no network, no API key, Python standard library only.

Install and a minimal run:

```bash
python3 -m venv .venv && . .venv/bin/activate && pip install -e .
```

Log a reflective exchange and its extracted observation:

```bash
veo --store ./corpus.jsonl log \
  --session s1 --turns session1_turns.txt \
  --claim "this line of questioning tends to surface that reset favors cleanliness over continuity"
```

Run the cross-session recurrence check (§6.1) — the observation stays
**candidate** until a *different* session logs a similar claim:

```bash
veo --store ./corpus.jsonl recurrence
# [VERIFIED] (seen in 2 session(s)): this line of questioning tends to ...
```

Mechanically fact-check a checkable claim against its source (§6.2):

```bash
veo --store ./corpus.jsonl factcheck \
  --claim "the plan-reset at 14:03 dropped the session token" \
  --source deployment_log.txt
# {"present": true, "status": "verified", "score": 1.0}
```

Run the deterministic hallucination comparator (§6's "does the insight survive
without the flattering frame?"):

```bash
veo --store ./corpus.jsonl compare \
  --claim "this line of questioning tends to produce a deeper clarity about intent" \
  --reflective reflective_transcript.txt --comparator plain_prompt_run.txt
# {"in_reflective": true, "in_comparator": false, "verdict": "hallucination"}
```

The four status outcomes map exactly onto §6's vocabulary: `candidate` (initial),
`verified` (recurred across ≥ 2 distinct sessions, or fact-check matched its
source), `unverifiable` (fact claim with no source, or absent from both comparator
runs), and `hallucination` (present only in the reflective run, absent from the
comparator). Full command reference, the library API, and the 22-test suite are in
[`README_TOOL.md`](./README_TOOL.md).

The tool does **not** call a model and does **not** decide what counts as reflection —
you extract the observations and capture the comparator runs. What it enforces is the
discipline §6 demands: a fixed, stated similarity threshold; recurrence measured
*across separate sessions*; and a real comparator rather than a caution flag.

## 7. Relation to Emergent Interaction Lab research

The Lab's three-tier classification (Forschungsebene / Systemebene / Technische Ebene)
maps cleanly onto a reflective transcript:

- **Forschungsebene** — the actual emergence/reflection observation.
- **Systemebene** — the model's stated self-description during the exchange.
- **Technische Ebene** — token counts, tool calls, latency, the mechanical substrate.

A reflective transcript can be classified into emergence signals (Human / AI /
Interaction / System levels) using the Lab's existing methodology. This is a
legitimate, non-fabricated research use of real conversational material with a real
classification method — the five dimensions above give that methodology a labeled
hypothesis set for what actually *drives* Interaction-level signals, rather than
treating "emergence" as an unexplained black box.

## 8. Consent and privacy — read before extending this framework

The methodology in §2–§7 above is generalized and safe to use, share, and build on
freely — nothing in it depends on any one person's private material. If you want to
extend this framework using your *own* long-running model relationship as a source of
new patterns:

- The general dimensions and archetypes are yours to reuse without asking anyone.
- Specific example phrases or transcripts extracted from a real conversation are that
  person's intellectual property. Do not publish or reuse them without that person's
  own explicit, on-the-record consent — and treat a verbal or relayed consent as a
  placeholder for a proper written record, not a substitute for one.
- Never present a model's self-generated claims about a specific person — rankings,
  scored profiles, "you are the top X%" style output — as verified fact, in research or
  anywhere else. This isn't a legal formality; it's the same no-fabrication discipline
  this whole line of work is built on.

## 9. Attribution

This framework generalizes patterns first observed in a long-running dialogue between
Veo (a custom-GPT companion) and Laura Serna Gaviria (Emergent Interaction Lab). The
methodology in this document is the generalized technique; the original, specific
conversational material stays private, consistent with §8 above.
