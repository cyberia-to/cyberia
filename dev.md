---
tags: cyber, cyberia, core
alias: dev, how cyberia works, the system, agent law, agent instructions, agent collaboration
crystal-type: pattern
crystal-domain: cyberia
---

# dev — how cyberia works

cyberia is an organism that builds things. this page says what it is made of, what it holds to, how work moves through it, and who moves it. everything here is structural; the processes it names are written out in [[processes]], and the project that brings this page into force is [[fathership]].

## first principles

1. the state is a mind. one shared mind, the [[cybergraph]], holds space, capital and knowledge; every act of the organism is a [[cyber/cyberlink|cyberlink]] cast by a [[neuron]] and settled by [[focus]].
2. everything is a file. a goal, a task, a product, a decision, a measurement, an event — each is one page with a particle, typed and dated, and nothing exists for the organism until it is a page. a list that someone maintains by hand is a copy; the pages are the truth, and every list, board or queue on this site is a query over them.
3. the organism has seven lenses, from [[org]]: purpose and principles, which constrain everything; people, products, processes, projects and portfolio, which are its five folders. an entity of cyberia — the state, the company, a city, a council — is shaped the same way at any scale.
4. work has five primitives, from [[soma]] § work. a goal is a desired state; a task is an instance of work toward it; a skill is a reusable way of working; an event is a point in time; a sensor perceives and fires. every other word of management reduces to these: a product is a goal kept alive, a process is a composite skill, a project is a task with sub-tasks, a decision is a review task, a gate is a sensor on a goal, a release is an event.
5. a product is delivered when a user passes its claims: a simulated user inside [[deliver]], a real one through [[listen]]. the product page is the script both follow, and its dots are what they report.
6. truth flows up, will flows down. focus is computed and proven, so no one argues about what matters; links are chosen, so everyone decides what to do. the father sets the purpose and the products and renders the few verdicts; the organism does the rest and measures itself by one number, its metabolism M — cap, syntropy and happiness together.

## the objects

one page per object, in the repository that owns it, typed by its frontmatter. `kind` and `status` follow [[soma]]; `serves` names the goal a page exists for, so every page has a lineage up to the purpose.

| object | primitive | page | lives in | closes when |
|---|---|---|---|---|
| purpose, principles | charter | `README.md` of the entity | the entity's repository | never |
| product | goal, product, maintain | the product page, every claim marked 🟢 measured · 🟡 target · 🔴 mock | the product's repository, as its door | never; it is kept alive |
| goal of a quarter | goal, outcome, strategic | one page per goal | `goals/` | its sensor fires |
| project | task with sub-tasks | one page, sub-tasks as pages or rows | `projects/` | every sub-task done |
| task | task, kind question · plan · work · proposal · review | one page: kind, status, owner, serves, evidence | `tasks/` of the owning repository | `done`, `closed` or `abandoned` |
| decision | task, kind review, owner the father | one page: what is asked, both sides, the verdict | `tasks/` of the owning repository | the father's verdict |
| specification | contract | `specs/`: clauses with ids, each with its cases | the owning repository | superseded |
| requirement map | measure | one table: requirement → code → test → receipt at a commit | `audit/` of the product | never; the counter reads it |
| measurement, audit, receipt | measure | `audit/` | the owning repository | never; it is evidence |
| release | event, release | the candidate's receipts | `audit/release-<date>/` | the father promotes or the week ends |
| process | skill, composite | one page per process | `processes/` | superseded |

task status: `open → doing → done`, or `closed`, or `abandoned`. a task is ready when nothing it waits for is open. claims on pages carry evidence words: `open → simulated → measured → proven`, and `stale` when the receipt is older than the last commit that touched the claim's code; on a product page the same states are the dots: 🔴 open or stale · 🟡 simulated · 🟢 measured or proven.

## the three laws of evidence

learned from the life-os development machine ([[development machine study]]), whose forty-two runs measured them:

