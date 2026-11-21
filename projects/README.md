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

the apparatus collects projects from the bottom: `apparatus/scripts/projects_collect.py` (run by the cockpit's collector every 15 minutes) reads `projects/*.md` of every repository under cyberia-to — on its default branch and on its release line (`release/phase1`, where soft3 integrates) — and **every page has a row here, whatever its status**: this is a management system, everything is seen (the owner, 2026-11-16). the row's stage is the page's status — draft, proposed, accepted, done (executed, implemented, delivered), rejected, superseded. the product column says which product the project serves: the collector fills it from the page's repository, the owner corrects it here, and the cockpit counts projects per product from it. the part of column makes the projects a tree, as the products are (the owner, 2026-11-18): it names the project this one is part of, set by the owner from the project's page in the cockpit (a signed command the executor writes here), or — for a top project. every project has its page in the cockpit (/project/<name>): the generic page shows what this table and the passport say; a passport may name a custom view in its front matter (`view: launch` — the launch of spacepussy draws its live chain), registered in apparatus `cockpit/project.js`. a page without a row is appended at the bottom — the lowest priority until the owner drags it up — with the page as its declaration, its first sentence as the delivery and its `date:` as the date; a row whose page's status changed takes the new stage. the collector never reorders and never deletes: priority and removal are the owner's hand. each run that changes the table is one commit on cyberia main.

| project | product | part of | waits for | delivery | date | stage |
| --- | --- | --- | --- | --- | --- | --- |
| [[cyberia/projects/pussy\|launch spacepussy]] | $PUSSY | — | — | the public pussy chain live with proofs, revertible, on the explorer | by readiness (red date 2026-11-05 passed) | doing |
| [[cyberia/projects/century-index\|launch century index]] | cx | button | — | the index published every day at cx.cyberia.my, and the first lease priced in CX signed | — | doing |
| [[cyberia/projects/button\|button]] | my cyberia | — | midao registration | a plot on cyberia.my sold with the button: paid by bank or by crypto, its documents signed and registered, the right recorded | — | accepted |
| [[soft3/projects/state-economics\|design state economics]] | soft3 | launch spacepussy | — | two products, three channels, four rules, one curve. | — | proposed |
| [[apparatus/projects/combine\|the combine]] | apparatus | — | — | Every pull request of the organisation passes the inspection of the whole infrastructure before the owner sees it: whether it serves a project and a product, wh | — | doing |
| [[cyberia-blog/projects/chronicle\|write the chronicle]] | cyberia | — | — | The whole history of the project, from every source, read and told as one chronology: interesting, understandable and connected, with the price of BOOT running | — | accepted |
| [[fathership]] | cyberia | — | — | — | — | doing |
| [[apparatus/projects/command\|command from the apparatus]] | apparatus | fathership | — | The owner, or a person the owner names, writes a command in the apparatus and signs it with a web3 wallet. | — | doing |
| [[kadek/projects/first-release\|ship the first kadek release]] | cyb | — | — | kadek v0.1.0: the first tagged release, carrying the foundation the closure order names phases 1 and 2 — clocks, configuration, admission, provenance, presentat | — | accepted |
| [[cyberia/projects/oxytocin\|sell oxytocin]] | cyberia | — | — | the one-threshold space in Sayan, Ubud, sold — everything for the sale is there, it has to sell | — | doing |
| [[cyberculture\|fill the civics of cyberia]] | cyberia | — | — | the six slots of cyberculture filled at cyberia: cosmology, calendar, ritual, canon (the library of concepts), etiquette, aesthetics | — | proposed |
| [[bostrom\|launch bostrom]] | $BOOT | — | launch spacepussy | bostrom reborn as a public soft3 chain from its burial snapshot — after spacepussy launches and is debugged | after launch spacepussy | open |
| [[cyberia/projects/events\|host events]] | cyberia | — | — | — | — | paused |
| [[cyberia/projects/genome-protocol\|research genome protocol]] | cyberia | — | — | a page of knowledge | — | research |
| [[cyberia/projects/migration-market\|research migration market]] | cyberia | — | — | a page of knowledge | — | research |
| [[cyberia/projects/tech\|research tech tree]] | cyberia | — | — | a page of knowledge | — | research |
| [[cyberia/projects/noid-market\|research noid market]] | cyberia | — | — | a page of knowledge | — | research |
| [[cyberia/projects/smart capital\|research smart capital]] | cyberia | — | — | a page of knowledge | — | research |
| [[soft3/projects/cybernode\|carve cybernode out of soft3]] | cybernode | — | — | the node carved out of soft3, its own repository | 2026-10-27 | done |
| [[foculus/projects/view-certificates\|prove finality with view certificates]] | cybernode | — | — | finality as evidence, not declaration: the quorum certificate without the | — | draft |
| [[kadek/projects/soft3-alignment\|align kadek with soft3]] | cyb | — | — | final audit. | — | proposed |
| [[mudra/projects/private-recovery-index\|build private recovery index]] | neural | — | — | make opening or restoring a private wallet depend on the wallet result requested, | — | draft |
| [[soft3/projects/component-page-canon\|give each component one page]] | soft3 | — | — | every component of the stack answers at one canonical address on | — | draft |
| [[soft3/projects/cybergraph-sync-tade-architecture\|merge cybergraph sync and tade]] | soft3 | — | — | Superseded in part: the sync repo has since merged into foculus — the structural-sync substrate and the fork-choice that completes its merge are now one crate. | 2026-06-07 | done |
| [[soft3/projects/goldilocks-parano1d\|port the proof gated chain to zheng]] | soft3 | — | — | parano1d is a production proof-native chain: 393 kLOC, 20 crates, mainnet live since 2026-08-21, every block carrying a recursive validity proof, PoW ordering o | — | proposed |
| [[soft3/projects/metabolic-oracle\|move the metabolic oracle into the core]] | soft3 | — | — | cyberia's architecture carried a mechanism that answers one question for a whole network: *is it alive?* It was written for cyberia's 147 agents. | — | proposed |
| [[soft3/projects/network-planes\|cut the network into planes]] | soft3 | — | — | builds on cybergraph + sync + tade (2026-06, implemented), which merged the sync repo into foculus to kill two owners of one mechanism, and on component boundar | — | proposed |
| [[soft3/projects/network-repos\|make each network a repository]] | soft3 | — | — | the owner, 2026-10-17: every network has a configuration — a set of contracts (plumb), the genesis distribution, the starting parameters, the starting graph: a | — | proposed |
| [[soft3/projects/privacy-frozen\|freeze the privacy design]] | soft3 | — | — | hemera note (2026-10-16): the hemera#15 decision this page waits for is taken — hemera 0.4 (x⁷ in every round, 6 + 6 + 48 rounds, 32-byte digest kept) is the fr | — | proposed |
| [[soft3/projects/proof-system-repair\|repair zheng into one proof]] | joy | — | — | hemera note (2026-10-16): the hash row below is decided — hemera 0.4 (hemera#15: x⁷ in every round, 6 + 6 + 48 rounds, Poseidon2 reference matrices, 32-byte dig | — | proposed |
| [[soft3/projects/proven-present\|prove every block]] | soft3 | — | — | the property, fixed by the owner on 2026-10-17 as a base property of the system, cross-cutting and necessary: | — | proposed |
| [[soft3/projects/rooted-civilization\|add what rooted civilization needs]] | soft3 | — | — | soft3.org sells a machine: collective, private, provable computing, thirty features, seven verbs. | — | proposed |
| [[soft3/projects/steps-blocks-epochs\|define the consensus clock]] | soft3 | — | — | soft3 has proofs (zheng), a state organ (bbg), a graph (cybergraph), a compiler (trident), a mining spec (fold-mining) — and no working blockchain. | — | proposed |
| [[soft3/projects/tade-one-exchange\|make tade the one exchange format]] | soft3 | — | — | builds on cybergraph + sync + tade (implemented 2026-06), which made tade the wire substrate under radio and foculus. | — | proposed |
| [[soft3/projects/term\|build term for programmable rights]] | soft3 | — | — | three inheritances, one language. | — | proposed |
| [[cyberia/projects/cyber-sheep\|research cyber sheep]] | cyberia | — | — | a page of knowledge | — | research |
| [[soft3/projects/vault-secret-custody\|give vault its own home]] | cy | — | — | Vault is now an independent component in | — | superseded |
| [[zheng/projects/dynamic-noun-memory\|add dynamic noun memory]] | joy | — | — | This project extends the native Zheng execution relation toward computed | — | draft |
| [[zheng/projects/tagged-symbolic-relation\|try tagged symbolic relation]] | joy | — | — | This project defines execution::tagged, an opt-in circuit kernel. | — | draft |
| [[cyberia-my/projects/globe\|the globe]] | my cyberia | — | — | the owner, 2026-11-17: the home of cyberia.my becomes a globe, and the map is the primary way to use the site. | 2026-11-17 | done |
| [[cyberia-my/projects/imagery\|serve our own satellite imagery]] | my cyberia | — | — | the owner, 2026-11-18: "maybe we think about a resource for serving satellite imagery?" — this page is that thought, for a decision. | — | proposed |
| [[soft3/projects/assumptions-registry\|keep the assumptions registry]] | soft3 | — | — | The stack keeps one list of everything it assumes and cannot prove. | — | proposed |
| [[soft3/projects/protocol-proofs\|prove the protocols]] | soft3 | — | — | A proof system is three statements, and each has a different kind of proof: | — | draft |
| [[soft3/projects/receipt\|define the receipt]] | soft3 | — | — | A proof is evidence. | — | proposed |
| [[apparatus/projects/fleet\|merge agents into one fleet]] | apparatus | — | — | The owner, 2026-11-18: merge machines, services and agents into one entity. | — | proposed |
| [[apparatus/projects/triggers\|turn contractions into triggers]] | apparatus | — | — | The owner, 2026-11-18: contractions now merge into processes, but with thought. | 2026-11-18 | done |
| [[midao/projects/midao-registration\|midao registration]] | $CAP | button | — | the legal body of $CAP formed in the Marshall Islands: a certificate, an operating agreement on its on-chain governance, and an account the button pays into | — | doing |
| [[cyberia-my/projects/cartography\|base cartography]] | my | button | — | on cyberia.my a person draws points, lines, plots and buildings on their own layers over the one globe, verifies a boundary standing on it, and publishes by one signature | — | accepted |
| [[apparatus/projects/calendar\|the calendar]] | apparatus | — | — | the owner, 2026-11-21: "a separate screen of the organisation's calendar — where events land in the future, and where everyone sees his priorities for now. | — | accepted |
| [[cyberia-my/projects/listings\|the land market]] | my | — | — | the owner, 2026-11-20: an admin interface and a funnel for the owners who want to place their plots on the map for sale or lease. | — | proposed |
| [[tru/projects/truth-market-at-genesis\|the truth market at genesis]] | cybergraph | — | — | On pussy's chain at genesis every staked cyberlink carries the whole truth mechanism of rewards §5: a side, a stake and a prediction of the crowd; a market on t | — | proposed |
| [[apparatus/projects/engine\|the process engine]] | apparatus | — | — | the owner, 2026-11-21: "processes can be expressed as schemes, looped ones too. | — | proposed |
| [[soft3/projects/activation\|activation]] | soft3 | — | — | A staked cyberlink on pussy's chain says two things the truth serum can score — which side its author stands on, and what its author expects of the crowd — in a | — | proposed |

research packs — a project whose output is a page of knowledge — sit in the same table and the same folder since 2026-10-23 (they were `research/`). moved to [[products]] on 2026-11-16 because they are kept alive, not delivered: cyber valley, the land console (my cyberia), cve, cyberstates, the meme state, etherland, cyberia capital, rockets. the source of everything is [github.com/cyberia-to](https://github.com/cyberia-to).
