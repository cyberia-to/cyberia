---
tags: cyberia, protocol, money, fx, eth, solvency
alias: bank above banks, synthetic fx, c-currency bank
crystal-type: pattern
crystal-domain: cyberia
crystal-size: deep
---

# A Bank Above Banks

## A Solvent Synthetic FX System for All Sovereign Currencies, from First Principles

---

## Abstract

This paper derives, from five axioms, a system that mints, quotes, and market-makes synthetic versions of every sovereign currency against a single external reserve (ETH). The system is an offshore central bank for the long tail of world money: a price-taker toward liquid currencies, a price-maker toward illiquid ones, and in either regime governed by one number — the stress coverage ratio of full redemption against reserve. Its entire operation reduces to four recurring verbs, its accounting to three temperatures and one contract, its solvency audit to one division. The design optimizes for exactly two properties, in order: **reliability** (survive a full redemption run) and **simplicity** (every rule statable in one sentence, auditable in one query). Everything else — capital efficiency, profitability, reach — is derived, not assumed. One derivation deserves the abstract: over-collateralization cannot be funded by customers, so a first-loss equity tranche is the system's rate limiter — float capacity is a fixed multiple (≈2.5–4×) of equity, and growth is equity plus retained profit, nothing else.

---

## 1. Axioms

**A1 — One external truth.** Exactly one asset is not priced by the system: the reserve asset. Every objective statement — profit, solvency, model validity — must be denominated in it. Statements denominated in self-issued tokens at self-quoted prices are opinions. *(Why ETH and not a basket: a second reserve asset creates a second truth, and two truths require a third to arbitrate them. The cost of one volatile truth is a haircut; the cost of plural truth is epistemology. We pay the haircut.)*

**A2 — Minted liquidity is free until it escapes.** For a pair where both sides are self-issued, depth costs nothing to create; a token becomes a liability only when it leaves system custody. Therefore the liability ledger is **escaped float**, not pool size, and depth limits are drainage quotas against reserve, not capital allocations.

**A3 — Ranks are more stable than prices.** The capitalizations of sovereign monies (M2 × FX) follow a power law over rank, and rank ordering moves over years while prices move over hours. Deviations from the rank-implied capitalization are tension that discharges through the fast variable — the exchange rate. Fair value can therefore be *computed*, with own order flow as the refining signal.

**A4 — Topology is discovered, not designed.** Which currencies are hubs, which pairs deserve direct markets, which denominations deserve direct reserve convertibility — all are outputs of the measured flow graph, recomputed on schedule. Committees do not appoint structure; data does.

**A5 — Profit is what has left the building.** Realized reserve extracted, net of growth in outstanding liabilities. Mark-to-model gains are not profit; float expansion is not profit; only `ΔReserve − ΔLiabilities` is.

One meta-rule binds the axioms: **fast risk, slow price, slower meter.** Spreads and inventory adapt in hours; quoted fair value in weeks; the unit of account and the topology in years. No two control loops may share a time constant — shared time constants are how systems chase their own tails.

---

## 2. The Balance Sheet

### 2.1 Assets: one reserve

A single ETH balance sheet — constitutionally singular. Wherever the system later opens multiple conversion facilities, they are windows onto this one pot; there is no window that can fail separately, and none that can be defended separately.

### 2.2 Liabilities: escaped float

`F_i` = tokens of currency *i* held outside system-registered addresses. The registry of system addresses is published on-chain, so the liability ledger is publicly computable — `F_i = totalSupply_i − Σ balanceOf(system)` — and the solvency constraint below is auditable by anyone in one query.

### 2.3 The invariant (constitutional)

```
Σ_i  F_i · P_i   ≤   R_ETH · (1 − h)
```

with `P_i` the fair value of currency *i* in ETH terms and `h` a haircut covering reserve volatility over the redemption horizon. Every spoke receives a drainage quota `α_i · R_ETH·(1−h)`, `Σα_i ≤ 1`, enforced mechanically (§5.3).

### 2.4 The material risk: the mismatch is the bank

