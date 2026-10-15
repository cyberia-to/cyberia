---
tags: cyber, cyberia, process
alias: deliver, the delivery process, delivery, the loop
crystal-type: process
crystal-domain: cyberia
---

# deliver

the one process of cyberia: how a product page becomes a measured claim. a skill of the composite kind, six steps, each owned by a role and closed by a sensor. the structure it serves is [[dev]]; the project that brings it into force is [[fathership]].

## the steps

| # | step | role | input | output | closed by |
|---|---|---|---|---|---|
| 1 | propose | seer | the state board, M, the charter | a product page, or a change to one, as a task of kind proposal | the owner's verdict; the page is a goal of kind product |
| 2 | specify | keeper | the product page | specifications in `specs/`, each claim traced to a dot on the page | rungs 1–7: convergence, then the owner's verdict; rungs 8–10: a review by another body |
| 3 | build | runner | a specification | tasks of kind work, each ending in a proposal of change | a review by another body; the merge |
| 4 | check | sensor, counter | a change | gates and measurements written to `audit/` | the gates of the task, the product and the state |
| 5 | release | runner | a green state | a candidate on the weekly train with its receipts | the owner's verdict |
| 6 | measure | counter, seer | the product in use | the dots on the product page; the next proposal | M rising |

a step takes a task of one kind and leaves a page behind; nothing moves between steps except pages and cyberlinks.

## two ways of working

- convergence, for what matters: every body takes the same brief independently in round one, so their errors stay uncorrelated; a chair, rotating, merges the results and keeps a list of disagreements; later rounds go one body at a time, each verifying the disputed points against pages and code; a round that changes nothing ends it, three rounds end it; what remains goes to the owner as one verdict with both sides. specifications of rungs 1–7, architecture, audits and product pages go this way.
- dispatch, for what is small: any free body takes the task on a cheap model; the reviewer is another body; a task red twice goes to convergence as a question.

the roles run on bodies; a body today is claude, codex, kimi or grok. a role is a portfolio of skills, never a body, so the same role moves between bodies without losing its history.

## the gates

a gate is a sensor on a goal. three scopes:

| scope | fires on | what runs | red means |
|---|---|---|---|
| task | every proposal of change | the repository's own checks named in its README; api compatibility against the last tag; a review by another body | no merge |
| product | a merge into any part of a product | the product and everything that depends on it on the ladder build and pass; the specification checks | no version bump for the product |
| state | every friday 12:00 utc, and any cut the owner asks for | the whole ladder from origin; integration; user runs; audits; receipts | a red candidate, published as red with its evidence |

the scope of a change is computed from the files it touches and the dependency graph of the ladder, never declared by its author. versions follow: a change inside the task scope is a patch, one that reaches the product scope a minor, one that reaches the state scope a major; the declared bump is at least the computed one, and a lower declaration is red.

## the train

the state gate is the release train: a candidate every friday from the default branches, `candidate-YYYYMMDD.N`, binaries per platform, `SHA256SUMS`, `sources.json`, `candidate.json`, `release-validation.json`; receipts in `audit/release-<date>/`; a freeze from the cut to the verdict; the owner alone promotes, publishes, tags. gates are executable and named in each repository's README; a red gate is published red, never fixed by hand on the artifact.

## the record

in phase 0 of [[fathership]] tasks are pages in `tasks/` of the owning repository with `kind`, `status`, `owner`, `serves` in the frontmatter, and the views of [[dev]] are queries over those pages; a pull request is the wire of a change and GitHub a mirror. in phase 1 the same pages are read from the [[cybergraph]]; in phase 2 the change itself travels as a [[patch]] and GitHub only reflects it. the strategic cadence of freezing the lower rungs — a temperature per rung that only falls — belongs to that later phase and is written when it is reached.
