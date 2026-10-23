---
tags: cyber, cyberia, process
alias: listen, the listening process, feedback
crystal-type: process
crystal-domain: cyberia
---

# listen

how what real people do and say becomes tasks and changes to product pages. [[deliver]] checks a page with a simulated user; listen checks it against the world.

trigger: a sensor fires — an issue arrives, lytics shows a path people take or abandon, a message lands in a channel, a number on a product page stops matching what people get.

## the graph

### 1 · gather · code node

- role: —
- makes: signals from every inbox: GitHub issues, lytics, channels, support, the markets
- green when: every signal has a source, a time and the product it concerns

### 2 · sort · splitter

- role: bridge-in
- makes: signals grouped by the claim on a product page they touch; noise set aside with a reason
- green when: every kept signal names a page and a claim

### 3 · weigh · worker

- role: counter
- makes: the weight of each group: how many, how often, what it costs the claim
- green when: a number with its method

### 4 · propose · worker

- role: seer
- makes: a task for [[deliver]] or a change to the product page
- green when: the proposal names the claim, the evidence and the lane

## return edges

- short: a signal sorted to the wrong claim comes back from weigh to sort.
- long: a signal class that recurs becomes a sensor of its own, so the next time it is gathered by code and not by reading.

## lanes

contained throughout; listen never changes a product, it proposes. an issue from outside is never the truth of work: it becomes a task and the issue closes with the task's link.

## pages

the signals as rows on the task that gathers them; the proposals as tasks of kind proposal in the product's repository; the weights in `audit/`.
