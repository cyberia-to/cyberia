---
tags: cyber, cyberia, cip, cryptography, article
crystal-type: entity
crystal-domain: cyberia
alias: proof of location, geolocation proof, location proof, anchor-free geolocation, RTT geolocation
---
# location proof

a protocol for cryptographically verifiable [[proof]] of physical location that requires no trusted anchors, no GPS, no certificate authorities, and no institutional hierarchy. the construction rests on four irreducible axioms and combines three primitives: the canonical signal propagation speed of the transmission medium, [[verifiable delay functions]], and [[Merkle]] causal clocks. a [[network]] of nodes measuring pairwise Round Trip Times self-organizes into a globally consistent 3D coordinate space through multidimensional scaling, calibrated to Earth's known circumference without external reference. honest geolocation reporting is a [[dominant strategy]] [[equilibrium]] when relay fees are latency-weighted, making geographic honesty economically self-enforcing without explicit [[cryptographic proof]] [[verification]]

## axioms

the entire construction rests on exactly four assumptions:

```
A1. I exist.
    (Cogito ergo sum — the irreducible act of observation.)

A2. Signal propagation speed is bounded by a canonical
    constant c_medium, known per medium and publicly verifiable.
    (Physics. Not negotiable.)

A3. Earth is a sphere of known circumference.
    (~40,075 km. Observable. Not an institutional claim.)

A4. At least one honest observer exists in the mesh.
    (Sybil bound. Weaker than any existing PKI assumption.)
```

no other assumptions are made. no trusted third parties. no known anchor positions. no GPS satellites. no IANA. no RIR. no certificate authorities.

## the problem

the existing internet addressing stack conflates two orthogonal concepts:

- identity — who you are
- location — where you are physically

an IP address encodes both simultaneously. this architectural error, present since 1973, produces a fragile hierarchy: IANA → RIR → AS → ISP → user. every layer is a point of control, censorship, and failure.

the correct separation:

```
pubkey    →  WHO   (permanent, cryptographic, self-sovereign)
geohash   →  WHERE (dynamic, physical, verifiable)
```

previous attempts at proof of location (Helium, FOAM) failed because they required trusted anchor nodes whose physical positions were declared by institutional fiat — reintroducing the same trust hierarchy they sought to replace. this protocol eliminates that requirement entirely.

## core primitives

### canonical signal propagation speed

different transmission media propagate signals at different but known and publicly verifiable speeds:

```
Vacuum / Starlink laser links:  c_vac  ≈ 299,792 km/s
Air / 5G mmWave:                c_air  ≈ 299,000 km/s
Fiber optic:                    c_fib  ≈ 200,000 km/s
Copper:                         c_cop  ≈ 200,000 km/s
```

each node declares its link medium. the declared `c_medium` is itself verifiable by the mesh — a node claiming fiber speeds on a Starlink link will exhibit RTTs inconsistent with its declared medium, providing an additional consistency check.

when medium is unknown or untrusted, the protocol uses a conservative lower bound:

```
c_min = c_fib ≈ 200,000 km/s
```

this ensures distance bounds are never underestimated.

### RTT as distance bound

Round Trip Time between two nodes A and B, over a medium with canonical speed `c_medium`, establishes a hard physical upper bound on their distance:

```
RTT(A, B) ≥ 2 × dist(A, B) / c_medium

therefore:

dist(A, B) ≤ RTT(A, B) × c_medium / 2
```

this bound cannot be violated. a relay attack — inserting a proxy between A and B — only increases RTT, never decreases it. therefore:

> a node can only prove itself farther from another node than it claims, never closer.

faking proximity is physically impossible regardless of transmission medium. this asymmetry is the foundational security property of the entire protocol.

### VDF — time cannot be compressed

a [[verifiable delay functions|verifiable delay function]] `VDF(x, t)` produces an output that requires sequential computation time `t` to produce, but can be verified instantly. applied to location challenges:

- node issues `challenge = VDF(timestamp, seed)`
- responding node cannot pre-compute the response before receiving the challenge
- eliminates pre-computation attacks where a node prepares fake responses in advance

### Merkle causal clock

RTT measurements from multiple nodes must be causally linked to prevent reordering attacks. this is a form of [[logical clock]]:

```
proof = MerkleNode(
  RTT_1 || RTT_2 || RTT_3 || ... || RTT_n,
  c_medium_declarations,
  timestamp,
  pubkey_N
)
```

the causal chain makes it impossible to selectively present favorable measurements while discarding inconsistent ones. all measurements and medium declarations are committed simultaneously.

