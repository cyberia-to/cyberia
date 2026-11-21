---
tags: cyber, cyberia, process, skill
alias: weekly train, week train, the week's train, release of the week, weekly release, the integrated set
crystal-type: skill
crystal-domain: cyberia
status: accepted
---

# weekly train

a skill of [[release]], inside its node 2, weekly: how the week's changes of every repository are proved together and become the next minor versions. the owner, 2026-11-21: the three trains are our train, each its own configuration.

trigger: the clock, Friday at 12:00 utc.

## the graph

| node | role | makes | green when |
|---|---|---|---|
| 1 gather · code node | — | the integrated set: the main lines of every repository that changed | the set names each repository and its commit |
| 2 prove · code node | sensor | every test tier and the fleet on the set as a whole — the stack's train | the train ends green |
| 3 cut · gate | runner | the second digit of every repository of the set that changed: a tag and a release each | the set is green; a repository outside the stack opens on its own green |
| 4 carry · code node | runner | the release line and the candidate with its binaries | the candidate is published with its sums and sources |
| 5 confirm · worker | sensor | a receipt per repository: the release exists at the commit the set named | every receipt matches the set |

## its arguments

| argument | value |
|---|---|
| scope | every repository that changed, as one set |
| takes | what the [[daily train]] could not: a backlog older than a week, a change across repositories |
| digit | the second: `vX.Y+1.0` |
| gate opened by | the machine, on a green set |
| carried to | the release line and the candidate |

## return edges

- short: a red set names the repository that broke it, which returns to [[deliver]]; the others wait for the next Friday.
- long: what broke the set becomes a check of that repository's own gates, so the day's train meets it first.
