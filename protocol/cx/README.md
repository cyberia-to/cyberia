---
tags: cyberia, protocol, cybernomics, cx
alias: cx, cx index, century index fix, index publication
crystal-type: entity
crystal-domain: cyberia
---
# cx

the published fix of the [[century-index]] — ticker CX. one CX is the basket that cost one dollar on the base date, so the level is a price: $1.41 on 2026-11-18, against $1 on 2022-01-07. the protocol page defines the instrument; this subgraph carries what it actually read.

## pages

- [[cx history]] — the monthly level since the base date, the quantities, the sources
- [[century-index]] — the protocol: basket, collar, floor, contract theses

## how the fix is built

1. pull each leg from its public source
2. carry every fix onto a dense daily calendar — a closed market holds its last print
3. average each leg over the trailing 365 days
4. hold the quantities fixed from the base date and sum them at today's averages

the arithmetic is integer fixed-point end to end, so the same day's data yields the same level on any machine — the index is reproducible by anyone holding the sources, which is the whole point of an obligation nobody has to be trusted about.

## the basket today

| leg | group | share | weight at base |
|---|---|---|---|
| BTC | crypto | 22.4% | 20% |
| ETH | crypto | 8.6% | 15% |
| CNY | fiat | 10.0% | 15% |
| USD | fiat | 10.6% | 15% |
| GOLD | elements | 26.1% | 15% |
| CU | elements | 10.0% | 10% |
| OIL | elements | 4.6% | 5% |
| UX | elements | 7.4% | 5% |

shares drift as prices move; the quantities behind them never do. measured in itself the index is constant, so the obligation carries no numéraire.