## relative location: anchor-free construction

### distance matrix from pairwise RTTs

given N nodes measuring pairwise RTTs, construct a distance matrix D where each entry is normalized to its declared medium:

```
D[i][j] = RTT(i, j) × c_medium(i,j) / 2
```

where `c_medium(i,j)` is the canonical speed of the link between nodes i and j, conservatively estimated when unknown. this matrix encodes the complete relative [[geometry]] of the [[network]].

### multidimensional scaling

from D alone — no known positions — classical Multidimensional Scaling (MDS) recovers a 3D coordinate embedding that preserves all pairwise distances. the solution is unique up to rotation, reflection, and translation.

```
D  →  MDS  →  {P_1, P_2, ..., P_N} ∈ ℝ³
```

for routing purposes, rotation and reflection are irrelevant — only relative distances matter. translation ambiguity is the only remaining degree of freedom.

### Earth as self-calibrating constraint

the translation ambiguity is resolved by Earth itself. the planet's circumference (~40,075 km) encodes directly into the maximum observable RTT, scaled by the fastest available medium:

```
Via fiber:    max RTT ≈ 2 × 20,037 km / 200,000 km/s ≈ 200ms
Via Starlink: max RTT ≈ 2 × 20,037 km / 299,792 km/s ≈ 134ms
```

as Starlink and other vacuum/near-vacuum links proliferate, the upper bound tightens — improving location precision globally. once the mesh is globally distributed, the spherical [[geometry]] of Earth forces a unique embedding. the coordinate system self-calibrates to Earth's scale from the canonical propagation speeds and the physical reality of the planet's size — no GPS, no external reference.

### Sybil resistance

a [[sybil attacks|Sybil]] node claiming position G must present RTTs consistent with G to all existing nodes simultaneously, across all declared media:

```
Honest node in Bali (fiber):
  RTT(Singapore) ≈ 20ms   c_fib  ✓
  RTT(Tokyo)     ≈ 70ms   c_fib  ✓
  RTT(London)    ≈ 180ms  c_fib  ✓
  → consistent with Bali in 3D embedding

Sybil claiming Bali from Moscow (fiber):
  RTT(Singapore) ≈ 160ms  c_fib  ✗
  RTT(Tokyo)     ≈ 140ms  c_fib  ✗
  RTT(London)    ≈ 60ms   c_fib  ✗
  → inconsistent, rejected by MDS

Sybil claiming Bali from Moscow (falsely claiming Starlink):
  declared c_medium = c_vac
  RTT(Singapore) ≈ 160ms  expected ≈ 13ms  ✗
  → medium declaration inconsistent, rejected
```

faking consistency with a dense global mesh is physically impossible regardless of medium. falsely declaring a faster medium only makes inconsistency more detectable.

## absolute location: observer bootstrap

### the observer as origin

