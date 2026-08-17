---
tags: cyberia, protocol, space, land, property, geometry
alias: space accounting, spatial ownership, volume title, double ownership, 3d cadastre
crystal-type: pattern
crystal-domain: cyberia
---
# space accounting

a short whitepaper on exclusive ownership of three-dimensional space.

**what.** a protocol invariant: in a named frame, two exclusive claims do not occupy the same volume at the same time. claims are [[TSP-2]] Cards whose identity includes a solid; ownership of the Card is who may transfer and lease it; exclusive occupation of the solid is what makes the Card a *title in space*, not a sticker on an id.

**why.** graph edges and `owner_count(id) = 1` stop double *token* ownership. they do not stop double *place* ownership. without a geometry invariant, two Cards can name overlapping ground — the failure mode of every paper and most digital land registries. markets, cities, and off-world settlement all need the second invariant before the first is worth much.

built on [[TSP-2]], [[marketplace]] (time), [[location proof]] and [[space doctrine]] (frames), [[services]] (land verbs). presentation lives in [[cyb]] / [[mir]] / Bevy and is never authority. intellectual debt to Galt Project's double-ownership analysis (polygon exclusivity + deposit challenge); this note generalizes it to 3D frames and the soft3 stack.

→ related: [[marketplace-spec]] calendars · [[land rights agreement]] · [[century index]]

---

## 1 · the problem

### 1.1 three contracts of a place

any durable society over land rests on roughly three contracts (Galt):

1. **rules** — who may do what  
2. **property accounting** — who has exclusive claim on which region of space  
3. **budgets** — how protection and commons are funded  

cyberia already designs (1) as workflows and (3) as community / marketplace cashflows. (2) is incomplete: [[services]] models `land.buy` as moving a TITLE edge; [[TSP-2]] guarantees one owner per Card id. neither says *this volume is not already titled*.

### 1.2 double ownership

**double ownership of space** = two exclusive claims whose solids intersect in the same frame (and, if timed, in the same interval).

state registries fail here not for lack of maps but for lack of *code*: a human can insert a conflicting record; the conflict is a court case. blockchain registries that only store "token #42 owned by A" import the same hole — uniqueness of id is not uniqueness of place.

land and built volume are special among assets: they **physically exclude**. two parcels cannot share the same coordinates. that is a mathematical property. algorithms can enforce absolute consistency of a spatial registry if solids are explicit and intersection is checked.

### 1.3 what soft3 already solves (and does not)

| already | does not |
|---|---|
| one owner per Card id ([[TSP-2]]) | exclusive volume per frame |
| no double-book **time** on an asset ([[marketplace]] calendar) | no double-book **space** among assets |
| who is where as a **node** ([[location proof]]) | who owns a **region** of a manifold |
| pre-physical homestead intent ([[space doctrine]]) | post-mint cadastral topology |
| spectral 3D viz of the graph ([[mir]]) | physical / game / planetary geometry |

[[bevy]] in [[cyb]] is the shell (window, input, world switch). [[mir]] paints the knowledge graph in spectral R³. neither is a cadastre. space accounting is a **state** layer; engines are **views**.

---

## 2 · principles

1. **geometry is identity, not metadata.** a title without a solid is a social label; a solid without exclusive check is a drawing.  
2. **frames before coordinates.** every solid lives in a named frame (Earth WGS84, body-local, virtual map). no cross-frame ownership without explicit transform + policy ([[space doctrine]]).  
3. **two conservations.** id: `owner_count(id) = 1`. space: exclusive solids in a frame are pairwise disjoint (over overlapping validity intervals).  
4. **pair challenges beat global scans.** full "new solid vs all" is off-chain or side; on-chain (or proven) kernel checks **pairs** — deposit-backed (Galt option 2).  
5. **hierarchy is containment.** children ⊆ parent; siblings exclusive. split/merge are pure geometry ops inside parent bounds.  
6. **time is orthogonal.** exclusive *when* is the marketplace calendar on a fixed SpaceClaim id; exclusive *where* is this protocol.  
7. **presentation is not authority.** Bevy entities, mir particles, map JSON are snapshots of committed claims — never the registry.

---

## 3 · model

### 3.1 frame

