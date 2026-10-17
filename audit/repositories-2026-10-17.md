---
tags: cyber, cyberia, audit, repositories
alias: repositories audit 2026-10-17, repository shape evidence
crystal-type: measure
crystal-domain: cyberia
---

# repositories · 2026-10-17

the evidence behind [[d7 repository shape]]: what the organization's 118 repositories are, who visits them, what couples them, and what the prior art says. measured on 2026-10-17 with `gh`, the crates.io api and the trees in `~/cyber`.

## the inventory

| count | what |
|---|---|
| 118 | repositories in `cyberia-to`; 75 public, 43 private, 3 archived |
| 87 | pushed in the last 30 days — the organization is alive, mostly by agents |
| 61 | Rust; 31 hold only pages; 7 Python; 5 TypeScript |
| 52 | named by the ladder (`soft3/release/components.toml`, 79 components on ten rungs) |
| 15 · 12 · 10 · 10 | warriors · language seeds · cyberia shelf · bootloader shelf (`.github/registry/groups.toml`) |

the ladder already distinguishes `crate`, `part` (a named part that is not its own crate: six parts of trident live in one repository, nine parts of cy in `cyb`), `product`, `network`, `ops`. the registry in `.github` exists because 118 doors need a map.

## who comes

stars: go-cyber 360 · cyb 174 · chaingear 82 · cyber 53 · space-pussy 12 · trident 10 · honeycrisp 7 · erga 5 · cyber-valley 3 · soft3 2; every other repository has one or none. the ~60 repositories of the new stack hold about 30 stars together.

traffic, 14 days, all 72 public repositories: **446 views by 188 unique visitors**. cyb 106 uniques, cyber 23, trident 12, soft3 6; **68 of 72 repositories had fewer than five visitors**. referrers are github.com itself, t.co and a few Google hits on trident; the most visited paths are `cyb/issues`, `cyb/releases`, `cyber/pulls`. the 20,736 clones are our own agents and runners (soft3 2,529, zheng 1,104, radio 869).

reading: on github the organization has three doors — cyb, cyber, trident — and the rest is invisible. a visitor who lands on `lens` sees one star and no context.

## crates.io

21 of the 47 main crates checked are published under `cyberia-to`; ~7,000 downloads in total, mostly our own ci. publishing already happens from folders: `unimem` and `rane` from honeycrisp, `strata-core` from strata, `cyber-tok` from plumb, three crates (`cyber-mudra`, `cyber-rune`, `inf-cli`) published without a repository link. six repository names are taken on crates.io by others — `cy`, `mir`, `optica`, `particle`, `trop-cli`, `wasmi` — so repository name and crate name are already different things. crates.io does not care how many repositories hold the crates.

## what couples the repositories

- path dependencies into siblings: honeycrisp 107 references, rs 51, strata 48, cyber-bao 39, evy 27, hemera 24; git dependencies on radio 18, hemera 7.
- `soft3/release/phase1.toml` pins eight sibling revisions for the release train; the rule "a bump pull request, never a path edit" exists only because the parts live apart.
- the component-boundary change of 2026-10-07 took **16 pull requests across 17 repositories**, several stacked on other open pull requests because origin defaults did not build against local siblings (`soft3/roadmap/component-boundaries.md`).
- continuation slices wait for the row's first pull request to merge in another repository ([[launch]] rows).
- open pull requests today: 113 across 38 repositories; 23 repositories hold one or two.

## prior art

- **polkadot-sdk** (Substrate + Polkadot + Cumulus, merged 2023-08): open-to-merge time fell about 25 % a month after the merge, the share of issues resolved rose from 39–48 % to 50–55 %, and the up-to-30 monthly "companion" pull requests disappeared; merged pull-request volume fell and the authors call that a misleading metric ([forum](https://forum.polkadot.network/t/one-repo-to-rule-them-all-a-data-driven-look-at-polkadot-s-monorepo/5976), [article](https://madhoney.blog/2024/01/29/one-repo-to-rule-them-all/), [announcement](https://forum.polkadot.network/t/psa-parity-is-currently-working-on-merging-the-polkadot-stack-repositories-into-one-single-repository/2883)).
- the rust norm: one workspace per product, many crates published from its folders — bevy (~50 crates), nushell (42 crates; our `nu` fork carries all 42 in one repository), iroh, wasmi, risc0. separate repositories appear where cadence, ownership or audience differ (tokio keeps mio and tracing apart).
- github mechanics ([rename](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository), [transfer](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)): a rename or a transfer keeps stars, issues and watchers and redirects the old address; folding repository B into a folder of A keeps nothing of B's — stars and watchers do not merge, old links die unless B stays as an archived pointer. issues move between repositories of one organization; pull requests do not. an archived repository keeps its stars and its page.

## the terms of cyberia, applied

from [[dev]] § the objects: a **product** is a goal kept alive, one per rung, its page the door of its repository; a **project** is a task tree that closes; a part (a chip) is a part of one product, never a dependency, and no component depends on a rung above its own; a **warrior** is one per target family. github knows one durable unit, the repository. so the mapping that follows from the ontology, not from taste: a repository is the door of something that stays — a product, a warrior, a network, the organization; parts are folders of their product; projects are pages and branches, never repositories.

against that rule the inventory reads:

| today | by the rule |
|---|---|
| 45 repositories for rungs 1–7 (kernel + core) | 7 product repositories, parts as workspace folders |
| zheng, lens, bbg beside joy | `joy/zheng`, `joy/lens`, `joy/bbg` — one audience: whoever proves |
| 12 empty language-seed repositories | folders of `neural` |
| true-cyber, ctx, uhash beside cyber | folders of `cyber` |
| cyberia-meme, cyberia-capital, episode-1, bootloader as repositories | projects: pages in `projects/`, their artifacts in the product's repository |
| warriors, one per chain | stay — each has its own audience and cadence |
| bostrom, space-pussy, go-cyber, chaingear | stay — networks and monuments; archived keeps the 442 stars |
| honeycrisp, optica | stay — a part with its own audience and name is the one exception a part earns |
| 43 private repositories | untouched by this question; public and private cannot share a repository |

## costs of folding, measured where possible

- history: `git subtree add` or `git filter-repo` keeps blame; a day of agent work per rung with the build green at the end.
- links: the old repository stays, archived, with a one-line README pointing at the folder; nothing breaks; crates.io `repository` fields update on the next publish.
- ci: a workspace builds everything unless workflows filter by path; the Mac runner is the bottleneck, so path filters are a precondition, not a nicety.
- size: cyb 797 MB and lytics 547 MB carry media that belongs in particles anyway; radio 296 MB (the iroh fork) is the heaviest honest part.
- queues: 113 pull requests over 38 repositories become ~10 queues; one is easier to read than thirty-eight, and it is also longer.
- permissions: one owner today; folder-level CODEOWNERS covers the rest.
