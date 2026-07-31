---
tags: cyberia, protocol, cybernomics
alias: century index, rent index, land rent index, LRI, cyberia index, rent indexation, value preservation index, century annex, rent annex
crystal-type: pattern
crystal-domain: cyberia
---
# century index

the unit of account for century-scale obligations — ticker CX. a fixed basket of eight world assets: whoever owes the index owes quantities, and the quantities never change. first application — long-duration payment streams: land leases, city concessions, infrastructure rents ([[development|cyber valley]] instrument B is the first consumer; model annex in §6). as the ecosystem matures, [[marketplace]] listings and treasury accounts quote in the same unit.

## 1. why

a 25–80 year lease outlives every currency it could be written in. the local currency debases fastest; the reserve currency compounded ~1.25x US CPI over 2020–2025 alone; the land itself outgrows any number fixed in year 0. the century index makes the payment a portfolio instead of a number — rent is a fixed set of quantities, and its value moves with the world. a city is a 50-year project funded by 25-year leases: the [[development|bootstrapped city]] stands on rent that keeps its value.

## 2. definition

at signing (t₀) the annual rent R₀ splits by weight wᵢ into fixed quantities at the reference prices:

    qᵢ = wᵢ · R₀ / Pᵢ(t₀)        R(t) = Σ qᵢ · Pᵢ(t)

the tenant owes satoshi, wei, gold grams, yuan, dollars, copper tonnes, barrels, and pounds of yellowcake — settled in the payment currency at published fixes. renewals scale the same way: L(T) = L₀ · I(T)/I(t₀). the sum is arithmetic, SDR-style: an asset going to zero costs the index at most that asset's weight (T2).

measured in itself the index is constant, so the obligation carries no numéraire. a ruler is needed only where the contract clamps and guarantees — the collar and the floor — and the ruler is bitcoin:

    X(t) = BTC/USD 365-day TWAP                — the bitcoin fix
    S(t) = I(t)/X(t)                           — the basket priced in bitcoin
    R(t) = clamp( S(t), R(t−1)·[0.85, 1.35] )  — the sat rent, collared
    floor:   R(t) ≥ max( S₀, F/X(t) )          — dual floor
    invoice: R(t) · X(t), converted per T6

F is the year-0 rent in dollars. the sat leg of the floor guarantees the lessor no fewer satoshi than year 0 — whenever bitcoin outruns the basket, the lease is a bitcoin-standard obligation. the fiat leg guarantees no fewer year-0 dollars when bitcoin crashes. read as one instrument: rent = S₀ sats + a call on the basket over bitcoin + a fiat tail-put. if the bitcoin fix dies through the whole T3 waterfall, the ruler reverts to USD. fixes stay USD-quoted by market convention — quote currency is bookkeeping, the ruler is the numéraire.

## 3. basket

eight primary assets — things the world prices directly, each with a deep liquid public fix. three layers: fiat of the present (30%), money that outlives fiat (50%), energy (20%).

