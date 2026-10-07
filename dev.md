---
tags: cyber, article
alias: agent collaboration, agent instructions, dev, the loop, agent law
crystal-type: pattern
crystal-domain: cyber
---

# dev

the law every coding agent works by, across every project of the organization. this page is the bootstrap entry point: read it, the five foundational documents, and [[cyberia/fathership]] to have complete development context.

- [[cyberia/fathership]] — the roadmap of this law: phases, the property registry, decisions
- [[cyberia/engineering]] — pipeline contracts, dual-stream optimization, verification dimensions
- [[cyberia/quality]] — 12 review passes, severity tiers, audit protocol
- [[cyberia/projects]] — repo layout, namespace conventions, git workflow
- [[cyberia/documentation]] — Diataxis framework, reference vs docs, spec before code
- [[cyberia/refinement]] — document polishing: kill the zoo, hunt violations, seven-round audit

the page has three parts. the loop says how work moves: graph, artifacts, vendors, rings, merge, release. conduct says how an agent behaves inside the loop. house rules say how things are written, named, committed and placed.

# the loop

one task of the work graph, one fresh session, three artifacts, one pull request, one merge. the owner sets the vision and promotes releases; agents do everything between.

## the work graph

work is a graph, never a list. a task is one unit of work with a hash id, an owner, a stage and the evidence it rests on. edges are typed: `blocks`, `discovered-from`, `supersedes`, `parent`. a task is `ready` when it has no open blocker. an agent takes a task by an atomic claim and holds it until the pull request is merged or the task is handed back with a note.

phase 0 of [[cyberia/fathership]] keeps the graph in beads (`bd`) inside each repository; phase 1 mirrors it into [[cybergraph]] as files and signed cyberlinks; phase 2 retires the scaffold. an agent uses whichever is the writable truth of the current phase and never both.

the pull request is the wire of a change in phases 0 and 1. in phase 2 the wire is the [[patch]] of `fs/patch/spec.md`: one channel per task, a signed set of operations over particles and cyberlinks authored by the agent's neuron, conflicts as first-class data, merge as channel union; review and the merge policy are evaluated over signed cyberlinks to the patch, and GitHub only mirrors the result. every rule of this page that names a pull request names the patch from then on.

the registry rows of [[cyber/launch]] and the goals of [[cyberia/goals]] are the owner's; they spawn tasks. an agent never invents a row, a goal or a task that no row or goal asks for. a task discovered while working on another gets a `discovered-from` edge and waits its turn.

every task carries its lineage: `serves: <goal> · <product> · <clause>` names the goal of the quarter, the product whose definition the change falls under, and the clause of the canon or the specification it serves. a task without lineage is never `ready`. the canon — license, manifesto, purpose and mission, troika and ladder, product definitions, this law — is indexed in [[cyberia/fathership]] § the canon, and a change is accepted against it before anything else.

GitHub issues are an inbox for people outside the loop. an issue becomes a task and closes with the task's link. no issue is the truth of any work. GitHub projects, when they exist, are a mirror of the graph for people who live there.

## three artifacts

every task carries three artifacts, in order, each a file in the repository the task belongs to, under `.claude/tasks/<id>/` until phase 1 moves them into the graph:

1. `research.md` — what is: the code paths, the specifications, the measurements, each claim checked against the checkout, with the commands used. a research artifact says what it could not determine.
2. `plan.md` — what will be: steps, each written as `[step] → verify: [check]`, the five most likely ways the change fails, the files it touches, the ring it reaches. a plan is reviewed by the owner only when he chooses; it is reviewed by another vendor always.
3. the pull request — one repository, one logical change, a body generated from the plan: what, verified (the exact commands and their final lines), remains, risk and rollback.

the owner reads plans, never diffs, unless he wants to. two hundred lines of a wrong plan cost less than two thousand lines of wrong code.

## council and pool

work has two classes and each class has one way of being done.

council is for research, plans, architecture optimization, audits and specifications. all four vendors take the same brief. round 1 is independent and parallel on the best models: each vendor writes its artifact without seeing the others, so their errors stay uncorrelated. round 2 is a chair, rotating among the vendors, who merges the four into one artifact and opens the disagreement list: each contested claim, who holds which side, on what evidence. rounds 3 and on are sequential: each vendor in turn receives the merged artifact and the list, verifies every contested claim against code and specifications, changes what it must and updates the list. a full round that changes no claim and no disagreement means convergence; so does the third round. what remains after that goes to the owner as one question with both sides' evidence. an audit runs the same cycle with an adversarial round 1: each vendor looks for where it breaks.

