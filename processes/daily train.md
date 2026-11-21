---
tags: cyber, cyberia, process, skill
alias: daily train, day train, the day's train, release of the day, daily release
crystal-type: skill
crystal-domain: cyberia
status: accepted
---

# daily train

a skill of [[release]], inside its node 1, daily: how one repository's fresh changes become its next patch version, live the same day. the owner, 2026-11-21: the three trains are our train, each its own configuration.

trigger: the clock, every day at 12:00 utc.

## the graph

| node | role | makes | green when |
|---|---|---|---|
| 1 gather · code node | — | the repository's set: what is merged since its last version | the set is on origin's main line; none of it is older than a week |
| 2 prove · code node | sensor | the repository's own gates on its head | green: its checks, or the commands the apparatus names for it |
| 3 cut · gate | runner | the last digit: a tag on the head and a release with the changelog of the set | the gates are green; the machine opens it |
| 4 carry · code node | runner | what the repository serves, put live from the release | production holds the new version |
| 5 confirm · worker | sensor | a receipt: the door answers from the new version | the receipt names the version it saw |

## its arguments

| argument | value |
|---|---|
| scope | one repository, by itself |
| takes | changes merged within the last week; an older backlog waits for the [[weekly train]] |
| digit | the last: `vX.Y.Z+1` |
| gate opened by | the machine, on green |
| carried to | production, the same day |

## return edges

- short: red gates return the repository to [[deliver]] as a unit; the train leaves without it.
- long: a gate that wavered is a unit of [[operate]].
