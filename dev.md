---
tags: cyber, article
alias: agent collaboration, agent instructions, dev
crystal-type: pattern
crystal-domain: cyber
---

# dev

principles for working with AI coding agents across any project. this page is the bootstrap entry point — read it and the five foundational documents to have complete development context:

- [[cyberia/engineering]] — pipeline contracts, dual-stream optimization, verification dimensions
- [[cyberia/quality]] — 12 review passes, severity tiers, audit protocol
- [[cyberia/projects]] — repo layout, namespace conventions, git workflow
- [[cyberia/documentation]] — Diataxis framework, reference vs docs, spec before code
- [[cyberia/refinement]] — document polishing: kill the zoo, hunt violations, seven-round audit

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
ephemeral agent storage. plans go to `<repo-root>/.claude/plans/`.

rules:

1. read what is already there before writing
2. before presenting a plan for approval, write it to a file first.
   the user reviews the file in their editor, not the chat
3. every plan the user signs off on gets committed to the repo.
   rejected plans get deleted
4. compress old entries when files grow stale — density over volume

## compaction survival

when context compacts, preserve: modified file paths, failing test
names, current task intent, and uncommitted work state.

## parallel agents

split parallel agents by non-overlapping file scopes. never let two
agents edit the same file. partition by directory. use subagents for
codebase exploration. keep main context clean for implementation.

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

## git

commit after every logical unit of work. do not wait for the user to
ask. one change per commit — never bundle two independent changes.

conventional prefixes: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`,
`chore:`. message describes why, not what.

before committing: zero lint warnings, all tests pass. if anything
fails, fix before committing.

## release train

the release train is the one way a binary reaches a person. it runs for [[cyb]], [[cyber]] and [[soft3]] first; every other component joins by the same rules when its owner says so. the train is the control behind phase 1 of [[cyber/launch]].

- truth is origin. a candidate is built only from committed, pushed inputs on the default branch of every repository it closes over. a working tree is never an input. `sources.json` records every sibling's HEAD; a dirty or unpushed input marks the candidate local, and a local candidate can never become a release.
- one candidate every friday, 12:00 UTC, cut by an agent from origin: `candidate-YYYYMMDD.N`, a draft pre-release on GitHub carrying binaries per platform, `SHA256SUMS`, `sources.json`, `candidate.json` (the three versions and every sibling HEAD) and `release-validation.json` (every gate with its result). platforms: macOS arm64 and x64, Linux arm64 and x64; cyb adds the Android apk. no Windows, no iOS.
- gates are executable and named in each repository's CLAUDE.md. a red gate is a red candidate; a red candidate is published as red with its evidence, never hidden and never fixed by hand on the artifact. cyb: `cargo check --tests --locked`, `cargo test`, `make fleet` green, the dmg and the apk build. cyber: `cargo build --release --locked`, `cargo test --locked`, `nu scripts/release.nu --locked-sources`, the graph builds with optica. soft3: `cargo test` in `crate/`, the node boots and answers `/status`, the conformance snapshot passes.
- versions are semver. one bump is one pull request named `chore: <component> <version>` that touches `Cargo.toml`, `CHANGELOG.md` and the sibling pins in the other two repositories, and nothing else. tags are `v<version>` on the default branch. the phase-1 manifest `soft3/release/phase1.toml` pins the sibling revisions the train closes over; a sibling that drifted from its pin is a red gate, and the fix is a bump pull request, never a path edit in a working tree.
- freeze: from the cut until the verdict nothing merges into the three default branches. fixes for the candidate go to `release/<date>` as `fix:` commits and are merged back after the verdict.
- roles: agents cut candidates, run gates, write receipts and open bump pull requests. only the owner merges a bump, promotes a candidate to a release, publishes to crates.io or pushes a tag. an agent never does any of those four, and `make ship` in cyb is the owner's hand, not an agent's.
- receipts live in `<repo>/audit/release-<date>/`: the commands run, their output, the hashes. release notes are a numbered list of what changed, each item linking its pull request, and every number in them comes from a receipt.
- the launch page work log gets one row per candidate: date, versions, verdict, link.
- every agent reads these rules: Claude through CLAUDE.md, Codex, Kimi Code and Grok Build through AGENTS.md in the same directory; the two files say the same thing and this page is their source. global copies live in `~/.agents/AGENTS.md`, `~/.codex/AGENTS.md`, `~/.kimi-code/AGENTS.md`.

## moving a page out of cyber

when a research page leaves the cyber wiki, nothing in it is thrown away by default. sort its content by what the code has done with it:

- settled and implemented → the owner's spec, or a section in an existing explainer; the page's own claims are replaced by measured numbers where measurement exists.
- a projection with a named assumption and an open question → the owner's `roadmap/`, one file per question, with the status the launch registry uses (proven · simulated · measured · open · blocked).
- a cross-component argument that no single owner holds → `soft3/docs/` as an explainer, with each projection marked measured, refuted as stated, or open.
- only duplicates of what already lives in a repo, and claims refuted and rewritten elsewhere, are deleted.

the ledger row in `cyber/restructure.md` names where each part went; a deleted page's row is removed, never marked. old wiki-links keep resolving through `alias:` on the destination.

## writing style

state what something is directly. never use "this is not X, it is Y"
formulations. never define by negation.

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
| node, vertex (in graph context) | particle                       |
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
