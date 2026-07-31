---
tags: cyberia, protocol, cybernomics
alias: century annex, rent annex, index annex
crystal-type: source
crystal-domain: cyberia
---
# century annex

model annex for a lease referencing the [[century index]] — the T1 document. everything a junior accountant needs to reproduce any invoice from public data. numbers below are a worked example at R₀ = $100,000/yr with indicative spot fixes of 2026-07-31; a signed annex replaces them with the 365-day TWAP fixes at signing (§3 of the index).

## 1. parameters

| parameter | value |
|---|---|
| R₀ (year-0 rent) | $100,000 |
| F (fiat floor leg) | $100,000 |
| weights BTC/ETH/GOLD/OIL/CU/U/CNH/USD | 20/15/15/5/10/5/15/15 |
| collar | +35% / −15% per year, in sats |
| numéraire | BTC · fixes USD-quoted |
| reset | annual anniversary, TWAP window ends 30 days before payment |
| settlement | IDR at JISDOR on invoice date (UU 7/2011) |

## 2. quantities (fixed for the life of the contract)

| leg | t₀ fix (example) | quantity qᵢ |
|---|---|---|
| BTC | $62,626 | 0.31935618 BTC (31,935,618 sats) |
| ETH | $1,857.97 | 8.073327 ETH |
| GOLD | $4,039.38/oz | 115.501 g |
| OIL | $91.82/bbl | 54.454 bbl |
| CU | $13,552.04/t | 737.90 kg |
| U | $80.00/lb U3O8 (indicative assessment level) | 62.50 lb |
| CNH | 6.765736 /USD | ¥101,486.04 |
| USD | 1 | $15,000.00 |

derived: X(t₀) = $62,626 · S₀ = R₀/X(t₀) = 1.596781 BTC = 159,678,089 sats.

## 3. worked invoice — hypothetical year 1

hypothetical year-1 TWAP fixes: BTC $75,000 · ETH $2,200 · GOLD $4,400 · OIL $85 · CU $14,500/t · U $90/lb · USD/CNY 7.00 · JISDOR 19,000.

1. mark quantities to market: I(t₁) = Σ qᵢ·Pᵢ = $108,503.30
2. price in bitcoin: S(t₁) = I/X = 108,503.30 / 75,000 = 1.446711 BTC
3. collar [S₀·0.85, S₀·1.35] = [1.357264, 2.155654] → 1.446711 passes unclamped
4. dual floor: max(S₀ = 1.596781, F/X = 100,000/75,000 = 1.333333) = 1.596781 → floor BINDS
5. R(t₁) = 1.596781 BTC = 159,678,089 sats
6. invoice: R·X = $119,758.57 → × 19,000 = Rp 2,275,412,768

reading of this year: the basket grew 8.5% but bitcoin grew 19.8% — the sat floor binds and the tenant owes the same sats as year 0, worth more dollars. the lease is behaving as a bitcoin-standard obligation, exactly as designed.

## 4. fix sources

per the [[century index]] §3 table: Pyth primary (BTC/USD, ETH/USD, XAU/USD, USD/CNH), ICE Brent, LME copper, and CME UxC uranium settles primary for the physical legs, institutional fallbacks per the T3 waterfall. TWAP = trailing 365 calendar days, last published value carried through market closures.

## 5. recomputation

any party may recompute steps 1–6 from the named public sources; on discrepancy the recomputation prevails (T5). disputes about this annex are arithmetic.
