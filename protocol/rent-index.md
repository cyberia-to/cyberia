---
tags: cyberia, protocol, cybernomics
alias: land rent index, LRI, rent index, rent indexation, value preservation index
crystal-type: pattern
crystal-domain: cyberia
---
# rent index

universal instrument for preserving the value of long-duration payment streams — land leases, city concessions, infrastructure rents, any contract where one party grants decades of use and receives years of payments. one formula, one basket, one oracle — every city cyberia develops prices its long leases with the same machine.

status: draft v0.2 · unsigned · first deployment [[development|cyber valley]]

## 1. problem

a lessor granting a 25–100 year right with a lump sum at signing and annual payments (or renewal lump sums) afterward carries three depreciation risks:

1. local-currency debasement — payments fixed in the local unit lose value fastest
2. reserve-currency debasement — dollar-fixed payments lose to monetary expansion (US CPI compounded ~1.25x over 2020–2025 alone)
3. asset appreciation — the land itself outgrows any fiat number written in year 0

a CPI clause covers risks 1–2 partially and lags real assets. the rent index instead defines the payment as a fixed-quantity basket of world assets, so the payment IS a portfolio, and its value moves with the world instead of with one printing press. this matters for city development specifically: a city is a 50-year project funded by 25-year leases — whoever cannot preserve the value of the annual stream is forced to sell land for survival, and [[development|the bootstrapped-city model]] dies.

## 2. definition

at contract signing (t₀) the annual rent R₀ is split into sleeves by weight wᵢ and converted into fixed quantities qᵢ at the reference prices of t₀:

    qᵢ = wᵢ · R₀ / Pᵢ(t₀)

each payment date t, the rent in numéraire currency is the mark-to-market of those quantities:

    R(t) = Σ qᵢ · Pᵢ(t)   ⇔   R(t) = R₀ · Σ wᵢ · Pᵢ(t)/Pᵢ(t₀)

equivalently: the tenant owes a fixed amount of dollars, yuan, gold grams, oil barrels, satoshi and wei every year — settled in the payment currency at published reference prices. renewal lump sums use the same formula: L(T) = L₀ · I(T)/I(t₀) where I is the same weighted sum.

the arithmetic (fixed-quantity, SDR-style) form is chosen over a geometric (constant-weight) form deliberately: if any single asset goes to zero over the contract horizon — a live possibility for any crypto asset — the arithmetic index loses at most wᵢ, while a geometric index goes to zero with it.

## 3. assets and reference prices

the reference basket spans four value classes: fiat anchors (USD, CNY), monetary metal (GOLD), real economy (OIL), digital hard assets (BTC, ETH).

| sleeve | role | reference fix | fallback |
|---|---|---|---|
| USD | numéraire anchor, local-debasement hedge | 1 (numéraire) | — |
| CNY | second-reserve diversification | WM/Refinitiv 4pm London USD/CNY | PBOC central parity |
| GOLD | monetary metal | LBMA PM fix (USD/oz) | COMEX front-month settle |
| OIL | energy / inflation-shock hedge | ICE Brent front-month monthly settle | EIA Brent spot monthly avg |
| BTC | hard digital asset | CME CF Bitcoin Reference Rate | median of 3 named exchanges' daily close |
| ETH | productive digital asset | CME CF Ether Reference Rate | median of 3 named exchanges' daily close |

all prices enter the formula as the trailing 365-day average of daily fixes (annual TWAP), which removes single-day manipulation and spike risk at reset dates. if a reference rate ceases publication, the fallback applies; if both cease, the parties adopt the successor rate by expert determination (ISDA-style waterfall).

sleeve composition is a per-deployment parameter. the oil sleeve is a considered trade: oil is a consumption good with mean-reverting real price and demand plateauing ~2030, kept small (5–10%) purely as an inflation-shock hedge; copper (LME cash settle) is the candidate replacement on the growing side of electrification, and a broad commodity index (BCOM) collapses both into one leg.

## 4. weights

backtest on approximate year-end prices, fixed-quantity basket, no collar:

| weights (BTC/ETH/GOLD/OIL/CNY/USD) | 2020→2025 | 2015→2025 |
|---|---|---|
| equal 1/6 | 2.09x | 630x |
| hard-money 15/5/25/10/10/35 | 1.70x | 212x |
| conservative 10/5/30/10/10/35 | 1.62x | 201x |
| no-crypto 0/0/40/15/15/30 | 1.31x | 1.9x |

(2015 numbers are dominated by ETH from $0.9; they show why uncapped crypto sleeves are unsignable, and why the collar in §5 is structural — a tenant protection the index cannot work without.)

recommended default: 10/5/30/10/10/35 (conservative). over 2020–2025 it returned 1.62x against ~1.25x US CPI — value preserved plus a real-asset premium, with two thirds of the basket in low-volatility sleeves.

## 5. collar, floor, cadence

- reset cadence: annual, on the contract anniversary, using the TWAP ending 30 days before the payment date (the tenant knows the invoice a month ahead)
- collar: year-over-year rent change clamped to ±20%; undelivered increase does NOT carry over (a carryover ratchet reintroduces the unbounded path the collar exists to remove)
- floor: R(t) ≥ R₀ in numéraire terms — the lessor never receives less than the year-0 rent
- renewal: extension option price fixed as L₀ · I(T)/I(t₀) with the same collar applied per elapsed year, so the option is priced by the same machine as the rent

## 6. settlement and legal wrapper

the index is a pricing formula; settlement adapts to each jurisdiction's currency law. the contract annex contains: the weights, the t₀ reference prices, the resulting quantities qᵢ, the fix sources and fallback waterfall, the collar/floor, and a worked example — the formula must be reproducible by a junior accountant from public data. disputes resolve by recomputation from the named public fixes; the annex algorithm is the contract.

per-jurisdiction examples: Indonesia (UU 7/2011) requires IDR settlement for domestic payments — invoice converts at JISDOR on the invoice date, exact drafting per local counsel.

## 7. oracle

the same formula runs as a daily on-chain fix: fixed-point arithmetic over the Goldilocks field per [[soft3]] conventions (the provable path admits no floats), signed by the publishing [[neuron]], anchored as a particle in the [[cybergraph]], provable by [[zheng]]. legal contracts reference public fixes; the oracle mirrors them and makes the index a public good — any lease, concession, or [[marketplace]] listing anywhere references one canonical daily fix. the [[marketplace]] prices demand for a single asset; the rent index preserves value of a stream across decades — two orthogonal pricing primitives of the same protocol.

## 8. deployments

| deployment | instruments | status |
|---|---|---|
| [[development|cyber valley]] | instrument B (annual leasehold), instrument G (participation rent base), extension options of instrument A | first consumer, contracts pending |

## 9. open questions

1. weights — 10/5/30/10/10/35 proposed; is 15% total crypto the right lessor upside vs tenant signability trade?
2. collar width — ±20% tested; ±15% is easier to sign, ±25% tracks the index tighter
3. oil sleeve — keep 10%, cut to 5% + add copper 5%, or swap the leg for BCOM (§3)
4. CNY sleeve — political optics of a yuan reference in some jurisdictions; keep, shrink, or replace with SDR
5. numéraire — USD chosen; a local-currency numéraire would make the USD sleeve an explicit FX hedge and change the floor semantics
6. assessed-land-value hybrid — the index tracks world money, assessed value tracks local land; rent = max(index path, assessed-value path) protects the lessor from both debasement and the land outgrowing the basket
