---
tags: cyber, cyberia, process
alias: release, the release process, the train, trains
crystal-type: process
crystal-domain: cyberia
---

# release

how what [[deliver]] merged becomes a version that production serves. one graph of five skills, started by three clocks — the trains of the day, the week and the moon. a train leaves at its time, takes what is ready, and what is not ready waits for the next.

trigger: a clock of the [[cyberia/calendar|calendar]] — every day at 12:00 utc, Friday at 12:00 utc, the full moon.

## the train in the five primitives

work has five primitives ([[dev]] § first principles 4): a goal, a task, a skill, an event, a sensor. a process is a composite skill; a release is an event. the rest follows, and nothing here is a kind of its own:

| word | primitive | in this process |
|---|---|---|
| release, the process | a composite skill | the graph below: five skills that carry one version from what is merged to what production serves |
| a train | a sensor: a clock | a trigger of this process. it fires at its time and starts one run |
| a run of a train | a task | one pass of the five skills with the train's arguments: its scope, its gates, its digit, who opens the gate |
| a release | an event | what a run leaves: a version at a point in time |
| the release culture, the trackers | goals and their sensors | what the runs are measured against |

so the three trains are three triggers of one process, each a row of the registry of triggers like every other clock of the organism; the releases are this process's events; and a fourth train would be a fourth trigger with its arguments, never a new graph. two things define a process — its unit and what starts it:

| process | unit | started by | ends when |
|---|---|---|---|
| [[deliver]] | one atomic change | an event: a page accepted, a change proposed | the change is on the main line and walked by a user |
| release | one version | a clock | production serves the version |

## the graph

| node | role | makes | green when |
|---|---|---|---|
| 1 gather · code node | — | the set: what is merged and not yet released, in the scope of this scale | every change of the set is on a main line of origin; the set names its repositories and commits |
| 2 prove · code node | sensor | the gates run on the set as a whole | green; a red set is recorded red with what broke it, and nothing of it travels |
| 3 cut · gate | runner; the owner at the scale of the moon | the version: a tag on the commit and a release with the changelog of what it carries | the gate of the scale opens |
| 4 carry · code node | runner | what the release serves, put live from it: the door, the site, the service, the binaries | production holds the released version |
| 5 confirm · worker | sensor | a receipt: the door answers from the new version | the receipt names the version it saw |

## the three trains and their arguments

| | the day | the week | the moon |
|---|---|---|---|
| clock | every day, 12:00 utc | Friday, 12:00 utc | the full moon |
| scope of the set (node 1) | one repository, by itself: its changes of the last week | every repository that changed, as one integrated set | the product: every repository of the release culture at its version |
| the gates (node 2) | the repository's own, on its head | every test tier and the fleet on the integrated set — the stack's train | every claim of every product page walked on the released set |
| the version (node 3) | the last digit | the second digit | the moon's own name, `year.moon` in [[lunar machine time]]: `56.11` |
| who opens the gate | the machine, on green | the machine, on green | the owner, by a signed answer to a prepared decision |
| what is carried (node 4) | production, the same day | the release line and the candidate | one product release of [[cyberia]], one changelog, beside the moon's report |
| takes from | deliver: merged changes | the days: what a day could not take — a backlog older than a week, a change across repositories | the weeks: the versions as they stand |

a version has three numbers, `vX.Y.Z`. the scales nest: a change that a day's train cannot take waits for the week's, and the moon's names what the weeks made.

## return edges

- short: a red set returns to [[deliver]] as a unit for the repository that broke it; the train does not wait and leaves without it.
- long: a gate that wavered — red once, green on the second run — is a unit of [[operate]]: a train must not depend on luck.
- culture: a repository the moon's release lists as outside the culture is a unit of deliver to bring it in.

## the release culture

a repository is in the release culture when it has a version — a tag `vX.Y.Z` on its main line — and gates that run on its head: its checks, or the commands the apparatus names for it (`apparatus/release/culture.toml`). the release itself writes the changelog, from the changes it carries. a repository outside the culture is delivered by nobody's promise.

## the trackers

each scale is seen by numbers that are measured, never reported; the cockpit draws them on the processes screen and puts the next train of each scale on the time screen.

| tracker | what it counts | green when |
|---|---|---|
| waiting to travel | merged changes of a repository not yet in a release, and the age of the oldest | nothing older than one day |
| heads with red gates | repositories of the culture whose head would not be released | none |
| the day's streak | consecutive days on which every repository with a change released green | it grows |
| the week's set | whether the last integrated set was green, and its age | green, not older than a week |
| the moon's coverage | repositories in the release culture, of all | it grows toward all |
| the moon's streak | consecutive moons released at the full moon | it grows |
| versions of another shape | tags that read as a version and are not three numbers | none |

measured on 21 November 2026, the day the trains began to run: 18 of 118 repositories are in the release culture; 17 carry changes older than a week, 3,894 in all; 5 have red gates on their head; the first release of the day was apparatus `v0.1.1`.

## lanes

the day's and the week's trains are cut, tagged and carried by the machine under its own name; the moon's is promoted by the owner alone. every release is cut from the main lines of origin; a copy from a working tree is never a deploy. a red gate is recorded red with its evidence, never fixed by hand on the artifact.

## pages

the engine is `apparatus/scripts/release.py`, its registry `apparatus/release/culture.toml`; the receipts are the releases themselves, on the repository they belong to.
