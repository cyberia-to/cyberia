---
tags: cyber, cyberia, article
crystal-type: pattern
crystal-domain: cyberia
alias: space doctrine, colonization doctrine, doctrine of space colonization
icon: "🪐"
---
# space doctrine

the conventional law of space is finders-keepers: whoever physically lands and uses a world holds it. this doctrine rejects that. a world is claimed first by the economy that prices it, the proofs that program the path to it, and the design that models it. physical arrival vests those claims — it does not originate them. the map, the market, and the model reach the planet before the lander does.

three factors invert the balance of power, and each is a lever [[cyberia]] can pull today, from Earth, before a single engine lights.

## why finders-keepers fails

occupation-based ownership makes space a pure rocket-and-capital race: the winner is whoever has the most launch capacity, and terrestrial hierarchy reproduces itself in orbit. worse, it is economically dead on arrival — value cannot be coordinated across light-minutes by any voting or longest-chain [[consensus]], so an occupied world has no working market until it is large enough to run one alone. the conventional doctrine hands the frontier to whoever already has the biggest booster, and then strands them without an economy when they get there.

## lever 1 — local currencies, quotable before landing

each world mints its own token. the token of world X is a distinct [[currency]] with its own conservation domain: it is emitted only against the [[impulse]] $\Delta\phi^+$ created inside X's anchored [[reward specification|reward]] subgraph, so it can never be printed for free, and cross-world value moves through market price rather than a shared mint. $CYB and the [[century index]] remain Earth's reference numéraire; $X floats against them.

per-world tokens are feasible only under convergence [[consensus]]. quoting a currency across light-minutes needs continuous cross-frame price reconciliation, and a committee that votes by interplanetary post decides nothing. [[foculus between planets|foculus]] does it: each world is its own pond, settling locally at local speed, reconciling only the shared boundary, safe through the two-week conjunction blackout. this is the foculus factor — convergence, not coordination, is what lets many worlds hold their own money and still quote each other.

so a currency exists before colonization. in the speculative phase the token mints slowly, backed by the semantic substrate of lever 3, and its exchange rate to Earth is discovered by the cross-frame market from day zero. a world has a priced economy before anyone stands on it.

## lever 2 — proof of location programs pre-physical incentives

[[location proof]] lets ownership and settlement incentives be written as code before physical arrival. the token's emission at X is scaled by a grounding coefficient $g(X,t)$ tied to the verifiable density of the location mesh at X: a floor while X is pure speculation, a knee at the first self-consistent proof, a ramp as the local mesh thickens past its cold-start threshold.

early anchored contributions escrow a homestead claim that vests when the first proof lands, so building the pre-economy is a stakeable investment and the first physical prover triggers the settlement that pays the armchair builders who came before. boots-on-ground and map-makers are aligned by one event rather than set against each other.

the design cannot outrun the physics. because $g$ tracks the verifiable resolution of the mesh — the distance-to-baseline ratio and the minimum node count [[location proof]] derives — the large multiplier cannot be minted faster than a real local mesh exists. the Moon grounds from Earth almost at once; Mars grounds only once Mars carries its own honest mesh; a fake landing pumps nothing. incentive is programmable ahead of arrival, and un-gameable past it.

## lever 3 — simulation as pre-colonization value

what to build on a world — modeled, played, tested — is valuable before anyone is there. a simulation of X is [[impulse]] anchored to X: terrain and resource models, construction plans, city layouts, energy and life-support loops, stressed in-sim until they hold. this is the same civilization stack [[cyber valley]] assembles on Earth, authored for another world first as a game.

a good simulation de-risks the real build and mints X's token in its speculative phase. the game is the pre-economy: designing X produces the substrate, lever 1 prices it, lever 2 vests it when the first lander proves the ground. the loop closes — model, market, proof — and it runs entirely before departure.

## the two-level coordinate system

a planetary system is dynamic, so the doctrine mandates two coordinate levels rather than one.

- local frame — co-moving with body X, self-calibrated by X's own circumference (axiom A3 of [[location proof]], generalized to A3(X)). a geohash here is time-invariant: a Martian holds a stable surface address while Mars orbits. semantics, property, and the token's anchor all live at this level.

- inter-frame transform — the map between X's frame and Earth's is a publicly computable function of time given by the [[ephemeris]]. observed Earth↔X round-trip time is checkable against it without trust, exactly as `c_medium` is; the dynamics strengthen [[sybil attacks|Sybil]] resistance, because a forger must reproduce a moving target's whole round-trip curve over time, not one number. ephemeris uncertainty folds into $g$. through blackout the transform is predicted from the ephemeris rather than measured — the local frame is untouched, and only inter-frame settlements wait, the correct [[foculus between planets|foculus]] behavior.

ownership takes the shape the frame allows. a solid body carries a geohash homestead. a flowing medium — a ring in Keplerian shear, a wind-driven atmosphere — carries no fixed-parcel title but an orbital-slot or flow-rate anchor instead. a gas giant, having no static frame, carries only vehicle-bound claims, never land. property is as real as the frame beneath it.

## relativism — the blunt solution

frames keep their own proper time, and within a frame no relativistic correction is needed — intra-frame drift is negligible. for ordering events across frames the doctrine adopts one canonical coordinate time, barycentric, tied to Earth's clock, and converts each frame's timestamps into it using corrections read from the same [[ephemeris]] that gives positions, so no new trust enters.

the blunt part is a guard band. relativistic clock drift between inner-system frames runs at microseconds per day, while interplanetary consensus granularity — the per-signal [[VDF]] delay plus light-time — runs at seconds to minutes. so fix a guard band of at least one second, which swamps the drift by orders of magnitude: two cross-frame events closer than the band are declared concurrent and must commute, and only events separated by more than the band take a definite order. this is provably safe because the band exceeds the worst-case drift, it costs nothing because [[vec|VEC]] already requires signals to commute, and it can be sharpened later without changing anything above it holds now.

## what this doctrine claims

a world belongs first to those who priced it, proved the path to it, and designed it. the lander triggers the claim rather than creating it. the frontier is won from Earth, in the market and the proof and the model, and the rocket arrives to vest what the graph already knows.

see [[location proof]] for the proof primitive, [[foculus between planets]] for the consensus that crosses the distance, [[reward specification]] for the mint the world tokens localize, [[your share of the sun]] for the vision at the end of it, and [[cyber valley]] for the civilization stack authored first as a game.
