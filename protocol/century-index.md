---
tags: cyberia, protocol, cybernomics
alias: century index, rent index, land rent index, LRI, cyberia index, rent indexation, value preservation index
crystal-type: pattern
crystal-domain: cyberia
---
# century index

the unit of account for century-scale obligations: a fixed-quantity basket of eight world assets, ticker CX. first application — preserving the value of long-duration payment streams: land leases, city concessions, infrastructure rents ([[development|cyber valley]] instrument B is the first consumer, model annex: [[century annex]]). one formula, one basket, one oracle for every city cyberia develops; as the ecosystem matures, [[marketplace]] listings and treasury accounts quote in the same unit.

## 1. problem

a 25–80 year lease with annual payments carries three depreciation risks: local-currency debasement, reserve-currency debasement (~1.25x US CPI over 2020–2025), and the land outgrowing any fiat number written in year 0. a CPI clause lags real assets; the century index defines the payment as a fixed-quantity basket of world assets — the payment IS a portfolio. a city is a 50-year project funded by 25-year leases: a lessor who cannot preserve the stream sells land for survival, and [[development|the bootstrapped city]] dies.

## 2. definition

at signing (t₀) the annual rent R₀ splits into sleeves by weight wᵢ, converted to fixed quantities qᵢ at t₀ reference prices:

    qᵢ = wᵢ · R₀ / Pᵢ(t₀)        R(t) = Σ qᵢ · Pᵢ(t) = R₀ · Σ wᵢ · Pᵢ(t)/Pᵢ(t₀)

the tenant owes fixed quantities — dollars, yuan, gold grams, barrels, copper tonnes, satoshi, wei — settled in the payment currency at published fixes. renewals: L(T) = L₀ · I(T)/I(t₀). arithmetic (SDR-style) rather than geometric: if one asset dies the index loses at most wᵢ; a geometric index dies with it.

the obligation itself is numéraire-free: measured in the index, the rent is R₀ forever — the index IS the numéraire of the contract, and changing the bookkeeping currency rescales every price without moving a single settlement amount. an external ruler appears in exactly three operational places — the collar, the floor, and the invoice — and it must be external, because the index measured in itself has zero volatility and self-referential protections clamp nothing.

the ruler is BTC, expressed through four variables:

    X(t) = BTC/USD 365-day TWAP          — the bitcoin fix
    S(t) = I(t)/X(t)                     — the basket priced in bitcoin (the sat target)
    R(t) — the rent in sats:   R(t) = clamp( S(t), R(t−1)·[1−d, 1+u] )   — collar in sats
    floor:   R(t) ≥ max( S(t₀), F/X(t) )                                  — dual floor
    invoice: R(t) · X(t), converted per T6

where F = the year-0 rent in dollars. the dual floor is one max() with two legs: the sat leg guarantees the lessor no fewer satoshi than year 0 (when bitcoin outruns the basket it binds and the lease IS a bitcoin-standard obligation); the fiat leg F/X(t) guarantees no fewer year-0 dollars when bitcoin crashes — the floor that survives either tail. economic reading: rent = S₀ sats + a call on basket-over-bitcoin outperformance + a fiat tail-put. if the bitcoin fix dies through the whole T3 waterfall, the numéraire reverts to USD — the last backstop. fixes stay USD-quoted by market convention: quote currency is bookkeeping, numéraire is the ruler. built for crypto-native tenants — a fiat-income tenant takes the USD-numéraire variant as a deployment parameter.

## 3. basket

eight primary assets. no derivatives of institutions (equity indices), no policy assets (carbon allowances), no assets without a market (hydrogen). all prices enter as trailing 365-day averages of daily fixes (annual TWAP) — no single-day manipulation or spike risk.