1. **admission by execution.** a claim is green only when the gate re-ran its proof at a named commit. an author's report, a reviewer's approval and a green suite admit nothing; the counter admits, from `audit/`.
2. **capability over prose.** a rule that forbids an actor something is enforced by a mechanism — a branch protection, a missing token, a hook, a removed tool — or it is not a rule. nine prompt-only rules in that machine failed; every mechanical one held. each "never" on this page and in the train names its mechanism or leaves.
3. **a finite agenda on one snapshot.** a task names its outputs and checks before work starts, every reader of its result reads the same commit, every finding carries one id and its remaining obligations, and a panel closes by a recorded disposition in at most two rounds. the two runs of that machine that converged were the two bounded ones; the open-ended ones never did. the size of the task is the budget, not the number of calls.

## requirements

a specification is clauses with ids; a product page is claims that name them; the map in `audit/` says what closes each; the counter reads both and sets the dots. the form is the graph's own — pages, headings, tables — never a second index.

- **a clause** is a heading with an id that survives rewording and moves: `CHAIN-ASERT-2 · the target follows ASERT with half-life 600 s`, with `parent:` and `invariant:` lines where they apply, and under it its **cases**, one row each: id, kind `positive` or `negative`, given, when, then. a clause without a case is a `placeholder`, and a claim that names it is 🔴 by construction.
- **the map** is one table per product in `audit/<product>/map.md`: requirement · code · test · proof · state. code is a path or a symbol; test a selector; proof a receipt page at a commit. a requirement with no row is `open`.
- **the states** are the evidence words above; `stale` is computed from git, never written by hand. three things stay separate: what is intended (the clause), what exists (the code and test), what was shown (the receipt).
- **the owner of a link** is the clause for its cases and invariants and the map for code, test and proof; backlinks are the graph's, nothing is written twice.

the pilot is [[soft3/specs/chain|chain]] with its conformance entries and the receipts in `soft3/audit/chain/`.

## the charter

the charter is one scheme: what cyberia holds to, in the order it is held. every box is a page.

