---
tags: cyberia, protocol, signal, construct
alias: signal studio, erp core, world construct, constructor
crystal-type: pattern
crystal-domain: cyberia
---
# signal studio — world construction surface

the universe constructor on cyberia.my/world. one surface, built on the
[[soft3]] ladder — the same primitives [[neural]] specifies, running
local-first in the browser, real all the way down:

- a **particle** is a [[hemera]] (Poseidon2) hash — content addressing, not a fake id
- the **neuron** is a [[mudra]] domain-scoped secp256k1 key (entropy → hemera KDF → d·G) — the same identity pipeline as the [[lytics]] tracker
- a committed **signal** carries an ADR-036 signature over its canonical body; VERIFY re-checks it in the page

## the ladder

| primitive | in the studio |
|---|---|
| [[word]] | typed particle — `kind:name` hashed to identity; the four faces (form · particle · type · meaning) on every word page |
| [[link]] | word —relation→ word; the relation is itself a word |
| [[sentence]] | a chain of links in one signal — detected and badged |
| [[signal]] | **the unit of submission**: one atomic batch of links, signed by the neuron; all land together or none do |
| [[motif]] | template — a declared recipe (burns → mints) stamped into the graph on every run |
| [[dialect]] | the cyberia ERP itself: TSP-1 coin · TSP-2 card · PLUMB verbs as relation-words (owns, located_in, burns, mints, pays, …) |
| [[lexicon]] | words ranked by focus — Σ weight of committed links touching them (a soft φ\* stub, honest about being local) |

## the create path

```
word → link → draft signal → COMMIT · SIGN → the graph grows
```

every mutation converges on signals. drafting a link opens the one draft
batch; committing hashes the canonical body (hemera), signs it (ADR-036),
and the links become the graph. running a motif burns/mints real stock
**and** emits its own committed signal. plot leases sync into the graph
as `you —owns→ plot —located_in→ city`.

## the dialect over the graph

[[cyberia/protocol/system]] is the dialect spec — nature (TSP-1/TSP-2),
PLUMB, traits, intent · template · schedule, views. the studio implements
it as a convention over words and links, not a second ontology:

- a Card is a word (person · city · plot · place · building · project · asset)
- a Coin is a word (kind `coin`) whose balance lives in the stock ledger
- a template run = intent (reserved → done) + stock ops + one signed signal
- views project, never mutate: lexicon · graph · signals · inventory ·
  balance · kanban · calendar · memory · conservation — every row real,
  no invented coefficients (the old soft P&L / balance-sheet fictions are
  gone; conservation shows Σ held vs minted/burned per coin)

## surfaces

| path | role |
|------|------|
| /world | studio hub — neuron identity, open draft, lexicon, signal feed |
| /world/words · /world/word/:particle | the lexicon; a word's four faces |
| /world/links · /world/links/new | the atom — into the draft batch |
| /world/signals · /world/signal/:id | batches; COMMIT · SIGN · VERIFY |
| /world/templates | motifs (burn → mint recipes) |
| /world/intents · /world/schedules | ops dialect |
| /world/views | projections |
| /genetics | the living layer — species words; seed → `species —produces→ coin`, then `plot —grows→ species` |
| /map | lease → plot → graph substrate |

## related

- [[cyberia/protocol/system]] — the dialect spec (kernel + ERP layers)
- [[neural]] specs — word · sentence · motif · dialect · lexicon law
- [[soft3]] — the five SDK ops the studio embodies: particle · cyberlink → signal · query · verify · submit
- [[cyberia/protocol/marketplace]] — claims when surplus exists