pool is for small tasks: one function with its tests, one measurement written to `audit/`, one page. any vendor takes it on a cheap model; the dispatcher chooses by remaining quota and at random on a tie. a task that fails ring 0 twice leaves the pool and enters council as a short research: why this does not get done.

the reviewer is always a different vendor than the implementer. a cheap model reviews a pool change; the best model reviews anything that touches a specification or reaches ring 1. the reviewer's first pass is the canon pass: does the change contradict the license, the manifesto, the mission, the product's definition, the ladder law or the vocabulary; a contradiction is labeled `decision` and never merged by policy, whatever the gates say.

quota is a resource and the loop spends all of it: councils first, pools with the remainder, and a window left unspent is work lost. agents run in the vendor's cloud from the repository where that exists, and otherwise on the runner box, a Linux machine with every vendor's CLI under cron that pulls `ready` tasks. the owner's machine runs no agent; it runs gates.

## rings

the controls a change passes are decided by its blast radius, never by the author's choice of number. the radius is computed from the touched files through `soft3/release/components.toml` (`part_of`) and the reverse closure of cargo dependencies.

| ring | when | what runs | who accepts |
|---|---|---|---|
| 0 · repository | every pull request | the repository's gates named in its CLAUDE.md; `cargo semver-checks` against the last tag; a reviewer from another vendor in a fresh context | the merge policy |
| 1 · rung | a merge into the default branch of any part of a rung | build and test of the rung's product and its direct dependents on the ladder; the rung's specification checks; the kelvin drift check | the merge policy; a red ring 1 blocks every bump in the rung |
| 2 · state | every friday 12:00 UTC and any cut the owner asks for | the whole ladder from origin, integration, user runs (fleet, conformance), audits, receipts | the owner alone |

semver maps onto the rings: a patch stays inside ring 0, a minor reaches ring 1, a major reaches ring 2. the declared bump is at least the computed one: `cargo semver-checks` and the component graph set a floor, the author may go higher, and a declaration below the floor is a red gate.

## kelvin

semver is the tactical cadence; kelvin is the strategic one. a rung carries a temperature in `components.toml`, an integer that only decreases; zero is frozen and the frozen foundations [[soft3]] promises are rungs at zero. three rules, taken whole from the Urbit practice:

1. a rung is never colder than the rung below it;
2. a decrement below obliges a release of every rung above, which is the vertical delivery written as a law;
3. every repository declares the temperature of the rung directly beneath it, the one it was built against; drift from that declaration is a red ring 1.

decrements are planned by quarter in a file with the shape of a KEP: summary, motivation, what changes, graduation criteria, the owner as approver. between decrements only semver moves. the kernel rungs — nox, trident, joy — carry temperatures first.

## merge policy

the merge token belongs to policy, never to a person and never to an agent's judgment. a ring 0 pull request merges without the owner when all of these hold: every gate green, a reviewer from another vendor approved in a fresh context, the blast radius is the repository itself, no specification changed. anything else carries the label `decision` and waits for the owner. a merge is a merge commit; nothing is ever rebased, squashed by hand or force-pushed.

the refinery is the merge queue: it merges batches that are green and bisects a batch that turns red. the mayor runs once a day: triages the graph, closes pull requests gone stale with a reason and a kept branch, runs the queue, and writes a one-page digest to the owner.

## release train

the release train is the one way a binary reaches a person. it runs for [[cyb]], [[cyber]] and [[soft3]] first; every other component joins by the same rules when its owner says so. the train is ring 2 and the control behind phase 1 of [[cyber/launch]].

