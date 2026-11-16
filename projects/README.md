---
tags: cyber, cyberia, projects
alias: projects of cyberia, the projects, cyberia projects, project list
crystal-type: entity
crystal-domain: cyberia
---

# projects

the projects lens of [[org]]: work that closes. a project is a task with sub-tasks ([[dev]] § the objects); it has an owner, a status and a page, and when every sub-task is done it is over — unlike a product, which is kept alive, and unlike the chronicle, which is infrastructure. a project's domain is an attribute of the project, as a product's is of the product; the registry of every domain the state holds is cybernode's, at [domains.cybernode.ai](https://domains.cybernode.ai).

this folder is the registry: one file per project, its passport — what it is, its domain, its repository, its stage, what it serves. a project that needs more than a passport keeps the rest in its own repository, never in a folder here.

a project is finite: it has a delivery, a date and a declaration — the page its link opens (the owner, 2026-11-16). what is kept alive and measured by revenue and capacity is a product and lives on [[products]]; a site is a product's door, never a project's. the order of this table is the priority: the first row is worked first. the owner moves a row up or down here, by hand or from the cockpit's projects tab, and every move is a commit — the history of priorities is the history of this file. there are no proposals any more, only projects (the owner, 2026-11-16): every repository keeps its projects in `projects/`, one page each, with `status:` in the front matter — `proposed` (a decision still open), `accepted` (decided, being delivered), `executed` or `done` (delivered, the date beside it), `rejected` or `superseded` (history). the page is the project's declaration. soft3's `proposals/` became `projects/` that day; cybernode was the first.

## how the table fills — from the bottom

