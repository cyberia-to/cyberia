---
tags: cyber, cyberia, audit, repositories
alias: repository layout audit 2026-11-22, workspace counts evidence
crystal-type: measure
crystal-domain: cyberia
---

# repository layout · 2026-11-22

the evidence behind [[workspace]] § measured: which of the home's repositories carry each directory of the standard layout at their current head. this report counts root entries only — it says that a repository has a `specs/` at its root, not what is inside it.

## the method

measured on 2026-11-22 against the working clones in `~/cyber`, one `git ls-tree` per repository head:

```sh
cd ~/cyber
for d in */; do
  r="${d%/}"
  git -C "$r" ls-tree --name-only HEAD | sed "s|^|$r\t|"
done > home-roots.tsv

# then, per name:
awk -F'\t' -v n=specs '$2==n {print $1}' home-roots.tsv | sort -u | wc -l
```

113 of the directories in `~/cyber` are git repositories and every one of them answered: 113 heads read, 2257 root entries in total. the heads are listed in § the revisions, so every number here can be reproduced.

the limits: these are the clones on the owner's desk, not the remotes — a repository whose origin has moved ahead is counted at the revision named below. the previous inventory, [[repositories audit 2026-10-17]], counted 118 repositories through `gh` and the crates.io api; it includes remotes with no clone here and archived repositories, which is why its total is higher and why it does not back these figures.

## the counts

| directory | repositories | | directory | repositories |
|---|---|---|---|---|
| `specs/` | 36 | | `rs/` | 21 |
| `audit/` | 30 | | `src/` | 21 |
| `docs/` | 29 | | `crates/` | 11 |
| `cli/` | 23 | | `roadmap/` | 19 |
| `scripts/` | 20 | | `tests/` | 14 |
| `.github/` | 37 | | `reference/` | 10 |

the other implementation directories of the standard are rare: `py/` in 1, `js/` in 2, `cw/` in 3. `Cargo.toml` stands at the root of 52.

the files of the root: `README.md` in 103, `LICENSE` in 30, `AGENTS.md` in 41, `CHANGELOG.md` in 13.

## what does not fit the standard

| what | repositories |
|---|---|
| `reference/` — the contract under its old name | apparatus, cyb, gaw, pearla, rs, tolya, trident, vitalina, xena, zenda |
| `proposals/` — `roadmap/` under its old name | foculus, soft3 |
| `crate/` — `rs/` under another name | soft3 |
| `.claude/` committed, holding plans and reports | 28 repositories |
| no `AGENTS.md` | 72 repositories |
| no `specs/` | 77 repositories |

for a graph or a landing page a missing `specs/` is right; for a component it is a hole. this report does not say which is which.

## the revisions

the head of each repository at the time of the measurement:

aos 77c2e6b82f · apparatus b1991b9e55 · arc 7f10855296 · bbg 2294281310 · bel 9668806709 · bita cff2b0af4d · bootloader d7e3ac029b · bostrom 3604c53cc4 · bt 7d52d029be · cloud-forest 5e2c0256a5 · conformance ff726be545 · crystal f2fab3c5f9 · ctx 3a4567b10a · cve e58ec8befb · cx d05fafef0d · cy 4f9799fe02 · cyb 8957982dd0 · cyber-valley 1eb6ecabb7 · cyber 68f1260a36 · cybergraph 0a70b6a9c1 · cyberia-blog 227e5927db · cyberia-capital fd043b412f · cyberia-meme aeeef0a3b0 · cyberia-my 33e2de92ea · cyberia.to 16a4c1746e · cyberia b367ffdec9 · cybernet e7ba0351f9 · cybernode 0642654438 · cyberstates 3d67ab4eb8 · cybervalley-io 3b98b4e466 · cybervalley c7b1fcda7f · cybics 4b082a314b · dif 75673ab9a3 · eidos d7d90fbac8 · endeka 67dded3800 · episode-1 697eefaed8 · erga ba703c3185 · evy 14c8d3e830 · file e29b4c7480 · foculus 4ae1a79b55 · fs f1ab2516b6 · gaw 55c90a9f2a · glia 477d91c0a7 · go-cyber cdf00d88bf · hemera b58ae54c09 · honeycrisp 595ce26265 · hub 88b8e7cd22 · ignes 2872e906d0 · inf bf379879b6 · joy 521ec9efd1 · kadek 97aeea58e8 · lens 11113c68f5 · li 41049277e4 · lytics 02c98495de · mail d674f472f6 · maker 6e28681419 · midao 6ded54a75b · mir b9c832d501 · mona ddb62bae26 · mudra 3969c7a3b2 · neural 47b086c2e3 · neuron cec2b8e901 · nika 3dfb67415a · nox 49348be573 · nu 1e58416ef0 · omi fd380006ae · opt b5dcfe8464 · optica aff8514950 · organiq 0169e85d11 · oxytocin 44e2843a65 · pearla 9d4b346e38 · perla d06b980d3f · portal e376fa09b3 · prysm f66cbd82ca · pure f219cb5a3b · qu a3820d6cc1 · quanta e240b60839 · radio 5e0dc1f78c · ren b791f6b540 · rockets aafd7f1afd · rs a6ebeeeead · rune 6d660d1c2d · sec 99e076daa9 · seer 308f209530 · seq 575898a50d · sigma 93ae6e201a · simulation 5483a3f7b4 · soft3 3045d54cb1 · soma 1d3fe69846 · space-pussy 2325ecd437 · spark 400cd9a178 · strata 5ef0c84d15 · superhuman 386c311c90 · sym 446865716d · tade c7d404aa8a · ten b4418cf182 · tok e27da0dff7 · tolya 26c89c31ac · trident dd3cbe880b · trisha fa6a3bee3d · tru 44725bd23c · true-cyber b58589f130 · uhash 054bf3dddb · valkyra 9820f3e183 · vault 4d73b907b9 · vitalina f656ef3cf9 · warriors 72a4f75289 · wav 3c47ffea54 · wysm d6e840e7d3 · xena bfefc5b7cd · zenda 50aecfa22c · zheng ecf2491bd7 · zoya ef8f582f25