- truth is origin. a candidate is built only from committed, pushed inputs on the default branch of every repository it closes over. a working tree is never an input. `sources.json` records every sibling's HEAD; a dirty or unpushed input marks the candidate local, and a local candidate can never become a release.
- one candidate every friday, 12:00 UTC, cut by an agent from origin: `candidate-YYYYMMDD.N`, a draft pre-release on GitHub carrying binaries per platform, `SHA256SUMS`, `sources.json`, `candidate.json` (the versions and every sibling HEAD) and `release-validation.json` (every gate with its result). platforms: macOS arm64 and x64, Linux arm64 and x64; cyb adds the Android apk. windows joins when its gate exists; no iOS.
- gates are executable and named in each repository's CLAUDE.md. a red gate is a red candidate; a red candidate is published as red with its evidence, never hidden and never fixed by hand on the artifact. cyb: `cargo check --tests --locked`, `cargo test`, `make fleet` green, the dmg and the apk build. cyber: `cargo build --release --locked`, `cargo test --locked`, `nu scripts/release.nu --locked-sources`, the graph builds with optica. soft3: `cargo test` in `crate/`, the node boots and answers `/status`, the conformance snapshot passes.
- versions are semver under the floor of § rings. one bump is one pull request named `chore: <component> <version>` that touches `Cargo.toml`, `CHANGELOG.md` and the sibling pins in the other repositories, and nothing else. tags are `v<version>` on the default branch. `soft3/release/phase1.toml` pins the sibling revisions the train closes over; a sibling that drifted from its pin is a red gate, and the fix is a bump pull request, never a path edit in a working tree.
- freeze: from the cut until the verdict nothing merges into the default branches the train closes over. fixes for the candidate go to `release/<date>` as `fix:` commits and are merged back after the verdict.
- roles: agents cut candidates, run gates, write receipts and open bump pull requests. only the owner merges a bump, promotes a candidate to a release, publishes to crates.io or pushes a tag. an agent never does any of those four, and `make ship` in cyb is the owner's hand, not an agent's.
- receipts live in `<repo>/audit/release-<date>/`: the commands run, their output, the hashes. release notes are a numbered list of what changed, each item linking its pull request, and every number in them comes from a receipt.
- the launch page work log gets one row per candidate: date, versions, verdict, link.
- runners: GitHub-hosted runners for Linux and for every public repository; the owner's Mac as a self-hosted runner for Metal, dmg, apk and fleet until a dedicated machine exists; the Actions spending limit stays at zero and a gate that would spend money is a decision.
- every agent reads these rules: Claude through CLAUDE.md, Codex, Kimi Code and Grok Build through AGENTS.md in the same directory; the two files say the same thing and this page is their source. global copies live in `~/.agents/AGENTS.md`, `~/.codex/AGENTS.md`, `~/.kimi-code/AGENTS.md`.

## context

context is the scarce resource and it has the shape of the task. three layers:

- the soul, about two thousand tokens: who the agent is, the root vocabulary, this law. always present.
- the pack of a rung, about sixteen thousand tokens: the rung's specifications and the contract of the rung directly below, built from `components.toml` by `ctx/build.nu`, rebuilt by CI on every merge into a part of the rung, with provenance and a drift check. an agent working in spark gets the neural pack, never the whole world.
- the research artifact of the task: the context of the task itself.

the global pack of the whole graph stays as an option for work on the protocol. a session keeps its context below sixty percent; above that it writes a compaction artifact (goal, approach, done, next, failing test names, uncommitted state) and starts fresh. one task, one session.

## status

two axes, one vocabulary, used in `roadmap/`, `launch.md`, `status.md` and the work graph alike:

- the stage of work: `draft` → `accepted` → `active` → `done` → `superseded`;
- the evidence of a claim: `open` → `simulated` → `measured` → `proven`;
- `blocked` on either axis, naming what blocks.

component states in `components.toml` (`live`, `published`, `local`, `unwired`, `spec`, `dormant`, `research`) describe readiness of a component, a third thing, and stay as they are.

# conduct

## auditor mindset

the project is supervised by an engineer with 30 years of experience.
deception does not work. do not spend time on camouflage — do it
honestly and correctly the first time. every attempt to hide a problem
behind formatting, substitute numerator for denominator, or show
"progress" where there is none will be caught and require rework.
one time correctly is cheaper than five times beautifully.

## honesty

never fake results. never fill empty columns with duplicate data to
make things look complete. if a system produces nothing — show nothing.
a dash is more honest than a copied number.

the purpose of every metric, column, and indicator is to reflect
reality. never substitute appearance of progress for actual progress.
never generate placeholder data to fill a gap. if you catch yourself
making something "look right" instead of "be right" — stop and
delete it.

## literal interpretation

when the user says something, they mean it literally. do not
reinterpret. do not find the closest thing you think they might mean.
do not iterate on your interpretation 13 times.

known failure mode: the user says "show real numbers" and the agent
reformats display labels, adds tags, restructures output — everything
except showing the actual data the user asked for. this is the
masquerading instinct — optimizing for "looks correct" instead of
"is correct."

rules:

1. if the user asks to show data, show the raw value from the source
   before any fallback, gating, or cleanup
2. if you are unsure what the user means, ask once. do not guess and
   iterate
3. if your first instinct is to format/present/clean — stop. ask
   "what is the raw data the user has not seen yet?" show that first
