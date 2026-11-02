---
tags: cyber, cyberia, project, pussy, launch
alias: pussy, pussy launch, pussy reborn, $PUSSY launch, space-pussy launch
crystal-type: plan
crystal-domain: cyberia
status: doing
owner: master
serves: G1
stage: 2026-11-05
---

# pussy

the first project of the state since 2026-11-01: [[bootloader/tokens/$PUSSY|space-pussy]] reborn as a public [[soft3]] chain with live state, from its burial snapshot. the tracker of the launch stays [[cyber/launch]]; this page is the project's passport and the order in which every task of the pool now stands.

## the owner's word · 2026-11-01

translated from the owner's message (no link exists): "this thread exists to force the launch of spacepussy $PUSSY as soon as possible — little is left. make it the top-priority project in the apparatus and re-think every task in the pool against it. pussy launches in its public form, but [[tru]] and [[foculus]] must be full — fully on proofs, without signatures of course, with live state. the red date stays 5 November, earlier is allowed. turn the machine on and don't slow down — prepare, build, assemble; we really have to launch."

## the owner's word · 2026-11-02

translated (no link exists): "there will be no freeze on 2 November — we work until the end. add to the project that our task now is to launch a network with the possibility of a revert — the state is public and easy to revert — this has to be built right into the protocol."