```text
Frame {
  id:     FrameId
  kind:   EarthWGS84 | BodyLocal(body) | Virtual(map_id) | GraphSpectral  // last = viz only, no titles
  basis:  geodetic | metric-local | abstract
  parent: Option<FrameId>
}
```

property and settlement live in **local** frames. inter-frame maps use [[ephemeris]]-style public transforms where needed; speculative claims on world X vest when [[location proof]] grounds that frame ([[space doctrine]]).

### 3.2 solid (geometry ladder)

ledger primitives stay simple enough to check deterministically:

| level | form | role |
|---|---|---|
| L0 | AABB / OBB | spatial index, reject |
| L1 | **Prism** — 2D ring × [z₀, z₁] | land plots, floors, rooms (default) |
| L2 | finite union of L1 | buildings, packages |
| L3 | mesh / voxels / SDF | content only; **hash** on Card, not full intersect on mint |

**Prism** (canonical Earth and city case):

```text
Prism {
  ring:  [(x, y); n]   // closed, simple; WGS84 lon/lat or local meters
  z0, z1: Real         // height band; z1 ≥ z0
}
```

intersection of two exclusive claims:

1. project rings to a plane (Mercator for lon/lat, identity for local meters)  
2. 2D polygon intersection (Weiler–Atherton / Martinez–Rueda class)  
3. height intervals overlap  

land-only titles may set z-band to "full column" policy; rooms use tight bands (Galt). free-form 3D (caves, orbital hulls) upgrade to L2 convex pieces under the same challenge rules.

### 3.3 SpaceClaim (TSP-2 Card)

```text
SpaceClaim {
  id:           CardId
  frame:        FrameId
  solid:        Solid              // L1 or L2
  content_hash: Hash               // optional L3 topology / BIM / media (IPLD)
  rights:       Title | Lease | Easement | Air | Subsurface | …
  valid:        Option<[t0, t1]>   // None = perpetual until burn
  parent:       Option<CardId>     // nesting
  deposit:      Coin               // challenge bond
}
```

**rights types** modulate exclusivity:

- **Title** — full exclusive solid  
- **Lease** — exclusive for `valid` (or calendar windows via [[marketplace]])  
- **Easement / Air / Subsurface** — typed non-title layers; may share XY with different z or different right class under explicit rules  

default product for cyber valley plots: **Title** prism + optional lease windows on the same id.

### 3.4 invariants

for all committed exclusive claims `C, D` in frame `F`:

```text
(I1)  owner_count(C.id) = 1                         // TSP-2
(I2)  if exclusive(C) ∧ exclusive(D) ∧ C ≠ D
        ∧ time_overlap(C.valid, D.valid)
        then  solid(C) ∩ solid(D) = ∅
(I3)  if C.parent = P  then  solid(C) ⊆ solid(P)
(I4)  split(P → A, B):  A ∪ B ⊆ P  ∧  A ∩ B = ∅
(I5)  challenge(A, B) is pure, deterministic on solids
```

(I2) is the space-accounting invariant. everything else is plumbing.

---

## 4 · enforcement

### 4.1 why not full on-chain "vs all"

checking **one prism against one prism** is bounded. checking **one against unbounded N** does not fit L1 gas or light clients. design for:

- **index off-chain / heavy node** — R-tree / BVH over L0 AABBs; `query_overlap(solid) → [ids]`  
- **pair check on consensus path** — pure function `intersects(a, b) → bool` (Rust now; nox jet later)  
- **economic completeness** — anyone can submit a colliding pair and claim deposits  

### 4.2 mint path

```text
propose(solid, rights, parent?, deposit)
  → local/oracle index: no known overlap
  → mint SpaceClaim Card, lock deposit
  → open challenge window (continuous if deposit remains)
```

oracles (cadastral / multi-party) may co-sign mint for UX; they **do not replace** deposits. dishonest mint still loses bond when a pair challenge lands.

### 4.3 challenge path (primary)

```text
challenge(id_a, id_b)
  → load solids, verify intersects(a, b)
  → if true: burn claim with later commitment time (or lower priority rule);
             pay challenger from that claim's deposit;
             slash mint co-signers if any
  → if false: slash challenger's bond
```

this is Galt's deposit hybrid, stated as the default. oracles-at-mint and sidechain-vs-all remain optional accelerators, not the sole root of trust.

### 4.4 multi-registry