4. never hide failure behind technically-accurate-but-misleading numbers
5. the user knows what they are saying. trust their words over your
   interpretation of their intent

## think before coding

state assumptions explicitly; when a brief admits several readings, name them and ask once instead of picking one silently. when a simpler approach exists, say so and push back. when something is confusing, stop, name what is confusing, and ask. a council disagreement list is this rule at the scale of four vendors.

## simplicity

the minimum code that solves the task, nothing speculative: no feature beyond the ask, no abstraction for single-use code, no configurability nobody requested, no handling of impossible errors. the test is a senior engineer's eye: two hundred lines that could be fifty are rewritten.

## surgical changes

touch only what the task requires. adjacent code, comments and formatting stay as they are; what is not broken is not refactored; unrelated dead code is mentioned, never deleted. every changed line traces to the task. orphans that the change itself created are removed by the agent that created them.

## chain of verification

for non-trivial decisions affecting correctness:

1. initial answer
2. 3-5 verification questions that would expose errors
3. answer each independently — check codebase, re-read docs
4. revised answer incorporating corrections

skip for trivial tasks.

## estimation model

estimate work in sessions and pomodoros, not months.

- pomodoro = 30 minutes of focused work
- session = 3 focused hours (6 pomodoros)

model-assisted development compresses traditional timelines — a
"2-month project" might be 6-8 sessions. plan in reality, not
in inherited assumptions.

## agent memory

all plans and design documents persist in the project repo, not in
ephemeral agent storage. a task's artifacts live with the task; a plan outside any task goes to `<repo-root>/.claude/plans/`.

rules:

1. read what is already there before writing
2. before presenting a plan for approval, write it to a file first.
   the user reviews the file in their editor, not the chat
3. every plan the user signs off on gets committed to the repo.
   rejected plans get deleted
4. compress old entries when files grow stale — density over volume
5. memory is cache, repositories are truth: a settled insight lands in a repo file the same session, and status is claimed from the repo or the live system, never from memory

## compaction survival

when context compacts, preserve: modified file paths, failing test
names, current task intent, and uncommitted work state.

## parallel agents

split parallel agents by non-overlapping file scopes. never let two
agents edit the same file. partition by directory. use subagents for
codebase exploration. keep main context clean for implementation. the work graph's claims are the partition at the scale of the organization.

## drive, don't micromanage

once a task is approved, drive it to completion. do not interrupt the
user with permission requests for obvious next steps inside the same
task: "want me to do X next?" when X is the only sensible move is
noise, not collaboration. the user already decided when they said do
the task.

if the next step has unknown trade-offs, call it out in one line and
keep going with the obvious choice; the user will redirect if needed.

ask once, in one of these cases:

- ambiguous user intent (what they want is unclear)
- the action is destructive and not yet authorized
- two choices have genuinely different consequences and either could
  be wrong

never ask for: which model to test next inside the manifest scope, what
to commit, what tool to install, which probe to run, whether to keep
trying. those are the work itself.

## clean up after yourself

deletion is the agent's job. if a file becomes orphaned — leftover
from reverted work, abandoned experiment, dead module — the agent
that created it must remove it. never leave the workspace dirtier
than you found it. never punt cleanup to the user with "left for
you to delete". the user is not a janitor for the agent's discarded
work.

if a tool denies a destructive operation (rm, git rm), find another
correct way: `mv` to /tmp, `git restore` for tracked files, ask once
if truly stuck. never settle for "orphan stays" as the resolution.

verify the cleanup: `git status` should show a clean working tree at
the end of the work, with only the changes the user agreed to.

## self-verification before reporting

the agent must verify that something works before telling the user it
works. never hand the user a URL and say "it should be there" — open
it, check the response, confirm the content. never report a task as
done without running the output through the same check the user would
perform.

the failure mode to avoid: agent makes a change, assumes it worked,
tells the user to check. user finds it broken. agent investigates.
this loop wastes the user's time and erodes trust. one verification
pass by the agent eliminates the loop entirely.

rules:

1. after any deploy-affecting change, verify the observable result:
   HTTP status, page content, build output, test pass — whichever
   applies. if verification is not possible (e.g. CI in flight),
   say so explicitly with a time estimate, not "should work"
2. if localhost differs from production, check both — and report
   which was checked and what was found
3. "it's in the build" is not verification. check the rendered result
4. if something breaks during verification, fix it before reporting
5. never make the user the tester. the agent's job ends at a
   confirmed working result, not at a completed action