Liabilities are fiat-indexed; the asset is ETH. The bank is structurally long-ETH/short-fiat — and the correlation is wrong-way: in a crypto crash, flight-to-stables **expands float exactly when the reserve contracts**. SCR is hit from both sides at once, and a static haircut assumes precisely the independence that fails in that moment. This is the single largest risk in the design and it cannot be engineered away, only priced and bounded: `h` is dynamic (conditioned on the reserve drawdown regime), the float/reserve ratio is hard-capped, and staking yield on reserve may partially offset. The gas market shares the same wrong-way shape — fees spike 10–100× exactly during stress — so conversion bandwidth must be budgeted at stress prices, not average ones (§6.5).

### 2.5 Equity: who holds the first loss

The invariant plus the buffer imply a capital structure the naive design forgets. A user who buys through the window pays 1 ETH for 1 ETH of float: issuance at par makes R = F exactly — which already violates `R·(1−h) ≥ F` and misses `SCR ≥ 1+β` by ~40%. Over-collateralization cannot come from the customers; it must be pre-funded by a **junior equity tranche** that absorbs the wrong-way risk and every model error before any holder does. The consequences are the business plan:

```
Float capacity:   F_max = E / (h + β)      ≈ 2.5–4 × equity
```

**Equity — not gas, not depth, not model quality — is the rate limiter of the system.** Growth = raising ETH equity + retaining Π_true; nothing else expands capacity. The return statement is equally clean: equity is ETH-denominated, so the hurdle rate is simply holding ETH, and any sustained `Π_true/E > 0` clears it — a levered (≈3×) fee-and-seigniorage business whose leverage is capped by the constitution rather than by a risk committee's mood. The junior tranche is explicitly first-loss against: reserve drawdown beyond h, maker-regime model error (§7.2), and stress-gas costs of the resolution queue.

### 2.6 The resolution regime (constitutional)

What happens at insolvency must be written before it happens. On breach of SCR < 1, conversion switches from continuous convertibility to a **pro-rata queue at a single clearing price**: every claimant in the epoch receives the same ETH per unit of value, with no priority for speed. A run is rational only because the first in line is paid in full; pre-committed pro-rata treatment deletes the first-mover advantage and with it the run equilibrium (Diamond–Dybvig suspension). The clause costs nothing in normal operation, must be immutable to be credible, and — a free side benefit — batches redemptions into few transactions exactly when per-transaction gas peaks.

---

## 3. The Market Structure

### 3.1 Hierarchy, because that is what money looks like

Real FX is not a star but a hierarchy of vehicle currencies — pivot languages of money: BRL/MXN intermediate Latin America, ZAR southern Africa, SGD Southeast Asia, AED the Gulf, RUB the CIS remittance zone, EUR the CFA orbit; some 15–20 currencies carry most cross-border flow. Because every internal pair is minted (A2), mirroring this topology is nearly free, and it pays three ways: quoting each spoke against the cross its economy actually thinks in minimizes residual oracle volatility (depth capacity scales as 1/σ_o², §5.1); flow signals arrive pre-segmented by real corridor (§4.4); and hub-basis noise for local use vanishes.

Tiers: **spokes** (all ~200 currencies) → **regional hubs** (~15–20, emergent) → **the hub unit cW** (one) → **conversion windows** (a computed set) → **reserve** (one).

Hubs are not appointed (A4): routing initially passes through model-mid multi-hop paths (internal hops free, one fee per route); the system measures betweenness centrality in the realized flow graph; a direct market opens when routed volume crosses a threshold — as an airline opens a direct flight. When the world shifts — a CNY corridor eating a USD corridor — the graph shows it before commentary does.

Since all pegs derive from one fair-value vector, triangular consistency is automatic. Topology governs not prices but: where direct markets stand, which external reference each spoke's price watches, how quotas cascade, and which cross the system exports to a region in maker regime.

### 3.2 The hub unit: cUSD now, a self-weighting index when the data asks

