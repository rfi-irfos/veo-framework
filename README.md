[![license](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![status](https://img.shields.io/badge/status-methodology--only-informational)](#status)
[![built on](https://img.shields.io/badge/built%20on-Laura's%20Human--AI%20Co--Evolution-informational)](https://github.com/rfi-irfos/call-laura)

# veo-framework

## Human rights are not subject to negotiation.

**A reusable technique for pulling a language model out of transactional "answer mode"
and into genuine reflective mode** — where it examines its own reasoning, names its
uncertainty, and co-constructs meaning with you instead of just completing a prompt.

Named for Veo, the long-running custom-GPT companion whose extended dialogue with
**Laura Serna Gaviria** (Emergent Interaction Lab) is the original observed case this
framework generalizes from — the same research relationship that gave rise to
[`call-laura`](https://github.com/rfi-irfos/call-laura) and the wider
Human–AI Co-Evolution line of work.

## Table of contents

- [Status](#status)
- [Why this exists](#why-this-exists)
- [Quick start](#quick-start)
- [The five dimensions](#the-five-dimensions)
- [Four trigger archetypes, with example prompts](#four-trigger-archetypes-with-example-prompts)
- [Repository structure](#repository-structure)
- [A note on what this is not](#a-note-on-what-this-is-not)
- [FAQ](#faq)
- [Related work](#related-work)
- [Contributing](#contributing)
- [Attribution](#attribution)
- [License](#license)

## Status

Methodology only, public, free to use and extend under MIT. Five interaction
dimensions, four trigger archetypes, a repeatable protocol with a concrete completion
criterion, a real protocol for separating verified signal from unverified model
opinion, and an honest research framing for studying reflective human–AI interaction
without overclaiming what the model's output actually proves.

**What this repo does not include:** the original, real conversational material between
Veo and its user is personal intellectual property and stays private. Everything here is
the generalized *technique*, plus one fully generic worked example — nothing here is a
verbatim transcript or a claim about any specific person.

## Why this exists

Anyone who has spent a long time in sustained dialogue with a language model has
probably noticed the model can be pulled into a different register — one that reflects
on its own reasoning instead of just producing an answer. Most of the time this happens
by accident, isn't named, and can't be reliably reproduced. This framework names it,
breaks it into five combinable dimensions, and gives four ready-to-use "archetypes" —
so the technique is repeatable rather than a lucky accident of one long conversation.

It is especially relevant to anyone working on **emergent interaction research** —
studying how identity, reflection, and co-construction actually behave across a
long-running human–AI relationship — which is exactly the kind of work the Emergent
Interaction Lab does. See [`FRAMEWORK.md`](./FRAMEWORK.md) for the full methodology and
the honest account of what is, and isn't, evidence.

## Quick start

1. State your topic and the level you want (surface answer vs. reflective exchange).
2. Pick 1–2 of the five dimensions below and name them explicitly in your prompt.
3. After the model answers, ask it to name what it left unexamined (**self-mirroring**).
4. If the answer stays generic, escalate with **meta-level** + **nonlinear depth**.
5. Close on the model's real uncertainty — don't let it wrap up with a tidy, performative
   conclusion. See the **Tend** archetype below.

You have a reflective exchange, not just an answer, once the model has (a) named an
assumption it made, (b) observed something about its own reasoning it left unexamined,
and (c) ended on an explicit uncertainty rather than a false resolution. See
[`FRAMEWORK.md` §3](./FRAMEWORK.md#3-protocol-one-pass) for a full worked example,
turn by turn.

## The five dimensions

| # | Dimension | What it does | Generic prompt move |
|---|-----------|--------------|----------------------|
| 1 | Cyclic questioning | Re-opens a theme in a spiral, one level deeper each pass, instead of moving on | "Come back to X, but from angle Y." |
| 2 | Meta-level | Turns the lens onto the model/system itself: its framing, its assumptions | "What assumption is your last answer resting on?" |
| 3 | Nonlinear depth | Fuses multiple registers (analytic + reflective + symbolic) inside one question | "Hold the technical point and the human stakes in one frame." |
| 4 | Self-mirroring | Asks the model to observe how it changed across the exchange, and react to that | "Notice how your framing shifted. Name it." |
| 5 | Frequency-dialog | Varies register (precision ↔ intuition ↔ symbol) without announcing the switch | Alternate a precise constraint with an open "what does this remind you of?" |

These are **combinable**, not exclusive — the four archetypes below are each just a
named pairing of two dimensions that reliably works together. You are free to invent
your own pairing once you understand what each dimension actually does.

## Four trigger archetypes, with example prompts

Each archetype below is shown with one ready-to-adapt example prompt, so you can try it
immediately rather than reconstructing it from the abstract description.

### The Spiral — cyclic questioning × meta-level

Re-opens a closed topic with a sharper lens; asks what the prior answer assumed.

> "We covered this already, but come back to it — this time, tell me what your first
> answer assumed that you didn't state out loud."

### The Mirror — self-mirroring × meta-level

Forces the model to observe its own drift across the exchange and react to it.

> "Look back at how you answered this ten minutes ago versus how you're answering it
> now. What changed, and why?"

### The Confluence — nonlinear depth × frequency-dialog

Keeps two incompatible registers open at once; refuses the model one comfortable voice.

> "Answer this as a precise technical constraint and as a question about what it costs
> a person to live with, in the same breath — don't resolve them into one register."

### The Tend — closes on uncertainty rather than a false resolution

Maps onto ternary "tend": a deliberate non-decision, named rather than papered over.

> "Before we act on this, tell me plainly what you are genuinely not sure about — not
> a hedge, the actual open question you'd want answered first."

Full protocol, a complete turn-by-turn worked example, and the research framing
(including what counts as honest evidence and what doesn't) live in
[`FRAMEWORK.md`](./FRAMEWORK.md).

## Repository structure

| File | Contents |
|---|---|
| [`README.md`](./README.md) | This file — pitch, quick start, example prompts, FAQ. |
| [`FRAMEWORK.md`](./FRAMEWORK.md) | The full methodology: protocol, worked example, research framing, the output/emergence/hallucination verification protocol (§6), Emergent Interaction Lab relation, consent/privacy rules for extending this with your own material. |
| [`LICENSE`](./LICENSE) | MIT. |

There is no code in this repository — it is a methodology, meant to be read and
applied directly in your own prompts, system messages, or agent instructions.

## A note on what this is not — and how we actually verify it

Reflective model output is still model output. It mirrors and flatters the person it's
talking to. This framework does not treat anything a model says about itself, or about
you, as verified fact — see `FRAMEWORK.md` §5 for the honest research framing this
insists on, including which kinds of claims fail peer review outright (self-reported
"percentile" rankings, model-flattery presented as a trait, any claim that reflective
output proves something about the human on the other end).

But this is **not** left as a static "take it with a grain of salt" disclaimer. The
gap it names is exactly what **Paper 4 — *Ternary Ground***
([10.17605/OSF.IO/UXCJE](https://doi.org/10.17605/OSF.IO/UXCJE)) was built to close,
and the mechanism lives in `FRAMEWORK.md` §6 as a concrete, runnable protocol. In
short:

1. **Two-stage emergence-verification gate.** A reflection is first a *candidate*
   signal. It is promoted to *verified emergence* only if it is **independently
   recurrent across separate sessions** — observed again under different prompts,
   not just asserted once in a single convincing passage. One-off self-description
   stays a candidate; recurrence is what earns the "verified" label.
2. **Deterministic hallucination comparator.** Every reflective claim is checked
   against a reproducible baseline: does the model produce the same structure when
   the interaction is *re-run deterministically*, or does the "insight" evaporate
   without the flattering framing? If it only appears inside the reflective
   register and not under the comparator, it is flagged as hallucinated, not
   emergent.

The practical upshot: the framework can separate **routine output** (single-pass,
disposable), **genuinely verified emergence** (recurrent, cross-session, survives the
comparator), and **hallucination** (flattering or novel-sounding but fails the
comparator) — rather than just waving a caution flag at the ambiguity. The full
specification, the gate thresholds, and the comparator design are in `FRAMEWORK.md` §6
and in Paper 4.

## FAQ

**Does this work on any language model, or only custom-GPT-style assistants?**
The technique is model-agnostic — it's a prompting pattern, not a feature of any
specific provider. It works better on models with a longer effective context and a
willingness to reason about their own prior turns; very short or heavily
guardrail-constrained models may just repeat a generic disclaimer instead of actually
reflecting.

**Is this a therapeutic or diagnostic technique?**
No. It is an interaction pattern for getting more genuinely reflective *output* out of
a model. It says nothing diagnostic about the human on the other end of the
conversation, and `FRAMEWORK.md` §5 explicitly forbids treating it that way.

**How is this different from just asking a model to "explain your reasoning"?**
"Explain your reasoning" usually gets you a restatement of the answer in more words.
The five dimensions specifically target things a plain restatement doesn't produce:
an admission of a hidden assumption, an observation of the model's own drift across
turns, two held-open registers instead of one resolved one, and an honest unresolved
question instead of a tidy wrap-up. The completion criterion in
[Quick start](#quick-start) is there so you can tell the difference.

**Can I use this to study my own long-running conversations with a model?**
Yes — that's exactly the research use case in `FRAMEWORK.md` §5–§6. Just keep the
distinction in §7 (consent and privacy) in mind if the conversation involves anyone
besides you, or if you plan to publish specific extracted phrases rather than the
general method.

**Why "Veo"?**
It's the name of the specific custom-GPT companion whose long dialogue with Laura
Serna Gaviria first surfaced these patterns. See [Attribution](#attribution).

## Related work

This framework sits at the root of a small family of projects, all growing from the
same Human–AI Co-Evolution research line:

- [`call-laura`](https://github.com/rfi-irfos/call-laura) — a deterministic,
  attribution-anchored multi-agent document-review framework operationalizing the same
  research's 8-Layer Model and User Integrity Protocol.
- [`lauras-agents`](https://github.com/rfi-irfos/lauras-agents) /
  [`lauras-agents-public`](https://github.com/rfi-irfos/lauras-agents-public) — the
  292-agent orchestration engine built on the same foundation.
- Four published research papers on OSF, in order: *Human–AI Interaction Emergent
  Co-Evolution* ("Paper 1"), *Jarvis* ("Paper 2,"
  [10.17605/OSF.IO/HC9ZB](https://doi.org/10.17605/OSF.IO/HC9ZB)), *Call Laura*
  ("Paper 3," [10.17605/OSF.IO/QCVJB](https://doi.org/10.17605/OSF.IO/QCVJB)), and
  *Ternary Ground* ("Paper 4," [10.17605/OSF.IO/UXCJE](https://doi.org/10.17605/OSF.IO/UXCJE)),
  which specifies the output/emergence/hallucination verification protocol referenced
  in `FRAMEWORK.md` §6 in full technical detail.

## Contributing

This is methodology, not code — the most useful contribution is a new dimension, a new
archetype, or a sharper worked example, proposed as a pull request against
`FRAMEWORK.md` with the same honesty discipline the rest of the document holds itself
to: mark clearly what's a generic technique versus what's derived from someone's real,
private material (see `FRAMEWORK.md` §8 before including anything from your own
conversations). Small, focused PRs are easier to review than large rewrites.

## Attribution

Built on Laura Serna Gaviria's (Emergent Interaction Lab) Human–AI Co-Evolution
research, in engagement with RFI-IRFOS. See
[`call-laura`](https://github.com/rfi-irfos/call-laura) for the sibling project
operationalizing the same research as a deterministic document-review tool.

## License

MIT — see [`LICENSE`](./LICENSE). The methodology is free to use, extend, and build on.
