---
tags: cyber, cyberia, process
alias: deliver, the delivery process, delivery
crystal-type: process
crystal-domain: cyberia
---

# deliver

how an accepted product page becomes a released product. the page is the goal; its claims are the units; a claim is delivered when a simulated user has passed it and the counter has turned its dot green.

trigger: a product page accepted by the owner, or a change to one that [[listen]] or [[govern]] produced.

## the graph

| # | node | kind | role | makes | green when |
|---|---|---|---|---|---|
| 1 | intake | splitter | seer | the page's claims cut into units by blast radius, each a task with its lane | every unit names its claim, its lane, its checks |
| 2 | design | worker + critic | keeper writes, sensor grades | a design per unit, at most five rounds | the critic's checks pass: the design traces to the claim, names its files, names its tests |
| 3 | build | workers | runner implements, sensor tests, each with its own critic, each in its own context | a change and its tests per unit | tests exit 0; the diff touches only the files of the design |
| 4 | integrate | code node | — | every test tier over the merged units: unit, integration, end to end | all tiers exit 0 |
| 5 | review | workers | one body per lens: the twelve passes of [[cyberia/quality]], alignment with the charter, a second model | a verdict per lens | every lens green; a red lens returns the unit |
| 6 | merge | gate | counter | the change on the default branch | the lane's condition: contained → green checks; wide → green checks and a clean trajectory; irreversible → the owner |
| 7 | use | worker | sensor plays the user | the page's claims walked as a user would, end to end, with evidence per claim | every claim passed; the counter sets the dot |
| 8 | release | gate | runner cuts, the owner promotes | a candidate on the weekly train with receipts | the owner's verdict |

node 7 is the user of the delivery: a body that takes the product page as a script and does what a person would — opens the door, follows the path, reads the numbers — and records what it saw. its harness is code where it can be code (the deck players and phone ledgers under `/tmp/jsd` are the shape); its judgment is one line per claim with the evidence. real users belong to [[listen]].

## return edges

- short: a red gate returns the unit to the node that produced it with unit, verdict, reason, evidence and scope; the scope names the files the fix may touch. a unit returned three times goes back to intake as a wrong cut.
- long: an accepted unit leaves a constraint in the brief of intake and, when it changed a contract, in the specification; the keeper writes it. a failure that was not turned into a constraint will be met again.
- product: a claim that node 7 could not pass returns to the page as 🔴 with the evidence, and the seer proposes the change to the page.

## lanes

the lane of a unit is computed from the files it touches and the ladder's dependency graph, never declared by its author. contained: one repository, one part, covered by tests. wide: a contract, a shared crate, anything a rung above depends on; the specifications of rungs 1–7 are wide and pass the owner's hand. irreversible: production data, money, deletion, a public deploy that people already use; this lane does not open without the owner, and that is a lane, not a threshold.

## the train

node 8 is the release train: a candidate every friday 12:00 utc from the default branches, `candidate-YYYYMMDD.N`, binaries per platform, `SHA256SUMS`, `sources.json`, `candidate.json`, `release-validation.json`, receipts in `audit/release-<date>/`, a freeze from the cut to the verdict. a red gate is published red with its evidence, never fixed by hand on the artifact. the owner alone promotes, publishes, tags. the versions of the ladder follow the lanes: contained is a patch, wide a minor, a change the whole state depends on a major; the declared bump is at least the computed one.

## pages

a task page per unit in `tasks/` of the owning repository; the design and the review verdicts on it; evidence in `audit/`; the dots on the product page. in phase 1 of [[fathership]] the same pages are read from the [[cybergraph]].