relative [[geometry]] is sufficient for routing. but absolute location (a geohash mappable to Earth's coordinate system) provides additional value: human-readable addresses, geographic filtering, physical proximity assertions.

absolute location can be bootstrapped from a single observer invoking Axiom A1:

```
Observer O declares: I exist at position P_0
O measures RTTs to N neighbors across available media
Mesh grows outward
Spherical constraint (A3) forces unique embedding
P_0 anchors the translation degree of freedom
```

this is not a trusted anchor in the traditional sense. O makes no claim that others must verify institutionally. O simply asserts their own existence as observer — irreducible under A1 — and the physical consistency of the mesh propagates outward.

### orientation resolution

the final ambiguity is orientation (which direction is North). resolvable by:

1. two observers who physically meet and agree on orientation
2. sun position + time of day (observable, no external trust)
3. [[consensus]] among bootstrap nodes on a canonical orientation convention

any of these is sufficient. the choice does not affect security properties.

## dynamic location updates

unlike IP addresses, geohash-based node IDs are dynamic — a node that moves updates its claimed position. the protocol handles this naturally:

```
1. Node broadcasts new geohash claim G_new with updated c_medium
2. Existing neighbors re-measure RTTs on available links
3. MDS re-runs locally around the moving node
4. New position confirmed or rejected by mesh consistency
5. Merkle clock records position transition causally
```

a node switching from fiber to Starlink mid-session updates its declared `c_medium` and the mesh re-verifies consistency automatically. mobile nodes are first-class citizens. location is not an identity — it is a continuously verified physical fact.

## off-Earth: the calibrating sphere generalizes, the baseline does not

Axiom A3 names Earth, but nothing in the construction is special to Earth. A3 reads generally: the host body is a sphere of known, observable circumference. any body — the Moon, Mars, a spun-up station — calibrates its own local frame the same way, from its own circumference and the canonical `c_medium`. so A3 generalizes to A3(body), and a mesh sitting on any single body self-locates internally exactly as on Earth.

what does not generalize for free is verifying a node on one body from a mesh on another. that is governed by a single ratio:

```
ρ = R / B      (distance to target) / (available baseline)
```

trilateration transverse resolution is `δ · R / B`, where `δ = c_medium × timing precision` is the range-measurement error. for a lone node off Earth, the only baseline available is Earth's own diameter — effectively the near-hemisphere span facing the target, B ≈ 12,742 km. at microsecond timing, δ ≈ 0.3 km:

```
body   distance R        R / B      transverse error   verdict
Moon   ~384,400 km       ~30        ~9 km              locatable by the existing Earth mesh
Mars   ~5.5×10⁷ km (opp) ~4,300     ~1,300 km          ≈ planetary radius — hemisphere at best
Mars   ~2.25×10⁸ km      ~17,700    ~5,300 km          exceeds Mars's radius — a local mesh is required
```

the crossover for an Earth-only baseline sits near 10⁸ km: a node stays pinnable from Earth while `δ · R / B` stays below the body's radius. the Moon is deep inside that bound; Mars straddles it at opposition and falls outside it the rest of the orbit.

### the Moon is provable now

a single lunar node is locatable to kilometer scale by the [[network]] already on Earth — no separate lunar mesh, no lunar cold start. the Moon is simply an external point of the Earth-anchored frame, its position expressed in the coordinates Earth's sphere already calibrated. building a high-precision lunar frame eventually wants the Moon's own circumference as A3(Moon), but the first node does not need it.

forgery is caught by signal shape. an Earth-bound node adding delay to claim a lunar position produces a near-field RTT-differential signature across the Earth stations — strongly curved, hyperbolic, betraying a near source. a genuine lunar node, far compared to the baseline, produces a far-field signature — a near-planar gradient pointing toward the Moon. a dense mesh separates the two, and the honest Earth mesh satisfies A4 already, so the lunar claim is checkable the moment it is made.

### Mars is the first-proofs case

at Martian distance both a genuine node and an Earth-bound forger look far-field, and the transverse resolution falls below the planet's own radius — so the Earth mesh can neither pin a Mars-surface geohash nor refute a delayed forgery. Mars needs its own local mesh, with short baselines near the target and its own A3(Mars) calibration. that reintroduces open problem 1 on Mars: below the minimum density N_min the local MDS geometry is underdetermined, and A4 read as at least one honest observer on Mars is not yet satisfiable. until that Martian mesh exists, a Mars-surface position can be spoofed by an Earth node inflating its own RTT, and nothing local contradicts it. proving where you are on Mars begins by proving there are enough of you there.

### binding two frames

once a body carries its own self-calibrated mesh — A3(body) plus a local honest observer — the Earth↔body RTT supplies a coarse inter-frame bound. RTT proves a node farther, never closer, so the link establishes the remote mesh is at least ρ light-time away, consistent with the body's orbit and ruling out an Earth-local forgery of the whole mesh. the two self-calibrated frames bind into one solar-system coordinate system, joined by the propagation-speed bound across the gap, each still resolving its own surface internally at local-baseline precision. see [[foculus between planets]] for how consensus, rather than location, crosses those same distances, and [[space doctrine]] for the two-level coordinate system and the economy this proof grounds.

## economic enforcement: the honest [[equilibrium]]

### latency-weighted relay fees

if relay fees are proportional to inverse latency:

```
fee = k / latency
```

then honest geolocation reporting becomes a [[dominant strategy]]:

```
Node claims G_claimed, actual position G_real.

If G_claimed = G_real:
  routing sends traffic that physically passes near node
  → actual relay latency matches declared c_medium
  → high fees earned

If G_claimed ≠ G_real:
  routing sends traffic routed via claimed position
  → actual relay path is suboptimal for declared medium
  → higher latency, lower fees
  → honest nodes outcompete on every route
```

### medium honesty as additional constraint

nodes that falsely declare a faster medium (e.g. claiming Starlink speeds on fiber) face double punishment:

- RTT inconsistency detected by mesh → position claim rejected
- even if undetected, actual relay latency exceeds declared medium expectation → lower fees

honest medium declaration is also a [[dominant strategy]].

### [[dominant strategy]] [[equilibrium]]

this is stronger than a [[nash equilibrium]]. honesty — both of position and medium — maximizes relay income regardless of what other nodes do:

```
∀ strategies S of other nodes:
  U(honest | S) ≥ U(lie | S)
```

the physical RTT measurements act as a continuous, decentralized oracle enforcing the [[equilibrium]]. no explicit [[verification]] of geohash claims is needed. the market enforces geographic honesty automatically.

### consequence

geographic honesty is economically self-enforcing. the protocol does not need to verify location claims cryptographically in steady state — continuous latency measurement by the relay market does it for free.

## full protocol summary

```
SETUP
  Nodes declare transmission medium and c_medium
  Nodes measure pairwise RTTs continuously
  VDF prevents pre-computation of challenge responses
  Merkle clock orders all measurements and declarations causally

RELATIVE LOCATION (anchor-free)
  Distance matrix D constructed from RTT mesh, normalized by c_medium
  MDS recovers 3D coordinate embedding
  Earth's circumference self-calibrates the scale
  Faster media (Starlink) improve precision
  Sybil resistance: consistency with global mesh across all media

ABSOLUTE LOCATION (observer bootstrap)
  One observer asserts: I exist at P_0  (A1)
  Translation ambiguity resolved
  Orientation resolved by physical observation or convention

DYNAMIC UPDATES
  Moving nodes and medium switches re-verify continuously
  Merkle clock records transitions causally

ECONOMIC ENFORCEMENT
  Relay fees ∝ 1/latency
  Honest position and medium reporting is dominant strategy
  No explicit cryptographic location verification needed in steady state
```

## what this replaces

| current stack | this protocol |
|---|---|
| IANA → RIR → AS → ISP | physics + mesh [[consensus]] |
| IP address (identity + location conflated) | pubkey (identity) + geohash (location) |
| DNS hierarchy | content-addressed naming |
| BGP (political routing) | RTT-optimal routing |
| trusted anchors | Earth's [[geometry]] |
| institutional [[sybil attacks]] resistance | physical RTT consistency |
| GPS (US military infrastructure) | canonical c_medium + MDS |
| single medium assumption | multi-medium aware (fiber, Starlink, 5G) |

## open problems

1. cold start — minimum mesh density N_min required for reliable MDS embedding. below this threshold the [[geometry]] is underdetermined.

2. adversarial MDS — behavior when a coordinated [[sybil attacks|Sybil]] cluster controls a geographic region. formal bounds needed.

3. medium [[verification]] — protocol for nodes to verify each other's declared `c_medium` without trusted hardware attestation.

4. heterogeneous paths — RTT over a path with mixed media (fiber + Starlink hop) requires per-segment `c_medium` estimation. conservative lower bound may introduce systematic bias.

5. fee mechanism design — exact fee function shape for robust [[dominant strategy]] [[equilibrium]] under various [[network]] topologies and medium mixtures.

6. integration with pubkey identity layer — binding geohash [[proof|location proofs]] to persistent cryptographic identities (e.g. Ed25519 keypairs) without re-introducing trusted registrars. see [[cyber/identity]].

7. Starlink constellation dynamics — satellite positions change continuously. inter-satellite laser links have variable routing paths affecting RTT. protocol must handle dynamic `c_medium` paths gracefully.

8. off-world extension — A3 generalizes to any host body of known circumference, but the Earth baseline pins only targets inside the `δ · R / B` crossover (~10⁸ km): the Moon is locatable now, Mars needs its own local mesh and inherits the cold-start bound of open problem 1. formal treatment needed for the inter-frame RTT bound that binds two self-calibrated meshes, and for near-field vs far-field forgery detection as a function of mesh density. see the off-Earth section above.

## conclusion

four axioms. three primitives. zero trusted institutions.

the [[geometry]] of physical space, the canonical propagation speeds of transmission media, and the irreducible fact of the observer's existence are sufficient to construct a globally consistent, [[sybil attacks|Sybil]]-resistant, dynamically updatable [[proof]] of physical location — across fiber, Starlink, 5G, and any future medium. geographic honesty is enforced not by [[cryptography]] but by economic gravity — lying about your location or your medium makes you a worse router and earns you less.

this is the missing layer beneath the pubkey identity revolution. without verifiable location, decentralized routing remains dependent on the same institutional hierarchies it seeks to replace. with it, the full stack — identity, location, content, routing — can be rebuilt from first principles.

see [[cyber/proofs]] for the complete proof taxonomy, [[cyber/communication]] for delivery proofs over the relay [[network]], [[storage proofs]] for content persistence guarantees, [[cyber/security]] for formal security analysis