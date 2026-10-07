---
tags: cyber, cyberia, fathership, roadmap, plan
alias: fathership, the father, governing by vision, dev roadmap, process roadmap, the loop roadmap
crystal-type: plan
crystal-domain: cyber
status: active
---

# cyberia/fathership

[[cyber/launch]] says what ships. this page says how: the way the owner governs the work of agents, and the road from a hand-driven process to development that runs on [[cybergraph]]. [[cyberia/dev]] is the law every agent works by; this page is the plan that brings that law into force, subsystem by subsystem.

version 2026.10 · phase 0 in delivery · single tracker of the way of working: every gate, decision and status change of the process lands here.

## the thesis

the owner is a father, not an architect. a father sets the vision, breaks the ties agents cannot break, and promotes releases. research, planning, implementation, review, merging within policy, cutting candidates and keeping the house clean are the agents' work, done in the open, with evidence, in files the owner reads when he chooses.

three numbers on the state board measure the stance, every week:

| number | what it says |
|---|---|
| share of merges with no owner action | how much of the loop runs itself |
| time from a task becoming `ready` to its change merged | how fast the loop turns |
| decisions brought to the owner, and how many were real ties | judgment or noise |

## the canon

the canon is what the father holds and what every change is accepted against. four layers, each with its documents, its keeper, its cadence and its role in acceptance. the index below is the only place that names all of them; every hub links here.

<svg viewBox="0 0 900 290" width="100%" xmlns="http://www.w3.org/2000/svg" font-size="12" style="font-family:inherit" fill="none" stroke="currentColor" stroke-width="1">
<defs><marker id="k" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="currentColor" stroke="none"/></marker></defs>
<rect x="20" y="14" width="440" height="56" rx="6" stroke-width="2"/>
<text x="32" y="34" fill="currentColor" stroke="none" font-weight="600">identity · 0K</text>
<text x="32" y="52" fill="currentColor" stroke="none" opacity="0.8">license · manifesto · purpose, vision, mission</text>
<text x="300" y="34" fill="currentColor" stroke="none" opacity="0.7">the owner alone, rarely</text>
<rect x="20" y="80" width="440" height="56" rx="6"/>
<text x="32" y="100" fill="currentColor" stroke="none" font-weight="600">strategy · by quarter</text>
<text x="32" y="118" fill="currentColor" stroke="none" opacity="0.8">troika · ladder · launch phases · goals of the quarter</text>
<text x="300" y="100" fill="currentColor" stroke="none" opacity="0.7">the owner, by proposal</text>
<rect x="20" y="146" width="440" height="56" rx="6"/>
<text x="32" y="166" fill="currentColor" stroke="none" font-weight="600">products · by release</text>
<text x="32" y="184" fill="currentColor" stroke="none" opacity="0.8">big: README · litepaper · whitepaper · specs — mini: README · specs</text>
<text x="300" y="166" fill="currentColor" stroke="none" opacity="0.7">product owner, accepted by decision</text>
<rect x="20" y="212" width="440" height="56" rx="6"/>
<text x="32" y="232" fill="currentColor" stroke="none" font-weight="600">law of work · by council</text>
<text x="32" y="250" fill="currentColor" stroke="none" opacity="0.8">dev · fathership · quality · engineering · projects · documentation</text>
<text x="300" y="232" fill="currentColor" stroke="none" opacity="0.7">council audits, the owner commits</text>
<line x1="460" y1="42" x2="520" y2="42" marker-end="url(#k)"/><line x1="460" y1="108" x2="520" y2="108" marker-end="url(#k)"/><line x1="460" y1="174" x2="520" y2="174" marker-end="url(#k)"/><line x1="460" y1="240" x2="520" y2="240" marker-end="url(#k)"/>
<rect x="522" y="14" width="358" height="254" rx="6" stroke-dasharray="4 3"/>
<text x="534" y="34" fill="currentColor" stroke="none" font-weight="600">acceptance</text>
<text x="534" y="58" fill="currentColor" stroke="none">1 · lineage: every task names the goal, the product</text>
<text x="534" y="74" fill="currentColor" stroke="none">    and the clause it serves; no lineage, never ready</text>
<text x="534" y="100" fill="currentColor" stroke="none">2 · canon pass: the reviewer's first pass; a contradiction</text>
<text x="534" y="116" fill="currentColor" stroke="none">    with any layer is a decision, never a merge</text>
<text x="534" y="142" fill="currentColor" stroke="none">3 · owner-only paths: canon files merge by the owner's hand</text>
<text x="534" y="158" fill="currentColor" stroke="none">    (CODEOWNERS), every change is a decision row</text>
<text x="534" y="184" fill="currentColor" stroke="none">4 · re-acceptance: a changed clause reopens every product</text>
<text x="534" y="200" fill="currentColor" stroke="none">    that cites it; the mayor opens the tasks</text>
<text x="534" y="226" fill="currentColor" stroke="none">5 · catalog lint: a product without a definition is red</text>
<text x="534" y="242" fill="currentColor" stroke="none">    on the board; the registry carries the catalog</text>
<text x="534" y="262" fill="currentColor" stroke="none" opacity="0.7">colder downward: identity changes least</text>
</svg>

