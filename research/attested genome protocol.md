---
tags: cyber, research, cyberia, migration
alias: attested genome, genome attestation, kinship proof
crystal-type: research
crystal-domain: cyberia
date: 2026-07-27
---

# attested genome protocol

**v0.2 · working spec**
*Changelog: v0.2 — concordance proof sketched. v0.1 — initial spec.*

A protocol for proving eligibility claims — kinship, ancestry, citizenship — without anyone surrendering the underlying data. It makes the blood/ancestry lane of the [[migration market model]] provable without a central registry.

---

## Core idea

Today a [[genetics|genome]] is a static file a lab hands you once, and citizenship is a stamp one bureaucracy owns. Both are single points of trust and single points of failure.

Here both become **living records built from independent attestations over time**. Nobody holds a master database. Labs attest to what they physically observed. States attest to who they recognize. Users — each a [[neuron]] holding its own keys — decide what predicate to prove to whom. Everything else is [[homomorphy|homomorphic]] and [[zero knowledge]] machinery, the same crypto stack cyber already runs.

---

## Actors

| Actor | Role | Never sees |
|---|---|---|
| **User** | holds raw genome + secrets; initiates queries; pays per query | — |
| **Lab** | sequences a physically present subject, [[signature|signs]] an attestation over the resulting commitment | other labs' data |
| **State** | attests citizenship of subjects; publishes policies as computable predicates | raw genomes |
| **Compute network** | evaluates encrypted predicates, produces proofs | plaintext genome, plaintext policy weights (if private) |

No actor is trusted individually. Trust is the intersection of independent attestations.

---

## Objects

**Genome record.** Not a file — an accumulating set of attestations bound to one commitment (in cyber terms a [[particle]] the record commits to, with spent queries tracked in a [[mutator set]]):

```
C   = Commit(G; r)                      // user-held genome, user-held blinding
Aᵢ  = Sign_labᵢ( C ‖ subject_binding ‖ panel_version ‖ timestamp ‖ concordance_proof )
```

A user may upload their own genome first (self-asserted, weight 0). Each subsequent lab that physically observes the subject re-sequences and proves **concordance** with the existing commitment — that the sample it drew matches the record already anchored. The record's strength is a function of the number of independent attestors, their reputation, and the time spread between attestations.

This is the key move: a genome is not verified once, it **accrues verification**. Colluding with one lab buys nothing when the policy demands k independent attestations separated in time.

**Citizenship record.** Structurally identical, different attestor — this is the same act a [[cyberia/protocol/services|Cyberstate Protocol]] state performs when `identity.issue_passport` mints a citizenship credential, and what the [[marketplace]] prices when it sells citizenship as a non-fungible spot asset:

```
Aₛ = Sign_state( C_subject ‖ status ‖ validity_window )
```

A state attesting "this commitment belongs to a citizen of ours" is doing exactly what a lab does for biology: signing an observation it is authoritative over. Nothing more is asked of it, and nothing about the citizen's genome is disclosed to it.

**Policy.** A predicate published and committed to by whoever grants the right:

```
P = Commit( f, θ, panel_version, min_attestations, attestor_whitelist )
```

Examples:
- `IBD_total(G, G_j) ≥ 1700 cM ∧ Aₛ(j) valid` — grandparent-degree kinship to a recognized citizen
- `IBD_total(G, G_j) ≥ 200 cM ∧ …` — third-cousin degree, ancestry-track equivalent
- `proj_W(G) ∈ Region ∧ …` — population-level predicate, only defensible where continental resolution applies (post-slavery restoration cases)

Policies are versioned and public by default. Auditability beats secrecy: hidden thresholds leak to adaptive probing anyway, and a policy nobody can audit is a policy nobody should trust.

---

## Proof of concordance

The operation every re-attestation depends on: a lab that just sequenced a physically present subject must prove its sample matches the anchored commitment — without learning the genome, and without the user revealing it.

**Identity panel, not the genome.** Concordance runs over a fixed, versioned panel of ~100 neutral SNPs — chosen for high heterozygosity and deliberately screened to be forensically minimal: no medically informative loci, no ancestry-informative markers. A hundred such sites individuate a human at ~10⁻³⁰ collision probability, so nothing beyond the panel ever needs to enter the protocol.

**Fuzzy, because sequencing is noisy.** Genotyping error runs ~0.1–1% per site, so the predicate can never be equality. It is a bounded Hamming distance:

```
concordant ⟺ d_H( panel(G), panel(G') ) ≤ t        // t sized to error rate, not to relatedness
```

Threshold matters in both directions: too tight and honest re-sequencing fails, too loose and a close relative passes as the same person. Siblings differ across a neutral panel far more than replicate runs of one sample, so the gap is comfortable — but it must be calibrated on empirical replicate data, not assumed.