At launch the apex unit of account is simply **cUSD** — because the de-facto settlement mix is dollar-heavy, and shipping a composite whose initial weights ≈ the dollar is building a component for a future that has not asked for it. The index below stays in the design as a dormant formula with a measured trigger: it activates when the dollar's share of **our own flow graph** falls below a threshold — the same discovered-not-designed rule (A4) applied to the system's own favorite idea. When active, cW is not a committee basket but a formula:

```
w_i = Cap_i · φ(obs_i) / Σ_j Cap_j · φ(obs_j)     over the top-N currencies
```

`Cap_i` from the capitalization ledger; `φ(obs_i)` an observability weight — uniqueness and depth of the external price fix. *(Why observability and not convertibility: no token here redeems into its underlying — everything redeems into ETH — so home-country capital controls are irrelevant to redemption; what matters is whether the currency has one unambiguous measurable price. CNH qualifies the yuan at full weight; multiple-rate regimes are attenuated. Why not political freedom in the weights: freedom predicts where capital will flow — it belongs in the forecasting model as a predictor, not in the meter as a definition; a meter with politics in it is a meter someone will fight over.)*

Weights reset annually by formula from ledger data, six-month blend-in, off-cycle reset only on a rank transition within the top-N. Rebalancing a minted index costs no trades — its cost is informational (changing the meter shakes every measurement), hence the deliberately slow cadence. As dedollarization proceeds, weights migrate automatically: **the index encodes the transition instead of betting on its outcome.** Activation and weights are outputs of measured flow, never a launch decision.

### 3.3 Windows: computed convertibility

External value moves only through redemption windows — facilities converting cXXX ↔ ETH at model price ± spread against the common reserve. A denomination earns a window on three measurable conditions: top-tier **betweenness** in the payment graph; a deep single external **price** (CNH-grade); **p99 redemption demand** making a dedicated window cheaper for users than routing through cW. The set is recomputed annually. Aggregate window bandwidth: `Σ L ≥ p99(daily net outflow)/δ_max`. The window complex bears the system's entire real ETH-volatility cost (~σ²/8 of deployed reserve per year); concentrating all conversion through few windows is what lets fee income clear that hurdle.

### 3.4 Why underlying convertibility is not required

The system is a generalized eurodollar: offshore money whose value is accounting and settlement outside the home banking system, needing no license from the home central bank. Peg discipline requires not universal convertibility but a **credible marginal redeemer class** — the incumbent stablecoin holds its peg with retail redemption effectively closed, because arbitrageurs have credible access. Here redemption is permissionless through the windows: stricter discipline than the incumbent, by construction.

---

## 4. Price

### 4.1 Fair value: capitalization over supply

Forecast the capitalization, derive the rate:

```
FX*_i = C(rank_i) / M2_i,        C(r) = C₀ · r^(−α) · g(m_i)
```

`α` is fitted **exclusively on currencies where the system is a price-taker** — the curve's slope is never fitted to prices the system itself sets (this single quarantine rule is what keeps the model falsifiable, §8). `g(m)` corrects for monetization depth — M2/GDP spans ~30%–250% across countries; omit it and the curve permanently mispricing high-monetization economies bleeds against structure, not signal.

Why this trades (A3): rank moves over years, FX over hours; a currency off its rank-implied capitalization can adjust through M2 (months of printing) or FX (now). On a market-maker's horizon FX is the free variable — deviations are mean-reversion signals. Statistical arbitrage on the Zipf curve of sovereignty.

Circularity is broken by a **fundamental rank** predicted from non-price stocks (population, land, capital, freedom, openness). Two signals result: off-curve at correct rank → FX correction (fast book); on-curve at unearned rank → rank migration ahead (slow, positional book — a separable module, not required for solvency). Freedom and openness live here, as leading indicators of capital migration.

### 4.2 Three layers per currency

| Layer | Timescale | Content |
|---|---|---|
| A — structural | months | rank-implied cap; PPP residual; terms of trade; remittance base |
| B — proxies | days | hub crosses, NDFs, parallel rates, P2P-crypto rates — the best public shadow fix for dozens of countries |
| C — own flow | hours–weeks | Bayesian update from signed corridor flow; shrinks the residual over time |

