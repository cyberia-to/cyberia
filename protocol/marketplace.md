---
tags: cyberia, system, marketplace, protocol
alias: marketplace, asset marketplace, cyberia marketplace, claim protocol
crystal-type: pattern
crystal-domain: cyberia
---
# marketplace

universal protocol for selling time-horizoned access to any asset. one contract architecture, one valuation oracle, one set of rules — venues, citizenship, memberships, subscriptions, commodities, licenses, and every other excludable good cyberia produces.

the demand for the citizenship and residency claims priced here is mapped in the [[migration market model]]: a ~900M want-to-leave market against a shrinking global supply of rooting, which is why a well-run sovereign asset compounds.

owner sets two numbers (reserve, premium). everything else clears against observed market demand.

built on [[cyberia/protocol/system]] (TSP-1/TSP-2 + PLUMB + traits). runs as CosmWasm contracts on [[bostrom]]. revenue settled in USDT bridged from ethereum.

→ for contract interfaces and data structures see [[cyberia/protocol/marketplace-spec]]

**design principle.** the protocol is either game-theoretically sound or it isn't. there are no simplified early versions where the economics are wrong and fixed later. deployment is staged by which assets go live — banya before citizenship, citizenship before bulk commodities. the protocol itself is complete and correct from the first contract instantiation.

---

## the problem

every asset cyberia sells faces the same fundamental question: what is the right price across every possible time horizon?

a banya can be rented by the hour, the day, the week, the month, the year, the decade, or sold outright. about ten such horizons exist. the owner does not know the optimal price at any of them, because price is not a property of the asset — it is a function of demand that nobody can know in advance.

every existing approach asks the owner to declare prices and adjust them by hand. this fails because the owner is guessing across ten horizons under uncertain demand. yield-management software for hotels solves a similar problem with centralized opaque optimization. crypto can solve it with a transparent on-chain mechanism.

three properties wanted:
- the protocol discovers prices across all horizons including outright sale
- the owner makes the minimum number of decisions
- buyers get strong guarantees about their claims or pay for the option to release

---

## the typology

three independent axes partition every good. classical theory (Samuelson 1954, Buchanan 1965) uses two — rivalrous and excludable. marketplace design needs a third — fungibility.

| axis | question | yes | no |
|---|---|---|---|
| excludable | can non-payers be denied access? | concert ticket | atmosphere |
| slot / spot | is the asset shared across time or across space? | banya at 14:00 | citizenship |
| fungible | is one unit interchangeable with another? | cubic meter of gravel | apartment 5B |

**excludability** is the bouncer condition. without it the protocol cannot enforce payment. marketplace operates only on excludable goods; common-pool resources and public goods live under [[cyberia/policies]].

the remaining two axes — sharing dimension and fungibility — give four product patterns:

```
                       slot                         spot
                  (time-shared)                (space-shared)
                     ┌────────────────────────────┬────────────────────────────┐
                     │ commodity                  │ subscription                │
   fungible          │  — gravel by cubic meter   │  — LLM call credits         │
   claims            │  — sand by tonne            │  — query credits            │
                     │  — generic parking spot     │  — storage GB-months        │
                     ├────────────────────────────┼────────────────────────────┤
                     │ unique booking             │ unique membership           │
   non-fungible      │  — banya Saturday 14:00    │  — citizenship              │
   claims            │  — apartment 5B            │  — board treasurer          │
                     │  — concert row 1 seat 5    │  — founding member #7       │
                     └────────────────────────────┴────────────────────────────┘
```

four cells, two token shapes, one protocol.

**slot** assets are shared across the **time axis** — different holders occupy the asset in sequence, each in their own exclusive window. capacity is enforced by a calendar: no two claims may overlap.

**spot** assets are shared across the **space axis** — N holders occupy the same asset simultaneously, each holding their position alongside the others. capacity is enforced by tier counts: each tier has a cap, and the count must not exceed it.