fixes are two-tier: primary = aggregated on-chain oracle feeds ([Pyth](https://pyth.network/price-feeds), 100+ first-party publishers, signed, historical via [benchmarks](https://docs.pyth.network/benchmarks); [Chainlink](https://data.chain.link/) as the second oracle network) — 24/7 wherever the underlying trades 24/7. institutional settles are the fallback tier of the T3 waterfall. the index publishes 365 days/yr; a leg whose market is closed carries its last fix forward, standard index practice. OIL and CU have no 24/7 market anywhere on earth — the exchange settle IS the world price, so it stays primary and the oracle mirrors it on-chain.

| leg | weight | layer | primary fix | fallback |
|---|---|---|---|---|
| USD | 15% | today's fiat | 1 (quote currency) | — |
| CNH | 15% | today's fiat | Pyth USD/CNH (offshore yuan, freely traded, no PBOC fixing) | [WM/Refinitiv](https://www.lseg.com/en/data-analytics/financial-benchmarks/wm-refinitiv-fx-benchmarks), then [PBOC parity](https://www.chinamoney.com.cn/english/bmkcpr/) |
| GOLD | 15% | hard money | Pyth XAU/USD | [LBMA PM fix](https://www.lbma.org.uk/prices-and-data/precious-metal-prices), then [COMEX settle](https://www.cmegroup.com/markets/metals/precious/gold.html) |
| BTC | 20% | hard money | Pyth BTC/USD daily close | [CME CF BRR](https://www.cfbenchmarks.com/data/indices/BRR), then median of 3 named exchanges |
| ETH | 15% | hard money | Pyth ETH/USD daily close | [CME CF ETH RR](https://www.cfbenchmarks.com/data/indices/ETHUSD_RR), then median of 3 named exchanges |
| OIL | 5% | energy | [ICE Brent front-month settle](https://www.ice.com/products/219/Brent-Crude-Futures) | [EIA Brent spot](https://www.eia.gov/dnav/pet/hist/RBRTED.htm) |
| CU | 10% | energy | [LME copper cash settle](https://www.lme.com/en/Metals/Non-ferrous/LME-Copper) | [COMEX HG settle](https://www.cmegroup.com/markets/metals/base/copper.html) |
| U3O8 | 5% | energy | [CME UxC U3O8 front-month settle (ticker UX)](https://www.cmegroup.com/markets/metals/other/uranium.html) | [UxC](https://www.uxc.com/) / [TradeTech](https://www.uranium.info/) weekly spot, [Sprott physical trust](https://sprott.com/investment-strategies/physical-commodity-funds/uranium/) NAV as market check |

the basket as a thesis on the century: fiat of the present (30%), money that outlives fiat (50%), energy (20%). oil: two-sided bet, peak demand (EV S-curve, IEA plateau ~2030) vs peak supply (5–8%/yr base decline, shale tier-1 depletion, capex under replacement) — held as a shock hedge. copper: the bottleneck of electrification — EVs carry 3–4x the copper of combustion cars, grids must double, ore grades halve while a mine takes 15+ years; aluminum substitution caps the upside. uranium — held as U3O8 yellowcake, the traded form ($/lb spot, CME futures UX): baseload of the AI age — datacenter demand meets supply concentrated in few hands and 15-year mine lead times; fix is an assessment wrapped in an exchange settle, the weakest fix in the basket, accepted at 5%. BTC doubles as the only global electricity price: mining difficulty-adjusts the coin to the marginal world kWh.

rejected: lithium (abundant, supply answered a 10x spike in 3 years, no contract-grade fix), EUA carbon (political construct), equity indices (derivative, jurisdiction-branded), hydrogen (no market). watchlist: compute, depoliticized carbon.

## 4. weights

the structure reads in round layers: 30 fiat / 50 hard money / 20 energy. the 35% crypto tilt is deliberate lessor asymmetry: the §5 floor caps downside at R₀, the collar meters upside — the lessor holds a call-like payoff whose value grows with volatility; the tenant's compensation lives in the negotiated R₀, never in the formula. ETH at 15% records the lessor's judgment that the 2021–2025 ETH/BTC drawdown (−58%) was an early-asset artifact.

backtest (approximate year-end prices, no collar): 2020→2025 = 2.17x vs ~1.25x US CPI; worst year 2021→2022 ≈ −24%, absorbed by the floor; 2015→2025 = 579x uncapped, early-ETH dominated — the collar is structural, not cosmetic.

## 5. collar, floor, cadence

- reset: annual, using the TWAP ending 30 days before payment — the tenant knows the invoice a month ahead
- collar: year-over-year change of the sat rent clamped +35/−15 (decided; +35 captured 100% of the backtested index path where ±20 lost up to a quarter, −15 halves descent toward the floor); settlement-currency conversion (T6) happens after and is never capped — local devaluation flows through in full
- floor: dual, R(t) ≥ max(S₀ sats, F/X(t)) — see §2 · renewal: same collar per elapsed year · undelivered increase does not carry over
- backtest 2020→2025 (year-end spot; production uses TWAP, smoother): sat-rent path 1.00→1.13→1.76→1.49→1.27→1.08, USD invoice 1.00→1.80→1.00→2.16→4.07→3.54 — vs 2.17x uncapped index; the fiat leg of the floor holds the 2022 invoice at exactly year-0 dollars where a sat-only floor let it dip to 0.87x

## 6. contract theses

model clauses; the annex algorithm is the contract, reproducible by a junior accountant from public data.

- T1 annex: weights, t₀ prices, quantities qᵢ, fix sources with fallbacks, collar/floor, one worked invoice. prevails over prose. model: [[century annex]].
- T2 fix death ≠ asset death: an asset falling — even to zero — triggers nothing (the sleeve rides down); only death of a price SOURCE triggers replacement, which must price the same asset.
- T3 cessation waterfall: dead = administrator cessation, 30 days unpublished, or methodology change. then: named fallback → regulator-designated successor (LIBOR→SOFR pattern) → equivalent fix by independent expert → last TWAP frozen as a bridge, never a settlement.
- T4 review valve: every 5th anniversary, mutual written consent only, replace ≤1 leg of ≤10% weight at then-current TWAP (value-neutral). silence = no change; no unilateral right; CNH and USD excluded. the watchlist's entry path.
- T5 recomputation: tenant may recompute any invoice from public sources within 30 days; recomputation prevails, manifest errors corrected retroactively. index disputes are arithmetic, never renegotiation.
- T6 settlement: the formula adapts to local currency law — e.g. Indonesia ([UU 7/2011](https://peraturan.bpk.go.id/Details/39197/uu-no-7-tahun-2011)) requires IDR settlement at [JISDOR](https://www.bi.go.id/en/statistik/informasi-kurs/jisdor/default.aspx) on the invoice date.
- T7 continuity: the annex survives assignment, sublease, succession; renewals reference the same t₀ quantities. quantities, not parties, define the obligation.
- T8 oracle precedence: the on-chain fix (§7) is evidence and automation; on divergence the annex computation from public fixes prevails.

## 7. oracle

the formula runs as a daily on-chain fix: fixed-point over the Goldilocks field per [[soft3]] (no floats in the provable path), signed by the publishing [[neuron]], anchored in the [[cybergraph]], provable by [[zheng]] — a public good any lease anywhere can reference. the [[marketplace]] prices demand for one asset; the century index preserves a stream across decades.

## 8. open questions

1. hybrid: rent = max(index path, assessed-land-value path) — covers both debasement and the land outgrowing the basket

resolved: numéraire = BTC via the §2 four-variable machine (sat collar, dual floor, USD reversion backstop) — the obligation itself stays numéraire-free, the ruler exists only in the collar and floor. collar = +35/−15 in sats. weights, basket, name: see status line.