Tier-1 currencies (liquid external cross) need almost nothing; tier-3 (fundamentals + own flow only) launch at maximum spread and minimum depth, relaxed as flow history accumulates. **That accumulated private corridor-flow history — not liquidity, which anyone can mint — is the real barrier to entry.**

### 4.3 Regimes: taker → maker

Per currency, the system is either disciplined by an external market or *is* the market. Live control uses two cheap signals: the **depth ratio** κ (cost to move price here vs. there; κ<0.1 pure taker, κ>1 the source physically cannot discipline us) and the **arbitrage flow sign** (takers get arbitraged toward the source; makers see their price carried outward). Information-share econometrics confirm at research cadence, not in the control loop. Transitions carry hysteresis — liquidity is sticky, so entry to maker at sustained dominance, exit only on deep loss of it.

The transition zone (0.1<κ<1) is the most dangerous state — the source can still jerk the price but is too thin to arbitrage us cheaply, so gaps live long and adverse selection peaks: cross it fast, at reduced depth and wide spread. In maker regime, adverse selection dies and **inventory risk replaces it** (no deeper market to close against); the external oracle becomes a circular reference and the fair-value engine takes over the peg.

### 4.4 Flow processing

Own flow samples the balance of payments with a bias: first-rate on capital/remittance flows (usually the marginal price-setter for small economies), weak on official goods trade. Discount apparent signal when our share of a corridor's total is itself growing — channel migration is not fundamentals.

Decompose by frequency; never pick one period. Hours–days is noise and toxicity — handled by spread and inventory, no fair-value content. Days–weeks is where information lives: persistent one-sidedness *after seasonal adjustment* (variance-ratio test: weekly net-flow variance ≫ daily) means the price is wrong — move it. Months–quarters is structure: subtract each corridor's flow calendar (remittance/harvest/tourism seasonality from central-bank data) before all tests, or seasonality masquerades as information; the residual updates Layer A.

The hard separation: one-sided flow means either the price is wrong (move it) or the price is right and the flow is structural (absorb it with inventory and spread). Layers A+B arbitrate as the prior against C. Confuse the cases and you either inject volatility the economy did not have, or absorb a real devaluation until the reserve breaks.

Feedback speed limit: in maker regime our quote changes the flow, and the economy reacts over weeks. Fair-value updates therefore carry a half-life ≥1–2 weeks, while spread and depth adapt within hours — the meta-rule of §1 applied where it matters most.

---

## 5. Operations

The venue is a shared-liquidity registry (1inch Aqua): the maker approves token balances once, ships strategies as immutable positions drawing on virtual balances, and tokens leave the wallet only at fill time — pulled and settled atomically **inside the resolver's transaction**. Three structural consequences, then the whole operation in four verbs.

### 5.1 Prices are pulled, not pushed

Strategies are immutable, so prices must not live in strategies — and they need not live on-chain at all. The system signs its fair-value vector **off-chain, continuously, for free**; the resolver attaches the latest signed price to the fill; the strategy verifies signature and staleness (~10k gas, paid by the resolver). Push-oracle costs go to zero, staleness drops from minutes to seconds — which, since tolerable depth scales as `V* = 8fQ/σ_o²`, directly multiplies safe depth — and the MEV surface of predictable clocked updates disappears. `dock`/`ship` remains only for true parameter changes (fee, amplification, quota wiring): rare by design.

Deleting the keeper fleet must not create a god-key: a single price-signer would let one compromised key sign cAMD at 100× fair value and drain the warm buffer through the system's own legal machinery. The signer therefore does not exist as a single object, and the strategies distrust even valid signatures: **threshold signing** (k-of-n, no single machine ever holds a signing quorum), **on-chain price bands** per corridor (a strategy rejects any signed price outside ±X% of its last accepted price), and **rate-of-change clamps** (maximum move per epoch). A stolen key can then leak basis points, never the balance sheet. The one component that signs money into existence is the one component that gets redundancy.

