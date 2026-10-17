---
tags: cyber, cyberia, task, decision
alias: d7 repository shape, d7
crystal-type: process
crystal-domain: cyberia
kind: review
status: open
owner: master
serves: fathership
---

# d7 · the shape of the repositories

118 repositories, 75 public; three of them are visited, the rest are invisible, and one change to a boundary costs sixteen pull requests. evidence: [[repositories audit 2026-10-17]].

## for folding

- github shows three doors — cyb, cyber, trident — and 68 of 72 public repositories had fewer than five visitors in two weeks; stars spread over sixty repositories never trend, one door does.
- the ontology already says it: a product is the durable thing, a part is never a dependency, a project closes; github's one durable unit is the repository, so a repository should be the door of something that stays.
- the release train's sibling pins, the companion pull requests, the slices waiting on another repository's merge — all are costs of living apart. polkadot-sdk measured the gain of merging: a quarter faster merges each month, companions gone.
- crates.io publishes from folders today; nothing on the package side needs a repository per crate.

## against folding

- a repository with its own audience and name is a marketing asset: honeycrisp speaks to Apple Silicon developers who will never open soft3; each warrior speaks to one chain's miners; trident has a site and its own users.
- folding loses what github attached to the old name — stars, watchers, issue addresses — unless the old repository stays as an archived pointer; the numbers at stake are one or two stars per part.
- one queue is longer; ci must filter by path or the Mac runner builds Metal for a typo in a page.
- a week of agent work and a period when two addresses exist for one thing.

## proposal

the rule: **a repository is the door of something that stays** — a product, a warrior, a network, the organization. parts are folders of their product's workspace and publish to crates.io from there. projects are pages and branches, never repositories. a part keeps its own repository only when it has its own audience under its own name; today that is honeycrisp and optica, and the list is a decision, not a drift.

the cut the owner proposed on 2026-10-17, kernel apart from core, refines the rule by audience and cadence:

- **core is one repository, `soft3`** — rungs 4–7: cybergraph (with file, neuron, tok, tru), neural (with inf, rune, eidos, mudra, spark, nu, rs, fs and the twelve seed repositories), cy (with glia, soma, seer, sigma, vault), radio, foculus, tade, soft3.js. one audience, the builders of the stack; one cadence, the weekly train; one door, soft3.org; the specs and `release/` already live there. the coupling is densest here, so one queue beats four.
- **kernel is three repositories, `nox` · `trident` · `joy`** — the kernel's worth is that strangers use it, and strangers arrive by name: vm people at nox (with strata and hemera), language people at trident (its own site and the only kernel repository with search traffic), provers at joy (with lens, zheng, bbg). the kernel freezes by the semver law; what freezes lives apart from what moves weekly. honeycrisp stays apart for its own audience.
- **the boundary is versioned**: soft3 depends on `cyber-nox`, `trident-lang`, `cyber-joy` from crates.io, never by path. every sibling pinned in `soft3/release/phase1.toml` — strata, hemera, lens, nox, zheng, bbg, radio, foculus — ends up inside nox, joy or soft3, so the pin file disappears, and "no component depends on a rung above its own" is checked by the compiler, not by review.

the order: (1) rung 3 first — zheng, lens, bbg into joy — as the proof, one day, build green, old repositories archived with pointers; (2) nox gathers strata and hemera; (3) soft3 gathers rungs 4–7, one rung per week on the train, kernel crates consumed from crates.io; (4) rung 9 — true-cyber, ctx, uhash into cyber; (5) the cyberia shelf last, when the optica build mounts folders as it mounts repositories today. warriors, networks and the bootloader monuments stay. rungs 1–7: 45 repositories → 5; public overall: 75 → about 30, the archived pointers fading from the front page.

## verdict

—