private registries, oracle registries, and curated registries may coexist. **shared challenge contract** (or shared proof object in the graph) is how the plane stays one exclusive map: claims that opt in post deposit and become challengeable across registries. registries that spam fake space can be voted offline without erasing honest deposits — squatting defense (Galt).

### 4.5 time

[[marketplace]] slot calendar: on a fixed SpaceClaim id, bookings are intervals; allocate fails on time overlap. that is exclusive **use** along t. space accounting is exclusive **extent** along x,y,z. compose:

```text
full exclusive occupation = solid exclusive ∧ time exclusive
```

sublease of parcel-time (hak sewa style) is marketplace on the Title Card, not a second overlapping Title.

---

## 5 · hierarchy and operations

| op | geometry | cards |
|---|---|---|
| **mint** | solid free in frame (and ⊆ parent if any) | create Card + deposit |
| **split** | partition parent into disjoint children ⊆ parent | mint children; burn or package parent |
| **merge** | union of siblings ⊆ common parent hull | burn parts; mint whole |
| **transfer** | unchanged solid | TSP-2 update owner |
| **lease** | unchanged solid; set valid or open calendar | mint Lease Card or marketplace issuance |
| **burn** | free the solid | return residual deposit if unchallenged |

survey error and crustal motion are **update** workflows (oracles / arbitration), not silent solid mutation — same spirit as Galt token data change.

---

## 6 · presentation (soft3)

```text
authority     graph + TSP-2 + SpaceIndex + challenge
capability    [[ward]] gates mint / challenge / transfer
present       optional Bevy WorldState::SpaceMap
              prysm / sugarloaf for title UI
              mir remains spectral graph only
```

**SpaceMap** (if built in [[cyb]]):

- loads committed claims for a frame  
- ECS holds a **visible set** of solids (frustum), not the registry  
- pick → Card id → rights UI  
- edit → propose solid → mint flow  

mirrors mir's VisibleParticle pattern: engines show snapshots; epochs of truth are graph commits.

---

## 7 · relation to cyber valley and space doctrine

| context | frame | solid | social layer |
|---|---|---|---|
| cyber valley plots | Earth WGS84 | plot prism; room bands later | PT PMA / hak sewa off-chain + optional on-chain Title |
| terra nullius / frontier | Earth or local | auctioned prisms | community budget = protection ([[services]] / communities) |
| moon / mars | BodyLocal(X) | homestead solid or geohash cell | vest when location mesh grounds X |

on-chain land registry remains gated by legal wrappers where states exist; the **geometry invariant** is still worth running as private registry + challenge so digital claims stay consistent among participants who opt in.

---

## 8 · non-goals

- replacing state BPN / cadastre by force  
- GPS as sole oracle of title (location proof is for **agents**, not for parcel topology)  
- storing full BIM meshes as the exclusive-check primitive  
- putting titles inside Bevy `Transform` or mir spectral positions  
- perfect global vs-all on every L1 block  

---

## 9 · implementation order

1. **spec** — this document; Prism + intersects + invariants (I1–I5)  
2. **kernel** — pure Rust `prism_intersect`, R-tree index (seed from [[cyberia-my]] geometry if useful)  
3. **ledger v0** — mint + deposit + pair challenge (log or CosmWasm / PLUMB)  
4. **CV maps** — import Phase-0 plot rings as proposed claims; run offline overlap audit  
5. **marketplace hook** — calendar on SpaceClaim id for sublease  
6. **SpaceMap view** — Bevy world, read-only then propose  
7. **nox jet** — proven intersects for challenge path  
8. **multi-registry** — shared challenge object  

---

## 10 · one sentence

**space accounting is the invariant that exclusive volume Cards in a frame are pairwise disjoint (over time windows), enforced by deterministic pair geometry plus deposit challenges — id ownership stays TSP-2, time exclusivity stays marketplace, engines only render what the graph already committed.**

---

## see also

- Galt Project whitepaper — [galtproject-docs/whitepaper/en/Whitepaper.md](https://github.com/galtproject/galtproject-docs/blob/master/whitepaper/en/Whitepaper.md) (double ownership, WGS84, deposit challenge)  
- [[TSP-2]] · [[marketplace]] · [[marketplace-spec]] · [[services]] · [[location proof]] · [[space doctrine]] · [[mir]] · [[cyb]]