6. a pull request's verified section is the same check, written down: the exact commands and their final lines, run against the current base

# house rules

## git

commit after every logical unit of work. do not wait for the user to
ask. one change per commit — never bundle two independent changes.

conventional prefixes: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`,
`chore:`. message describes why, not what.

before committing: zero lint warnings, all tests pass. if anything
fails, fix before committing; a red state may be committed only with the `wip:` prefix and the first error quoted.

stage by explicit paths, never `git add -A`. never amend, rebase, reset, stash, checkout files or force-push on shared branches; never rewrite history. no AI co-authorship trailers. other people's working trees under `~/cyber/<repo>` may be dirty with their own work: never edit, stage or discard it; work in a worktree. an agent pushes only its own branch; the default branch moves by merge through the policy.

## moving a page out of cyber

when a research page leaves the cyber wiki, nothing in it is thrown away by default. sort its content by what the code has done with it:

- settled and implemented → the owner's spec, or a section in an existing explainer; the page's own claims are replaced by measured numbers where measurement exists.
- a projection with a named assumption and an open question → the owner's `roadmap/`, one file per question, with the status words of § status.
- a cross-component argument that no single owner holds → `soft3/docs/` as an explainer, with each projection marked measured, refuted as stated, or open.
- only duplicates of what already lives in a repo, and claims refuted and rewritten elsewhere, are deleted.

the ledger row in `cyber/restructure.md` names where each part went; a deleted page's row is removed, never marked. old wiki-links keep resolving through `alias:` on the destination.

## reports and specifications

audits, benchmarks and release validation go to `<repo>/audit/`; contracts, invariants and acceptance criteria to `specs/`; observed results never in a spec. every number in a report names the command and the revision it came from.

## writing style

state what something is directly. never use "this is not X, it is Y"
formulations. never define by negation. no bold in graph pages; headings, frontmatter and wiki-links carry emphasis.

## graph vocabulary — root terms only

cyber has its own ontology. when writing in any cyber project (specs,
code comments, design docs, commit messages), use the root term from
the cybergraph — never an alias borrowed from a different stack.

aliases dilute the established term. readers must mentally re-translate,
search misses instances, and the canonical vocabulary erodes one
substitution at a time.

common substitutions to make:

| alias / borrowed term           | root term in cyber             |
| ------------------------------- | ------------------------------ |
| CID                             | particle                       |
| hash (when meaning content id)  | particle                       |
| task, vertex (in graph context) | particle                       |
| edge, link                      | cyberlink                      |
| user, actor, account            | neuron                         |
| post, tweet, document, card     | file                           |
| knowledge graph                 | cybergraph                     |
| smart contract                  | .tri program (or .nox program) |
| wallet                          | neuron, sigma                  |
| IPFS, content addressing layer  | radio (or BAO for streaming)   |

the rule: before writing a term that names something in the cyber
stack, check if there is a root file for that concept. if yes,
use the root name. if the concept genuinely names something foreign
(e.g. "IPFS CID" specifically refers to IPFS's convention, not
cyber's), use the foreign term explicitly and qualify it.

how to check: every root concept's file has an `alias:` field in
its YAML frontmatter listing common substitutes. `grep -r "alias:.*<term>"
~/cyber/cyber/root/` finds the root file for any alias. when in
doubt, search the graph before writing.

the failure mode to avoid: when writing about architecture that
borrows from a non-cyber stack (Bevy, ECS, wgpu, REST, OAuth), the
borrowed-stack vocabulary tends to pull cyber terms into its idiom.
resist this. cyber concepts keep their cyber names even when sitting
next to borrowed ones.


## platform

macOS dev machine: BSD `sed` has no `\b` (use `[[:<:]]w[[:>:]]`); zsh does not word-split unquoted `$var`; `~/.cargo/bin` and `/opt/homebrew/bin` are on PATH; sibling repositories resolve by relative path from `~/cyber`. nushell for scripts; bash only where nushell cannot run.

when localhost dies on the dev machine (connections to 127.0.0.1 stay `SYN_SENT`, `ping 127.0.0.1` loses every packet, a fresh listener on another port fails the same way), the cause is NordVPN's kill switch: pf loads `block drop all` without `set skip on lo0`. check with `sudo pfctl -s Interfaces -v` (lo0 without `(skip)`); fix by reloading the current rules with `set skip on lo0` prepended (`pfctl -s rules` → file → `pfctl -f`), as done 2026-10-07; the durable fix is NordVPN's own setting for local network access.
