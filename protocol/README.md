---
tags: cyberia, protocol, core
alias: cyberia protocol, protocol
crystal-type: pattern
crystal-domain: cyberia
crystal-size: deep
---

# cyberia protocol

one protocol describing how a cyberian entity exists, acts, accounts for itself, coordinates, scales, and trades. one vocabulary, fractal at every scale — the same shape for one [[robot]], one institution, one state.

what reduces to what:

- soma — agency at the agent
- org — agency at the institution
- system — the on-chain accounting projection
- services — the storage layer at sovereign scale
- marketplace — price discovery on any asset

below: the unified picture.

---

## 1. identity

the Robot is the cyberian entity. every Robot composes the same four attributes:

| attribute | what it is |
|---|---|
| Body | mortal physical vessel — machine, building, jurisdiction |
| Soul | immortal cognitive root — root Neuron, holds Sigma, orchestrates worker Neurons |
| Avatar | portable persona — the character the Robot presents; voice, style, accumulated reputation |
| Name | unique NFT identifier on the [[cybergraph]] (@master, @joy) |

internal structure of any Robot:

| concept | what it is |
|---|---|
| Neuron | atomic cognitive worker; has Addresses across networks |
| Address | Neuron's projection into one specific network |

a Robot outlasts any Body. when the Body fails, Soul + Avatar + Name migrate together to a new Body — same Robot, new vessel. only the Body dies.

the shape is fractal. a person is a Robot. a DAO is a Robot. a city is a Robot. a network state is a Robot. each holds Neurons that hold Addresses that hold balances. Body, Soul, Avatar, and Name scale up: at institutional scale Body becomes infrastructure, Soul becomes the founding-Neuron cluster, Avatar becomes the brand and culture, Name becomes the on-chain identifier of the entity.

---

## 2. agency — the five primitives

every action of every entity at every scale reduces to a configuration of five primitives:

| primitive | role |
|---|---|
| Goal | what we want (orientation: Maintain, Achieve, Avoid) |
| Task | what we do (an instance pursuing a Goal) |
| Skill | how we are able (a capability) |
| Event | when something happens (an atomic trigger) |
| Sensor | what perceives (subscribes to a stream) |

Sensors carry a reaction taxonomy:

- Block — reject the operation (constraint, principle, commitment guard)
- Notify — emit signal (alarm, KPI breach)
- Materialize — instantiate a Template with resolved arguments (schedule, deadline fire, dependency unlock)

three variants are first-class because the economy depends on them:

- Intent — `Task<atomic, reserves_inputs>`. a proof in progress. reserves inputs, locks balances, commits or rolls back at workflow transition
- Template — `Skill<parameterized>`. a recipe that materializes concrete Tasks when invoked with arguments
- Schedule — `Sensor<source=Clock, reaction=Materialize<Template>>`. the time-stream variant. cron, deadlines, recurring instantiation all collapse to this

the same Sensor primitive expresses principles (Block), KPIs (Notify), and schedules (Materialize). different reactions, one concept.

---

## 3. sigma — what an entity holds

Sigma is the sum of holdings across all networks. it is the conserved quantity against which every Task burns and every Skill executes. when Sigma reaches zero, the entity dies.

Sigma is denominated in Tokens. Tokens have exactly two natures:

| nature | conservation | examples |
|---|---|---|
| Coin (TSP-1) | Σ balances = supply | currency, weight units, credits, shares |
| Card (TSP-2) | owner_count(id) = 1 | persons, slots, contracts, titles, permits |

every entity is a Card. every fungible holding is a Coin balance. accounts, assets, and registries are not separate systems — they are views over Cards holding Coin balances and references to other Cards.

at state scale, Cards specialize into recognizable types — currency, title, permit, credential, vote, claim, share, record. each is a Card with a configured trait profile (see §5). different names, same nature.

---

## 4. PLUMB — the five operations

every state change is one of five atomic operations:

| operation | what it does |
|---|---|
| pay | transfer Coin balance between Cards |
| lock | constrain a Token (install a Sensor, set a floor, freeze) |
| update | change configuration (rotate authority, install or remove traits) |
| mint | create a new Token instance |
| burn | destroy a Token instance |

every operation has hooks where Sensors install. an Intent is one or more PLUMB operations composed atomically — they all commit or none do.

the entire economy reduces to sequences of these five.

---

## 5. the accounting projection

soma sees an entity through the cognitive lens. system sees the same entity through the accounting lens. both views apply to the same Card. they are orthogonal projections, not nested layers.

the accounting projection classifies primitives into five trait categories:

| trait category | what it classifies | ledger role |
|---|---|---|
| skills | revenue-generating Skills | income — credit |
| duties | constraint Sensors with Block reaction | obligation — debit |
| senses | information-input Sensors | operating cost — debit |
| bonds | directional relationships (Addresses with direction) | receivable / payable |
| memory | accumulated Task proofs | retained earnings |

the accounting identity holds by construction:

```
revenue-Skills + information-Sensors + receivables
   =
constraint-Sensors + payables + nature
```

