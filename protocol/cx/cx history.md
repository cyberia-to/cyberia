---
tags: cyberia, protocol, cybernomics, cx
alias: cx history, century index history, index history, cx series
crystal-type: pattern
crystal-domain: cyberia
---
# cx history

the published level of the [[century-index]] from its base date to 2026-09-18. one CX is the basket that cost $1 on 2022-01-07; today it costs $1.43. every price enters as a trailing 365-day average, so the series moves at the pace of a year, not a day — which is what a century-scale obligation asks of it.

## reading

- since 2022-01-07 the basket returned +43.1% in dollars
- the last twelve months: +7.1%
- the range since the base date: 0.83 low, 1.46 high

## quantities

fixed on 2022-01-07, unchanged since — the obligation is these quantities, not the number they priced at.

| leg | quantity | unit | fix at base | weight |
|---|---|---|---|---|
| BTC | 0.000004197 | BTC | 47,642.04 | 20% |
| ETH | 0.000053024 | ETH | 2,828.89 | 15% |
| CNY | 0.96724 | CNY | 0.155079 | 15% |
| USD | 0.15000 | USD | 1 | 15% |
| GOLD | 0.000083486 | troy oz | 1,796.69 | 15% |
| CU | 0.000010687 | tonne | 9,357.05 | 10% |
| OIL | 0.0007021 | bbl | 71.20 | 5% |
| UX | 0.0015148 | lb U3O8 | 33.00 | 5% |

## monthly level

| month | level | month | level |
|---|---|---|---|
| 2022-01 | 1.01 | 2024-06 | 1.03 |
| 2022-02 | 1.01 | 2024-07 | 1.05 |
| 2022-03 | 1.02 | 2024-08 | 1.08 |
| 2022-04 | 1.03 | 2024-09 | 1.10 |
| 2022-05 | 1.02 | 2024-10 | 1.12 |
| 2022-06 | 1.01 | 2024-11 | 1.15 |
| 2022-07 | 1.01 | 2024-12 | 1.18 |
| 2022-08 | 0.99 | 2025-01 | 1.20 |
| 2022-09 | 0.97 | 2025-02 | 1.22 |
| 2022-10 | 0.95 | 2025-03 | 1.22 |
| 2022-11 | 0.92 | 2025-04 | 1.23 |
| 2022-12 | 0.89 | 2025-05 | 1.24 |
| 2023-01 | 0.87 | 2025-06 | 1.25 |
| 2023-02 | 0.86 | 2025-07 | 1.28 |
| 2023-03 | 0.85 | 2025-08 | 1.31 |
| 2023-04 | 0.83 | 2025-09 | 1.34 |
| 2023-05 | 0.83 | 2025-10 | 1.38 |
| 2023-06 | 0.83 | 2025-11 | 1.39 |
| 2023-07 | 0.83 | 2025-12 | 1.40 |
| 2023-08 | 0.84 | 2026-01 | 1.41 |
| 2023-09 | 0.84 | 2026-02 | 1.42 |
| 2023-10 | 0.85 | 2026-03 | 1.44 |
| 2023-11 | 0.86 | 2026-04 | 1.45 |
| 2023-12 | 0.88 | 2026-05 | 1.46 |
| 2024-01 | 0.90 | 2026-06 | 1.46 |
| 2024-02 | 0.92 | 2026-07 | 1.44 |
| 2024-03 | 0.95 | 2026-08 | 1.43 |
| 2024-04 | 0.97 | 2026-09 | 1.43 |
| 2024-05 | 1.00 | — | — |

## sources

this series is a reconstruction from free public data — evidence and orientation, never the contractual fix. a signed annex names its own sources with fallbacks, per the cessation waterfall in [[century-index]].

| leg | source | observed range |
|---|---|---|
| BTC | Coinbase BTC-USD daily close | 2021-01-07 … 2026-09-18 · 2081 observations |
| ETH | Coinbase ETH-USD daily close | 2021-01-07 … 2026-09-18 · 2081 observations |
| CNY | ECB reference rate via Frankfurter | 2021-01-07 … 2026-09-18 · 1461 observations |
| USD | quote currency, fixed at 1 | 2021-01-07 … 2021-01-07 · 1 observations |
| GOLD | LBMA gold PM fix (USD) | 1968-04-01 … 2026-09-17 · 14685 observations |
| CU | IMF global copper price via FRED (monthly) | 1992-01-01 … 2026-07-01 · 415 observations |
| OIL | Brent Europe spot via FRED (daily) | 1987-05-20 … 2026-09-15 · 9087 observations |
| UX | IMF uranium price via FRED (monthly) | 1992-01-01 … 2026-07-01 · 415 observations |

copper and uranium publish monthly and carry forward between prints, as a closed market does. the uranium assessment is the weakest fix in the basket, which is why it carries the smallest weight.

## drift

quantities never change, so shares do. the basket was written at 35% crypto, 30% fiat, 35% elements; since 2022-01-07 bitcoin and ether have given up 1.8 points of share against the rest, leaving the basket at 33.1% crypto today. this is the arithmetic of fixed quantities, not a flaw in the fixes — but over a 25-80 year lease it is the property that decides what the obligation actually tracks. the T4 review valve exists for exactly this question, and it moves at most one leg of at most 10% weight every fifth year.

## what a lease actually paid

the machinery of §2 run from the base date: the basket priced in bitcoin, each annual step collared at +35%/−15%, the dual floor holding underneath. a lease signed on 2022-01-07 at one CX of rent invoiced $0.99 in its first year and $2.49 in its last — +25.6% a year, compounded.

| year | basket in btc | rent owed | invoice | set by |
|---|---|---|---|---|
| 2022-01-07 | 0.00002098 | 0.00002098 | $0.99 | basket |
| 2023-01-07 | 0.00003219 | 0.00003617 | $0.99 | dollar floor |
| 2024-01-07 | 0.00003038 | 0.00003403 | $0.99 | dollar floor |
| 2025-01-07 | 0.00001772 | 0.00002892 | $1.93 | collar, fall held |
| 2026-01-07 | 0.00001386 | 0.00002458 | $2.49 | collar, fall held |

of the 4 anniversaries after signing: the basket set the rent outright in 0 years, the collar capped a rise in 0 and held a fall in 2, the dollar floor bound in 2 and the satoshi floor in 0. where a floor bound, the tenant owed year-zero money regardless of the basket — the dollar leg when bitcoin had fallen, the satoshi leg when it had outrun the basket: the protocol's bitcoin-standard reading. where the collar held a fall, the rent in sats came down 15% a year while the basket in sats fell faster; the dollar invoice still moved with bitcoin. 

## today

| leg | fix (usd) | share |
|---|---|---|
| BTC | 80,764.32 | 23.6% |
| ETH | 2,567.47 | 9.5% |
| CNY | 0.144894 | 9.7% |
| USD | 1 | 10.4% |
| GOLD | 4,428.47 | 25.8% |
| CU | 12,580.69 | 9.3% |
| OIL | 84.40 | 4.1% |
| UX | 67.66 | 7.1% |

the fix is published daily at [cyberia.my/cx](https://cyberia.my/cx) and rebuilt from source by [[cx]]. generated 2026-09-18.
