---
tags: cyber, cyberia, process
alias: release, the release process, the train, trains
crystal-type: process
crystal-domain: cyberia
---

# release

how what [[deliver]] merged becomes a version that production serves: three trains in a line — daily, weekly, moonly — each started by its own clock and each a skill of its own. a train leaves at its time, takes what is ready, and what is not ready waits for the next.

trigger: a clock of the [[cyberia/calendar|calendar]] — every day at 12:00 utc, Friday at 12:00 utc, the full moon.

## the train in the five primitives

work has five primitives ([[dev]] § first principles 4): a goal, a task, a skill, an event, a sensor. a process is a composite skill; a release is an event. the rest follows, and nothing here is a kind of its own:

| word | primitive | in this process |
|---|---|---|
| release, the process | a composite skill | the graph below: three trains in a line, each a skill of five steps that carries a version from what is merged to what production serves |
| a train | a sensor: a clock | a trigger of this process. it fires at its time and starts one run |
| a run of a train | a task | one pass of the train's own skill, on its own page: its scope, its gates, its digit, who opens the gate |
| a release | an event | what a run leaves: a version at a point in time |
| the release culture, the trackers | goals and their sensors | what the runs are measured against |

so the three trains are three triggers of one process, each a row of the registry of triggers like every other clock of the organism, and each wakes its own node; the releases are this process's events; and a fourth train would be a fourth node with its skill page and its trigger. two things define a process — its unit and what starts it:

| process | unit | started by | ends when |
|---|---|---|---|
| [[deliver]] | one atomic change | an event: a page accepted, a change proposed | the change is on the main line and walked by a user |
| release | one version | a clock | production serves the version |

## the graph

| node | role | makes | green when |
|---|---|---|---|
| 1 daily · code node | runner | the last digit of one repository: its changes of this week, live the same day | every repository with a fresh change and green gates is released; a red one is recorded red |
| 2 weekly · code node | runner, sensor | the second digit of every repository that changed, proved as one integrated set | the set is green and its versions are cut; a red set names what broke it |
| 3 moonly · gate | the owner | one product release of [[cyberia]], named by its moon in [[lunar machine time]] | the owner's signed word |

the nodes are a line: a change the day cannot take — older than a week, or across repositories — waits for the week; the moon names what the weeks made. each node is woken by its own clock, its train.

## skills

each train is a skill with a graph of its own inside its node — the same five steps, gather, prove, cut, carry, confirm, set to its scale. a train is changed on its own page: its scope, its gates, its digit, who opens its gate; the others do not move.

- [[daily train]] — one repository by itself, every day at 12:00 utc: the last digit, deployed.
- [[weekly train]] — the integrated set, Friday at 12:00 utc: the second digit.
- [[moonly train]] — the product, at the full moon: one release under the moon's name, by the owner's word.

## return edges

- short: a red set returns to [[deliver]] as a unit for the repository that broke it; the train does not wait and leaves without it.
- long: a gate that wavered — red once, green on the second run — is a unit of [[operate]]: a train must not depend on luck.
- culture: a repository the moon's release lists as outside the culture is a unit of deliver to bring it in.

## the release culture

a repository is in the release culture when it has a version — a tag `vX.Y.Z` on its main line — and gates that run on its head: its checks, or the commands the apparatus names for it (`apparatus/release/culture.toml`). the release itself writes the changelog, from the changes it carries. every change in it stands with its link: the pull request it came by and the issues that request and its commits name; the link is a pull request, never a commit — a change of the product travels by a pull request (the owner, 2026-11-22: "not to a commit — to a pull request"). the cut of a train is where this is checked (`apparatus/scripts/release.py`): from 2026-11-22 09:00 utc a commit of the product pushed with no pull request holds its repository's release red, recorded with the commits that came bare, and the repository is a unit of [[deliver]] until each of them stands with a request — the bare commit reverted, and the request carrying the change again; a commit pushed before that hour can be given none, and the release lists it with its own commit and says it came from before the rule. working state — the paths the `direct` zone of `apparatus/combine/zones.toml` names: a journal line, a receipt, a task page, a project declaration — is no change of the product and is not listed. a repository outside the culture is delivered by nobody's promise.

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