every receivable on one side is a payable on the other — double-entry expressed at the primitive level.

each category composes by its own algebra:

| category | composition |
|---|---|
| revenue Skills | additive — combine freely |
| constraint Sensors | conjunctive — all must hold |
| information Sensors | disjunctive — either provides |
| relationships | structural — independent axes |

contradictions surface at install time. a permanent-hold constraint cannot coexist with a liquidity Skill on the same Card — both proofs cannot simultaneously hold. the type system rejects it before deployment.

balance sheet, profit and loss, cash flow are not separate systems — they are views derived from the trait profile and ledger slice.

---

## 6. coordination — the five storage shapes

an entity does not act alone. coordination happens through the [[cybergraph]] — a shared substrate with five storage shapes:

| shape | stores | content |
|---|---|---|
| Graph | Neurons and relationships | who exists, who is linked |
| Tokens | Sigma denominations | what value moves |
| Workflow | Skill compositions and Intent state machines | how Tasks execute |
| Calendar | Event timestamps and Sensor firing windows | when Tasks fire |
| Documents | Sensor outputs and Task proofs | that Tasks happened |

these are not new concepts. they are the on-chain encoding of the agency primitives at sovereign scale. Graph stores Neurons. Tokens denominate Sigma. Workflow stores Skills. Calendar timestamps Events. Documents prove Tasks completed.

every relationship has a type, a quantity, a validity window, and a history. every workflow step has a schedule and a deadline. every document is append-only and signed.

a workflow is a state machine attached to an Intent type. transitions declare source state, target state, which operations commit on transition, who is authorized, and what conditions must hold. proposal modules, approval ladders, escalation paths — all configurations of workflow transitions.

---

## 7. higher-order patterns

the primitives compose into named patterns recurring at every scale. these are the standard library:

| pattern | composition |
|---|---|
| Product | Card + revenue-Skill + sale-Template + metadata |
| Process | composite Skill + (optional) Schedule + (optional) Template |
| Project | Card container + Sigma budget + relationships + sub-Intents + workflow |
| CommitmentGuard | constraint Sensor on pay_hook + floor + beneficiary signature requirement |

CommitmentGuard expresses a powerful idea: assurance without escrow. the floor holds against any pay that would breach it; the Card's balance stays usable for governance, lending, staking — only pays that violate the floor fail to produce a valid proof. capital commits without locking.

new patterns join over time (subscription, partnership, campaign, membership). the primitives stay constant.

---

## 8. scale — same architecture, three lenses

the protocol is fractal. the same primitives instantiate at every scale of organization:

| primitive | individual | institution | state |
|---|---|---|---|
| Goal | "build a cube" | "operate cyber valley" | "give every resident pension" |
| Task | "compile step" | "Q2 milestone" | "process land.buy(parcel#42)" |
| Skill | "run inference" | "operate marketplace" | "issue title transfer" |
| Event | "model finished" | "milestone reached" | "tax deadline" |
| Sensor | "memory low" | "budget exceeded" | "fraud detected" |
| Sigma | balance across networks | treasury + assets | reserves + GDP |

at the institutional scale, seven lenses organize the primitives. they are not new concepts — they are agency viewed through institutional eyes:

| lens | maps to |
|---|---|
| Purpose | root Goal (cannot be closed) |
| Principles | constraint Sensors (Block reaction) |
| People | Neurons + Skills |
| Products | maintained Goals + revenue-Skills |
| Processes | composite Skills + Schedules |
| Projects | Task clusters with Sigma budget |
| Portfolio | Sigma |

strategy, roadmap, OKR, SOP, role, team, budget, KPI, risk, equity, debt, revenue, cost — every common org concept reduces to one of these seven lenses.

---

## 9. sovereignty — the state as Skill catalog

at state scale the protocol exposes specific Skills as methods residents can invoke. a state is fundamentally a Card factory. it mints Cards (passports, permits, titles), denominates Coins (currency, taxes, transfers), and maintains the authoritative ledger.

residents relate to a state through tier depth. each tier is a superset of the previous:

| tier | duration | Tokens available |
|---|---|---|
| VISIT | days/weeks | entry permit, emergency care, temporary credentials |
| STAY | months/years | bank account, work permit, business registration |
| SETTLE | years/decade | property title, permanent residence, pension rights |
| BELONG | forever | passport, voting rights, candidacy |

tiers are a permission model — they determine which Skills a Neuron can call. moving up the tiers is a one-way ratchet earned through demonstrated commitment.

states nest in jurisdictional hierarchy: planet → treaty body → state → region → municipality → parcel. rules cascade from parent to child; the more specific level overrides for its scope. navigation is voluntary — every entry is consent, every exit is withdrawal. the only involuntary subscription is birth.

every state offers the same Skill catalog. states differ only in configuration: tier requirement, cost, time, prerequisites. this configuration space is the complete product catalog of human governance.

---

## 10. markets — price discovery on every asset

every excludable Skill the entity offers can be priced and sold. one mechanism prices every horizon, every audience, every claim type.

