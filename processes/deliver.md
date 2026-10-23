---
tags: cyber, cyberia, process
alias: deliver, the delivery process, delivery
crystal-type: process
crystal-domain: cyberia
---

# deliver

how an accepted product page becomes a released product. the page is the goal; its claims are the units; a claim is delivered when a simulated user has passed it and the counter has turned its dot green. the [[dev|three laws of evidence]] hold at every node: admission by execution, capability over prose, a finite agenda on one snapshot.

trigger: a product page accepted by the owner, or a change to one that [[listen]] or [[govern]] produced.

## the graph

| node | role | makes | green when |
|---|---|---|---|
| 1 intake · splitter | seer | claims cut into units by blast radius, each a task with its lane | the unit names its claim, requirement ids, lane, outputs and checks |
| 2 design · worker + critic | keeper writes, sensor grades | a design per unit, at most five rounds | the design traces to the claim, names its files and tests |
| 3 build · workers | runner implements, sensor tests, each with its own critic | a change and its tests per unit | tests exit 0; the diff stays inside the design's files |
| 4 integrate · code node | — | every test tier over the merged units, then the fleet | all tiers and the fleet green |
| 5 review · workers | one body per lens, all reading one commit | a verdict per lens; findings with one id each | every lens green or every finding disposed, in at most two rounds |
| 6 merge · gate | counter | the change on the default branch | the lane's condition |
| 7 use · worker | sensor plays the user | the claims walked end to end, a receipt per claim | every claim passed; the counter sets the dot |
| 8 release · gate | runner cuts, the owner promotes | a candidate on the weekly train | the owner's verdict |

notes on the nodes:

- intake: the task page's first commit is the task; a change of scope is a dated line on it, never an edit of the first sentence.
- integrate: the fleet is the products that use a changed part, built and tested against it; a synthetic green is not evidence that a consumer still works.
- review: the lenses are the twelve passes of [[cyberia/quality]], alignment with the charter and a second model; a finding keeps one canonical id and its remaining obligations; a third round is a diagnosis of the cut, not another call.
- merge: contained → green checks; wide → green checks and a clean trajectory; irreversible → the owner.
- use: the receipt names the commit; a receipt older than the last commit touching the claim's code is stale, and the dot comes from the receipt, never from the report.

node 7 is the user of the delivery: a body that takes the product page as a script and does what a person would — opens the door, follows the path, reads the numbers — and records what it saw. its harness is code where it can be code (the deck players and phone ledgers under `/tmp/jsd` are the shape); its judgment is one line per claim with the evidence. real users belong to [[listen]].

## return edges

- short: a red gate returns the unit to the node that produced it with unit, verdict, reason, evidence and scope; the scope names the files the fix may touch. a unit returned three times goes back to intake as a wrong cut.
- long: an accepted unit leaves a constraint in the brief of intake and, when it changed a contract, in the specification; the keeper writes it. a failure that was not turned into a constraint will be met again.
- product: a claim that node 7 could not pass returns to the page as 🔴 with the evidence, and the seer proposes the change to the page.
- resume: a body whose attempt failed or timed out keeps its saved work and continues in the same context; starting from zero is the last option, taken once and recorded.

## what the critic and the tester look for

the failure modes that recurred in every run of the life-os machine ([[development machine study]]); each is a check, not a reminder:

| failure | the check |
|---|---|
| completion overstated: partial or rejected work reported as done | the report names the commit and the command; the critic re-runs the command |
| guessed shapes: a response or file format assumed, shipped as done | the design shows the observed shape of every entry point it uses, captured from a real call |
| tests from invalid premises: an impossible positive, a control after a return, a substitute reader | the tester shows the valid control first; a test that cannot fail on the real path is not a test |
| broad suites rerun instead of the affected check | the task names its selectors; a run outside them is a finding |
| a prerequisite's exit code unread, the dependent step started anyway | every step reads the previous step's outcome, not its transport |
| the real path touched last, after synthetic green | the fleet and node 7 run before the lenses, not after |
| a failed attempt re-authored from zero | the resume edge above |

## lanes

the lane of a unit is computed from the files it touches and the ladder's dependency graph, never declared by its author. contained: one repository, one part, covered by tests. wide: a contract, a shared crate, anything a rung above depends on; the specifications of rungs 1–7 are wide and pass the owner's hand. irreversible: production data, money, deletion, the production chain; this lane does not open without the owner, and that is a lane, not a threshold. the landings and decks — the doors of the products — stay wide for now: green checks and a clean trajectory open them, so the state moves fast; the day comes to freeze and stabilise them, and on that day they move to the irreversible lane by a decision, not by drift.

## the train

node 8 is the release train: a candidate every friday 12:00 utc from the default branches, `candidate-YYYYMMDD.N`, binaries per platform, `SHA256SUMS`, `sources.json`, `candidate.json`, `release-validation.json`, receipts in `audit/release-<date>/`, a freeze from the cut to the verdict. a red gate is published red with its evidence, never fixed by hand on the artifact. the owner alone promotes, publishes, tags. the versions of the ladder follow the lanes: contained is a patch, wide a minor, a change the whole state depends on a major; the declared bump is at least the computed one.

## pages

a task page per unit in `tasks/` of the owning repository; the design and the review verdicts on it; evidence in `audit/`; the dots on the product page. in phase 1 of [[fathership]] the same pages are read from the [[cybergraph]].
