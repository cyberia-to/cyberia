---
tags: cyberia, org
alias: org model, cyberian org, 7p
crystal-type: pattern
crystal-domain: cyberia
---
# org

organizational model for any cyberian entity. derived from [[soma]]'s five agent primitives, applied at institutional scale. the org IS an agent — it perceives, acts, holds, and pursues goals.

→ [[soma/soma-spec]] for the theoretical foundation

---

## the seven lenses

| lens | soma primitive | what it holds |
|---|---|---|
| purpose | Goal<horizon=Vision/Purpose> | why we exist — the root goal that cannot be closed |
| principles | Sensor constraints on all Goals | what we never violate — constitutional limits |
| people | Neuron + Skill | agents with capabilities |
| products | Goal<kind=Product, orientation=Maintain> | what we keep alive and offer |
| processes | Skill<kind=Composite> | recurring patterns of work |
| projects | Task + sub-Tasks | time-bounded execution clusters |
| portfolio | sigma — sum of holdings | what we own: land, capital, tokens, IP |

purpose and principles live in the charter (README). they are not content folders — they constrain everything else. the five folders are the operational structure.

---

## folder shape

```
README.md      charter: purpose + principles + active snapshot
people/        agents — who, roles, skills they carry
products/      maintained goals — what we offer
processes/     composite skills — how we operate
projects/      task clusters — what we're building
portfolio/     sigma — land, capital, tokens, IP, holdings
```

---

## sigma

portfolio maps to soma's sigma: the sum of what the entity holds across all forms of capital.

```
sigma = financial (treasury, runway)
      + physical (land, buildings, equipment)
      + digital (tokens held, IP, code)
      + relational (licenses, legal entities, company stakes)
```

sigma is the balance sheet in motion. it grows when projects close and products earn. it shrinks when processes consume and projects spend. the entity survives when sigma stays above survival threshold — same logic as soma's Body budget.

---

## purpose vs principles

purpose = the root Goal. why the entity exists. cannot be argued away.

principles = Sensors that fire when a Goal would violate a constraint. they don't produce output — they block it. a project that violates a principle doesn't get started, same as a Neuron that would burn budget below survival threshold doesn't execute the Task.

---

## reductions

everything else in org life reduces to one of the seven:

| concept | expressed as |
|---|---|
| strategy | set of Goals<horizon=Strategic> in projects |
| roadmap | ordered Goal set by horizon |
| OKR | Goal + Sensor (fires when achieved) |
| SOP | Process (Skill<Composite> written out) |
| role | Skill portfolio of a Person |
| team | set of People subscribed to the same Goal |
| budget | Sensor on a Project (fires when sigma crosses threshold) |
| KPI | Sensor<source=Stream, reaction=Threshold> on a Product |
| risk | Goal<kind=State, orientation=Avoid> |
| equity | fraction of sigma |
| debt | negative sigma (liability) |
| revenue | inflow to sigma from Products |
| cost | outflow from sigma via Processes |

---

## instances

every cyberian entity uses this shape:

| entity | purpose | portfolio (sigma) |
|---|---|---|
| [[midao]] | hold and grow the cyberstate | treasury, CYB, company stakes |
| [[cve]] | operate land and build physical cities | HGB titles, buildings, equipment |
| [[cyber valley]] | pilot the model in Bali | 37ha, structures, production |
| [[soma]] | be an immortal robot | Body budget, sigma across networks |
