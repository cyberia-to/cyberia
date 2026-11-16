---
tags: cyber, cyberia, projects
alias: projects of cyberia, the projects, cyberia projects, project list
crystal-type: entity
crystal-domain: cyberia
---

# projects

the projects lens of [[org]]: work that closes. a project is a task with sub-tasks ([[dev]] § the objects); it has an owner, a status and a page, and when every sub-task is done it is over — unlike a product, which is kept alive, and unlike the chronicle, which is infrastructure. a project's domain is an attribute of the project, as a product's is of the product; the registry of every domain the state holds is cybernode's, at [domains.cybernode.ai](https://domains.cybernode.ai).

this folder is the registry: one file per project, its passport — what it is, its domain, its repository, its stage, what it serves. a project that needs more than a passport keeps the rest in its own repository, never in a folder here.

a project is finite: it has a delivery, a date and a declaration — the page its link opens (the owner, 2026-11-16). what is kept alive and measured by revenue and capacity is a product and lives on [[products]]; a site is a product's door, never a project's. the order of this table is the priority: the first row is worked first. the owner moves a row up or down here, by hand or from the cockpit's projects tab, and every move is a commit — the history of priorities is the history of this file. there are no proposals any more, only projects (the owner, 2026-11-16): every repository keeps its projects in `projects/`, one page each, with `status:` in the front matter — `proposed` (a draft: a decision still open, not yet a project of the state), `accepted` (a project: it enters this table), `executed` or `done` (delivered, the date beside it), `rejected` or `superseded` (history). the page is the project's declaration. soft3's `proposals/` became `projects/` that day; cybernode was the first.

## how the table fills — from the bottom

the apparatus collects projects from the bottom: `apparatus/scripts/projects_collect.py` (run by the cockpit's collector every 15 minutes) reads `projects/*.md` on the default branch of every repository under cyberia-to, and every page whose status is `accepted`, `executed` or `done` must have a row here. a page without a row is appended at the bottom — the lowest priority until the owner drags it up — with the page as its declaration, its first sentence as the delivery and its `date:` as the date; a row whose page says executed or done is marked done with that date. the collector never reorders and never deletes: priority and removal are the owner's hand. each run that changes the table is one commit on cyberia main, "projects: <name> accepted in <repo> — enters the list".

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

research packs — a project whose output is a page of knowledge — sit in the same table and the same folder since 2026-10-23 (they were `research/`). moved to [[products]] on 2026-11-16 because they are kept alive, not delivered: cyber valley, the land console (my cyberia), cve, cyberstates, the meme state, etherland, cyberia capital, rockets. the source of everything is [github.com/cyberia-to](https://github.com/cyberia-to).
