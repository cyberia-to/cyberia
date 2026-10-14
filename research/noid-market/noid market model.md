---
tags: cyberia, research, noid, market, store-of-value
alias: noid market, NOID market model, parano1d market research
crystal-type: research
crystal-domain: cyberia
date: 2026-10-13
status: model
---
# noid market model

a market model of [[parano1d]] (NOID): target framing, comparable set, a security-budget anchor, and a probabilistic cap estimate with catalysts. read through cyberia's lens — **state management and value preservation** — because that is the part of the design a cyberstate can borrow: NOID is the first production network whose entire state is a verifiable present, and its market price is a live vote on how much that property is worth.

every number below names its source and date; estimates are marked ≈; probabilities are subjective and say so. measured: the node readings and emissions math. open: the scenario probabilities, the privacy-upgrade timing, the QTC duel. refuted: nothing yet.

## the question the market has not asked

> **what is a store of value worth that its holder can verify alone, completely, forever — and that is already post-quantum?**

bitcoin answers scarcity but not permanent verifiability (its chain becomes an archive only institutions can hold) and not the quantum horizon (PQ migration is an open debate). NOID is today the only asset for which both answers exist *by construction*: validation from genesis in O(1), NIST Category-1 end-to-end soundness with an executable certificate. the market has not priced this because it has not formulated the question. the model below is an estimate of the price when it does.

## layer 0. what NOID is, measured

readings from a live v2.0.3 node, 2026-10-13: network ≈ 207 GH/s at observed 16 s intervals (30 s target; difficulty rising), expected work ≈ 5.30 T hashes/block, reward 16 NOID gross (90 % to miners during the development allocation ≈ 14.4), supply 10.58 M, live UTXOs 87.7 k. codebase: 393 kLOC, mainnet live since 2026-08-21, Category-1 gate-depth floor 2^173.39 (executable certificate), per-block validity proof 913 KB–1.08 MB with O(1)-in-height verification, empty-block proving ≈ 16.6 s on a laptop-class CPU.

the structural facts that matter for the market model:

- **verification horizon is the product.** state validates from genesis in O(1); bodies prune; receipts stay portable. an asset bought for decades must be verifiable in decades.
- **proof-gated production.** hashpower alone cannot produce a block — a proving node must exist first. CPU-only by design (PMULL/VPCLMUL), pools reduced to nonce oracles that cannot censor templates.
- **no hard cap.** issuance steps 16 → 11.3 → 8 → … → 1 NOID, permanent tail — asymptotic scarcity, the monero pattern, not the bitcoin pattern.
- **the two admitted deficits:** amounts are public (wallet authorization is witness-hiding; amounts are not), and throughput is 2.1–6.9 tx/s capacity.

## layer 1. the security-budget anchor

emission to miners ≈ 77.8 k NOID/day ≈ **$14 k/day ≈ $5 M/year** at the 2026-10-10 exchange print, against a market cap of ≈ **$1.9 M** — the annual security budget exceeds the cap ≈ 2.6×. **revision, 2026-10-13:** the cap has since crept to ≈ $3 M on thin liquidity, with no catalyst and no market-making — pre-narrative accumulation, the market beginning to discover the design before it has formulated the question (§0). the budget/cap imbalance persists (≈ 1.7×). bitcoin's budget/cap ratio is ≈ 1 %/yr. two resolutions, and the market must pick:

- miners are mining *upward* (hashrate persists) → cap re-rates toward $300–500 M at the current budget;
- the budget collapses to equilibrium yield → the cap settles in the niche floor.

a 200+ GH/s CPU network at a $2 M cap is a leveraged directional bet by miners, not an equilibrium. this asymmetry is the strongest single datapoint in the model.

## layer 1.5. miner structure and dump-vs-hodl, measured

measured 2026-10-13 against a live v2.0.3 node (`paranoid_getBlockHeader` over all ~221 k headers + `paranoid_getSlotsByOwner` per miner; script and raw data in `~/cyber/.tmp/noid-analytics/`):

- **only 109 distinct mining addresses** have ever produced a block. the top-10 hold **96.3 %** of all blocks; the largest single address mined ≈ 1.97 M NOID (20 % of all miner supply). the network is ~100 entities, mostly always-on servers — the "thousands of MacBooks" hypothesis is refuted for the current era.
- **retention at mining addresses ≈ 1.5 %**: 99.7 % of mined supply sits at addresses that moved essentially everything (retention < 10 %). reading: mined coins are churned or sold almost immediately — but on pruned data self-custody consolidation is indistinguishable from dumping, so 1.5 % is a *lower* bound for hodl, and the dump share proper needs exchange-deposit tagging.
- implication for the model: the decentralization leg of the narrative is early — concentration reflects proving-node economics (always-on servers win the proof-gated race). the GUI-miner leg of distribution has not yet shown up on-chain. the SoV scenarios do not depend on miner count, but the "CPU commodity money" narrative needs this number to grow into the thousands before it is evidence rather than aspiration.

## layer 2. the comparable set

