---
tags: cyber, cyberia, process
alias: govern, governance process, how the charter changes, how the father sets a law
crystal-type: process
crystal-domain: cyberia
---

# govern

how the charter changes and how the owner's verdicts are rendered. the charter is the scheme on [[dev]]: identity, the product line, the roles, the process. it changes by one path, and every verdict is a page.

trigger: a proposal — a task of kind proposal whose subject is a page of the charter; or a review task addressed to the owner by any process.

## the graph

### 1 · propose · worker

- role: anyone, an agent included
- makes: the proposal: summary, motivation, the change quoted, what it contradicts today, acceptance criteria
- green when: every contradiction with the charter is named

### 2 · audit · workers

- role: every body, adversarial first
- makes: where it breaks identity, strategy, a product page, the vocabulary; which pages cite the clause
- green when: a disagreement list, converged or at its third round

### 3 · verdict · gate

- role: the owner
- makes: the decision on the task page: for, against, the verdict
- green when: written by the owner's hand

### 4 · amend · code node

- role: keeper
- makes: the charter page changed, the decision logged, the pages that cite the clause reopened as tasks
- green when: every citing page has a task; the scheme on [[dev]] resolves

## return edges

- short: a proposal that contradicts the charter without saying so returns to propose.
- long: a verdict becomes a rule; the next proposal on the same clause starts from it.

## lanes

the charter is the irreversible lane by definition: no policy and no agent merges it. the queue of verdicts is a query — review tasks of the owner, status open — and the organism keeps it under five by settling what it can before asking.

## pages

the proposal and the verdict are one task page in `tasks/` of the repository that owns the clause; the log of decisions is the query of those pages with status done, by date.
