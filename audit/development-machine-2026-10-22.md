---
tags: cyber, cyberia, audit, process, fathership
alias: development machine study, life-os development machine, development.zip study
crystal-type: measure
crystal-domain: cyberia
---

# the development machine of life-os · 2026-10-22

the owner handed over `development.zip`: the development workspace of a personal-finance product ("life-os"), 2026-09-14 → 2026-10-20, built with Claude Opus, Codex/Astra and Kimi as native adapters under a human-plus-Claude "root" orchestrator. read to decide what [[fathership]] takes, what it leaves, and how [[dev]] stays small. measured from the archive itself and from the two reviewers' own registries inside it.

## what it is

| | |
|---|---|
| runs | 42 in five weeks (28 in september, 14 in october); each a frozen task, a call allowance, native calls with receipts, reviews, typed evidence, a closure gate, an immutable publication |
| the machine | `runtime/` — 22,845 lines of Python: ten call operations + nine admin operations; adapters, artifact writer, controller, gate, publisher, checkpoints, measure, role memory |
| its own specification | `specs/current/dev-machine`: release 1 = 31 requirements (2026-09-21) → release 22 = **326 requirements** (2026-10-20); 22 immutable version copies, 95 MB |
| one run | `2026-10-20-role-memory-curation`, a 12-call task: 15 subdirectories, 36 call files, 41 evidence files (32k lines), proof 36k lines, private 250k lines, three task-freeze revisions |
| the archive | 5,982 files, 421 MB — of which the product is absent: this is development records only |
| the reviewers | `analysis/claude` (180 MB) and `analysis/kimi`: observations CO/KO, conclusions CC, proposals CP with trace, significance scale, generated schemas, review runs of the review |

## what it measured about itself

| finding | evidence in the archive |
|---|---|
| process records outweighed product change in every analysed run | CO-012, CC-008; the baseline run: 98 calls, 30 wall hours, +33,242 lines, **0 of 13 requirements delivered** |
| the only runs judged *good* were the two smallest and bounded | repository-manageability: 5 calls, four fixed outcomes; compatibility-repair: 4 calls, six file-level items, 1.8 hours (CC-013) |
| open-ended machine building did not converge; bounded repair did | CC-004, CC-013; the machine's requirement count ×10 in a month |
| prompt rules did not change behaviour; removing a tool did | H-010, H-015, H-020 `did_not_work`; CC-002: "only removing the tool did"; H-025 worked because dispatch was checked against a role matrix |
| what admitted results: root re-running the proof, never author claims, reviewer votes or green suites | CC-001, KO-012 — the one control present in all eight runs |
| late contact with the real path was the main source of rework | CC-005, KO-005: defects surfaced after synthetic suites were green |
| panels converged when all reviewers read one immutable snapshot and findings had canonical ids with remaining obligations; closed by disposition, not by vote | KO-014: across seven runs no reopening |
| owner attention went to polling, re-explaining, authorising cap increases | CC-007, KO-018; ten idle overnight hours in the baseline |
| call caps made spending visible but did not bound cost | CC-006: five runs grew their frozen ceiling mid-run |
| role memory as a store: the first comparison showed no effect | H-026 `did_not_work`; the lesson text itself says a prose reminder did not prevent recurrence |
| hypotheses: 11 worked, 9 did not | the eleven that worked show the model the exact shape, input or envelope, or check dispatch mechanically; the nine that failed are all "explicitly require/forbid X in the prompt" |

## what cyberia takes

1. **admission by execution.** a claim is green only when the gate re-ran its proof at a named commit; author text, reviewer approval and a green suite admit nothing. the dots already come from `audit/` by the counter; the audit page names the commit it measured.
2. **capability over prose.** every "agents never X" in the doctrine gets a mechanism — branch protection, no publish token on agent hosts, a hook — or leaves the doctrine. their nine failed hypotheses are the same rule nine times.
3. **a finite agenda on one snapshot.** a task names its outputs and checks before work starts; every review lens reads the same commit; findings carry one canonical id and a list of remaining obligations; a panel closes by recorded disposition in at most two rounds; a third round is a diagnosis of the approach, not another identical call.
4. **the real consumer before the review.** a change to a part is built against the products that use it before any lens reads it (the fleet gate); a synthetic green is not evidence.
5. **resume, never re-author.** a failed or timed-out attempt keeps its saved work and continues in the same session; re-running from zero is the last option.
6. **frozen task, visible amendments.** the task page's first commit is the task; a change of scope is a dated line in the page, never an edit of the original sentence.
7. **a light experiment register.** when fathership changes the process, the decision line carries *expected effect · check · outcome*; outcome is `worked` or `did not`, written after the next run that exercised it.
8. **their list of agent failure modes** goes into the critic's and tester's passes: completion overstated; guessed shapes shipped as done; tests from invalid premises; broad suites rerun instead of the affected check; a prerequisite's exit code unread; the real path touched last.

## what cyberia leaves

| their mechanism | why not |
|---|---|
| hash-bound ledgers: every reference `{path, sha256}`, immutable version copies per release, receipts and journals | git is the hash-bound ledger; a commit sha is the receipt. re-implementing git in JSON cost them 95 MB of spec copies and most of the record growth |
| a specification of the machine itself, a runtime of 23k lines | the machine grew ten times faster than the product; by their own verdict machine runs did not converge. our process is `dev.md` plus seven process pages, and no code beyond the scripts that exist |
| the per-run artifact zoo: freezes, routes, dispatch policies, boundaries, normalisations, snapshots, selections | three artifacts suffice: the task page, the pull request, the audit receipt |
| role memory as a curated, hash-indexed, admitted store with curation runs | memory is a cache; lessons live where they bite — a gate, a hook, a checklist line; the first measurement showed no effect |
| a review-of-the-reviews layer with its own registries and schemas | the content is gold, the form weighs more than the runs; one audit page per retrospective |
| manual orchestration as law: no engine, no subagents, no scheduler | it made the owner the bottleneck. they banned automation because automatic transitions admitted unproven work; the cure is a gate that runs the proof, which is what the counter and the train are |
| call caps as the unit of budget | the bound that held was the size of the task, not the number of calls: ≤ 400 lines, one pull request, one snapshot |

## how this simplifies ours

- `dev.md` gains the three laws (admission by execution · capability over prose · finite agenda on one snapshot) and nothing else; the objects table stays at three artifacts per task.
- `processes/deliver.md`: the review node reads one commit, closes by disposition, ≤ 2 rounds; the integrate node runs the fleet before the lenses; the test role gets the failure-mode checklist.
- `projects/fathership.md`: the decisions log gains *expected effect · check · outcome*; fathership stays a project with a closing condition, never a product with its own specification. a cap: process work is bounded like any task — one pull request, one snapshot, no runtime of its own.
- every "never" in `CLAUDE.md` and the train is audited once for its mechanism; the ones without one are either enforced or struck.

the reverse lesson, in one line: they built a correct machine and starved the product; the machine's own reviewers said so in week two, and the machine kept growing for four more weeks because every improvement was itself a run. fathership closes when the loop is in force, and then it is over.