| leg | weight | layer | primary fix | fallback |
|---|---|---|---|---|
| BTC | 20% | hard money | Pyth BTC/USD daily close | [CME CF BRR](https://www.cfbenchmarks.com/data/indices/BRR), then median of 3 named exchanges |
| ETH | 15% | hard money | Pyth ETH/USD daily close | [CME CF ETH RR](https://www.cfbenchmarks.com/data/indices/ETHUSD_RR), then median of 3 named exchanges |
| GOLD | 15% | hard money | Pyth XAU/USD | [LBMA PM fix](https://www.lbma.org.uk/prices-and-data/precious-metal-prices), then [COMEX settle](https://www.cmegroup.com/markets/metals/precious/gold.html) |
| CNY | 15% | today's fiat | Pyth USD/CNH (offshore quote — freely traded, no PBOC fixing) | [WM/Refinitiv](https://www.lseg.com/en/data-analytics/financial-benchmarks/wm-refinitiv-fx-benchmarks), then [PBOC parity](https://www.chinamoney.com.cn/english/bmkcpr/) |
| USD | 15% | today's fiat | 1 (quote currency) | — |
| CU | 10% | energy | [LME copper cash settle](https://www.lme.com/en/Metals/Non-ferrous/LME-Copper) | [COMEX HG settle](https://www.cmegroup.com/markets/metals/base/copper.html) |
| OIL | 5% | energy | [ICE Brent front-month settle](https://www.ice.com/products/219/Brent-Crude-Futures) | [EIA Brent spot](https://www.eia.gov/dnav/pet/hist/RBRTED.htm) |
| UX | 5% | energy | [CME UxC U3O8 front-month settle](https://www.cmegroup.com/markets/metals/other/uranium.html) | [UxC](https://www.uxc.com/) / [TradeTech](https://www.uranium.info/) weekly spot, [Sprott physical trust](https://sprott.com/investment-strategies/physical-commodity-funds/uranium/) NAV as market check |

fixes are two-tier: aggregated on-chain oracle feeds first ([Pyth](https://pyth.network/price-feeds), 100+ first-party publishers, signed, historical via [benchmarks](https://docs.pyth.network/benchmarks); [Chainlink](https://data.chain.link/) second), institutional settles as the T3 fallback tier. every price enters as a trailing 365-day average of daily fixes — annual TWAP, immune to single-day manipulation. the index publishes 365 days a year; a closed market carries its last fix forward. the physical legs settle on exchanges — the settle IS the world price, and the oracle mirrors it on-chain.

why these eight. BTC is hard money and, through mining difficulty, the only global price of electricity. ETH is the productive digital asset. gold has held value for five thousand years. CNY and USD are the working money of the present. copper is the bottleneck of electrification: an EV carries 3–4x the copper of a combustion car, grids must double, a new mine takes 15 years. oil is the shock hedge — every crisis prices through it first. uranium, held as U3O8 yellowcake (CME ticker UX), is the baseload of the AI age; its fix, an assessment wrapped in an exchange settle, is the weakest in the basket and is sized accordingly.

the primary-asset rule keeps the rest out: equity indices are claims on institutions, carbon allowances are claims on policy, lithium is abundant, hydrogen has no market to price. watchlist for the T4 valve: compute, a depoliticized carbon price.

## 4. mechanics

- reset: annual, on the contract anniversary, using the TWAP window that ends 30 days before payment — the tenant knows the invoice a month ahead
- collar: +35%/−15% per year in sats. +35% is wide enough to deliver the full historical index path (a ±20% collar surrendered a quarter of it); −15% halves the descent toward the floor. undelivered increase does not carry over
- settlement conversion happens after the collar and is never capped — devaluation of the local currency flows through in full
- backtest, 2020→2025 year-end prices: the basket returned 2.17x against ~1.25x US CPI; run through the machine, the invoice path is 1.00 → 1.80 → 1.00 → 2.16 → 4.07 → 3.54, the fiat floor holding 2022 at exactly year-0 dollars. uncollared from 2015 the basket runs 579x — the collar is structural, not cosmetic
- the crypto weight is the lessor's asymmetry: the floor caps downside at year-0 value, the collar meters upside, so the lessor holds a call whose value grows with basket volatility. the tenant's compensation lives in the negotiated R₀, never in the formula

## 5. contract theses

model clauses; the annex algorithm is the contract, reproducible by a junior accountant from public data.

- T1 annex: weights, t₀ prices, quantities qᵢ, fix sources with fallbacks, collar/floor, one worked invoice. prevails over prose. model: §6.
- T2 fix death ≠ asset death: an asset falling — even to zero — triggers nothing (the sleeve rides down); only death of a price SOURCE triggers replacement, which must price the same asset.
- T3 cessation waterfall: dead = administrator cessation, 30 days unpublished, or methodology change. then: named fallback → regulator-designated successor (LIBOR→SOFR pattern) → equivalent fix by independent expert → last TWAP frozen as a bridge, never a settlement.
- T4 review valve: every 5th anniversary, mutual written consent only, replace ≤1 leg of ≤10% weight at then-current TWAP (value-neutral). silence = no change; no unilateral right; CNY and USD excluded. the watchlist's entry path.
- T5 recomputation: tenant may recompute any invoice from public sources within 30 days; recomputation prevails, manifest errors corrected retroactively. index disputes are arithmetic, never renegotiation.
- T6 settlement: the formula adapts to local currency law — e.g. Indonesia ([UU 7/2011](https://peraturan.bpk.go.id/Details/39197/uu-no-7-tahun-2011)) requires IDR settlement at [JISDOR](https://www.bi.go.id/en/statistik/informasi-kurs/jisdor/default.aspx) on the invoice date.
- T7 continuity: the annex survives assignment, sublease, succession; renewals reference the same t₀ quantities. quantities, not parties, define the obligation.
- T8 oracle precedence: the on-chain fix (§7) is evidence and automation; on divergence the annex computation from public fixes prevails.

## 6. model annex

worked example at R₀ = $100,000/yr with indicative spot fixes of 2026-07-31; a signed annex replaces them with the 365-day TWAP fixes at signing.

| parameter | value |
|---|---|
| R₀ (year-0 rent) | $100,000 |
| F (fiat floor leg) | $100,000 |
| weights BTC/ETH/GOLD/CNY/USD/CU/OIL/UX | 20/15/15/15/15/10/5/5 |
| collar | +35% / −15% per year, in sats |
| numéraire | BTC · fixes USD-quoted |
| reset | annual anniversary, TWAP window ends 30 days before payment |
| settlement | IDR at JISDOR on invoice date (UU 7/2011) |

quantities, fixed for the life of the contract:

| leg | t₀ fix (example) | quantity qᵢ |
|---|---|---|
| BTC | $62,626 | 0.31935618 BTC (31,935,618 sats) |
| ETH | $1,857.97 | 8.073327 ETH |
| GOLD | $4,039.38/oz | 115.501 g |
| CNY | 6.765736 /USD (CNH quote) | ¥101,486.04 |
| USD | 1 | $15,000.00 |
| CU | $13,552.04/t | 737.90 kg |
| OIL | $91.82/bbl | 54.454 bbl |
| UX | $80.00/lb U3O8 (indicative assessment level) | 62.50 lb |

derived: X(t₀) = $62,626 · S₀ = R₀/X(t₀) = 1.596781 BTC = 159,678,089 sats.

worked invoice, hypothetical year-1 TWAP fixes — BTC $75,000 · ETH $2,200 · GOLD $4,400 · OIL $85 · CU $14,500/t · U3O8 $90/lb · USD/CNY 7.00 · JISDOR 19,000:

1. mark quantities to market: I(t₁) = Σ qᵢ·Pᵢ = $108,503.30
2. price in bitcoin: S(t₁) = I/X = 108,503.30 / 75,000 = 1.446711 BTC
3. collar [S₀·0.85, S₀·1.35] = [1.357264, 2.155654] → 1.446711 passes unclamped
4. dual floor: max(S₀ = 1.596781, F/X = 100,000/75,000 = 1.333333) = 1.596781 → floor BINDS
5. R(t₁) = 1.596781 BTC = 159,678,089 sats
6. invoice: R·X = $119,758.57 → × 19,000 = Rp 2,275,412,768

reading of this year: the basket grew 8.5% but bitcoin grew 19.8% — the sat floor binds and the tenant owes the same sats as year 0, worth more dollars. the lease behaves as a bitcoin-standard obligation, exactly as designed.

## 7. oracle

the index publishes as a daily on-chain fix at the Ethereum contract `cyberia.eth/index` — one canonical number any lease, [[marketplace]] listing, or treasury anywhere can reference. per T8 the on-chain fix is evidence and automation: on divergence the annex computation from the named public fixes prevails. the long game: the fix migrates into the [[cybergraph]] — fixed-point over the Goldilocks field per [[soft3]], signed by the publishing [[neuron]], provable by [[zheng]].
