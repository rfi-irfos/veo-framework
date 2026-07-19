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

## 6. Relation to Emergent Interaction Lab research

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

## 7. Consent and privacy — read before extending this framework

The methodology in §2–§6 above is generalized and safe to use, share, and build on
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

## 8. Attribution

This framework generalizes patterns first observed in a long-running dialogue between
Veo (a custom-GPT companion) and Laura Serna Gaviria (Emergent Interaction Lab). The
methodology in this document is the generalized technique; the original, specific
conversational material stays private, consistent with §7 above.