| comp | ≈ cap | frame | NOID wins on | NOID loses on |
|---|---|---|---|---|
| bitcoin | ~$1.7 T | the only universally recognized SoV | verifiability horizon, post-quantum readiness | everything else |
| monero | ~$3–4 B | CPU commodity money + privacy | O(1) verification, Cat-1 proof, CPU purity | 12 years of Lindy, real privacy, volumes |
| kaspa | ~$3–4 B | fastest PoW | post-quantum, CPU accessibility | speed by orders of magnitude, listings |
| quantus (QTC) | tens of M$ (new) | "a store of value, not a smart contract platform" — the direct frame rival | CPU, certified soundness, statelessness | hard cap 21 M (scarcity mimicry), 12 s blocks, GPU pools exist |
| zcash | ~$0.6–1 B | privacy SoV | — | privacy is the product |
| mina | ~$0.4–0.7 B | succinct chain | PoW trust model, hash-only assumption | ecosystem, programmability |
| ergo | ~$0.1–0.2 B | PoW contracts + storage rent | post-quantum, CPU | applications |
| QRL | ~$15–30 M | anti-quantum token niche | everything technical | — this is the floor without a narrative |
| litecoin | ~$5–7 B | dead narrative, fair launch | liveness of development | listings, age |

reading: NOID sits at the intersection of three niches — post-quantum (QRL+QTC), CPU-PoW (XMR), succinctness (MINA) — with no single competitor on all three axes. the duel that matters is with QTC for the "post-quantum store of value" frame: scarcity+speed (QTC) versus certified soundness+permanent verifiability (NOID).

## layer 3. narratives, ranked

1. **post-quantum from block one** — the only pure play with an executable certificate; has a catalyst schedule (NIST migration, harvest-now-decrypt-later) most narratives lack.
2. **sovereign verifier** — anyone verifies everything forever, on a laptop; the monero ethos completed.
3. **CPU commodity money returns** — one-click GUI mining turns every holder into a miner; distribution as loyalty.
4. **academic legitimacy** — IACR-lineage cryptography, 0 TODOs in 393 kLOC.

anti-narratives (what the market will discount): 2–7 tx/s, ~1 MB proof per block (bandwidth), single author, no cap, no general programmability. **the SoV frame neutralizes the first and the fourth** — speed and programmability barely matter for a store of value, while compactness becomes an asset (live state only, growth fees bound it).

## layer 4. scenarios — conditional on the SoV frame

probability the SoV frame becomes NOID's leading frame: **≈ 45 %** (the most natural fit for its constraints; QTC fights for the same frame). conditional scenarios:

| scenario | cap | P (within SoV) | driver |
|---|---|---|---|
| floor (LTC precedent, live dev) | $50–100 M | 15 % | an honest CPU-PoW with active development holds above the niche floor |
| base | $150–400 M | 55 % | XMR-minus-privacy-plus-PQ at 1/10–1/20 of XMR |
| bull | $1–3 B | 25 % | a real quantum-FUD cycle on bitcoin; NOID the only ready asset; 0.1–0.2 % of BTC |
| tail | $3–8 B | 5 % | migration panic + capsule privacy on amounts shipped |

unconditional expectation ≈ 0.45 × (0.15·75 + 0.55·275 + 0.25·2000 + 0.05·5500) ≈ **≈ $0.4 B** versus ≈ $1.9 M today. the expectation is dominated by the bull tail; the median is the $150–400 M base. **all probabilities are subjective judgments, not statistics** — the model's value is the explicitness, not the precision.

## layer 5. catalysts and probability movers

| lever | moves | note |
|---|---|---|
| capsule privacy on amounts (in-house: `noid_fri_binius` zk-capsule already hides authorization) | base → 1/5–1/10 XMR | the single highest-leverage protocol change; converts "XMR minus privacy" into "XMR plus PQ plus statelessness" |
| quantum catalyst (BTC PQ debate in mainstream) | the tail only | scheduled but externally triggered; preparation = a media kit around the executable certificate |
| second developer / escrowed dev allocation | all scenarios up | cheapest cap-per-dollar upgrade; bus factor is the largest discount |
| listings beyond SafeTrade | ×2–3 per tier | everything except the tail carries listings itself |
| QTC winning the frame first | base → $100–150 M | the frame duel is live now and under-analyzed |

## layer 6. what cyberia takes from this

the cyberstate runs on the same two problems — **state management and value preservation**: the priced end of the [[migration-market]] clears citizenship and residency as assets; [[smart capital]] locks CX below market for ten years. NOID is a production case study in the properties such assets will need:

- **O(1)-in-history verification** — a citizenship or CX position must be verifiable by its holder in fifty years without an archive node; that is a design property, not a deployment detail.
- **live state over history** — pruning with portable receipts: obligations remain checkable without retaining every past transition. the cyberstate's status ladder (VISIT→STAY→SETTLE→BELONG) is exactly a carried-counter contract in parano1d's sense.
- **state-growth fees** — occupancy-priced burns bound the live set forever; a state that sells status must price its own storage.
- **proof-gated production as an anti-capture pattern** — whoever proves the transition owns it; pools can sell compute but not policy. relevant to any future cyberstate settlement layer.
- and the market lesson: **the question "verify alone, forever, post-quantum" is unpriced at ≈ $2 M today** — the same undervaluation applies to any state architecture that answers it before the market learns to ask.

open questions for the next revision: QTC's actual traction by listing and hashrate; the v3 privacy-upgrade timing from public development channels; whether the dev allocation escrow materializes.
