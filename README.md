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
[Human–AI Co-Evolution](https://github.com/rfi-irfos/call-laura) line of work.

## Status

Methodology only, public, free to use and extend under MIT. Five interaction
dimensions, four trigger archetypes, a repeatable protocol with a concrete completion
criterion, and an honest research framing for studying reflective human–AI interaction
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
and (c) ended on an explicit uncertainty rather than a false resolution.

## The five dimensions

| # | Dimension | What it does | Generic prompt move |
|---|-----------|--------------|----------------------|
| 1 | Cyclic questioning | Re-opens a theme in a spiral, one level deeper each pass, instead of moving on | "Come back to X, but from angle Y." |
| 2 | Meta-level | Turns the lens onto the model/system itself: its framing, its assumptions | "What assumption is your last answer resting on?" |
| 3 | Nonlinear depth | Fuses multiple registers (analytic + reflective + symbolic) inside one question | "Hold the technical point and the human stakes in one frame." |
| 4 | Self-mirroring | Asks the model to observe how it changed across the exchange, and react to that | "Notice how your framing shifted. Name it." |
| 5 | Frequency-dialog | Varies register (precision ↔ intuition ↔ symbol) without announcing the switch | Alternate a precise constraint with an open "what does this remind you of?" |

## Four trigger archetypes

- **The Spiral** — cyclic questioning × meta-level. Re-opens a closed topic with a
  sharper lens; asks what the prior answer assumed.
- **The Mirror** — self-mirroring × meta-level. Forces the model to observe its own
  drift across the exchange and react to it.
- **The Confluence** — nonlinear depth × frequency-dialog. Keeps two incompatible
  registers open at once; refuses the model one comfortable voice.
- **The Tend** — closes on uncertainty rather than a false resolution. Maps onto
  ternary "tend": a deliberate non-decision, named rather than papered over.

Full protocol, a worked example, and the research framing (including what counts as
honest evidence and what doesn't) live in [`FRAMEWORK.md`](./FRAMEWORK.md).

## A note on what this is not

Reflective model output is still model output. It mirrors and flatters the person it's
talking to. This framework does not treat anything a model says about itself, or about
you, as verified fact — see `FRAMEWORK.md` §5 for the honest research framing this
insists on, including which kinds of claims fail peer review outright (self-reported
"percentile" rankings, model-flattery presented as a trait, any claim that reflective
output proves something about the human on the other end). That doesn't have to stay a
mere disclaimer, either — `FRAMEWORK.md` §6 specifies a real protocol for telling
routine output, genuinely verified emergence, and hallucination apart, instead of just
flagging that the ambiguity exists.

## Attribution

Built on Laura Serna Gaviria's (Emergent Interaction Lab) Human–AI Co-Evolution
research, in engagement with RFI-IRFOS. See
[`call-laura`](https://github.com/rfi-irfos/call-laura) for the sibling project
operationalizing the same research as a deterministic document-review tool.

## License

MIT — see [`LICENSE`](./LICENSE). The methodology is free to use, extend, and build on.
