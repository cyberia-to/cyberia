---
tags: cyberia, protocol, cybernomics
alias: land rent index, LRI, rent index, rent indexation, value preservation index
crystal-type: pattern
crystal-domain: cyberia
---
# rent index

universal instrument for preserving the value of long-duration payment streams — land leases, city concessions, infrastructure rents, any contract where one party grants decades of use and receives years of payments. one formula, one basket, one oracle — every city cyberia develops prices its long leases with the same machine.

status: draft v0.4 · unsigned · first deployment [[development|cyber valley]] · decided: 7-leg basket BTC/ETH/GOLD/OIL/CU/CNY/USD = 15/5/35/5/10/15/15

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

equivalently: the tenant owes a fixed amount of dollars, yuan, gold grams, oil barrels, copper tonnes, satoshi and wei every year — settled in the payment currency at published reference prices. renewal lump sums use the same formula: L(T) = L₀ · I(T)/I(t₀) where I is the same weighted sum.

the arithmetic (fixed-quantity, SDR-style) form is chosen over a geometric (constant-weight) form deliberately: if any single asset goes to zero over the contract horizon — a live possibility for any crypto asset — the arithmetic index loses at most wᵢ, while a geometric index goes to zero with it.

## 3. the basket

seven legs, four value layers. every leg is a primary asset with a deep liquid public fix — no derivatives of institutions (equity indices), no policy-manufactured assets (carbon allowances), no assets without a market (hydrogen).

| leg | weight | layer | reference fix | fallback |
|---|---|---|---|---|
| USD | 15% | today's fiat | 1 (numéraire) | — |
| CNY | 15% | today's fiat | WM/Refinitiv 4pm London USD/CNY | PBOC central parity |
| GOLD | 35% | hard money | LBMA PM fix (USD/oz) | COMEX front-month settle |
| BTC | 15% | hard money | CME CF Bitcoin Reference Rate | median of 3 named exchanges' daily close |
| ETH | 5% | hard money | CME CF Ether Reference Rate | median of 3 named exchanges' daily close |
| OIL | 5% | departing energy | ICE Brent front-month monthly settle | EIA Brent spot monthly avg |
| CU | 10% | arriving energy | LME copper cash official settle | COMEX HG front-month settle |

all prices enter the formula as the trailing 365-day average of daily fixes (annual TWAP), which removes single-day manipulation and spike risk at reset dates.

the basket reads as a thesis on the century: fiat of the present (30%), money that outlives fiat (55%), the energy passing away (5%), the energy arriving (10%). BTC doubles as the only global electricity price — mining arbitrages cheap power planet-wide and difficulty-adjusts the coin to the marginal world kWh, so the electric economy enters the basket twice: through its scarce metal (copper) and its monetized output (bitcoin).

oil at 5% carries genuine two-sided uncertainty on a 25-year horizon. peak-demand case: transport is ~60% of demand, EV adoption is on an S-curve, China gasoline has peaked, IEA sees a demand plateau ~2030. peak-supply case: base decline of existing fields runs 5–8%/yr, shale tier-1 inventory is depleting and Permian productivity gains flattened after 2023, upstream capex has run below replacement since 2015 — if supply peaks with or before demand, real prices hold or rise for decades. the empirical anchor between the two: real oil has no long-run drift (the 1980 real peak still stands). net: a small sleeve as inflation-shock and supply-shock hedge.

copper at 10% is the bottleneck of electrification: EVs carry 3–4x the copper of combustion cars, renewables multiples per MW of thermal, grids must roughly double, ore grades halve over decades and a new mine runs 15+ years from permit to production. the substitution ceiling (aluminum replaces at ~2.5–3x price ratio) and China-construction legacy demand are the honest caps on the thesis.

considered and rejected: lithium (geologically abundant, supply answered a 10x spike within 3 years, chemistry-substitution risk, no contract-grade fix), EUA carbon (programmed scarcity but a purely political construct — cap, price, and existence are one reform away from change), equity indices (derivative claims on institutions, jurisdiction-branded), hydrogen (no market, no price — a derivative of electricity cost with no instrument), uranium (strong thesis, assessment-grade fix only — first candidate for the §7 review valve if exchange-grade pricing matures).

watchlist for the review valve: uranium (exchange-grade fix maturing), compute (GPU-hour is a primary commodity of this century with no liquid index yet), depoliticized carbon (a global physical carbon price rather than a jurisdictional allowance).

## 4. weights

decided: CNY/USD symmetric at 15/15; remaining 70% = BTC 15 / ETH 5 / GOLD 35 / OIL 5 / CU 10.

