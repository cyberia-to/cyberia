---
tags: cyber, cyberia, fathership, roadmap, plan
alias: fathership, the father, governing by vision, dev roadmap, process roadmap, the loop roadmap
crystal-type: plan
crystal-domain: cyber
status: active
---

# cyberia/fathership

[[cyber/launch]] says what ships. this page says how it ships: the way the owner governs the work of agents, and the road from today's hand-driven process to development that runs on [[cybergraph]] itself. [[cyberia/dev]] is the law every agent works by; this page is the plan that changes that law phase by phase.

version: 2026.10 · status: phase 0 in delivery · this page is the single tracker of the process; every gate, decision and status change of the way of working lands here.

## the stance

the owner is a father, not an architect. a father sets the vision, names the goals, reads the plans he wants to read, breaks the ties agents cannot break, and promotes releases. everything else — research, planning, implementation, review, merging within policy, cutting candidates, keeping the house clean — is the agents' work, done in the open, with evidence, in files the owner can read when he chooses.

the measure of the stance is three numbers, reported on the state board every week:

- the share of merges that needed no owner action;
- the time from a task becoming `ready` to its change merged;
- the number of decisions brought to the owner, and how many of them were real ties.

## the phases

| phase | what | gate | when |
|---|---|---|---|
| 0 | the loop on scaffolding: a work graph in the repositories, three artifacts per task, rings of control, a merge policy, council and pool across four vendors, boards rendered from the graph, the backlog cleared | every property below with phase 0 is proven; the launch worker runs again under the loop and produces merged work for a week without an incident | 2026-10 |
| 1 | the dev dialect on cybergraph: a task is a file, its state is signed cyberlinks, `ready` is an inf query, boards are optica renders, agents read and write through cy; the scaffold and the graph run side by side, the scaffold written, the graph read | one week in which every board the owner reads is rendered from the graph and agrees with the scaffold | 2026-11 → 2026-12 |
| 2 | the graph is the only truth: the scaffold is retired, GitHub is the wire (pull requests) and a mirror (projects for people who live there) | thirty days of the loop with no scaffold; `ready`, claims and boards answered by inf faster and more reliably than the scaffold did | 2027-01 |

phase 1 is the dog-food that proves the product: the development of cyber runs on cyber. its ladder is already named: file, particle, cyberlink, neuron, inf, cy, optica. the scaffold exists so that the process works in weeks while the dialect is built in months, and its data model (hash ids, typed dependencies, atomic claims, compaction of closed work) is the shape the dialect will have, so the export is a session, not a project.

## the loop

one task of the work graph, one fresh agent session, three artifacts, one pull request, one merge.

```
vision (owner)            launch.md registry rows · quarterly goals · this page
   │
   ▼
work graph                tasks · blocks / discovered-from · ready · claim
   │
   ▼
research.md ──► plan.md ──► pull request ──► review (other vendor) ──► merge (policy)
   │                                                                      │
   └──── council for the important, pool for the small ───────────────────┘
                                                                          │
ring 0 (repo) ──► ring 1 (rung) ──► ring 2 (state, friday) ──► candidate ──► owner promotes
```

the full law of the loop is [[cyberia/dev]] § the loop, § work graph, § vendors, § rings, § merge policy. this page tracks whether the law is in force.

## property registry

the registry is the owner's. states are the evidence axis of [[cyberia/dev]] § status: `open` · `simulated` · `measured` · `proven`, with `blocked` when something outside the row holds it. evidence names a file, a command or a run; a dash means none yet.