the apparatus collects projects from the bottom: `apparatus/scripts/projects_collect.py` (run by the cockpit's collector every 15 minutes) reads `projects/*.md` of every repository under cyberia-to — on its default branch and on its release line (`release/phase1`, where soft3 integrates) — and **every page has a row here, whatever its status**: this is a management system, everything is seen (the owner, 2026-11-16). the row's stage is the page's status — draft, proposed, accepted, done (executed, implemented, delivered), rejected, superseded. a page without a row is appended at the bottom — the lowest priority until the owner drags it up — with the page as its declaration, its first sentence as the delivery and its `date:` as the date; a row whose page's status changed takes the new stage. the collector never reorders and never deletes: priority and removal are the owner's hand. each run that changes the table is one commit on cyberia main.

| project | delivery | date | stage |
|---|---|---|---|
| [[cyberia/projects/pussy\|launch spacepussy]] | the public pussy chain live with proofs, revertible, on the explorer | by readiness (red date 2026-11-05 passed) | doing |
| [[cyberia/projects/century-index\|launch century index]] | the index published every day at cx.cyberia.my, and the first lease priced in CX signed | — | doing |
| [[fathership]] | — | — | doing |
| [[cyberia/projects/oxytocin\|sell oxytocin]] | the one-threshold space in Sayan, Ubud, sold — everything for the sale is there, it has to sell | — | doing |
| [[bostrom\|launch bostrom]] | bostrom reborn as a public soft3 chain from its burial snapshot — after spacepussy launches and is debugged | after launch spacepussy | open |
| [[cyberia/projects/events\|events]] | — | — | paused |
| [[cyberia/projects/genome-protocol\|genome protocol]] | a page of knowledge | — | research |
| [[cyberia/projects/migration-market\|migration market]] | a page of knowledge | — | research |
| [[cyberia/projects/cyber-sheep\|cyber sheep]] | a page of knowledge | — | research |
| [[cyberia/projects/tech\|tech tree]] | a page of knowledge | — | research |
| [[cyberia/projects/noid-market\|noid market]] | a page of knowledge | — | research |
| [[cyberia/projects/smart capital\|smart capital]] | a page of knowledge | — | research |
| [[soft3/projects/cybernode\|cybernode]] | the node carved out of soft3 as rung 7, its own repository | 2026-10-27 | done |
| [[foculus/projects/view-certificates\|view certificates]] | > finality as evidence, not declaration: the quorum certificate without the | — | draft |
| [[kadek/projects/soft3-alignment\|kadek on soft3]] | Status: applied to specs, 2026-09-25. | — | proposed |
| [[mudra/projects/private-recovery-index\|private recovery index]] | make opening or restoring a private wallet depend on the wallet result requested, | — | draft |
| [[soft3/projects/component-page-canon\|One component, one page: the URL canon]] | > every component of the stack answers at one canonical address on | — | draft |
| [[soft3/projects/cybergraph-sync-tade-architecture\|cybergraph-sync-tade-architecture]] | > Superseded in part: the sync repo has since merged into foculus — the structural-sync substrate and the fork-choice that completes its merge are now one crate | 2026-06-07 | done |
| [[soft3/projects/goldilocks-parano1d\|goldilocks-parano1d]] | > parano1d is a production proof-native chain: 393 kLOC, 20 crates, mainnet live since 2026-08-21, every block carrying a recursive validity proof, PoW ordering | — | proposed |
| [[soft3/projects/metabolic-oracle\|the metabolic oracle]] | status: proposed · date: 2026-10-23 · owner's call: "this mechanism — without the agents — belongs in the core of cyber, not in cyberia's architecture." | — | proposed |
| [[soft3/projects/network-planes\|network-planes]] | > builds on cybergraph + sync + tade (2026-06, implemented), which merged the sync repo into foculus to kill two owners of one mechanism, and on component bound | — | proposed |
| [[soft3/projects/network-repos\|network-repos]] | the owner, 2026-10-17: every network has a configuration — a set of contracts (plumb), the genesis distribution, the starting parameters, the starting graph: a | — | proposed |
| [[soft3/projects/privacy-frozen\|privacy-frozen]] | hemera note (2026-10-16): the hemera#15 decision this page waits for is taken — hemera 0.4 (x⁷ in every round, 6 + 6 + 48 rounds, 32-byte digest kept) is the fr | — | proposed |
| [[soft3/projects/proof-system-repair\|one proof — the repair of zheng]] | hemera note (2026-10-16): the hash row below is decided — hemera 0.4 (hemera#15: x⁷ in every round, 6 + 6 + 48 rounds, Poseidon2 reference matrices, 32-byte dig | — | proposed |
| [[soft3/projects/proven-present\|proven-present]] | the property, fixed by the owner on 2026-10-17 as a base property of the system, cross-cutting and necessary: | — | proposed |
| [[soft3/projects/rooted-civilization\|rooted-civilization]] | > soft3.org sells a machine: collective, private, provable computing, thirty features, seven verbs. | — | proposed |
| [[soft3/projects/state-economics\|state-economics]] | > two products, three channels, four rules, one curve. | — | proposed |
| [[soft3/projects/steps-blocks-epochs\|steps-blocks-epochs]] | > soft3 has proofs (zheng), a state organ (bbg), a graph (cybergraph), a compiler (trident), a mining spec (fold-mining) — and no working blockchain. | — | proposed |
| [[soft3/projects/tade-one-exchange\|tade-one-exchange]] | > builds on cybergraph + sync + tade (implemented 2026-06), which made tade the wire substrate under radio and foculus. | — | proposed |
| [[soft3/projects/term\|term]] | > three inheritances, one language. | — | proposed |
| [[soft3/projects/vault-secret-custody\|Vault has its own home]] | Vault is now an independent component in | — | superseded |
| [[zheng/projects/dynamic-noun-memory\|Dynamic noun memory for native execution]] | This project extends the native Zheng execution relation toward computed | — | draft |
| [[zheng/projects/tagged-symbolic-relation\|Experimental tagged symbolic relation]] | This project defines execution::tagged, an opt-in circuit kernel. | — | draft |

research packs — a project whose output is a page of knowledge — sit in the same table and the same folder since 2026-10-23 (they were `research/`). moved to [[products]] on 2026-11-16 because they are kept alive, not delivered: cyber valley, the land console (my cyberia), cve, cyberstates, the meme state, etherland, cyberia capital, rockets. the source of everything is [github.com/cyberia-to](https://github.com/cyberia-to).