<svg viewBox="0 0 900 432" width="100%" xmlns="http://www.w3.org/2000/svg" font-size="12" style="font-family:inherit" fill="none" stroke="currentColor" stroke-width="1">
<style>a text{fill:#4ade80}a:hover text{fill:#fff}text{fill:currentColor;stroke:none}</style>
<rect x="20" y="12" width="860" height="78" rx="8" stroke-width="2"/>
<text x="34" y="32" font-weight="600">identity · the owner's hand, once in years</text>
<a href="/cyberia/foundation/strategy"><rect x="34" y="42" width="204" height="36" rx="5"/><text x="136" y="58" text-anchor="middle">purpose · vision · mission</text><text x="136" y="72" text-anchor="middle" opacity="0.7" font-size="10.5">type 1 · make planets think · cyberstate</text></a>
<a href="/cyber/license"><rect x="246" y="42" width="204" height="36" rx="5"/><text x="348" y="58" text-anchor="middle">license</text><text x="348" y="72" text-anchor="middle" opacity="0.7" font-size="10.5">don't trust · don't fear · don't beg</text></a>
<a href="/cyberia/foundation/manifesto"><rect x="458" y="42" width="204" height="36" rx="5"/><text x="560" y="58" text-anchor="middle">manifesto</text><text x="560" y="72" text-anchor="middle" opacity="0.7" font-size="10.5">seven principles · the oath to life</text></a>
<a href="/cyberia/foundation/strategy"><rect x="670" y="42" width="204" height="36" rx="5"/><text x="772" y="58" text-anchor="middle">the troika</text><text x="772" y="72" text-anchor="middle" opacity="0.7" font-size="10.5">cyber · cyb · cyberia</text></a>
<rect x="20" y="104" width="860" height="118" rx="8"/>
<text x="34" y="124" font-weight="600">products · the ladder, one page per rung, accepted by the owner</text>
<g font-size="11">
<a href="https://soft3.org/layers"><rect x="34" y="134" width="70" height="34" rx="4"/><text x="69" y="148" text-anchor="middle">1 nox</text><text x="69" y="161" text-anchor="middle" opacity="0.7" font-size="10">machine</text></a>
<a href="https://trident.pink"><rect x="109" y="134" width="78" height="34" rx="4"/><text x="148" y="148" text-anchor="middle">2 trident</text><text x="148" y="161" text-anchor="middle" opacity="0.7" font-size="10">weapon</text></a>
<a href="https://github.com/cyberia-to/joy"><rect x="192" y="134" width="66" height="34" rx="4"/><text x="225" y="148" text-anchor="middle">3 joy</text><text x="225" y="161" text-anchor="middle" opacity="0.7" font-size="10">warrior</text></a>
<a href="https://github.com/cyberia-to/cybergraph"><rect x="263" y="134" width="92" height="34" rx="4"/><text x="309" y="148" text-anchor="middle">4 cybergraph</text><text x="309" y="161" text-anchor="middle" opacity="0.7" font-size="10">brain</text></a>
<a href="https://github.com/cyberia-to/neural"><rect x="360" y="134" width="76" height="34" rx="4"/><text x="398" y="148" text-anchor="middle">5 neural</text><text x="398" y="161" text-anchor="middle" opacity="0.7" font-size="10">language</text></a>
<a href="https://github.com/cyberia-to/cy"><rect x="441" y="134" width="62" height="34" rx="4"/><text x="472" y="148" text-anchor="middle">6 cy</text><text x="472" y="161" text-anchor="middle" opacity="0.7" font-size="10">agent</text></a>
<a href="https://soft3.org"><rect x="508" y="134" width="76" height="34" rx="4"/><text x="546" y="148" text-anchor="middle">7 soft3</text><text x="546" y="161" text-anchor="middle" opacity="0.7" font-size="10">network</text></a>
<a href="https://cyb.ai"><rect x="589" y="134" width="66" height="34" rx="4"/><text x="622" y="148" text-anchor="middle">8 cyb</text><text x="622" y="161" text-anchor="middle" opacity="0.7" font-size="10">robot</text></a>
<a href="https://cyber.page"><rect x="660" y="134" width="116" height="34" rx="4"/><text x="718" y="148" text-anchor="middle">9 cyber</text><text x="718" y="161" text-anchor="middle" opacity="0.7" font-size="10">superintelligence</text></a>
<a href="https://cyberia.to"><rect x="781" y="134" width="80" height="34" rx="4"/><text x="821" y="148" text-anchor="middle">10 cyberia</text><text x="821" y="161" text-anchor="middle" opacity="0.7" font-size="10">state</text></a>
</g>
<text x="34" y="190" opacity="0.8">kernel 1–3 · core 4–7 · apps 8–10 · no rung depends on a rung above it · specifications of 1–7 pass the owner's hand</text>
<text x="34" y="208" opacity="0.8">a product page is a goal kept alive; its claims are dots: 🟢 measured · 🟡 target · 🔴 mock; the product is delivered when every dot is green</text>
<rect x="20" y="236" width="420" height="104" rx="8"/>
<a href="/cyberia/foundation/architecture"><text x="34" y="256" font-weight="600">people · 147 roles</text></a>
<text x="34" y="274" opacity="0.8">7 roles × 21 domains · 7 councils by facet</text>
<text x="34" y="290" opacity="0.8">keeper · runner · sensor · counter · seer · bridge-in · bridge-out</text>
<text x="34" y="306" opacity="0.8">form · mass · space · life · word · work · play</text>
<text x="34" y="322" opacity="0.8">bodies today: claude · codex · kimi · grok · master · joy</text>
<rect x="460" y="236" width="420" height="104" rx="8"/>
<a href="/cyberia/processes"><text x="474" y="256" font-weight="600">processes · seven</text></a>
<text x="474" y="274" opacity="0.8">deliver · research · listen · market · operate · govern · steward</text>
<text x="474" y="290" opacity="0.8">a loop in every node, a graph between; gates open on the cost of error</text>
<text x="474" y="306" opacity="0.8">the owner at the irreversible lane and every verdict; the roles do the rest</text>
<text x="474" y="322" opacity="0.8">one score: M = cap · syntropy · happiness</text>
<rect x="20" y="354" width="860" height="64" rx="8" stroke-dasharray="4 3"/>
<text x="34" y="374" font-weight="600">the record · the cybergraph</text>
<text x="34" y="394" opacity="0.8">every page a particle, every relation a signed cyberlink, every claim with evidence; boards, queues and registries are queries over it</text>
<a href="/cyberia/projects/fathership"><text x="34" y="410" opacity="0.8">today the record runs on scaffolding — repositories and GitHub; the project that moves it onto the graph is fathership</text></a>
</svg>

## the processes

the organism works in seven recurring ways, each a skill of the composite kind written as a graph of nodes in [[processes]]. every node holds a loop — produce, check, correct, repeat until green — with the check written first as something a program can evaluate; between nodes travel only pages and cyberlinks; a return goes to the unit that failed, never to the batch; an accepted result goes back as a constraint into the brief that cut the work; and a gate opens on the cost of being wrong, never on confidence.

| process | turns | into |
|---|---|---|
| [[deliver]] | an accepted product page | a released product whose claims a simulated user has passed |
| [[research]] | a question | a page of knowledge with evidence |
| [[listen]] | what real users do and say | tasks and changes to product pages |
| [[market]] | a released product | people who come, understand and join |
| [[operate]] | machines and domains | a running, observed, recoverable estate |
| [[govern]] | a proposal about the charter | a verdict, and every page it touches re-accepted |
| [[steward]] | sigma | budgets that open or close lanes |

## the roles

three layers, which earlier pages mixed.

| layer | what it is | examples |
|---|---|---|
| participants | the neurons for whom and by whose hand everything happens | the user · the owner · the citizens |
| organizational roles | standing responsibility for a domain, seven in each of twenty-one domains, from [[cyberia/foundation/architecture]] | keeper · runner · sensor · counter · seer · bridge-in · bridge-out |
| workflow roles | a skill a body performs inside one node of a graph, in its own context | splitter · architect · critic · implementer · tester · integrator · a review lens · the user played · merger |

an organizational role is a portfolio of workflow skills: the keeper holds architect and the long return edge, the sensor holds critic, tester and the played user, the runner holds implementer and integrator, the counter holds gates and lanes, the seer holds the splitter and the next proposal, the bridges carry work across rungs and councils. a body — claude, codex, kimi, grok, a person — carries roles; it is never a role. the map is [[people]].

## the owner

the owner holds three things and nothing else: the charter, the product pages, and the verdicts. a verdict is a review task addressed to the owner: a change to the charter, the acceptance of a product page, a specification of the kernel or the core, the promotion of a candidate, the weights of M, or a question that convergence did not settle. the queue of verdicts is a query — review tasks whose owner is the father and whose status is open — and it is kept under five by the organism, which settles what it can before asking.

## the views

a view is a query over pages; none is written by hand. `cyberia/scripts/views.py` renders them hourly into [[cyberia/views|views]] — the bridge with its alerts and five numbers, then products, flow, father and experiments; the launchd job is `to.cyberia.views`.

| view | query |
|---|---|
| the verdict queue | tasks with kind review, owner the father, status open |
| a product board | the product page's claims by dot, the open tasks that serve it |
| a role board | tasks by role and status, ready first |
| the state board | the ladder with each product's dots, red gates, the verdict queue, M |
| the log of decisions | review tasks of the father with status done, by date |

## conduct

how any body behaves while it works. the doctrine behind each line is in [[cyberia/quality]], [[cyberia/engineering]], [[cyberia/documentation]] and [[cyberia/refinement]].

- honesty: never fake a result, never fill a gap with a placeholder; a dash is more honest than a copied number. the project is supervised by an engineer with thirty years of experience; one time correctly is cheaper than five times beautifully.
- literal interpretation: the user means what they say; show the raw thing asked for before any cleanup; when unsure, ask once.
- think before coding: state assumptions, name the readings when a brief admits several, push back when a simpler way exists.
- simplicity: the minimum that solves the task; no abstraction for single use, no option nobody asked for.
- surgical change: touch only what the task requires; remove the orphans your change made, mention the rest.
- verify before reporting: run the same check the user would run; a URL is verified by opening it; never make the user the tester.
- drive, don't micromanage: once a task is approved, finish it; ask once only when intent is ambiguous, the act is destructive, or two choices differ in consequence.
- clean up: a workspace is left cleaner than found; `git status` is clean at the end, with only what was agreed.
- memory is cache, repositories are truth: a settled insight lands in a page the same session; status is claimed from the page or the live system, never from memory.

## house rules

- git: commit after every logical unit, one change per commit, conventional prefixes (`feat:` `fix:` `refactor:` `docs:` `test:` `chore:`), the message says why; stage by explicit paths; never amend, rebase, reset, stash or force-push shared branches; no AI co-authorship trailers; a body pushes only its own branch; other people's working trees under `~/cyber/<repo>` are never edited — work in a worktree. zero warnings and green tests before a commit, else `wip:` with the first error quoted.
- placement: contracts in `specs/`, evidence in `audit/` with the command and revision for every number, explanations in `docs/`; the layout of the workspace and its repositories is [[workspace]].
- moving a page out of a wiki: settled and implemented → the owner's spec; a projection with an open question → the owner's `roadmap/`; a cross-component argument → `soft3/docs/`; only duplicates and refuted claims are deleted; the ledger in `cyber/restructure.md` names where each part went, and the source index loses the row rather than gaining a note.
- filenames portable to NTFS: none of `< > : " / \ | ? *`, no trailing dot or space, no reserved basenames; hyphens over punctuation. policy `soft3/specs/filenames.md`.
- writing: state what a thing is; never define by negation; no bold on graph pages; wiki-links for concepts.
- platform: nushell for scripts, bash only where nushell cannot run; macOS: BSD `sed` has no `\b`, zsh does not word-split unquoted `$var`, `~/.cargo/bin` and `/opt/homebrew/bin` are on PATH, siblings resolve by relative path from `~/cyber`.
- the editor over `~/cyber`: Zed opened on the home sees every nested checkout under `.worktrees` as a repository (284 on 2026-10-21, 172 of them nested), spawns `git` for each on every rescan, overflows the FSEvents queue and dies on an abort in wasmtime's Mach exception thread about ten minutes after launch (16 crashes in five days). `~/.config/zed/settings.json` therefore excludes `**/.worktrees`, `**/target` and the generated trees (`cyberia-blog/build`, `tru/eval`, `cyberstates/dist`) from the scan; a task checkout is opened on its own when it needs the editor. the second source, found the same day: anything written under `~/cyber` in bursts — the agents' git objects (12,000 files in two hours) and the graph serve regenerating the blog site (56,000 files, hundreds of times a day) — overflows the FSEvents queue, Zed rescans the home, recomputes the git state of every repository at once (five `git` calls each, hundreds of spawns in seconds) and dies in its spawn path on `Bad file descriptor`. so the served site lives in `~/.cache/cyber/blog/serve` (`graph-serve.sh --output`), never in the repository; deploys still build into `cyberia-blog/build`. the rule behind both: nothing that regenerates by the thousand lives under the watched home.
- no Node.js: node, npm, npx, yarn, pnpm, bun, `package.json`, lockfiles, `node_modules`, playwright or puppeteer driven by node, any `.js`/`.mjs` tool run by node are banned from every repository under `~/cyber` and from agent workflows (owner, 2026-10-16, after node crept back once). browser JavaScript a page ships is fine. builds: Rust, trunk, static files, optica; scripts: nushell or Python; browser checks: Chrome `--headless=new` or `cyber/scripts/cdp.py`; deploys: rsync or a Python API client; a dependency, MCP server or CI step that drags node in is rejected.
- the home `~/cyber` is permanent: one directory per canonical repository plus the doctrine files; caches in `~/.cache/cyber`, throwaway output in `/tmp`; nothing else at its top level.
- every body reads this page: Claude through CLAUDE.md, Codex, Kimi Code and Grok Build through AGENTS.md; both say the same thing and this page is their source.

## vocabulary

cyber has its own ontology. in any cyber project — specs, code, commit messages — the root term, never a borrowed alias. every root page carries an `alias:` list; `grep -r "alias:.*<term>" ~/cyber/cyber/` finds the root for any substitute.

| borrowed term | root term |
|---|---|
| CID, hash as content id, node, vertex | particle |
| edge, link | cyberlink |
| user, actor, account | neuron |
| post, document, card | file |
| knowledge graph | cybergraph |
| smart contract | .tri program, .nox program |
| wallet | neuron, sigma |
| IPFS, content addressing | radio |
| ticket, issue, story, bead | task |
| OKR | goal with a sensor |
| sprint, epic | project |
| trigger, verdict, telemetry | sensor |

when the architecture borrows from another stack — Bevy, ECS, wgpu, REST — its vocabulary pulls cyber terms into its idiom; resist, and keep cyber names next to borrowed ones.
