---
tags: cyber, cyberia, process
alias: deliver, the delivery process, delivery
crystal-type: process
crystal-domain: cyberia
---

# deliver

how an accepted product page becomes a released product. the page is the goal; its claims are the units; a claim is delivered when a simulated user has passed it and the counter has turned its dot green. the [[dev|three laws of evidence]] hold at every node: admission by execution, capability over prose, a finite agenda on one snapshot.

trigger: a product page accepted by the owner, or a change to one that [[listen]] or [[govern]] produced. the releases have their own clocks: the day, the week, the moon (§ the three releases).

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
| 8 release of the day · gate | runner cuts; the machine promotes what is contained | the patch version of one repository — the last digit: every change merged since the last release, each small and ready to travel, live the same day | cut from origin, the gates green, the door answering from the new version |
| 9 release of the week · code node, then gate | runner integrates, sensor tests | the minor version of every repository that changed — the second digit: their main lines merged and tested as one set, the pins moved together | all tiers and the fleet green on the integrated set |
| 10 release of the moon · gate | the owner promotes | one product release of cyberia, named by its moon: every repository of the release culture at its week's version, one changelog, one report | the owner's verdict |

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

## the three releases

a change is delivered when it is live, and it goes live only by a release: what production serves is what a release holds, cut from origin. a copy from a working tree is never a deploy. three releases run on three clocks of the [[cyberia/calendar|calendar]], each a skill of its own with a trigger that starts it and a tracker that says whether it works.

| | of the day (node 8) | of the week (node 9) | of the moon (node 10) |
|---|---|---|---|
| clock | the sun: every day, 12:00 utc | the week: Friday, 12:00 utc | the moon: the full moon |
| scope | one repository, by itself | every repository that changed, together | the whole product: every repository of the release culture |
| version | the last digit | the second digit | the moon's own name, `year.moon` in [[lunar machine time]] — the release of this moon is `56.11` |
| what it takes | changes merged since the last release, each contained: small, tested, ready to travel | the main lines of the week, merged into one set | the last green release of the week of each repository |
| what it proves | the repository's own gates on the commit it cuts | every test tier and the fleet on the integrated set; the pins of the siblings moved by one bump | node 7 walks every claim of every product page on the released set |
| who promotes | the machine, when the lane is contained; a wide change waits for the week | the machine, when the set is green | the owner |
| where it lands | production, the same day: the door, the site, the service | the release line and the candidate with its binaries | the product release of [[cyberia]]: one changelog, the moon report beside the money's |
| red | published red with its evidence; nothing goes live; the unit returns to its node | the set is published red; the repository that broke it is named and returns | the release waits for the next moon; what was red is the first unit of the moon |

the day's release is what keeps a merged change from waiting: on 21 November 2026 a merged change to a site's config sat unserved until somebody asked for it to be copied to the server by hand. the week's release is what the train was: integration is where the parts meet, and it is tested once a week on everything, not on each part alone. the moon's release is the product: one thing a person can be told about, with one name.

### the release culture

a repository is in the release culture when it carries four things: a version in its manifest, a changelog, its gates named in its `AGENTS.md`, and a door or an artifact where a release is seen. a repository outside it is delivered by nobody's promise. the moon's release lists which are in and which are not; bringing one in is a unit of deliver.

### the triggers

| trigger | fires | starts | where it lives |
|---|---|---|---|
| the day's cut | every day, 12:00 utc | node 8 in every repository of the release culture that has a merged change since its last release | a workflow of the repository; for what a server serves, the machine's deploy step from origin |
| the week's cut | Friday, 12:00 utc | node 9 once, over the organisation | one workflow in the stack's root, which the others answer |
| the moon's cut | the full moon | node 10 once | the apparatus, which knows the moon; the owner's verdict is asked as a prepared decision |
| a red release | a release published red | the return edge to the node that produced the change | the combine |

### the trackers

each release is seen by numbers that are measured, never reported. the cockpit draws them on the processes screen and puts the next cut of each on the calendar.

| tracker | what it counts | green when |
|---|---|---|
| waiting to travel | merged changes of a repository not yet in a release, and the age of the oldest | nothing older than one day |
| live is what was released | the version the door serves against the last release | the same |
| the day's streak | consecutive days on which every repository with a change released green | it grows |
| the week's set | whether the last integrated set was green, and its age | green, not older than a week |
| out of pin | repositories whose siblings are pinned to a revision behind their main line | none after the week's cut |
| the moon's coverage | repositories of the release culture in the last moon's release, of all the products | it grows toward all |
| the moon's streak | consecutive moons released on the full moon | it grows |

measured on 21 November 2026, before any of this runs: 7 of 26 products have a release at all; the newest is 50 days old; the stack's root has 492 commits since its release; the train's last two runs were cancelled, and its schedule on the main lines is still weekly while this page said daily.

every release is cut from the default branches, with `SHA256SUMS`, `sources.json`, `candidate.json`, `release-validation.json` and receipts in `audit/release-<date>/`, and a freeze from the cut to the verdict. a red gate is published red with its evidence, never fixed by hand on the artifact. the owner alone tags and publishes the moon's release; the day's and the week's are tagged by the machine under its own name. 
the versions of the ladder follow the lanes: contained is a patch, wide a minor, a change the whole state depends on a major; the declared bump is at least the computed one.

## pages

a task page per unit in `tasks/` of the owning repository; the design and the review verdicts on it; evidence in `audit/`; the dots on the product page. in phase 1 of [[fathership]] the same pages are read from the [[cybergraph]].