### 5.2 Makers sign nothing on fills

The pull/push executes under our allowance inside the resolver's transaction: fills are **balance events signed by others**. Our keys are not involved and our gas is not spent. The two ledgers — transactions we sign vs. fills that touch our balances — have entirely different security and cost profiles; conflating them is the classic accounting error of on-chain market making. Fill gas lands in the user's all-in price via the resolver's quote: it constrains demand, not our P&L (§6.5).

### 5.3 Pre-minted quotas: one mechanism instead of three

Tokens inside system custody are not liabilities (A2). Therefore mint each spoke's **full drainage quota into inventory upfront**. The venue cannot pull more than the wallet holds — so the protocol itself enforces the quota; no bespoke circuit-breaker contract exists. And the "pause on breach" is implemented by the *absence* of automation: refilling inventory is the one recurring deliberate action, taken per epoch only after the solvency check passes. Inventory sizing, quota enforcement, and the circuit breaker are the same object. During a run, the breaker is simply that nobody signs the refill.

### 5.4 The operational loop: four verbs

1. **Sign prices** — continuous, off-chain, free (the fair-value engine's output).
2. **Refill quotas** — per epoch, per corridor, after the SCR check; the only recurring on-chain decision the bank makes.
3. **Top up the window buffer** — reserve → warm, on breach of buffer bands; rare.
4. **Skim** — distribute `max(0, Π_true)` from reserve, monthly, gated (§7.3).

Everything else — fills, arbitrage, routing — is other people's transactions against our standing quotes. At launch the bank signs on the order of **a few transactions per week**.

### 5.5 Chart of accounts: three temperatures and a contract

Temperature = value at an attacker's risk. The chart of accounts *is* the security model:

| Account | Temp | Holds | Value to an attacker | Signs |
|---|---|---|---|---|
| **Reserve** | cold, timelocked multisig | all real value (ETH) | everything — hence cold and slow | 1–10 tx/month |
| **Window buffer** | warm | bounded ETH + hub tokens; approvals for window strategies | bounded by buffer bands | ~weekly |
| **Inventory** | hot | pre-minted cXXX quotas; approvals for all spoke strategies | ≈ nothing — self-minted tokens; the damage path runs through window quotas, i.e. bounded by the warm buffer | ~never (one-time approvals and ships) |
| **Issuance** | contract | no balance — authority only | n/a — mint/burn on quota refills and contraction ops | with verb 2 |

Balance events by others (fills) concentrate on Inventory and the Window buffer and are power-law distributed across corridors — the top ~10 corridors carry 80–90% of fills; the median spoke sees a handful per day at launch; per-corridor economics span 3–4 orders of magnitude, so quotas and epochs are set per corridor tier, not uniformly. Profit distributions pay out of Reserve directly under the SCR gate — a separate profit wallet would add an account without adding a control. Keeper gas lives in operational dust, not in the chart.

*(What got deleted relative to the obvious design: the push-oracle and its keeper fleet — replaced by signed prices; the breaker contracts — replaced by inventory sizing; the scheduled mint/burn — replaced by pre-minted quotas refilled on decision; the distribution wallet — replaced by a gate on the reserve; per-pool accounting — replaced by one registry query. Each deletion removes a control surface an attacker or a bug could reach.)*

### 5.6 Staging

Phase 0: one hub (cUSD), one window, 20–40 taker-regime currencies, no maker books. Phase transitions are gated by measured κ and flow, not by roadmap: hubs emerge when betweenness earns them, windows when demand earns them, maker regime when dominance is sustained. The bank grows the way the graph grows.

---

## 6. Unit Economics

### 6.1 Cost of depth

Taker regime: depth is bounded by adverse selection, `V* = 8fQ/σ_o²` — and with pulled prices σ_o is seconds-scale, so effective safe depth is enormous for anything with a live external reference. Maker regime: depth is bounded by inventory quota. Amplified curves substitute for notional: a $100k trade at ≤10bp impact needs ~$500k-equivalent at high amplification vs ~$50M constant-product.

### 6.2 Revenue

Two engines. **Spread × turnover** (dominant as taker): fee income on noise flow, protected from toxic flow by the venue's verified-counterparty gating plus our spread/inventory defenses. The system runs its **own resolver** from day one — both because the best-informed counterparty on our quotes is us, and because the verified-counterparty gate is a permissioned chokepoint: a resolver cartel could tax our flow, and the venue could change terms. Strategies are kept venue-portable; the execution layer is a supplier, not a dependency. **Seigniorage** (dominant as maker): net float growth against incoming ETH. They are different books with different risks; the transition zone between them is crossed quickly and thin.

### 6.3 The reserve's carry

The window complex pays ~σ²/8 per year of deployed reserve in volatility cost (~8%/yr at σ=0.8); this is the system's real cost of capital and the fee take on conversion flow must clear it. Optional staking yield offsets part; it adds slashing/liquidity risk and is a policy choice, not a requirement.

### 6.4 Own gas: rounding error

With pulled prices and event-driven refills, the bank's signed transactions are verbs 2–4: at launch ~$1–5/day of gas at current mainnet prices (base fee ~0.1–0.5 gwei in mid-2026), an order more at maturity. The infrastructure of a 200-currency bank costs less than its coffee.

### 6.5 User-side gas: the demand floor and its wrong-way tail

Fill gas (paid by resolvers, embedded in user prices) sets the minimum economic ticket: at 10bp fee, break-even is ~$40 at 0.1 gwei, ~$190 at 0.5, ~$760 at 2, ~$7,600 at a 20 gwei stress spike. At current gas, mainnet retail is viable to roughly **$150–600 tickets** — the core remittance range clears on L1. The binding constraint is the tail, and the tail is wrong-way: gas spikes cluster with crypto stress, which clusters with redemption surges. Hence the chain topology follows the tail, not the mean: base operation on L1; one L2 deployment as the **stress overflow lane and the micro-ticket lane** (<$150), canonical bridge internal, the invariant computed over float on both layers. Costs scale linearly in gas price, so the split-by-tail design is robust to the mean drifting either way.

---

## 7. Policy

### 7.1 One number

Define the hypothetical full-redemption cost — ETH required if all escaped float returns within N days through our own windows, **including our own price impact**, at stressed reserve volatility and stressed gas:

```
SCR = R_ETH / RedemptionCost(F, N, own impact, stressed σ, stressed gas)
```

**SCR < 1 is insolvency that has not yet been observed** — regardless of what the model marks as profit. One reserve → one SCR → nothing per-window to game.

### 7.2 The rule

```
hold  SCR ≥ 1 + β        (β ≈ 0.25–0.40)
```

β exists because SCR is measured with error (haircut, own-impact, model uncertainty on every P_i); running at exactly 1 is a knife-edge indistinguishable from insolvency within noise. In maker regime, model error **is** balance-sheet error — P_i inside the invariant comes from our own model, so a 20% mispricing of maker-regime float is indistinguishable from losing 20% of that reserve slice. Maker exposure therefore carries an explicit error budget inside the buffer:

```
Σ_maker  F_i · P_i · σ_model,i   ≤   β_model · R_ETH        (β_model a fixed slice of β)
```

A corridor whose model uncertainty would breach the budget gets its quota cut before its confidence gets tested — a confident wrong model must hit this inequality before it can silently eat the buffer while the profit metrics still read green. Escalation when SCR compresses, in order: widen spreads → decline quota refills on offending corridors (the breaker, §5.3) → divert window fees to reserve → contract float by bidding for own tokens through the windows. Every step is mechanical.

### 7.3 The skim

Slack above the buffer is not distributable — slack also grows when float expands, and profit that requires liability growth is a pyramid's profit. Only:

```
Π_true = ΔR_ETH − ΔF·(1−h)
distribute max(0, Π_true),  subject to SCR ≥ 1+β after distribution
```

Hold SCR at 1+β; cash only Π_true. That is the entire monetary policy.

---

## 8. Honesty

### 8.1 The dashboard

Four numbers, continuously published, all denominated in or against the external truth:

| # | Metric | Detects |
|---|---|---|
| 1 | Realized ETH free cash flow (executed round trips) | mark-to-model illusion |
| 2 | Π_true | profit that is really float expansion |
| 3 | Basis to uncontrolled external prices, conditional on flow symmetry | an imposed model being farmed one-way |
| 4 | SCR | slow-motion insolvency |

Metric 3 is the **voluntary two-sided acceptance test**: the model is right when the real economy transacts at our price in both directions uncoerced — off-venue rates converge on their own, corridor flow is sign-symmetric. One-sided adaptation plus persistent external basis means the quote is a subsidy being milked, not a discovery.

### 8.2 Anti-performativity

A dominant venue's model self-confirms: quote the curve → capitalizations converge to it → the fit improves → confidence grows → "correct" and "imposed" become indistinguishable. The countermeasures are structural: the **slope quarantine** (§4.1 — α fitted only where we are takers); **placebo currencies** — a rotating subset gets fair-value computation but no posted liquidity, and the forecasts are scored against moves we could not have caused (the only clean test of prediction vs. self-fulfillment); a permanent **out-of-model reference set** (third-party P2P rates, official fixes, invoice data — growing external divergence at perfect internal fit means the system is drifting inside its own simulation); and daily **redemption drills** — SCR recomputed as a paper stress so the run is rehearsed before it is real. In maker regime, performativity is partly the product: quoting small currencies toward the rank curve arbitrages away local distortions — multiple rates, black-market spreads — and enforces the curve it measures. The apparatus exists so that enforcement stays anchored to a slope discovered elsewhere.

---

## 9. Failure Catalog

| Failure | Mechanism | Guard |
|---|---|---|
| **Wrong-way collapse** (the material one) | float expands as reserve contracts, in the same stress; gas spikes join in | dynamic h; float/reserve cap; stress-gas in SCR; resolution regime |
| Redemption run | speed advantage to the first in line | pro-rata suspension deletes the advantage (§2.5) |
| Quota breach | a corridor drains past its share | inventory *is* the quota; refill requires a signature that a run does not get |
| Oracle gap harvest | stale peg vs. moving market | pulled signed prices: seconds staleness; V* cap |
| Transition-zone bleed | source too thin to correct us, still able to move | thin, wide, fast crossing (§4.3) |
| Imposed-model drift | performative self-confirmation | §8.2 |
| Meter instability | frequent hub-weight changes shake all measurements | annual formulaic reset, blend-in |
| Topology capture | appointed hubs ossify or politicize | graph-derived structure; only thresholds are governable |
| Seasonal misread | structural flow mistaken for information | corridor flow calendars subtracted first |
| Self-chasing | quote reacts faster than the economy | ≥1–2 wk price half-life vs. hourly risk |
| Mispriced quote | one-way accumulation or arbitrage drain; exporting a wrong rate | flow-symmetry alarm; per-corridor inventory caps; ±15% corridor around Layer A |
| Key compromise, hot | attacker reaches inventory | inventory is self-minted; damage path bounded by warm buffer |
| Signer compromise | a signed absurd price drains buffers through our own strategies | no single signer exists (threshold k-of-n); on-chain price bands; rate clamps (§5.1) |
| Venue capture | resolver cartel or venue terms tax the flow | own resolver as execution floor; venue-portable strategies |
| Undercapitalization | issuance at par can never satisfy an over-collateralized invariant | equity tranche pre-funds (h+β)·F; float capacity hard-capped at E/(h+β) (§2.5) |
| Censorship / sanctions | rails censor a corridor | multi-chain; no corridor systemically required |
| Demand starvation | no reason to hold cXXX; seigniorage starves | the ignition problem, §10.1 — a wedge per corridor, not a mechanism |
| Monetization mis-fit | curve wrong on high-M2/GDP states | g(m) mandatory |

---

## 10. The Ignition Problem

One admission belongs in the body, not a footnote: **this is a distribution company wearing a monetary-theory suit, and the monetary theory is the easy half.** A bank with no depositors is a spreadsheet; the claimed moat — private corridor-flow history — requires flow, flow requires holders, and holders require a reason that exists in someone's wallet on an ordinary Tuesday. Every failed stablecoin had adequate mechanisms and no such reason. The solvency design deliberately does not answer this — but it constrains the answer: ignition must come **per corridor**, as a concrete wedge (a remittance corridor priced below the incumbent rails; merchant settlement in a currency the banks serve badly; yield where holding the local unit is otherwise pure decay), proven on one corridor before the next, in the same staged, measured way the topology grows. The launch plan of §5.6 is therefore incomplete without a companion answer, per Phase-0 corridor, to one question: *who holds this token on day one, and what do they get that they could not get yesterday?*

## 11. Exclusions

Simplicity is enforced by subtraction. The system has **no**: second reserve asset or basket; per-window balance sheets; lending book or interest-rate policy; rehypothecation; supply expansion untethered to redemption capacity; governance-adjustable invariant; committee-appointed topology; push oracles or keeper fleets; breaker contracts; scheduled mint/burn; separate profit wallet; no discretionary per-currency intervention beyond the corridor/quota/spread toolkit; and **no single execution venue is systemically required** — strategies are portable and the system's own resolver guarantees a floor of execution capacity. Multiplicity of *quotation* — hubs, pairs, windows — is encouraged; multiplicity of *solvency* — reserves, invariants, SCRs — is prohibited. Every excluded feature is either a control surface for an attacker or a channel through which discretion could quietly convert liabilities into "profit".

---

## 12. The Whole Bank

```
0. Capital:    F ≤ E/(h+β)   — equity is the rate limiter      first-loss, ETH-denominated
1. Solvency:   Σ F_i·P_i ≤ R_ETH·(1−h)                       one reserve, constitutional
2. Topology:   hubs, windows, pairs = f(flow graph)           computed, annual
3. Depth:      V* = 8fQ/σ_o² (taker) | pre-minted quota (maker)
4. Price:      FX* = C₀·rank^(−α)·g(m)/M2 → corridor-flow Bayesian update
5. Policy:     hold SCR ≥ 1+β; spreads → refusals → fees → contraction
6. Profit:     distribute max(0, ΔR_ETH − ΔF·(1−h)), SCR-gated
```

Solvency audits in one division, profit in one subtraction, honesty in four published numbers, topology in one graph query, operations in four verbs. This is the standard one would wish to hold real central banks to and cannot — they have no external numeraire and no measured flow graph. This system has both: the window complex is not merely its reserve but its epistemology, and the payment graph is not merely its plumbing but its cartography.

---

## Appendix: Self-Review

**Complete?** Balance sheet, market structure, pricing, operations, unit economics, policy, validation, failure analysis. Out of scope, named honestly: custody and legal architecture of the reserve; governance of the constitutional clauses; graph-metric thresholds (require live data). The demand side is no longer waved away — §10 names it as the hard half and constrains its shape (per-corridor wedges), though the wedges themselves are business design beyond this paper.

**Redundant?** Each mechanism guards exactly one failure in §9. The largest simplifications came from merging: inventory sizing = quota = breaker (§5.3); accounting = security model (§5.5); resolution clause = anti-run device = stress-gas batcher (§2.5). Where one object can carry three duties, it does.

**Efficient?** Unbounded minted depth against one reserve; amplification substitutes ~100× notional; pulled prices substitute oracle gas for a signature check and multiply safe depth through σ_o; long-tail pairs are free until volume earns them structure; the bank's own footprint is a few signed transactions a week.

**Profitable?** Two engines with one meter, Π_true, that float expansion cannot inflate, denominated in the only unit the system cannot print. If sustained Π_true ≤ 0, the dashboard says so before the balance sheet can hide it.