### the index

identity · the owner alone, rarely

- [[cyber/license]] — the law in six words: don't trust, don't fear, don't beg
- [[cyberia/foundation/manifesto]] — seven principles and the oath to life
- [[cyberia/foundation/strategy]] § purpose, vision, mission — type 1 civilization · make planets think · build cyberstate, led by superintelligence

strategy · the owner, by proposal, by quarter

- [[cyberia/foundation/strategy]] § the troika — three sovereign forms: cyber the protocol, cyb the interface, cyberia the physical
- `soft3/release/components.toml` and [soft3.org/layers](https://soft3.org/layers) — the ladder: ten products, one per rung, the product line
- [[cyber/launch]] — the phases of the protocol launch; the single tracker of what ships
- [[cyberia/fathership]] — the phases of the way of working; this page
- [[cyberia/goals]] — the goals of the quarter, at most five, each with its measure

products · the product owner proposes, a decision accepts

- README · litepaper · whitepaper · `specs/` of each rung and warrior — what the product is, for whom, done when; § the product line

law of work · council audits, the owner commits

- [[cyberia/dev]] — the law every agent works by
- [[cyberia/quality]] · [[cyberia/engineering]] · [[cyberia/projects]] · [[cyberia/documentation]] · [[cyberia/refinement]] — review passes, pipeline contracts, repo layout, documentation, polishing

doctrines · the law of one domain each, under the identity layer

- [[cyberia/foundation/space doctrine]] — claim beyond Earth
- `warriors/mining.md` · `warriors/interface.md` — how a warrior mines and how it speaks
- `cyberstates/doctrine.md` — what a state is
- `endeka/foundation/axioms.md` — the family form; today an orphan with no inbound link

the index is a property of the registry (29): a canon document that no hub links is a defect, and a value statement that lives outside this index has no force in acceptance.

### how the father sets a law

a law changes by one procedure, the same for every layer; the layers differ only in who proposes and how often.

1. a proposal file in `cyberia/proposals/<date>-<slug>.md`, in the shape of a KEP: summary · motivation · what changes, quoted · what it contradicts in the canon today · acceptance criteria · the owner as approver. anyone may write it, an agent included.
2. a council audit, adversarial round first: where does it contradict identity, strategy, a product definition, the vocabulary; which products cite the clause it changes.
3. the owner's word: the owner commits the change to the canon file; canon paths are owner-only in CODEOWNERS, so no policy and no agent merges them. the decision lands as a row in § decisions with the proposal's link.
4. re-acceptance: the mayor opens one task per product whose definition cites the changed clause; those tasks carry the lineage `serves: <proposal>` and the product's owner answers them within the quarter.
5. cadence by layer: identity changes only by the owner's explicit act and is expected to change once in years; strategy by quarter, when goals are set; product definitions by release; the law of work whenever a council audit finds it wanting.

the owner's own tools are therefore four files and one list: `cyberia/goals.md` for the quarter, § decisions here and in [[cyber/launch]] for verdicts, the canon index above for what is law, the proposals directory for what wants to become law, and the state board for what the loop brings him.

## the product line

every repository is a product: a mini product when it is a part, a big product when it is a rung of the ladder or a warrior. the definition is what acceptance checks a change against, so every product has one, and its size follows the product's.

- mini · a part, a crate, a page set — the README: what it is, for whom, which rung and `part_of`, done when, owner; `specs/` for its contracts
- big · a rung, a warrior — the README as the door; a litepaper, the whole argument in ten minutes; a whitepaper, mechanisms, mathematics, proofs, `status: draft` allowed; `specs/`; `roadmap/`

the README of every product carries the same five fields in its frontmatter: `product`, `rung`, `part_of`, `paper` (the litepaper and whitepaper paths, or `README` for a mini product), `done-when`. `components.toml` carries `paper =` for every component, and the registry in `.github` lints the catalog: a product without a definition is red on the component board.

coverage of the ten rungs today, from the checkout of 2026-10-07; the paper paths are in the subsystem text and the registry:

| rung | README | litepaper | whitepaper |
|---|---|---|---|
| 1 nox | yes | — | misplaced in crystal |
| 2 trident | yes | — | vision, 2026-05 |
| 3 joy | spec only | — | — |
| 4 cybergraph | yes | — | — |
| 5 neural | yes | — | — |
| 6 cy | yes | — | — |
| 7 soft3 | yes | — | — |
| 8 cyb | yes | — | draft |
| 9 cyber | yes | [[cyber/litepaper]] | [[cyber/whitepaper]] draft |
| 10 cyberia | yes | — | [[cyberia/foundation/whitepaper]] |

seven rungs have no litepaper and five have no paper at all. a litepaper is a council task: four vendors, one brief, convergence; the owner accepts it as a decision. property 35 tracks the seven.

## the map

<svg viewBox="0 0 900 342" width="100%" xmlns="http://www.w3.org/2000/svg" font-size="12" style="font-family:inherit" fill="none" stroke="currentColor" stroke-width="1">
<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="currentColor" stroke="none"/></marker></defs>
<rect x="20" y="10" width="860" height="62" rx="6" stroke-dasharray="4 3"/>
<text x="32" y="28" fill="currentColor" stroke="none" font-weight="600">owner · the father</text>
<rect x="150" y="36" width="330" height="28" rx="4"/>
<text x="315" y="54" fill="currentColor" stroke="none" text-anchor="middle">vision · launch registry rows · quarterly goals</text>
<rect x="520" y="36" width="340" height="28" rx="4"/>
<text x="690" y="54" fill="currentColor" stroke="none" text-anchor="middle">verdict · ties · candidate → release</text>
<line x1="315" y1="64" x2="315" y2="108" marker-end="url(#a)"/>
<text x="322" y="92" fill="currentColor" stroke="none" opacity="0.8">tasks</text>
<line x1="690" y1="108" x2="690" y2="64" marker-end="url(#a)"/>
<text x="697" y="92" fill="currentColor" stroke="none" opacity="0.8">decisions · candidates · boards</text>
<rect x="20" y="110" width="860" height="108" rx="6"/>
<text x="32" y="128" fill="currentColor" stroke="none" font-weight="600">the loop · one task, one session, three artifacts, one change, one merge</text>
<g>
<rect x="36" y="146" width="92" height="40" rx="4"/><text x="82" y="164" fill="currentColor" stroke="none" text-anchor="middle">task</text><text x="82" y="178" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">ready · claimed</text>
<rect x="142" y="146" width="92" height="40" rx="4"/><text x="188" y="164" fill="currentColor" stroke="none" text-anchor="middle">research.md</text><text x="188" y="178" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">what is</text>
<rect x="248" y="146" width="92" height="40" rx="4"/><text x="294" y="164" fill="currentColor" stroke="none" text-anchor="middle">plan.md</text><text x="294" y="178" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">step → verify</text>
<rect x="354" y="146" width="92" height="40" rx="4"/><text x="400" y="164" fill="currentColor" stroke="none" text-anchor="middle">change</text><text x="400" y="178" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">pull request · patch</text>
<rect x="460" y="146" width="92" height="40" rx="4"/><text x="506" y="164" fill="currentColor" stroke="none" text-anchor="middle">review</text><text x="506" y="178" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">another vendor</text>
<rect x="566" y="146" width="92" height="40" rx="4"/><text x="612" y="164" fill="currentColor" stroke="none" text-anchor="middle">merge</text><text x="612" y="178" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">by policy</text>
<rect x="672" y="146" width="92" height="40" rx="4"/><text x="718" y="164" fill="currentColor" stroke="none" text-anchor="middle">rings 0 · 1 · 2</text><text x="718" y="178" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">by blast radius</text>
<rect x="778" y="146" width="92" height="40" rx="4"/><text x="824" y="164" fill="currentColor" stroke="none" text-anchor="middle">candidate</text><text x="824" y="178" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">friday · receipts</text>
<line x1="128" y1="166" x2="142" y2="166" marker-end="url(#a)"/><line x1="234" y1="166" x2="248" y2="166" marker-end="url(#a)"/><line x1="340" y1="166" x2="354" y2="166" marker-end="url(#a)"/><line x1="446" y1="166" x2="460" y2="166" marker-end="url(#a)"/><line x1="552" y1="166" x2="566" y2="166" marker-end="url(#a)"/><line x1="658" y1="166" x2="672" y2="166" marker-end="url(#a)"/><line x1="764" y1="166" x2="778" y2="166" marker-end="url(#a)"/>
<path d="M612,186 L612,208 L82,208 L82,186" marker-end="url(#a)" stroke-dasharray="3 3"/>
<text x="347" y="200" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">merged · the task closes · the next ready task</text>
</g>
<rect x="20" y="238" width="860" height="94" rx="6" stroke-dasharray="4 3"/>
<text x="32" y="256" fill="currentColor" stroke="none" font-weight="600">the ground · what carries tasks and changes, by phase</text>
<rect x="36" y="268" width="262" height="54" rx="4"/>
<text x="46" y="284" fill="currentColor" stroke="none">phase 0 · 2026-10</text>
<text x="46" y="299" fill="currentColor" stroke="none" opacity="0.8">tasks: beads in the repository</text>
<text x="46" y="313" fill="currentColor" stroke="none" opacity="0.8">change: pull request · GitHub is the wire</text>
<line x1="298" y1="295" x2="318" y2="295" marker-end="url(#a)"/>
<rect x="320" y="268" width="262" height="54" rx="4"/>
<text x="330" y="284" fill="currentColor" stroke="none">phase 1 · 2026-11 → 12</text>
<text x="330" y="299" fill="currentColor" stroke="none" opacity="0.8">tasks: cybergraph read, beads written</text>
<text x="330" y="313" fill="currentColor" stroke="none" opacity="0.8">change: pull request · GitHub is the wire</text>
<line x1="582" y1="295" x2="602" y2="295" marker-end="url(#a)"/>
<rect x="604" y="268" width="266" height="54" rx="4"/>
<text x="614" y="284" fill="currentColor" stroke="none">phase 2 · 2027-01</text>
<text x="614" y="299" fill="currentColor" stroke="none" opacity="0.8">tasks: cybergraph only</text>
<text x="614" y="313" fill="currentColor" stroke="none" opacity="0.8">change: patch · GitHub is a mirror</text>
</svg>

the owner touches the loop at two points: the vision that spawns tasks, and the verdict on ties and candidates. the loop is the same in every phase; the ground under it changes.

## the phases

| phase | tasks | change | GitHub | when |
|---|---|---|---|---|
| 0 · scaffolding | beads | pull request | the wire | 2026-10 |
| 1 · the dialect | graph read, beads written | pull request | the wire | 2026-11 → 12 |
| 2 · the graph | graph only | [[patch]] | a mirror | 2027-01 |

gates:

- phase 0 · every phase-0 property proven; the launch worker runs a week under the loop without an incident
- phase 1 · one week in which every board the owner reads is rendered from [[cybergraph]] and agrees with beads; beads exports to the graph within a minute
- phase 2 · thirty days without the scaffold; `ready`, claims and boards answered by inf faster than beads did; a week in which every merge entered as a [[patch]]

phase 1 is the dog-food that proves the product: the development of cyber runs on cyber, on parts that already exist — file, particle, cyberlink, neuron, inf, cy, optica. the scaffold exists so that the process works in weeks while the dialect is built in months; its data model (hash ids, typed dependencies, atomic claims, compaction of closed work) is the shape the dialect will have, so the export is a session, not a project. the same holds for the pull request: the [[patch]] of `fs/patch/spec.md` has the shape a pull request already has — a channel, signed operations, first-class conflicts — minus the snapshot.

## the subsystems

the canon above is what the loop is accepted against; seven subsystems make the loop itself. each names what it is, where its law is written, where it lives, and which properties of the registry prove it.

### 1 · work graph

work is a graph: tasks with hash ids, `blocks` and `discovered-from` edges, `ready` when nothing blocks, atomic claims. the owner's registry rows and goals spawn tasks; agents never invent one. GitHub issues are an inbox for outsiders: an issue becomes a task and closes with its link.

law [[cyberia/dev]] § the work graph · home `bd` in every repository, `.github` for the dispatch · properties 1, 20, 22, 25

### 2 · artifacts and context

three artifacts per task: `research.md` (what is, checked against the checkout), `plan.md` (`[step] → verify: [check]`, five likely failures), the change whose body is generated from the plan. context has the shape of the task: a two-thousand-token soul, a sixteen-thousand-token pack per rung built from `components.toml`, the research artifact. one task, one session, context under sixty percent.

law [[cyberia/dev]] § three artifacts, § context · home `ctx/build.nu`, `.claude/tasks/<id>/` until phase 1 · properties 2, 13

### 3 · vendors

<svg viewBox="0 0 900 250" width="100%" xmlns="http://www.w3.org/2000/svg" font-size="12" style="font-family:inherit" fill="none" stroke="currentColor" stroke-width="1">
<defs><marker id="b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="currentColor" stroke="none"/></marker></defs>
<rect x="20" y="10" width="420" height="230" rx="6" stroke-dasharray="4 3"/>
<text x="32" y="28" fill="currentColor" stroke="none" font-weight="600">council · research, plans, architecture, audits, specs</text>
<text x="32" y="48" fill="currentColor" stroke="none" opacity="0.8">round 1 · independent, parallel, best models</text>
<rect x="32" y="56" width="90" height="26" rx="4"/><text x="77" y="73" fill="currentColor" stroke="none" text-anchor="middle">claude</text>
<rect x="132" y="56" width="90" height="26" rx="4"/><text x="177" y="73" fill="currentColor" stroke="none" text-anchor="middle">codex</text>
<rect x="232" y="56" width="90" height="26" rx="4"/><text x="277" y="73" fill="currentColor" stroke="none" text-anchor="middle">kimi</text>
<rect x="332" y="56" width="90" height="26" rx="4"/><text x="377" y="73" fill="currentColor" stroke="none" text-anchor="middle">grok</text>
<line x1="77" y1="82" x2="200" y2="108" marker-end="url(#b)"/><line x1="177" y1="82" x2="215" y2="108" marker-end="url(#b)"/><line x1="277" y1="82" x2="240" y2="108" marker-end="url(#b)"/><line x1="377" y1="82" x2="255" y2="108" marker-end="url(#b)"/>
<rect x="112" y="110" width="230" height="40" rx="4"/>
<text x="227" y="127" fill="currentColor" stroke="none" text-anchor="middle">round 2 · a rotating chair merges</text>
<text x="227" y="142" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">one artifact · the disagreement list</text>
<line x1="227" y1="150" x2="227" y2="170" marker-end="url(#b)"/>
<rect x="72" y="172" width="310" height="40" rx="4"/>
<text x="227" y="189" fill="currentColor" stroke="none" text-anchor="middle">rounds 3…n · sequential, each verifies the disputed claims</text>
<text x="227" y="204" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">stop: an unchanged round, or three rounds</text>
<text x="227" y="232" fill="currentColor" stroke="none" text-anchor="middle">converged → the artifact · a tie → one question to the owner</text>
<rect x="460" y="10" width="420" height="230" rx="6" stroke-dasharray="4 3"/>
<text x="472" y="28" fill="currentColor" stroke="none" font-weight="600">pool · one function, one measurement, one page</text>
<rect x="472" y="44" width="396" height="26" rx="4"/>
<text x="670" y="61" fill="currentColor" stroke="none" text-anchor="middle">ready tasks → dispatcher · by remaining quota, random on a tie</text>
<line x1="520" y1="70" x2="520" y2="94" marker-end="url(#b)"/><line x1="620" y1="70" x2="620" y2="94" marker-end="url(#b)"/><line x1="720" y1="70" x2="720" y2="94" marker-end="url(#b)"/><line x1="820" y1="70" x2="820" y2="94" marker-end="url(#b)"/>
<rect x="475" y="96" width="90" height="26" rx="4"/><text x="520" y="113" fill="currentColor" stroke="none" text-anchor="middle">claude · cheap</text>
<rect x="575" y="96" width="90" height="26" rx="4"/><text x="620" y="113" fill="currentColor" stroke="none" text-anchor="middle">codex · cheap</text>
<rect x="675" y="96" width="90" height="26" rx="4"/><text x="720" y="113" fill="currentColor" stroke="none" text-anchor="middle">kimi · cheap</text>
<rect x="775" y="96" width="90" height="26" rx="4"/><text x="820" y="113" fill="currentColor" stroke="none" text-anchor="middle">grok · cheap</text>
<line x1="670" y1="122" x2="670" y2="146" marker-end="url(#b)"/>
<rect x="520" y="148" width="300" height="26" rx="4"/>
<text x="670" y="165" fill="currentColor" stroke="none" text-anchor="middle">review · always another vendor than the implementer</text>
<line x1="670" y1="174" x2="670" y2="198" marker-end="url(#b)"/>
<rect x="520" y="200" width="300" height="26" rx="4"/>
<text x="670" y="217" fill="currentColor" stroke="none" text-anchor="middle">ring 0 green → merge · red twice → council</text>
<text x="670" y="236" fill="currentColor" stroke="none" text-anchor="middle" opacity="0.7">quota is a resource: councils first, pools with the rest, nothing unspent</text>
</svg>

vendors are assigned by the class of work, never by loyalty. claude and codex run in their clouds from the repository; every vendor also runs from the runner box, a Linux machine with the vendors' CLIs under cron that pulls `ready` tasks labeled for it. the owner's machine runs no agent.

law [[cyberia/dev]] § council and pool · home `.github` for the dispatcher and the quota ledger · properties 8, 9, 10

### 4 · control

<svg viewBox="0 0 900 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-size="12" style="font-family:inherit" fill="none" stroke="currentColor" stroke-width="1">
<defs><marker id="c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="currentColor" stroke="none"/></marker></defs>
<rect x="20" y="16" width="520" height="268" rx="8"/>
<text x="34" y="36" fill="currentColor" stroke="none" font-weight="600">ring 2 · state · the owner promotes</text>
<text x="34" y="52" fill="currentColor" stroke="none" opacity="0.8">every friday 12:00 UTC · the whole ladder from origin</text>
<text x="300" y="36" fill="currentColor" stroke="none" opacity="0.8">integration · user runs · audits · receipts</text>
<rect x="50" y="70" width="460" height="196" rx="8"/>
<text x="64" y="90" fill="currentColor" stroke="none" font-weight="600">ring 1 · rung</text>
<text x="64" y="106" fill="currentColor" stroke="none" opacity="0.8">on a merge into any part of the rung · the product and its direct dependents</text>
<text x="300" y="90" fill="currentColor" stroke="none" opacity="0.8">spec checks · kelvin drift</text>
<rect x="80" y="124" width="400" height="124" rx="8"/>
<text x="94" y="144" fill="currentColor" stroke="none" font-weight="600">ring 0 · repository</text>
<text x="94" y="160" fill="currentColor" stroke="none" opacity="0.8">every change · the repository's gates · cargo semver-checks</text>
<text x="94" y="176" fill="currentColor" stroke="none" opacity="0.8">a reviewer from another vendor in a fresh context</text>
<text x="94" y="204" fill="currentColor" stroke="none">patch stays here · minor reaches ring 1 · major reaches ring 2</text>
<text x="94" y="222" fill="currentColor" stroke="none">the ring comes from the touched files, never from the author</text>
<text x="94" y="238" fill="currentColor" stroke="none" opacity="0.8">declared bump ≥ computed bump; lower is a red gate</text>
<text x="580" y="36" fill="currentColor" stroke="none" font-weight="600">kelvin · the strategic cadence</text>
<g>
<rect x="580" y="46" width="200" height="20" rx="3"/><text x="590" y="60" fill="currentColor" stroke="none">10 cyberia</text><text x="770" y="60" fill="currentColor" stroke="none" text-anchor="end" opacity="0.7">warm</text>
<rect x="580" y="68" width="200" height="20" rx="3"/><text x="590" y="82" fill="currentColor" stroke="none">9 cyber</text>
<rect x="580" y="90" width="200" height="20" rx="3"/><text x="590" y="104" fill="currentColor" stroke="none">8 cyb</text>
<rect x="580" y="112" width="200" height="20" rx="3"/><text x="590" y="126" fill="currentColor" stroke="none">7 soft3</text>
<rect x="580" y="134" width="200" height="20" rx="3"/><text x="590" y="148" fill="currentColor" stroke="none">6 cy</text>
<rect x="580" y="156" width="200" height="20" rx="3"/><text x="590" y="170" fill="currentColor" stroke="none">5 neural</text>
<rect x="580" y="178" width="200" height="20" rx="3"/><text x="590" y="192" fill="currentColor" stroke="none">4 cybergraph</text>
<rect x="580" y="200" width="200" height="20" rx="3" stroke-width="2"/><text x="590" y="214" fill="currentColor" stroke="none">3 joy</text><text x="770" y="214" fill="currentColor" stroke="none" text-anchor="end" opacity="0.7">K declared</text>
<rect x="580" y="222" width="200" height="20" rx="3" stroke-width="2"/><text x="590" y="236" fill="currentColor" stroke="none">2 trident</text><text x="770" y="236" fill="currentColor" stroke="none" text-anchor="end" opacity="0.7">K declared</text>
<rect x="580" y="244" width="200" height="20" rx="3" stroke-width="2"/><text x="590" y="258" fill="currentColor" stroke="none">1 nox</text><text x="770" y="258" fill="currentColor" stroke="none" text-anchor="end" opacity="0.7">cold → 0K</text>
</g>
<line x1="800" y1="50" x2="800" y2="262" marker-end="url(#c)"/>
<text x="812" y="110" fill="currentColor" stroke="none" opacity="0.8">colder</text>
<text x="812" y="126" fill="currentColor" stroke="none" opacity="0.8">downward</text>
<text x="580" y="280" fill="currentColor" stroke="none" opacity="0.8">a rung is never colder than the one below</text>
<text x="580" y="294" fill="currentColor" stroke="none" opacity="0.8">a decrement below obliges a release above</text>
</svg>

the controls a change passes are decided by its blast radius, computed from the touched files through `soft3/release/components.toml` and the reverse closure of cargo dependencies. semver is the tactical cadence under a floor; kelvin is the strategic one: an integer per rung that only decreases, zero is frozen, decrements planned by quarter with graduation criteria and the owner as approver. the release train is ring 2, its rules unchanged.

law [[cyberia/dev]] § rings, § kelvin, § release train · home `soft3/release/` (`train.py`, `train_gates.py`, `components.toml`), `.github` reusable workflows for rings 0 and 1 · properties 3, 4, 5, 6, 11, 19

### 5 · merge

the merge token belongs to policy. a ring 0 change merges without the owner when every gate is green, a reviewer from another vendor approved, the blast radius is the repository, and no specification changed; anything else is labeled `decision`. the refinery is the merge queue: green batches merge, a red batch is bisected. the mayor runs daily: triage, stale changes closed with a reason and a kept branch, the queue, a one-page digest.

law [[cyberia/dev]] § merge policy · home `.github` (policy workflow, refinery, mayor) · properties 7, 15, 16, 17, 18

### 6 · boards and status

boards are renders of the graph, never a second store: the state board (the ladder: rings, red gates, decisions waiting), a product board per rung, a component board per repository filtered by owner — today an agent, later a person, to the graph one neuron. one status vocabulary everywhere: the stage of work (`draft → accepted → active → done → superseded`) and the evidence of a claim (`open → simulated → measured → proven`), `blocked` on either.

law [[cyberia/dev]] § status · home optica selections published through `cyberia.blog`, GitHub projects as a mirror at most · properties 12, 14

### 7 · the dialect and the patch

phase 1 makes the work graph a dialect of [[cybergraph]]: a task is a file, `blocks`, `discovered-from`, `claim` and `done` are typed cyberlinks signed by the agent's neuron, `ready` is an inf query, a board is an optica selection; agents write through cy headless. phase 2 replaces the pull request with the [[patch]]: one channel per task, a signed set of operations over particles and cyberlinks, conflicts as first-class data, review as a signed cyberlink to the patch, merge as the union of channels; GitHub mirrors the result.

law `fs/patch/spec.md` ([[patch]]), [[cyberia/dev]] § the work graph · home `neural` (the dialect), `fs` (the patch), `cy`, `cybergraph` · properties 21, 23, 24, 26, 27, 28

## property registry

the registry is the owner's. state is the evidence axis: `open` · `simulated` · `measured` · `proven`, `blocked` naming what blocks. each subsystem above lists its rows; evidence for rows past `open` follows the table.

| # | property | phase | state | close by |
|---|---|---|---|---|
| 1 | work graph in the repositories (beads) | 0 | open | 2026-10-14 |
| 2 | three artifacts before every merge | 0 | open | 2026-10-14 |
| 3 | ring 0 in every ladder repository | 0 | open | 2026-10-21 |
| 4 | ring 1 computed from components.toml | 0 | open | 2026-10-28 |
| 5 | ring 2 is the train over the whole ladder | 0 | measured | 2026-10-31 |
| 6 | the semver floor is a law | 0 | open | 2026-10-21 |
| 7 | the merge policy holds the ring 0 token | 0 | open | 2026-10-21 |
| 8 | council converges across four vendors | 0 | open | 2026-10-28 |
| 9 | pool spends every vendor's quota | 0 | open | 2026-10-28 |
| 10 | the reviewer is another vendor | 0 | open | 2026-10-21 |
| 11 | kelvin on nox, trident, joy; drift is red | 0 | open | 2026-10-31 |
| 12 | one status vocabulary everywhere | 0 | open | 2026-10-21 |
| 13 | context: soul, pack per rung, research | 0 | open | 2026-10-28 |
| 14 | boards rendered from the graph | 0 | open | 2026-10-31 |
| 15 | a mayor runs daily with a digest | 0 | open | 2026-10-31 |
| 16 | the refinery merges green, bisects red | 0 | open | 2026-11-07 |
| 17 | the pull request backlog is cleared | 0 | measured | 2026-10-08 |
| 18 | the launch worker runs under the loop | 0 | blocked | 2026-11-07 |
| 19 | runners: GitHub plus the owner's Mac | 0 | open | 2026-10-21 |
| 20 | GitHub issues become tasks | 0 | open | 2026-10-31 |
| 21 | the dev dialect is specified | 1 | open | 2026-11-15 |
| 22 | beads exports to cyberlinks in a minute | 1 | open | 2026-11-30 |
| 23 | agents write to the graph through cy | 1 | open | 2026-12-15 |
| 24 | the owner's boards come from the graph | 1 | open | 2026-12-31 |
| 25 | beads retired; inf answers `ready` | 2 | open | 2027-01-31 |
| 26 | a change is a patch over a channel | 2 | open | 2027-01-15 |
| 27 | review and merge are signed links | 2 | open | 2027-01-31 |
| 28 | GitHub is a mirror | 2 | open | 2027-01-31 |
| 29 | the canon index is linked from every hub | 0 | open | 2026-10-14 |
| 30 | `cyberia/goals.md` exists; dispatch orders by it | 0 | open | 2026-10-14 |
| 31 | every task carries `serves:` lineage | 0 | open | 2026-10-21 |
| 32 | the canon pass is the reviewer's first pass | 0 | open | 2026-10-21 |
| 33 | canon paths are owner-only in CODEOWNERS | 0 | open | 2026-10-14 |
| 34 | the product catalog is linted by the registry | 0 | open | 2026-10-28 |
| 35 | the seven rungs without a litepaper have one | 0 | open | 2026-12-31 |
| 36 | the contradictions below are decided | 0 | open | 2026-10-21 |

evidence:

- 5 · `soft3/release/train.py`, `train_gates.py`; candidates cut since 2026-09-25
- 13 · `ctx/build.nu` has provenance and atomic replace; the pinned list is by hand, dated 2026-09-13
- 17 · `.github/audit/pr-sweep-2026-10-07.md`
- 18 · paused since 2026-09-24 by the owner; waits for 1, 7, 9
- 26 · `fs/patch/spec.md` v0.1 written; no implementation

## decisions waiting

the inventory of 2026-10-07 found these contradictions in the canon. each is the owner's; an agent writes the proposal, the owner decides.

- D1 · civilization target: [[cyberia/foundation/strategy]] and `foundation/vision.md` say type 1; the organization profile and the soft3 rung say type 2. proposal: a sequence, type 1 is the purpose of the state on this planet, type 2 the destination of the stack.
- D2 · one mission sentence: "cyberstate, led by superintelligence" (profile, strategy) · "guided by" (cyberia.to) · "the superintelligent nation" (manifesto, whitepaper) · "a network of cities" (cyberia README). proposal: the strategy's wording everywhere; the others become aliases.
- D3 · troika and ladder: the troika is the strategic frame, the ladder the product line; soft3 is absent from the troika. proposal: rungs 1–7 and 9 belong to the cyber horse, 8 to cyb, 10 to cyberia, written into strategy § the troika.
- D4 · cyber as "the god" (profile) and "the protocol for superintelligence" (README). proposal: the profile keeps the poetry, the README is the definition, the profile links it.
- D5 · `cyberia/foundation/vision.md` speaks in the nomad-community voice of 2025; the whitepaper speaks as the nation. proposal: retire vision.md into the whitepaper's history section.
- D6 · the nox vision paper lives at `crystal/vision.md`; `cyb-014/decide/whitepaper.md` duplicates `cyb/decide/whitepaper.md` byte for byte. proposal: move the first to `nox/docs/vision.md`, delete the second.

## decisions

- 2026-10-07 · GitHub issues are an inbox, never the truth of work; a pull request is the wire of a change, never its record; boards are renders of the graph, GitHub projects a mirror at most
- 2026-10-07 · the scaffold is beads, chosen for a data model that is the shape of the dialect; export in phase 1, retirement in phase 2
- 2026-10-07 · vendors by class of work, never by loyalty: council to convergence for the important, pool until the quota is spent for the small; the reviewer is always another vendor
- 2026-10-07 · the semver floor is a law: declared bump ≥ computed bump
- 2026-10-07 · kelvin starts at nox, trident, joy; decrements planned by quarter
- 2026-10-07 · the owner's Mac stays the self-hosted runner for Metal, dmg, apk, fleet until a dedicated machine exists; every other gate on GitHub-hosted runners; spending limit zero
- 2026-10-07 · the backlog is cleared by agents under the sweep rules; in doubt, close and redo in the loop
- 2026-10-07 · in phase 2 GitHub is a mirror only; the wire is the [[patch]] of `fs/patch/spec.md`

## work log

| when | # | where | what | state |
|---|---|---|---|---|
| 2026-10-07 | 17 | .github | read-only triage of 282 open pull requests | running |
| 2026-10-07 | — | cyberia | this page; the rework of [[cyberia/dev]] | for reading |
