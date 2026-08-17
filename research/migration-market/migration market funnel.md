---
tags: cyber, research, cyberia, migration
alias: migration funnel, migration market funnel, status currencies funnel
crystal-type: diagram
crystal-domain: cyberia
date: 2026-07-27
---

# migration market funnel

one-screen render of the [[migration market model]]: 5.7B adults filtered through
aspiration and capability, sorted across the nine status currencies, and
resolving into rooting or a jurisdiction portfolio. the nomad awareness ladder
sits at the bottom. figures are model estimates, not a census.

diagram source: `diagrams/migration_funnel.py` — regenerate with
`python3 diagrams/migration_funnel.py` and paste the output between the svgbob
fence below. optica renders the fence to inline theme-adaptive SVG.

```svgbob
 +----------------------------------------------------------------------------+
 |                           WORLD ADULTS  .  5.7B                            |
 +----------------------------------------------------------------------------+
 |                  the settled 4.5B stay outside the funnel                  |
 +----------------------------------------------------------------------------+
                                        |
                                        |
                                        v
 +----------------------------------------------------------------------------+
 |                       WANT TO LEAVE  .  ~900M  [16%]                       |
 +----------------------------------------------------------------------------+
 |       gap ~500  .  survival ~170  .  trajectory ~130  .  values ~100       |
 +----------------------------------------------------------------------------+
                                        |
                                        |
                                        v
 +------------------------------------+  +------------------------------------+
 |         TRAPPED  .  ~750M          |  |           ABLE  .  ~150M           |
 +------------------------------------+  +------------------------------------+
 | barriers: access . money . skills  |->|      aspiration x capability       |
 |    removable via corridors  -->    |  |      actively preparing ~25M       |
 +------------------------------------+  +------------------------------------+
                                                            |
                                                            |
                                                            v
                    +--------------------------------------+
                    |   MOVING  .  ~25-35M PEOPLE / YEAR   |
                    +--------------------------------------+
                                        |
                                        |
                                        |
                                        |
                                        v

              NINE STATUS CURRENCIES  .  totals include dependents

 +-----------------++-----------------++-----------------++------------------+
 |   BLOOD ~1.5M   || MARRIAGE ~1.8M  ||  SPONSOR ~0.3M  ||   STUDY ~2.6M    |
 +-----------------++-----------------++-----------------++------------------+
 | birth: parents, || union by choice ||third party pays || degree as ticket |
 | kids + ancestry ||spouses,partners ||   PSR, parole   ||  5-10 yr clocks  |
 |cannot be bought ||hence sham checks||   crowdfunded   ||  $150B to unis   |
 +-----------------++-----------------++-----------------++------------------+
 +-----------------++-----------------++-----------------++------------------+
 |   LABOR ~11M    ||  SUFFERING ~7M  ||   MONEY ~0.3M   ||  IDEOLOGY 1000s  |
 +-----------------++-----------------++-----------------++------------------+
 | skill: points,  || move; ~1M grant ||capital: CBI/RBI ||   conviction:    |
 | permits, shifts || asylum, upfront || investor visas  || decree 702,visas |
 |$860B remittance ||120M stock queue ||  $20-25B / yr   ||  2024+ frontier  |
 +-----------------++-----------------++-----------------++------------------+
               +------------------------------------------------+
               |        CLUB CITIZENSHIP  .  ~4-5M / yr         |
               +------------------------------------------------+
               |    free movement: EU/EEA, ECOWAS, Mercosur,    |
               |intra-GCC, EAEU  .  inherited key = Blood -1 gen|
               +------------------------+-----------------------+
                                        |
                                        v
 +--------------+    +--------------+    +--------------+    +---------------+
 |     VISA     |    |  RESIDENCY   |    |      PR      |    |   PASSPORT    |
 +--------------+--->+--------------+--->+--------------+--->+---------------+
 |   presence   |    |living rights |    |   resident   |    |    rooting    |
 +--------------+    +--------------+    +--------------+    +---------------+
         |                                                           |
         |                                                           |
         v                                                           v
 +------------------------------------+  +------------------------------------+
 |              ROOTING               |  |    PORTFOLIO  .  the market gap    |
 +------------------------------------+  +------------------------------------+
 |     ~10M close a position / yr     |  |       60-80M open positions        |
 | stock ~200M  .  exited the market  |  |     demand maturity: N0 --> N3     |
 +------------------------------------+  +------------------------------------+
                                                            |
                                                            |
                                                            v
                                         +------------------------------------+
                                         |          + MOBILE RESERVE          |
                                         +------------------------------------+
                                         |able, not yet willing . buys options|
                                         |shock -> a wave in weeks [2022 case]|
                                         +------------------------------------+
                                        |
                                        |
                                        v

                       NOMAD SEGMENT  .  AWARENESS LADDER

 +----------------+  +----------------+  +----------------+  +----------------+
 | N0 ASLEEP ~28M |  | N1 HURTING ~8M |  |N2 SEEKING ~2-3M|  | N3 BUILD ~0.3M |
 +----------------+  +----------------+  +----------------+  +----------------+
 | visa = routine |->| risk seen now  |->|wants multi-jur |->|no-presence port|
 |  status: no Q  |  | banking, taxes |  | market = junk  |  | hand-assembled |
 | woken by shock |  |risk: false exit|  |no product/name |  |owns the method |
 +----------------+  +----------------+  +----------------+  +----------------+
   lever: shocks      lever: content       lever: method     source of method

 +----------------------------------------------------------------------------+
 |                                MONEY TRAIL                                 |
 +----------------------------------------------------------------------------+
 |      remittances $860B  .  universities $150-200B  .  CBI/RBI $20-25B      |
 |              smuggling $10B  .  sponsorship $2-5B crowdfunded              |
 |       flow: labor 11 . study 2.6 . blood+marriage 3.3 . suffering 7        |
 |    . club 4.5 . money 0.3 . irregular 2.5 . nomad churn 2.5  =  25-35M     |
 +----------------------------------------------------------------------------+
```