**fungibility maps to token type.** fungible claims are balances on a TSP-1 Coin — interchangeable, sold by quantity. non-fungible claims are individual TSP-2 Cards — each has identity, each is unique. the asset itself is always a TSP-2 Card: one entity, one owner.

the kind and fungibility flags are orthogonal. a slot asset can issue fungible claims when time-windows are commodified (parking lot: generic access credits, allocated at redemption). a spot asset can issue non-fungible claims when membership has identity (numbered citizenship #1–#147). no constraint.

---

## price discovery

### slot: competing horizons

a slot asset has one calendar and many competing horizons. the banya's April can be sold as 720 individual hours, 30 days, 4 weeks, or one month. each horizon is a legitimate claim on the same underlying resource. the protocol must price all of them simultaneously and let the market choose.

**the term structure of slot prices**

per-unit price decreases with duration. the buyer of a long window accepts a lower per-hour rate in exchange for certainty of access — they do not need to re-book. the seller accepts lower per-hour revenue in exchange for certainty of occupancy. this is the same trade-off as short vs long rates in fixed income: short rates are higher because the lender stays flexible; long rates are lower because the borrower gets stability.

```
price_per_hour(duration) = base_rate(utilization) × duration_factor(duration)

duration_factor is a decreasing schedule set per asset:
   1 hour    → 1.00   (spot rate)
   8 hours   → ~0.85
   1 day     → ~0.75
   1 week    → ~0.60
   1 month   → ~0.50
   1 year    → ~0.40
```

the owner sets these factors at asset creation. the market validates them through revealed demand: if weekly bookings fill instantly while hourly slots sit empty, the weekly factor is too low and should be raised.

**utilization premium**

the base rate rises as the calendar fills. a nearly-booked banya is scarce; the last available windows command a premium. the bonding curve handles this: `base_rate = curve.price_at(utilization)` where utilization is hours booked divided by total hours in the booking window. the two forces compose: duration pushes price down, scarcity pushes price up.

**flexible preemption as the reallocation layer**

duration discounts and utilization pricing still leave a residual problem: a cheap long booking sold under low demand may block higher-value short bookings that arrive later.

flexible claims close this gap. the long-term holder bought at the prevailing rate and accepted preemption risk. when high-value short-term demand spikes, a new buyer preempts the flexible holder: pays the holder their original price plus a configured premium (the holder profits from having provisioned liquidity) and pays the owner the incremental revenue above the original price. the window realloc­ates to its highest-value use.

the three layers together — term structure, utilization curve, flexible preemption — make the slot calendar self-optimizing without requiring the owner to forecast demand or solve an allocation problem explicitly.

### spot: tier clearing

spot assets have no calendar. the optimization problem is tier pricing: how many holders at each tier, at what price.

each tier has its own bonding curve: as spots are claimed, per-spot price rises within the tier. early joiners pay less, late joiners pay a scarcity premium. the curve calibrates new entrant price to remaining capacity — a tier at 90% of cap is more expensive to join than one at 10%.

tier escalation allows existing holders to upgrade from a lower tier to a higher one by paying the differential. this prevents lock-in and lets the asset organically deepen holder commitment over time without re-issuance.

for spot assets with fungible claims (LLM credits, storage credits) the bonding curve is the AMM: it provides liquidity for any quantity without an order book. buyer pays the integral of the curve from current supply to current supply + N. this is the only case where the curve acts as a traditional AMM; for NF claims (slot or spot) the curve is a utilization-indexed price schedule, not a liquidity pool.

---

## the valuation oracle

**the core mechanism.** one number per asset, derived entirely from observed on-chain cash flows. no owner declaration required.

```
annual_GR  = realized(now − 365d → now) + pipeline(now → now + 365d)
V_implied  = annual_GR / r
```

where `r` is the asset's **gross cap rate**, set at creation and expressed as `cap_rate_bps / 10_000`.

### gross revenue, not net income

real estate valuation normally uses `NOI / r_net` (net operating income — revenue minus expenses). this protocol uses `GR / r_gross` (gross revenue). not a mistake — a deliberate choice with full economic equivalence.

the substitution:

```
NOI = GR × (1 − opex_margin)
V   = NOI / r_net
    = GR × (1 − opex_margin) / r_net
    = GR / r_gross

where  r_gross = r_net / (1 − opex_margin)
```

the gross income multiplier (GIM = 1 / r_gross) is a standard commercial real estate screening tool. it collapses both the discount rate and the expected OPEX margin into one calibrated number per asset class. the two formulations are identical — the choice is which inputs are easier to observe.

**why GR rather than NOI:**

OPEX (wages, utilities, maintenance) is off-chain. there is no trustworthy way to record it in contract state without a second oracle, off-chain attestation, and dispute resolution. GR is the sum of executed payment transactions, fully on-chain, unmanipulable: every revenue event calls `RecordRevenue` when funds arrive.

there is also a manipulation-resistance argument. if V_implied used declared OPEX, an owner targeting a cheap buyout could inflate OPEX → suppress V_implied → set reserve at the depressed number. GR removes this attack surface entirely.

### cap rate calibration per asset class

`r_gross` absorbs both the investor risk premium and the expected OPEX margin for the asset class. the DAO configures defaults; individual assets can override within a permitted band:

| asset class | r_net | OPEX margin | r_gross | GIM |
|---|---|---|---|---|
| land | 3–4% | ~0% | 3–4% | 25–33× |
| residential / glamping | 5–6% | 30–40% | 8–10% | 10–12× |
| event space / banya | 5–7% | 40–50% | 9–12% | 8–11× |
| spot membership | 5–6% | 20–30% | 7–9% | 11–14× |
| sovereign / citizenship | 4–5% | 15–25% | 5–7% | 14–20× |
| digital services | 8–12% | 10–20% | 10–15% | 7–10× |
| commodity / bulk | 6–8% | 30–40% | 10–13% | 8–10× |

example: banya, 45% OPEX margin, r_net = 5.5%. r_gross = 5.5% / (1 − 0.45) = 10%. GIM = 10×. a banya generating $100k/year in gross revenue implies V = $1M.

### backward + forward GR window

```
realized   = sum of RevenueSamples in trailing 12 months (on-chain)
pipeline   = sum of committed revenue from approved issuances
             whose windows fall in the forward 12 months
```

the two-year window smooths seasonal variance. a summer camp looks similar in July (high pipeline) and January (high trailing). a monthly subscription service produces stable GR year-round.

**new assets:** V_implied = 0 until revenue history accumulates. auto-listing collapses to `reserve_price`. this is correct: no market evidence exists yet. the owner's floor governs.

### growth and optionality

the formula assumes no perpetual growth (g = 0 in the Gordon growth model). for assets where appreciation is expected — citizenship of a growing network state, founding membership slots — the owner demands `premium_bps` above V_implied. the separation of concerns:

- V_implied prices today's cash flows: objective, on-chain, unmanipulable
- premium_bps prices the owner's belief in future growth: subjective, declared, transparent

---

## auto-listing

owner declares two numbers. contract maintains one active ask:

```
current_ask = max(reserve_price, V_implied × (1 + premium_bps / 10_000))
```

the ask drifts with demand. owner revisits once a year at most.

**why the discount-rate differential makes this work.** buyer and seller both want to transact; the gap between their private discount rates creates surplus. example:

```
seller r = 8%  →  V_implied = $100k / 0.08 = $1.25M
buyer  r = 5%  →  private V = $100k / 0.05 = $2.00M
surplus: $750k between them
```

seller sets `premium_bps = 2000`. current_ask = $1.25M × 1.20 = $1.50M. buyer acquires the asset $500k below private value. seller captures $250k above oracle value. premium_bps determines where in the surplus the deal clears.

when an asset sells: active issuances continue under new owner. existing claims persist as obligations. forward pipeline accrues to the new owner.

---

## claim classes

two classes, orthogonal to every other dimension. both slot and spot, both non-fungible and fungible assets support both.

**Guaranteed** — full price. once paid, the claim is yours until expiry. no preemption. for slot: window locked. for spot: seat locked. certainty as a product.

**Flexible** — discounted (e.g. 30% off). preemptable: a later buyer acquires your claim by paying your original price plus a configured premium. optionality as a product.

the carry trade for Flexible holders: buy cheap when demand is low. when demand spikes, a higher bidder preempts you. you pocket original price plus premium — a net profit on a temporary hold. this is rational if you do not need the slot with certainty.

owner benefits twice from Flexible: fills the calendar faster at lower price point; collects incremental revenue on preemption when demand rises.

operators choose which class to offer per issuance. both are in the contract from deployment.

---

## audiences

per-asset discount classes. declared at the asset, snapshotted into each issuance at submit time. protects buyers from mid-flight changes.

examples:
- venue: resident −50%, builder −30%, student −10%
- citizenship: solidarity −70%, professional −20%
- gravel: bulk-order −15%, builder-cooperative −10%
- LLM credits: founder −80%, employee −50%, contributor −30%

one discount per claim: `max(category_discount, audience_discount)`. not additive.

gate options: operator (bot-enforced), on-chain allowlist, credential NFT badge. all three are in the contract; operators choose per asset.

---

## the bridge

revenue settles in USDT on ethereum. bostrom side works in a bridged cw20:

```
ETH treasury (USDT)  →  off-chain relayer set  →  cw-bridge-eth  →  cw-usdt
```

cw-bridge-eth requires k-of-n attestor agreement before minting. each relayer independently calls `Attest` with the same (tx_hash, recipient, amount). the contract counts confirmations; mint executes when the k-th unique attestor confirms. duplicate confirmation from same attestor is rejected. single-key control of the money supply is not acceptable for state infrastructure regardless of deployment stage.

withdrawal mirrors: holder burns cw-usdt with `eth_recipient`, relayers observe the burn event and pay USDT on ethereum. withdrawal likewise requires k-of-n co-signing before payout.

---

## network effects

non-fungible spot assets compound differently than other cells. each new citizenship holder or lifetime member makes the asset more valuable to existing ones. this flows through V_implied: more holders → more renewal GR → higher V_implied → higher current_ask for new claims. slot assets cap at one holder per time window. fungible assets show a softer version — more consumers do not change per-unit value. non-fungible spot is where network effects compound hardest and the oracle captures them most cleanly.

this is why high-quality spot assets — citizenship of a prospering state, membership of a thriving guild — can achieve high V_implied per claim. the formula is not wrong: the network effect is real revenue.

---

## deployment sequence

all contracts and mechanisms deploy together. stages describe which asset types go live, not which features switch on.

```
A  Slot + NF      venue bookings, events, physical spaces
B  Spot + NF      citizenship, residency, memberships, credentials, permits
C  Slot/Spot + F  commodity economy: aggregates, water, compute credits
D  Hybrid         bonded access (spot membership unlocks slot booking)
E  order book     richer NF price discovery
F  combinatorial  package bid allocation
```

stage A = first ship; oracle live, V_implied = 0 for new assets is correct. stage B = first programmatic visa — machine-verifiable on-chain rights to belong. stage C = every unit cyber valley produces becomes a redeemable claim.

---

## related

- [[cyberia/protocol/marketplace-spec]] — contract interfaces, data structures, message types, implementation sequences
- [[cyberia/protocol/system]] — ERP kernel: TSP-1/TSP-2, PLUMB, traits, intents, workflows
- [[cyberia/foundation/architecture]] — agent organization; agents own and operate asset instances per zone
- [[cyberia/protocol/services]] — 81-method state API with tier model (VISIT, STAY, SETTLE, BELONG). marketplace implements `identity.enter`, `identity.register`, `identity.issue_passport` as Spot asset ExecuteMsgs
- [[cyberia/foundation/whitepaper]] — the cyberstate vision; marketplace is the economic core that makes it computable

---

discover all [[concepts]]
