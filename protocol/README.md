---
tags: cyberia, protocol, core
alias: cyberia protocol, protocol
crystal-type: pattern
crystal-domain: cyberia
crystal-size: deep
status: proposal
---

# cyberia protocol

what cyberia adds on top of the [[cyb/robot]] architecture to become a sovereign network state. two layers: sovereignty (the state as a Card factory with tiers and jurisdictions) and markets (universal price discovery on every excludable Skill the state offers).

Both layers follow [cyb anatomy](../../cyb/anatomy.md) and
[architecture](../../cyb/specs/architecture.md). A named robot attaches neurons;
soul configures behavior, soma performs cognition, avatar visualizes the robot
and body supplies devices/resources. Progs and tasks carry work IDs and retained
state. Neurons carry authenticated authority. Sigma manages qualified subjects
and assets; ward checks grants and vault performs scoped key operations.

Coins, Cards, PLUMB operations and the accounting projection are application
contracts. Their [domain roles](../../cyber/specs/domain-ladder.md) distinguish
service, token book/issuer, graph partition and runtime work. This document
proposes a governance/economic profile; adoption and enforcement follow each
named network and legal wrapper.

---

## 1. sovereignty — the state as Skill catalog

At state scale, services expose Skills residents can invoke. A state robot
coordinates the progs that issue Cards (passports, permits, titles), account for
Coins and retain their complete obligations. Issuer authority belongs to named
neurons or an explicit collective policy. The state name and each service/role
ID remain application data. Each mint, transfer and governance action captures
its subject, network, payload and current grant before execution.

residents relate to a state through tier depth. each tier is a superset of the previous:

| tier | duration | Tokens available |
|---|---|---|
| TOUCH | hours | day entry, picnic, short trail |
| VISIT | days/weeks | overnight, events, temporary credentials |
| STAY | months/years | bank account, work permit, longer housing |
| SETTLE | years/decade | property title, permanent residence, pension rights |
| BELONG | forever | passport, voting rights, candidacy |

full funnel: [[ladder]]

Tiers supply credential conditions for the Skills a neuron may invoke. A
verified tier is checked alongside the current action grant and the service's
admission policy; a role label alone grants no execution access. The proposed
tier progression is a one-way ratchet earned through demonstrated commitment,
with revocation, credential expiry and legal exceptions specified separately.

states nest in jurisdictional hierarchy: planet → treaty body → state → region → municipality → parcel. rules cascade from parent to child; the more specific level overrides for its scope. navigation is voluntary — every entry is consent, every exit is withdrawal. the only involuntary subscription is birth.

every state offers the same Skill catalog. states differ only in configuration: tier requirement, cost, time, prerequisites. this configuration space is the complete product catalog of human governance.

---

## 2. markets — price discovery on every asset

every excludable Skill the state offers can be priced and sold. one mechanism prices every horizon, every audience, every claim type.

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

exclusive **where** (volume in a frame) is not the same as exclusive **when** (calendar on an asset). spatial title invariants — pairwise disjoint solids, deposit challenges, TSP-2 Cards — live in [[space accounting]].

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

## related

- [[cyb/robot]] — the Robot architecture this protocol assumes
- [[cyberia/protocol/system]] — minimal ERP on tokens (Coin · Card · PLUMB · Template · Intent · View)
- [[orgs]] — world construction / entities & skills (was erp-core)
- [[cyberia/protocol/bank-above-banks]] — solvent synthetic FX for all sovereign currencies against one ETH reserve
- [[cyberia/protocol/marketplace]] — the marketplace protocol in detail
- [[cyberia/protocol/marketplace-spec]] — contract interfaces and data structures
- [[cyberia/protocol/maps]] — nested spatial scales (sector · block · district · region)
- [[ladder]] — VISIT → STAY → SETTLE → BELONG (the fundamental funnel)
- [[cyberia/foundation/governance]] — the 147 organizational roles and the capitulation curve
- [[cyberia/foundation/org]] — the seven lenses applied to specific cyberian entities
- [[soma]] — cognition, durable tasks and tool orchestration over neuron execution

---

discover all [[concepts]]