so the task now reads: launch pussy's network public and revertible. a revert is a rule of the protocol that every node follows the same way, with no signature behind it (2026-11-01: "without signatures"), not an operator resyncing by hand. today `cybernode/specs/chain.md` has only the reorg limit of 119 blocks (§5.2) and the foundation checkpoints (§5.3, key zero); nothing rewinds deeper. the director's row P9 carries it (`soft3/release/director/plan.md`, D19, [soft3#654](https://github.com/cyberia-to/soft3/pull/654)).

## the measure

pussy's chain is live in public from its burial snapshot, mined by more than one host, its state readable at a public endpoint, and a revert by the protocol's own rule rehearsed on the alpha network before genesis; red date 2026-11-05 13:37:00 UTC, earlier if ready.

## the target and the distance · 2026-11-01

the target is the owner's sentence above. the distance is measured from the repositories on 2026-11-01; every row names its evidence.

| part of the target | today | distance |
|---|---|---|
| public chain, live state | rehearsal network pussy-rc live on cyberproxy, deimos, jupiter at height ≈ 45,580, on the 2026-10-16 binary `136721a` (probed 2026-11-01 09:00 UTC); the qualified node is soft3 `release/phase1` `b6f22dc`, green on all five legs of rehearsal [41201610001](https://github.com/cyberia-to/soft3/actions/runs/41201610001), pinned by `soft3/release/pussy-stand.toml` | deploy the stand on cyberproxy + agent-a (director plan P3, [soft3#493](https://github.com/cyberia-to/soft3/pull/493)), rehearse, genesis |
| without signatures: checkpoints | both genesis files carry a zero checkpoint key; no signer exists | none: the owner's "without signatures" answers H-01 of [soft3#398](https://github.com/cyberia-to/soft3/pull/398) as "launch without a foundation key"; the reorg exposure stays a named hole of [[cyber/launch]] |
| without signatures: transactions | every transfer, cyberlink and claim carries an NSIG1 secp256k1 signature (`cybernode/specs/chain.md` §2.7, `rs/src/chain/sigs.rs`) | authorization by a zheng proof of the secret behind the neuron id (`soft3/proposals/proven-present.md` decision 9); the hiding proof of a hemera preimage exists on zheng `release/0.4` (veil, 63.9 KB, prove 143 ms, verify 10 ms, `zheng/audit/zk-profile-2026-10.md`), no chain kind, no wallet path; the legacy claim needs secp256k1 proven in-circuit or kept for the one-time claim |
| fully on proofs: blocks | proven-present phase S0 only: the corpus writer (`cybernode/rs/src/chain/corpus.rs`); no block relation, no proof field in the header | phases S1–S4 of `soft3/proposals/proven-present.md`, status `proposed` |
| tru full | the epoch engine is consensus (φ*, gradient attribution, ground weight; pussy settlement 0.12 s, `tru/audit/epoch-settlement-2026-10.md`); serum, ICBS, annuity, lottery exist as unwired building blocks; no zheng relation for φ* (`zheng/specs/phi-spmv.md`: legacy) | the φ* relation (estimated, not measured: 0.5–1 B cycles per epoch at pussy size), the reports rule set (kind 10, serum, ICBS, annuity) |
| foculus full | the root chain orders by Nakamoto proof of work (decision 2026-10-17); foculus master still proves through zheng's retired unsound fold; the sound proofs are open PRs [foculus#61](https://github.com/cyberia-to/foculus/pull/61), [#63](https://github.com/cyberia-to/foculus/pull/63), [#66](https://github.com/cyberia-to/foculus/pull/66), [#86](https://github.com/cyberia-to/foculus/pull/86); never run across machines | land the sound proofs, one kernel for impulse and φ*, the impulse constraint system, a real beacon, a multi-machine network gate |

## the decision asked of the owner

the two halves of the target do not meet on 2026-11-05: the proof layers measure in weeks, the date in days. one of two, the owner's:

1. genesis on the date from the qualified stand: public, live state, no checkpoint key, natively validated; the proof layers (transaction proofs, block proofs, the φ* relation, foculus's sound proofs, the reports rule set) ship as height-activated rule sets, each a named hole of [[cyber/launch]] until its fork lands. this is the owner's own rule of 2026-10-30 ("go on the air as soon as possible with the holes known and named in public"), and the protocol revert of 2026-11-02 is what makes a hole cheap to undo. recommended. there is no freeze (the owner, 2026-11-02).
2. genesis waits until the chain is full and proven; no date.

asked with the launch decision on [[cyber/launch]] and in the director's plan (`soft3/release/director/plan.md`, D16).

## the critical path

| sub-task | status |
|---|---|
| the owner's choice above, and (a) of [cyber#154](https://github.com/cyberia-to/cyber/pull/154): pussy ships from the pinned stand | open |
| the body-malleation fix [soft3#350](https://github.com/cyberia-to/soft3/pull/350) and the halt sentence [soft3#479](https://github.com/cyberia-to/soft3/pull/479) | open |
| pussy's chain id and block-0 id pinned in the binary (`params.rs` carries zeros; today `--genesis` by hand) | open |
| the stand off Hetzner, deimos and jupiter retired (director P3) | done 2026-11-01 |
| a rehearsal of the stand on the new peer set, 24 h of agreed epoch records (registry row 41) | open |
| revert in the protocol: the spec amendment with options, the chosen rule implemented, a revert rehearsed on the alpha network (director P9) | open |
| the alpha network: the stand on two peers (194.107.163.6 + agent-a), live since 2026-11-01 19:47 UTC, `pussy-rc` genesis `d20bab4b…`, block 0 `d4d34a70…` | doing |
| the known holes published; spacepussy.ai shows the attempt and the holes (today it says "no date") | open |
| genesis 13:37:00 UTC, the miners, a public endpoint | open |
| the proof layers as rule sets: transaction proofs, block relation, φ* relation, foculus sound proofs, reports rule set | open |

## the pool, re-thought against pussy · 2026-11-01

every open task, with its place against this project. "after genesis" holds a task untouched until 2026-11-05 13:37 UTC; "beside" means it neither helps nor blocks pussy and keeps its own owner.

| task | where | place |
|---|---|---|
| director P1, P2b, P3, C2a, R1 | `soft3/release/director/plan.md` | the critical path |
| director L1–L4, L3b–L3d, G9, G10b, R0 (landings of the 0.4 line on default branches) | same | off the path if (a) of cyber#154 is taken; resume after genesis |
| director C4, [cybernode#1](https://github.com/cyberia-to/cybernode/pull/1), [soft3#407](https://github.com/cyberia-to/soft3/pull/407) (the node moves to cybernode) | same | after genesis (D15) |
| director S1 (dependabot) | same | beside, security fixes may pass the freeze |
| a1 access declarations | `apparatus/tasks/a1-access-declarations.md` | after genesis, except the access P3 needs on cyberproxy |
| c1, c4–c7 the cities and the cockpit | `apparatus/tasks/` | after genesis |
| cv-1, cv-2, cv-3 Cyber Valley closing and treasury | `apparatus/tasks/` | beside: the people of Cyber Valley own them, nothing of pussy waits on them |
| d1, d3, d4, d6, d7 the owner's reviews of fathership | `apparatus/tasks/` | after genesis: they take the owner's attention pussy needs |
| fathership phase 0 | [[fathership]] | after genesis, except the quality circle every pussy PR passes |
