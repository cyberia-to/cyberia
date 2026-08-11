---
tags: cyber, cyberia, cryptography, article
crystal-type: entity
crystal-domain: cyberia
alias: ephemeris, ephemerides
icon: "🛰️"
---
# ephemeris

the known trajectory of a body through time. given a body's orbital elements, an ephemeris returns its position at any moment, so the distance between two bodies — and the round-trip light-time between them — is a computable function of time rather than a measured mystery.

the [[space doctrine]]'s two-level coordinate system runs on it. the local frame of a body X is co-moving and self-calibrated by X's circumference, so a geohash there is time-invariant; the ephemeris supplies the second level, the transform between X's frame and Earth's, as a public function of time. observed Earth↔X round-trip time is checked against the ephemeris exactly as a declared `c_medium` is checked in [[location proof]] — a claim that fails to match the predicted geometry is rejected.

three properties make it a trustless input:

- observable, not institutional. an orbit is measured by anyone who watches the sky over time, the same footing as axiom A3's known circumference. no registrar declares it.
- verifiable. any node recomputes a body's position from its published elements and confirms the round-trip time it sees is consistent. faking presence at X means reproducing X's whole moving round-trip curve over time, not a single number — so the dynamics strengthen [[sybil attacks|Sybil]] resistance rather than weakening it.
- uncertainty-priced. a well-observed planet has a tight ephemeris; a freshly-discovered asteroid has a loose one. that uncertainty widens the round-trip tolerance band and so lowers the grounding coefficient $g(X,t)$ the [[space doctrine]] scales a world token's mint by — an unsure orbit grounds a weaker economy until it is pinned down.

each body's orbital elements live in the graph as [[particles]], refined by observation and finalized like any other fact through [[foculus between planets|foculus]]. through a conjunction blackout the inter-frame transform is predicted from the ephemeris rather than measured — the local frame is untouched, and only inter-frame settlements wait.

see [[location proof]] for the coordinate construction and [[space doctrine]] for the economy the ephemeris helps ground.
