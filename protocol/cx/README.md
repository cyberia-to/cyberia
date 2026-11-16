---
tags: cyberia, protocol, cybernomics, cx
alias: cx, cx index, century index fix, index publication
crystal-type: entity
crystal-domain: cyberia
---
# cx

the published fix of the [[century-index]] — ticker CX. one CX is the basket that cost one dollar on the base date, so the level is a price: $1.31 on 2026-11-16, against $1 on 2022-01-07. the protocol page defines the instrument; this subgraph carries what it actually read.

## pages

- [[cx history]] — the monthly level since the base date, today's holdings, the sources
- [[century-index]] — the protocol: basket, collar, floor, contract theses

## how the fix is built

1. pull each leg from its public source
2. carry every fix onto a dense daily calendar — a closed market holds its last print
3. average each leg over the trailing 365 days
4. chain the weighted daily returns: each day the index earns Σ wᵢ · P̄ᵢ(t)/P̄ᵢ(t−1), the basket rebalanced to its weights every day
5. read the death rule: a leg whose average closes below a tenth of its peak since the base date leaves the basket, weight pro rata to the rest, never to return

the arithmetic is integer fixed-point end to end, so the same day's data yields the same level on any machine — the index is reproducible by anyone holding the sources, which is the whole point of an obligation nobody has to be trusted about.

## the basket

| leg | group | weight | of peak |
|---|---|---|---|
| BTC | crypto | 20% | 73% |
| ETH | crypto | 15% | 72% |
| CNY | fiat | 15% | 93% |
| USD | fiat | 15% | 100% |
| GOLD | elements | 15% | 99% |
| CU | elements | 10% | 100% |
| OIL | elements | 5% | 91% |
| UX | elements | 5% | 98% |

the weights hold every day by construction. measured in itself the index is constant, so the obligation carries no numéraire; a lease owes a number of CX.