backtest on approximate year-end prices, fixed-quantity basket, no collar: 2020→2025 = 1.77x (vs ~1.25x US CPI), 2015→2025 = 213x uncapped — the 2015 number is dominated by ETH from $0.9 and shows why uncapped crypto sleeves are unsignable and why the collar in §5 is structural, a tenant protection the index cannot work without.

## 5. collar, floor, cadence

- reset cadence: annual, on the contract anniversary, using the TWAP ending 30 days before the payment date (the tenant knows the invoice a month ahead)
- collar: year-over-year rent change clamped to ±20%; undelivered increase does NOT carry over (a carryover ratchet reintroduces the unbounded path the collar exists to remove)
- floor: R(t) ≥ R₀ in numéraire terms — the lessor never receives less than the year-0 rent
- renewal: extension option price fixed as L₀ · I(T)/I(t₀) with the same collar applied per elapsed year, so the option is priced by the same machine as the rent

## 6. recommended contract theses

model clauses for any lease referencing the index. the annex algorithm is the contract; a junior accountant must be able to reproduce every invoice from public data.

T1 — quantities annex. the contract annex states: the seven weights, the seven t₀ reference prices, the resulting quantities qᵢ, the fix sources with fallback waterfall, the collar and floor, and one fully worked example invoice. the annex prevails over any prose description of the index.

T2 — fix death vs asset death. these are different events with opposite treatments. if an ASSET loses value — even to zero — nothing is triggered: the sleeve rides down, that is the design (§2), and no party may demand substitution of a losing asset. only the death of a REFERENCE FIX (the price source) triggers replacement, and the replacement must price the same asset.

T3 — fix cessation waterfall. a fix is dead when its administrator announces permanent cessation, or it is unpublished for 30 consecutive days, or its methodology materially changes the priced asset. then, in order: (a) the named fallback fix in the annex table; (b) the successor rate formally designated by the fix administrator or its regulator (the LIBOR→SOFR pattern); (c) an equivalent fix for the same asset selected by an independent expert appointed under the contract's arbitration rules; (d) until (a)–(c) resolves, the last published 365-day TWAP value is frozen — the frozen value is a bridge, never a settlement of the dispute.

T4 — review valve. every 5th contract anniversary the parties may, by mutual written consent only, replace at most one leg of at most 10% weight, at the then-current TWAP prices so the swap is value-neutral on the day. silence means no change; neither party holds a unilateral right; the CNY and USD legs are excluded from the valve. the valve is how assets that lack instruments today (§3 watchlist) enter the basket tomorrow.

T5 — calculation and recomputation. the lessor (or a named calculation agent) computes each invoice and delivers it with the fix values used. the tenant may recompute from the named public sources within 30 days; on discrepancy the recomputation from public data prevails, and manifest errors are corrected retroactively without penalty. disputes about the index are disputes of arithmetic, resolved by recomputation, never by renegotiation.

T6 — settlement. the index is a pricing formula; settlement follows the jurisdiction's currency law. per-jurisdiction example: Indonesia (UU 7/2011) requires IDR settlement for domestic payments — invoice converts at JISDOR on the invoice date, exact drafting per local counsel.

T7 — continuity. the annex survives assignment, sublease, and corporate succession on either side; renewal and extension options reference the same annex and the same t₀ quantities. the index outlives the parties' reorganizations because the quantities, not the parties, define the obligation.

T8 — oracle precedence. while the on-chain oracle (§7) publishes, its daily fix and the annex computation must agree; on divergence the annex computation from the named public fixes prevails. the oracle is evidence and automation, never a new source of truth.

## 7. oracle

the same formula runs as a daily on-chain fix: fixed-point arithmetic over the Goldilocks field per [[soft3]] conventions (the provable path admits no floats), signed by the publishing [[neuron]], anchored as a particle in the [[cybergraph]], provable by [[zheng]]. legal contracts reference public fixes; the oracle mirrors them and makes the index a public good — any lease, concession, or [[marketplace]] listing anywhere references one canonical daily fix. the [[marketplace]] prices demand for a single asset; the rent index preserves value of a stream across decades — two orthogonal pricing primitives of the same protocol.

## 8. deployments

| deployment | instruments | status |
|---|---|---|
| [[development|cyber valley]] | instrument B (annual leasehold), instrument G (participation rent base), extension options of instrument A | first consumer, contracts pending |

## 9. open questions

1. collar width — ±20% tested; ±15% is easier to sign, ±25% tracks the index tighter
2. numéraire — USD chosen; a local-currency numéraire would make the USD sleeve an explicit FX hedge and change the floor semantics
3. assessed-land-value hybrid — the index tracks world money, assessed value tracks local land; rent = max(index path, assessed-value path) protects the lessor from both debasement and the land outgrowing the basket