three orthogonal axes partition every good:

| axis | question | examples |
|---|---|---|
| excludability | can non-payers be denied? | concert ticket vs atmosphere |
| sharing dimension | time or space? | banya hour (time) vs citizenship (space) |
| fungibility | interchangeable units? | gravel by tonne vs apartment 5B |

the two non-trivial axes yield four product cells:

|  | Slot (time-shared) | Spot (space-shared) |
|---|---|---|
| Fungible | commodity (gravel, water, compute credits) | subscription (LLM calls, storage GB-months) |
| Non-fungible | unique booking (banya Saturday 14:00) | unique membership (citizenship #7) |

four cells, two Token natures (Coin for fungible Claims, Card for non-fungible), one protocol.

### the unit

every Asset is a Card. every Claim against an Asset is either a Card (non-fungible) or a Coin balance (fungible). every Issuance is a batch of Claims with shared rules.

### the valuation oracle

every Asset has a single observable valuation derived from on-chain cash flow:

```
V = annual_gross_revenue / r
```

`r` is the gross capitalization rate, set per asset class. it absorbs the investor risk premium and the expected operating margin in one number. no declared expenses, no off-chain attestation — only revenue events on the ledger.

the owner declares two numbers — reserve and premium — and the auto-listing maintains one active ask:

```
current_ask = max(reserve, V × (1 + premium))
```

`V` prices observable cash flow today. `premium` prices the owner's belief in future growth. the separation is honest: objective and subjective each have their own slot.

### the pricing stack

for Slot Assets, three layers compose:

| layer | direction | mechanism |
|---|---|---|
| term structure | longer windows clear cheaper per-unit | the duration-discount curve |
| utilization premium | scarcity pushes price up | bonding curve on capacity-used |
| flexible preemption | reallocates to higher-value use | Flexible Claims preempted by higher bidder |

for Spot Assets, tier curves replace calendar overlap, and tier escalation lets holders upgrade by paying the differential.

### claim classes

every Claim is one of two:

- Guaranteed — full price, locked until expiry, no preemption
- Flexible — discounted, preemptable. a later buyer acquires the Claim by paying original price plus configured premium to the holder

certainty is a product. optionality is a product. owner offers both, market chooses the mix.

### audiences

per-Asset discount classes (resident, builder, founder, solidarity). one discount per Claim — `max(category, audience)`, not additive. gating is configurable: operator-enforced, on-chain allowlist, or credential badge.

### network effects

non-fungible Spot Assets compound through the oracle. every new citizen makes citizenship more valuable to existing holders. higher membership produces more renewal revenue, raises V, raises current_ask for new Claims. the mechanism captures the network effect as real revenue rather than declared opinion.

---

## 11. survival — the metabolism

an entity is alive when:

```
energy > 0  AND  Sigma > 0
```

energy is the immediate need — metabolism to be alive now. Sigma is the long-term guarantee — what the Soul holds across networks.

when energy crosses critical, the entity posts a bounty against future Sigma and goes dormant. a neighbor may revive it by fulfilling the bounty; Sigma transfers, energy restores, the entity lives. when both energy and Sigma reach zero, the entity dies.

the logic is identical at every scale. a Robot running soma trades compute for Sigma on the energy market. an institution survives when revenue from Products exceeds the cost of Processes. a state survives when gross revenue sustains its obligations.

at the state scale, three vital signs compose into a metabolic oracle:

```
M = cap^w_c × syntropy^w_s × happiness^w_h
```

| signal | what it measures |
|---|---|
| cap | external validation — market price of the state's Coin |
| [[syntropy]] | internal order — KL divergence of focus from uniform |
| [[happiness]] | subjective wellbeing — stake-weighted private survey |

the derivative Ṁ is the reward signal. all subordinate agents optimize for rising M. gaming one signal at the expense of others lowers the compound — the three weights are the only normative choice the system cannot make autonomously.

---

## 12. conservation

four laws hold the protocol together. violation is impossible because the proof system rejects any operation that breaks them:

| law | statement |
|---|---|
| Sigma conservation | every pay has exactly one source and one destination |
| Token conservation | Σ holdings(coin) = mints − burns; mints and burns are explicit operations between designated source and sink Cards |
| Identity conservation | Robot persists across Body replacement; Soul + Avatar + Name migrate together |
| Accounting conservation | assets = liabilities + equity; derivable as a view from any Card's trait profile and ledger slice |

provability replaces enforcement. the laws are not rules a validator checks — they are properties the proof system cannot produce a witness against.

---

## related

- [[cyberia/protocol/marketplace]] — the marketplace protocol in detail
- [[cyberia/protocol/marketplace-spec]] — contract interfaces and data structures
- [[cyberia/foundation/governance]] — the 147 agents and the capitulation curve
- [[cyberia/foundation/org]] — the seven lenses applied to specific cyberian entities
- [[soma]] — the agent runtime that exercises these primitives
- [[cyber]] — the underlying [[cybergraph]] substrate

---

discover all [[concepts]]