| # | property | owner | phase | state | evidence | close by |
|---|---|---|---|---|---|---|
| 1 | a work graph exists in the repositories: tasks with hash ids, `blocks` and `discovered-from` edges, `ready` = no open blockers, atomic claims; the scaffold is beads | .github | 0 | open | — | 2026-10-14 |
| 2 | every task carries three artifacts before merge: `research.md` (what is, verified against code), `plan.md` (`[step] → verify: [check]`), the pull request whose body is generated from the plan | .github | 0 | open | — | 2026-10-14 |
| 3 | ring 0 is executable in every ladder repository: the repository's gates, cargo-semver-checks against the last tag, a reviewer agent in a fresh context from another vendor | .github | 0 | open | — | 2026-10-21 |
| 4 | ring 1 is executable: a merge into the default branch of any part of a rung builds and tests the product and its direct dependents, computed from `components.toml` (`part_of` and the reverse closure of cargo dependencies) | soft3 | 0 | open | — | 2026-10-28 |
| 5 | ring 2 is the release train, unchanged in its rules, extended to the whole ladder: every friday from origin, receipts, owner promotes | soft3 | 0 | measured | `soft3/release/train.py`, `train_gates.py`, candidates since 2026-09-25 | 2026-10-31 |
| 6 | the semver floor is a law: the declared bump is at least the computed bump; a lower declaration is a red gate | soft3 | 0 | open | — | 2026-10-21 |
| 7 | the merge policy holds the token for ring 0: green gates, a reviewer from another vendor approving, blast radius equal to the repository, no specification change → merged without the owner; anything else is labeled `decision` | .github | 0 | open | — | 2026-10-21 |
| 8 | council mode runs to convergence for research, plans, architecture and audits: four vendors independent in round 1, a rotating chair, sequential rounds, stop on an unchanged round or after three, ties to the owner as one question | .github | 0 | open | — | 2026-10-28 |
| 9 | pool mode spends every vendor's quota on small tasks with cheap models, dispatched by remaining quota; a task that fails ring 0 twice escalates to council | .github | 0 | open | — | 2026-10-28 |
| 10 | the reviewer is always a different vendor than the implementer | .github | 0 | open | — | 2026-10-21 |
| 11 | kelvin temperatures are declared for nox, trident and joy in `components.toml`; a rung is never colder than the rung below; a decrement below obliges a release above; every repository declares the temperature of the rung directly beneath it; drift is a red ring 1 | soft3 | 0 | open | — | 2026-10-31 |
| 12 | one status vocabulary across `roadmap/`, `launch.md`, `status.md` and the work graph: the stage axis and the evidence axis of [[cyberia/dev]] § status | cyberia | 0 | open | — | 2026-10-21 |
| 13 | context has the shape of the task: a soul of about two thousand tokens, a pack per rung built from `components.toml` and drift-checked in CI, a research artifact per task; the global pack stays as an option | ctx | 0 | open | `ctx/build.nu` has provenance and atomic replace; the pinned list is by hand and dated 2026-09-13 | 2026-10-28 |
| 14 | boards are rendered from the graph: state (the ladder), product (a rung), component (a repository, filtered by owner); GitHub projects are a mirror at most | .github | 0 | open | — | 2026-10-31 |
| 15 | a mayor runs daily: triage of the graph, closing of stale pull requests with a reason, the merge queue, a one-page digest to the owner | .github | 0 | open | — | 2026-10-31 |
| 16 | the merge queue is a refinery: batches merged only green, bisected when red; never a rebase, never a force push | .github | 0 | open | — | 2026-11-07 |
| 17 | the pull request backlog is cleared by the rules of the 2026-10-07 sweep: merge what is whole and re-verified, close the rest with a reason, keep every branch, carry every `DECIDE` thesis into a task | .github | 0 | measured | `.github/audit/pr-sweep-2026-10-07.md` | 2026-10-08 |
| 18 | the launch worker runs again under the loop: tasks instead of registry rows, claims in the graph, the pool as its runner | cyber | 0 | blocked | paused since 2026-09-24 by the owner; waits for 1, 7, 9 | 2026-11-07 |
| 19 | runners: GitHub-hosted for Linux and public repositories; the owner's Mac as a self-hosted runner for Metal, dmg, apk and fleet until a dedicated machine exists; the Actions spending limit stays at zero | cybernode | 0 | open | — | 2026-10-21 |
| 20 | GitHub issues are an inbox: an outside report becomes a task and the issue closes with the task's link; no issue is ever the truth of work | .github | 0 | open | — | 2026-10-31 |
| 21 | the dev dialect is specified: task as file, `blocks` / `discovered-from` / `claim` / `done` as typed cyberlinks signed by the agent's neuron, `ready` as an inf query, the board as an optica selection | neural | 1 | open | — | 2026-11-15 |
| 22 | the scaffold exports to cyberlinks: every task and edge in the scaffold appears in the graph within a minute of its change | cybergraph | 1 | open | — | 2026-11-30 |
| 23 | agents write to the graph through cy headless with their own neuron; a claim is a signed link | cy | 1 | open | — | 2026-12-15 |
| 24 | the boards the owner reads are rendered from the graph for a week and agree with the scaffold | .github | 1 | open | — | 2026-12-31 |
| 25 | the scaffold is retired; inf answers `ready`, claims and boards faster and more reliably than the scaffold did, measured over thirty days | cybergraph | 2 | open | — | 2027-01-31 |

## council and pool

| mode | for | who | stop |
|---|---|---|---|
| council | research, plans, architecture optimization, audits, specifications | all four vendors: round 1 independent and parallel on the best models; round 2 a rotating chair merges and opens the disagreement list; rounds 3 and on sequential, each vendor verifies the disputed claims against code and specs | an unchanged full round, or three rounds; what remains goes to the owner as one question with both sides' evidence |
| pool | ring 0 tasks: one function with tests, one measurement, one page | any vendor on a cheap model, chosen by remaining quota, random on a tie; the reviewer another vendor, a cheap model unless the diff touches a specification | green ring 0; two red runs escalate the task to council |

the quota ledger is a resource: councils first, the remainder feeds pools, an unspent window is lost work. vendors with cloud execution from the repository (Claude, Codex) run there; every vendor can also run from the runner box, a Linux machine with the vendor's CLI under cron that pulls `ready` tasks labeled for it. the owner's machine runs no agent.

## decisions

| date | decision |
|---|---|
| 2026-10-07 | GitHub issues are an inbox for outsiders, never the truth of work; pull requests are the wire of a change, never its record; boards are renders of the graph, GitHub projects a mirror at most |
| 2026-10-07 | the scaffold is beads, chosen for a data model that is the shape of the dialect; the export to cyberlinks is a property of phase 1, the retirement a property of phase 2 |
| 2026-10-07 | vendors are assigned by the class of work, never by loyalty: council for the important until convergence, pool for the small until the quota is spent; the reviewer is always another vendor |
| 2026-10-07 | the semver floor is a law: declared bump ≥ computed bump, a lower declaration is a red gate |
| 2026-10-07 | kelvin starts at the kernel rungs (nox, trident, joy); decrements are planned by quarter |
| 2026-10-07 | the owner's Mac stays the self-hosted runner for Metal, dmg, apk and fleet until a dedicated physical machine exists; every other gate runs on GitHub-hosted runners; the spending limit stays at zero |
| 2026-10-07 | the pull request backlog is cleared by agents under the sweep rules; when in doubt, close and redo in the loop |

## work log

| when | # | where | what | state |
|---|---|---|---|---|
| 2026-10-07 | 17 | .github | read-only triage of every open pull request into buckets A–H | running |
| 2026-10-07 | — | cyberia | this page and the rework of [[cyberia/dev]] | open for the owner's reading |
