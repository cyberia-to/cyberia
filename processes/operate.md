---
tags: cyber, cyberia, process
alias: operate, operations, the operating process, ops
crystal-type: process
crystal-domain: cyberia
---

# operate

how the machines, domains, keys and sites of the state keep running, stay observed and come back after a failure. the record is [[cybernode]]: the server is the truth, the repository mirrors it, and the sync is the first and last step of every change.

trigger: a change that must reach a machine; an alarm; a certificate, a domain or a key nearing its end; a runbook that proved wrong.

## the graph

### 1 · plan · worker

- role: runner
- makes: the change written as a runbook step: command, expected state, rollback
- green when: the rollback is written before the command

### 2 · stage · worker

- role: runner
- makes: the change on a staging path or a backup first
- green when: a test passes where one exists: `nginx -t`, a probe, a dry run

### 3 · apply · gate

- role: runner, the owner on the irreversible lane
- makes: the change on the machine
- green when: the probe from outside answers as expected; local probes are evidence, never the verdict

### 4 · observe · code node

- role: sensor
- makes: monitors, logs, alarms
- green when: the alarm that would have caught this failure exists

### 5 · mirror · code node

- role: keeper
- makes: the repository matches the machine; the runbook carries what was learned
- green when: `sync.sh` shows no drift

## return edges

- short: a probe that fails returns to stage with the evidence; the rollback runs first.
- long: every incident leaves a line in the runbook and, where it can, a monitor; a procedure that failed twice is rewritten, not annotated.

## lanes

contained: a static site's docroot, a monitor, a DNS record that has a backup of the zone. wide: nginx, certificates, cron, anything shared by several sites. irreversible: deletion of data, a key, a payment, a change to the production chain; the owner's hand, always.

## pages

the runbooks and mirrors in [[cybernode]]; incidents as tasks of kind issue; what was learned on the runbook, dated.