**Two implementations, pick by trust model:**

- *Fuzzy extractor (non-interactive).* At anchoring, the user publishes helper data `h = SecureSketch(panel(G))`. A later lab reproduces the stable key from its own read plus `h`, and signs with it. No interaction with the user, no ZK circuit — the lab's ability to derive the key *is* the proof. Cost: `h` leaks entropy about the panel, which is why the panel must be neutral by construction.
- *2PC on the distance (interactive).* User holds `panel(G)`, lab holds `panel(G')`; a garbled circuit or OT-based protocol outputs one bit: distance ≤ t. On 100 markers this is milliseconds. Leaks nothing but the bit, at the cost of the user being online.

**What cryptography cannot prove here.** That the biological sample came from the person claiming it, and was drawn now. Both are chain-of-custody problems: biometric binding at draw time, and a protocol-issued nonce the lab must incorporate at collection so an attestation cannot be replayed from an old or third-party sample. Sample substitution remains the cheapest attack on the whole system — which is precisely why the design demands several independent attestors over time rather than one perfect one.

---

## Flow

1. **Anchor.** User commits to their genome; keeps `G, r`.
2. **Accrue.** Labs that physically sample the user sign attestations of concordance. The record hardens over time.
3. **Recognize.** States sign citizenship attestations over the commitments of their nationals — building, in aggregate, a queryable set of anchored citizens without a central registry.
4. **Publish.** A state publishes policies: which predicate, which threshold, how many attestations, which attestors count.
5. **Query.** A user pays to evaluate a policy against the network. Linear parts (projections, kinship scores) run in CKKS; set-based kinship (IBD windows) runs as private set intersection returning cardinality only; the threshold comparison switches to [[tfhe|TFHE]] and yields a single encrypted bit.
6. **Prove.** The user receives a [[proof]] — a zheng-style zero-knowledge proof the verifier checks without learning anything but the outcome:

```
π = ZK{ ∃ G, r, {Aᵢ} :
        C = Commit(G;r)
      ∧ |{Aᵢ}| ≥ min_attestations ∧ attestors ⊆ whitelist
      ∧ f_θ(G, ·) = 1
      ∧ nullifier = H(C ‖ policy_id) }
```

The verifier learns: this human satisfies this policy, once. Nothing else.

---

## Why this shape

**Attestation beats custody.** Every existing design asks who should hold the database. This one has no database to hold — only signed claims about observations, distributed among the parties already authoritative over them.

**Kinship over ethnicity.** The defensible predicate is relatedness to a specific recognized person, not similarity to a reference panel. Panels are conventions assembled by committees; centimorgans are physical facts. This also collapses the normative question — a state defines only its own citizenry, which it already does.

**[[sybil attacks|Sybil]] resistance for free.** A genome is a natural unique identifier. `nullifier = H(C ‖ policy_id)` makes one human one application, per policy, without identity documents. The same primitive generalizes to proof-of-unique-personhood far beyond migration — a biological complement to stake- and [[karma]]-based defenses.

**A market in policies.** Once predicates are computable and provable, jurisdictions compete by publishing better ones, and users shop across them. Eligibility stops being a bureaucratic secret and becomes a queryable surface.

---

## Limits and honest failure modes

- **Physical binding is the weak point.** Everything rests on labs correctly binding a biological sample to a subject. Multi-attestation raises the cost of forgery but never to infinity. This layer, not the cryptography, is where the protocol will actually be attacked.
- **Relatives never consented.** A genome discloses information about siblings, children, cousins. No threshold scheme fixes this; it is a property of the medium.
- **Adaptive querying leaks.** Each honest bit is information. Rate-limit via nullifiers, pin thresholds and panel versions, add calibrated noise before comparison.
- **Endogamy breaks fixed thresholds.** Ashkenazi, Finnish, Icelandic and other bottlenecked populations show inflated background relatedness; thresholds must be calibrated per population or the predicate produces false positives at scale.
- **IBD has a horizon.** Reliable to roughly five or six generations. Beyond it, segments vanish into noise — which happens to match the depth ancestry law actually cares about.
- **Dual use.** A national network of anchored kinship claims is also a forensic instrument of unusual power. That is the strongest political argument against building it, and it deserves a direct answer rather than a footnote.

---

## Open questions

- [ ] Attestor reputation: how is lab weight assigned, revoked, and slashed?
- [ ] Concordance: empirical calibration of `t` on replicate data; panel neutrality audit; entropy budget for published helper data
- [ ] Threshold decryption ceremony between user and state — who runs it, what happens on abort
- [ ] Verifiable FHE vs. moving the decisive computation entirely into ZK
- [ ] Query pricing and its effect on adaptive-probing economics
- [ ] Governance of policy publication: what stops a jurisdiction from encoding a discriminatory predicate
