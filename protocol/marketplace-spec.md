---
tags: cyberia, system, marketplace, spec
alias: marketplace spec, marketplace-spec
crystal-type: spec
crystal-domain: cyberia
---
# marketplace spec

contract interfaces, data structures, state schemas, message types, and cross-contract sequences for the marketplace protocol.

for economic rationale, product overview, and phasing see [[cyberia/protocol/marketplace]].

---

## data model

### Asset

one cw-asset instance per physical or logical asset.

```rust
Asset {
    owner: Addr,
    meta_ipfs: Multihash,

    kind: Slot | Spot | Hybrid,
    claim_fungibility: Fungible | NonFungible,
    capacity: Capacity,

    cap_rate_bps: u16,                      // r_gross × 10_000; set at creation
    tier_curves: Map<u32, BondingCurve>,    // horizon_hours → curve
    audiences: Vec<Audience>,

    // oracle inputs
    // GROSS_REVENUE_LOG: Map<u64, RevenueSample>  — stored separately in contract state
    // ACTIVE_ISSUANCES: Set<Addr>                 — tracked for pipeline computation

    sale_offer: Option<SaleOffer>,
}

Capacity {
    Schedule(BTreeMap<u64, Booking>),       // Slot + NF: interval list
    RateCap(u64),                           // Slot + F: max units per period
    TierCounts(Map<u32, (u32, u32)>),       // Spot + NF: (current, cap) per tier
}

SaleOffer {
    reserve_price: Uint128,
    premium_bps: u16,
}

RevenueSample {
    amount: Uint128,
    kind: ClaimSale | PreemptionPremium | TierUpgrade | SubscriptionStream,
}
```

### Issuance

one cw-issuance instance per event, visa round, or production batch.

```rust
Issuance {
    asset: Addr,
    creator: Addr,

    status: IssuanceStatus,

    window_start: u64,                      // hours since unix epoch
    window_duration: u32,                   // hours; for F = batch validity period

    meta_ipfs: Multihash,
    audiences_snapshot: Vec<Audience>,      // frozen at submit; immutable after

    deposit_locked: Uint128,
    networth: Uint128,                      // accumulated revenue; split on close

    // NF-specific
    base_price: Option<Uint128>,
    categories: Option<Vec<Category>>,

    // F-specific
    supply_cap: Option<u64>,
    supply_minted: Option<u64>,
    coin: Option<Addr>,                     // cw-coin address; set after Approve
}

IssuanceStatus {
    Submitted,
    Approved,
    Declined,
    Open,                                   // F only: cw-coin live, minting active
    Cancelled,
    Closed,
    Expired,                                // F only: after valid_until
}

Category {
    id: u8,
    name: String,
    base_price: Uint128,
    discount_bps: u16,
    cap: u32,
    sold: u32,
}

ClaimClass {
    Guaranteed,
    Flexible { premium_bps: u16 },          // premium paid to preempted holder
}
```

state machines:
```
NF:  Submitted → Approved → Closed
         └→ Declined
         └→ Cancelled  (from Submitted or Approved)

F:   Submitted → Approved → Open → Closed → Expired
         └→ Declined
         └→ Cancelled  (from Submitted or Approved)
```

### Claim (NF)

stored as cw721 extension on cw-claim global contract.

```rust
ClaimExt {
    asset: Addr,
    issuance: Option<Addr>,

    valid_from: Option<u64>,                // hours since epoch; None = instant activation
    valid_until: Option<u64>,              // None = perpetual
    tier: u32,
    category_id: Option<u8>,
    audience_id: u8,
    price_paid: Uint128,

    class: ClaimClass,
    transferable: bool,                     // false = soulbound
    revoked: bool,
    redeemed: bool,

    meta_ipfs: Option<Multihash>,
}
```

### Claim (F)

balance on a cw-coin contract. no per-unit record.

```rust
CoinConfig {
    asset: Addr,
    issuance: Addr,
    tier: u32,
    audience_id: u8,
    class: ClaimClass,

    name: String,
    symbol: String,
    decimals: u8,

    supply_cap: u64,
    supply_minted: u64,
    valid_from: u64,
    valid_until: u64,

    minter: Addr,                           // = the issuance contract
}
```

### Audience

```rust
Audience {
    id: u8,
    name: String,
    discount_bps: u16,
    gate: AudienceGate,
}

AudienceGate {
    Open,
    Operator,                               // v1: bot signs on behalf of buyer
    Allowlist(Addr),                        // v4: membership contract query
    Badge(Addr, TokenId),                   // v6: buyer holds specific credential NFT
}
```

---

## oracle

### annual_GR

```rust
fn annual_gr(now_h: u64) -> Uint128 {
    let realized: Uint128 = GROSS_REVENUE_LOG
        .range(now_h.saturating_sub(8760)..now_h)
        .map(|(_, s)| s.amount)
        .sum();

    let pipeline: Uint128 = ACTIVE_ISSUANCES
        .iter()
        .filter_map(|addr| load_issuance(addr))
        .filter(|i| {
            i.window_start >= now_h
                && i.window_start < now_h + 8760
                && matches!(i.status, Approved | Open)
        })
        .map(|i| i.networth)
        .sum();

    realized + pipeline
}
```

pipeline is committed revenue (already paid, already recorded in issuance.networth) from approved issuances whose windows fall in the forward 12 months.

### V_implied

```rust
fn implied_valuation(now_h: u64) -> Uint128 {
    let gr = annual_gr(now_h);
    if gr.is_zero() { return Uint128::zero(); }
    gr.multiply_ratio(10_000u128, asset.cap_rate_bps as u128)
}
```

returns zero for new assets with no history. auto-listing falls back to reserve_price.

### current_ask

```rust
fn current_ask(now_h: u64) -> Option<Uint128> {
    let offer = asset.sale_offer.as_ref()?;
    let v = implied_valuation(now_h);
    let with_premium = v + v.multiply_ratio(offer.premium_bps as u128, 10_000u128);
    Some(max(offer.reserve_price, with_premium))
}
```

None when sale_offer is None: asset not for sale.

---

## pricing stack

four layers applied to every claim purchase:

```rust
fn final_price(
    tier_curve: &BondingCurve,
    utilization_bps: u32,       // (slots used / total cap) × 10_000
    audience: &Audience,
    category: Option<&Category>,
    qty: u64,
) -> Uint128 {
    let base = tier_curve.price_at(utilization_bps);
    let discount = max(
        audience.discount_bps,
        category.map(|c| c.discount_bps).unwrap_or(0),
    );
    base * (10_000 - discount as u128) / 10_000 * qty as u128
}
```

discount: one discount per claim, max of category and audience, not additive.

bonding curve v1: piecewise linear.
```
curve = [(supply_0, price_0), (supply_1, price_1), ...]
price_at(u) = linear interpolation over supply breakpoints
```

continuous curves (constant product, exponential) in v2.

---

## calendar (Slot + NF)

base unit: 1 hour. interval list, not per-hour bitmap. one booking = one storage write regardless of duration. overlap check = two B-tree lookups.

```rust
SCHEDULE: Map<u64 /* start_hour */, Booking>

Booking { start_hour: u64, end_hour: u64, issuance: Addr }

fn allocate(start: u64, duration: u32, issuance: Addr) -> Result<()> {
    let end = start + duration as u64;
    if let Some((_, b)) = SCHEDULE.range(..=start).rev().next() {
        if b.end_hour > start { return Err("overlap with left neighbor"); }
    }
    if let Some((_, b)) = SCHEDULE.range(start..).next() {
        if b.start_hour < end { return Err("overlap with right neighbor"); }
    }
    SCHEDULE.save(start, Booking { start_hour: start, end_hour: end, issuance });
    Ok(())
}

fn free(start: u64) {
    SCHEDULE.remove(start);
}
```

invariants enforced at allocate time:
```
duration ≥ asset.min_duration_hours
start    ≥ now_h + asset.cancel_lead_hours
start    ≤ now_h + asset.max_horizon_hours   // e.g. 8760 = 1 year forward
```

---

## tier counts (Spot + NF)

```rust
TIER_COUNTS: Map<u32 /* tier */, (u32 /* current */, u32 /* cap */)>

fn allocate_tier(tier: u32) -> Result<()> {
    let (curr, cap) = TIER_COUNTS.load(tier)?;
    require!(curr < cap, "tier at capacity");
    TIER_COUNTS.save(tier, (curr + 1, cap));
    Ok(())
}

fn release_tier(tier: u32) {
    TIER_COUNTS.update(tier, |(curr, cap)| (curr - 1, cap));
}
```

tier escalation (upgrade without re-issuance):

```rust
fn escalate_claim(token_id: TokenId, new_tier: u32, sender: Addr) -> Result<()> {
    let claim = CLAIM_EXT.load(token_id)?;
    require!(claim.owner == sender, "not holder");
    require!(new_tier > claim.tier, "must escalate, not downgrade");
    let delta = tier_price(new_tier).checked_sub(claim.price_paid)?;
    usdt.transfer_from(sender, self_addr, delta)?;
    release_tier(claim.tier);
    allocate_tier(new_tier)?;
    CLAIM_EXT.update(token_id, |c| ClaimExt { tier: new_tier, price_paid: c.price_paid + delta, ..c });
    RecordRevenue(delta, TierUpgrade);
    Ok(())
}
```

---

## non-fungible flows

### submit issuance (slot event)

```
shaman → registry.CreateIssuance {
    asset, window_start, duration_hours,
    categories, deposit
}
   ├─ instantiate cw-issuance(asset, ...) → addr I
   ├─ I.submsg: asset.Allocate(window_start, duration_hours, I)
   ├─ I.submsg: usdt.TransferFrom(shaman → I, deposit)
   ├─ registry: claim.AddMinter(I)
   └─ registry indexes I
```

Allocate fails if window overlaps an existing booking → CreateIssuance rolls back.

### submit issuance (spot visa round)

```
authority → registry.CreateIssuance {
    asset, tier, cap,
    window_duration, deposit
}
   ├─ instantiate cw-issuance(asset, ...) → addr I
   ├─ asset: ACTIVE_ISSUANCES.insert(I)
   ├─ registry: claim.AddMinter(I)
   └─ registry indexes I
```

### buy claim (NF)

```
buyer → issuance.BuyClaim {
    category_id, audience_id, qty,
    class, max_price
}
   ├─ resolve audience from audiences_snapshot
   ├─ final = final_price(curve, utilization, audience, category, qty)
   ├─ require final ≤ max_price
   ├─ require category.sold + qty ≤ category.cap
   ├─ submsg: usdt.TransferFrom(buyer → issuance, final)
   ├─ submsg: claim.Mint(buyer, ClaimExt { asset, issuance, tier, ... })
   ├─ if Spot: submsg asset.IncrementTier(tier, qty)
   ├─ category.sold += qty
   ├─ networth += final
   └─ submsg: asset.RecordRevenue(final, ClaimSale)
```

### preempt flexible claim (phase 6)

```
new_buyer → issuance.PreemptFlexible { token_id }
   ├─ require claim.class == Flexible
   ├─ compensation = claim.price_paid × (1 + flexible_premium_bps / 10_000)
   ├─ new_price = current ask for this tier / category
   ├─ require funds_attached ≥ compensation + (new_price − claim.price_paid)
   ├─ submsg: usdt.Transfer(compensation → original holder)
   ├─ submsg: usdt.Transfer(incremental → issuance)
   ├─ submsg: claim.TransferNft(token_id → new_buyer)
   ├─ claim.price_paid = new_price
   ├─ networth += incremental
   └─ emit ClaimPreempted
```

### close issuance (NF)

```
operator → issuance.Close
   ├─ require status == Approved
   ├─ require now_h > window_end (slot) OR operator discretion (spot round)
   ├─ split networth: dao_bps + master_bps + provider_bps = 10_000
   ├─ submsg: usdt.Transfer(provider_share → asset.owner)
   ├─ submsg: usdt.Transfer(dao_share → dao_addr)
   ├─ submsg: usdt.Transfer(deposit_locked → creator)
   ├─ submsg: asset.Free(window_start)           // slot
   │  OR submsg: asset.DecrementTier(tier, sold) // spot
   ├─ submsg: asset.RecordRevenue(networth, ClaimSale)
   └─ status = Closed
```

---

## fungible flows

### submit fungible issuance

```
operator → registry.CreateIssuance {
    asset, kind: Fungible,
    supply_cap, window_start, window_duration,
    base_curve, deposit
}
   ├─ instantiate cw-issuance(asset, ...) → addr I
   ├─ I.submsg: usdt.TransferFrom(operator → I, deposit)
   └─ registry indexes I
```

### approve fungible issuance

```
operator → I.Approve
   ├─ status: Approved → Open
   ├─ submsg: instantiate cw-coin {
   │      asset, issuance: I, supply_cap,
   │      valid_from: window_start,
   │      valid_until: window_start + window_duration,
   │      minter: I,
   │  } → addr C
   ├─ I.coin = C
   └─ asset: ACTIVE_ISSUANCES.insert(I)
```

### mint units (F)

```
buyer → I.MintUnits { qty, audience_id, max_price }
   ├─ price = curve.integrate(supply_minted, supply_minted + qty)
   ├─ apply audience discount
   ├─ require price ≤ max_price
   ├─ require supply_minted + qty ≤ supply_cap
   ├─ submsg: usdt.TransferFrom(buyer → I, price)
   ├─ submsg: cw-coin.Mint(buyer, qty)
   ├─ supply_minted += qty
   ├─ networth += price
   └─ submsg: asset.RecordRevenue(price, ClaimSale)
```

bonding curve for N units: `price = ∫[s → s+N] f(x) dx` where f(x) is the curve function and s = supply_minted.

### redeem units (F)

```
operator → I.Redeem { holder, qty, evidence }
   ├─ require status == Open
   ├─ require now_h ∈ [valid_from, valid_until]
   ├─ submsg: cw-coin.BurnFrom(holder, qty)
   └─ emit CoinRedeemed { holder, qty, asset, evidence }
```

evidence is a free-form delivery receipt ID, weighbridge ticket, or API call reference. paper trail only — off-chain fraud prevention is the asset's responsibility.

### close fungible issuance

```
automatic at valid_until   OR   operator → I.Close
   ├─ if supply_minted > redeemed: submsg cw-coin.BurnRemaining
   ├─ split networth
   ├─ submsg: usdt.Transfer(provider_share → asset.owner)
   ├─ submsg: usdt.Transfer(dao_share → dao_addr)
   ├─ submsg: usdt.Transfer(deposit_locked → creator)
   ├─ submsg: asset.RecordRevenue(networth, ClaimSale)
   └─ status = Closed
```

### what fungible flows omit (intentional)

| feature | reason absent |
|---|---|
| Categories | units are units; no "early bird gravel" subdivisions |
| Guaranteed / Flexible class | cannot preempt a cubic meter already sold |
| calendar overlap check | bulk delivery is continuous, not slot-bookable |
| per-claim extension record | claims are balances, not identities |
| secondary preemption market | secondary trading is standard cw20 transfer |

---

## contracts

### cw-registry (1 instance)

factory, address book, minter grant for cw-claim.

```
ExecuteMsg:
  CreateAsset {
      kind, claim_fungibility, cap_rate_bps,
      meta_ipfs, audiences
  }                                          # OPERATOR
  CreateIssuance {
      asset, window_start, window_duration,
      categories?, supply_cap?, base_curve?,
      deposit
  }                                          # any neuron OR OPERATOR
  GrantOperator { addr }                     # OPERATOR
  RevokeOperator { addr }                    # OPERATOR

QueryMsg:
  Assets { start_after, limit }
  Issuances { start_after, limit }
  IssuancesByAsset { asset, start_after, limit }
  IssuancesByCreator { creator, start_after, limit }
  IsOperator { addr }

State:
  CONFIG {
      asset_code_id, issuance_code_id,
      claim_addr, coin_code_id,
      usdt_addr, dao_addr,
      dao_bps, master_bps
  }
  OPERATORS: Set<Addr>
  ASSETS: Vec<Addr>
  ISSUANCES: Vec<Addr>
  ASSET_BY_OWNER: Map<Addr, Vec<Addr>>
  ISSUANCE_BY_ASSET: Map<Addr, Vec<Addr>>
  ISSUANCE_BY_CREATOR: Map<Addr, Vec<Addr>>
```

### cw-asset (N instances)

per-asset state. variant selected at instantiate from `kind × claim_fungibility`.

```
ExecuteMsg (all variants):
  UpdateMeta { meta_ipfs }
  SetAudiences { audiences }
  SetTierCurve { horizon_hours, curve }
  SetSaleOffer { reserve_price, premium_bps }
  ClearSaleOffer
  BuyAsset { }                               # attach funds ≥ current_ask
  TransferOwnership { new_owner }            # OPERATOR only
  RecordRevenue { amount, kind }             # active issuance only
  RecordConsumption { qty }                  # active issuance only (F)

ExecuteMsg (Slot + NF only):
  Allocate { start_hour, duration_hours, issuance }
  Free { start_hour }

ExecuteMsg (Spot + NF only):
  IncrementTier { tier, by, issuance }
  DecrementTier { tier, by }
  SetTierCap { tier, cap }
  EscalateClaim { token_id, new_tier }

QueryMsg:
  Config
  Audiences
  TierCurve { horizon_hours }
  CurrentAsk
  ImpliedValuation
  GrossRevenue { window_hours }
  Utilization { tier? }
  Calendar { from_hour, to_hour }            # Slot + NF only
  TierCounts                                 # Spot + NF only

State:
  CONFIG, AUDIENCES, TIER_CURVES, SALE_OFFER
  GROSS_REVENUE_LOG: Map<u64, RevenueSample>
  ACTIVE_ISSUANCES: Set<Addr>
  SCHEDULE: Map<u64, Booking>               # Slot + NF only
  TIER_COUNTS: Map<u32, (u32, u32)>         # Spot + NF only
```

### cw-issuance (N instances)

per-issuance state. lifecycle and revenue tracking.

```
ExecuteMsg (NF):
  UpdateMeta { meta_ipfs }                   # creator while Submitted
  AddCategory { category }                   # creator while Submitted
  UpdateCategory { id, updates }             # creator while Submitted
  Approve                                    # OPERATOR
  Decline { reason }                         # OPERATOR
  Cancel { reason }                          # OPERATOR or creator while Submitted
  Close                                      # OPERATOR
  BuyClaim {
      category_id, audience_id, qty,
      class, max_price
  }
  PreemptFlexible { token_id, new_buyer }    # phase 6

ExecuteMsg (F):
  UpdateMeta { meta_ipfs }                   # creator while Submitted
  UpdateCurve { curve }                      # creator while Submitted
  Approve                                    # OPERATOR; instantiates cw-coin
  Decline { reason }                         # OPERATOR
  Cancel { reason }                          # OPERATOR or creator while Submitted
  Close                                      # OPERATOR or automatic at valid_until
  MintUnits { qty, audience_id, max_price }
  Redeem { holder, qty, evidence }           # OPERATOR

QueryMsg:
  Config
  Status
  Networth
  AudiencesSnapshot
  Categories                                 # NF
  Buyers { start_after, limit }              # NF
  Coin                                       # F: returns cw-coin address
  Supply                                     # F: (cap, minted, redeemed)
  CurveAt { supply }                         # F: price at given supply level

State:
  CONFIG
  STATUS: IssuanceStatus
  AUDIENCES_SNAPSHOT: Vec<Audience>
  DEPOSIT_LOCKED: Uint128
  NETWORTH: Uint128
  CATEGORIES: Vec<Category>                  # NF
  BUYERS: Map<Addr, Vec<TokenId>>            # NF
  COIN_ADDR: Option<Addr>                    # F
  SUPPLY_MINTED: u64                         # F
  CURVE: BondingCurve                        # F
```

### cw-claim (1 instance, global cw721)

unified non-fungible claim store. cw721 base + ClaimExt.

```
ExecuteMsg:
  Mint { to, ext: ClaimExt }                 # active NF issuance only (MINTER role)
  TransferNft { recipient, token_id }        # standard cw721
  SendNft { contract, token_id, msg }        # standard cw721
  Approve { spender, token_id, expires }     # standard cw721
  Revoke { spender, token_id }               # standard cw721
  ApproveAll { operator, expires }           # standard cw721
  RevokeAll { operator }                     # standard cw721
  Redeem { token_id }                        # OPERATOR: marks redeemed
  RevokeToken { token_id, reason }           # OPERATOR: marks revoked
  AddMinter { addr }                         # registry only
  RemoveMinter { addr }                      # registry only

QueryMsg:
  OwnerOf, Approval, Approvals, AllOperators # cw721 standard
  NumTokens, ContractInfo, NftInfo, AllNftInfo
  Tokens, AllTokens
  ClaimInfo { token_id }                     # returns ClaimExt
  ClaimsByAsset { asset, start_after, limit }
  ClaimsByIssuance { issuance, start_after, limit }
  ClaimsByOwner { owner, start_after, limit }
  IsRedeemed { token_id }
  IsValid { token_id, at_hour? }             # checks revoked, redeemed, valid_until

State:
  cw721_base
  CLAIM_EXT: Map<TokenId, ClaimExt>
  MINTERS: Set<Addr>
```

### cw-coin (N instances, per fungible batch)

cw20-base with supply cap enforcement, time-bounded validity, single-minter.

```
ExecuteMsg:
  Transfer { recipient, amount }             # cw20 standard
  Send { contract, amount, msg }             # cw20 standard
  Burn { amount }                            # cw20 standard
  BurnFrom { owner, amount }                 # cw20 standard (via allowance)
  IncreaseAllowance, DecreaseAllowance       # cw20 standard
  TransferFrom                               # cw20 standard (via allowance)
  Mint { recipient, amount }                 # minter only; enforces supply_cap
  ExpireSupply                               # callable after valid_until; burns remainder

QueryMsg:
  Balance, TokenInfo, Allowance, AllAllowances   # cw20 standard
  Minter
  ValidityWindow                             # (valid_from, valid_until)
  SupplyCap
  SupplyMinted

State:
  cw20_base
  MINTER: Addr
  SUPPLY_CAP: u64
  VALIDITY: (u64, u64)                       // (valid_from, valid_until)
```

instantiated by cw-issuance on Approve. one instance per (issuance, tier, audience_id, class) combination.

### cw-bridge-eth + cw-usdt

threshold attestation model. k-of-n independent relayers must confirm before any mint or withdrawal executes. there is no single-attestor mode.

```
cw-bridge-eth:
  InstantiateMsg:
    attestors: Vec<Addr>,
    threshold: u32,                              // k in k-of-n; e.g. 3 of 5

  ExecuteMsg:
    Attest { eth_tx_hash, recipient, amount }    // any attestor; idempotent per (attestor, tx)
    Withdraw { bostrom_sender, eth_recipient, amount }  // relayers co-sign off-chain, submit here
    AddAttestor { addr }                         // admin; raises n
    RemoveAttestor { addr }                      // admin; must keep n > threshold
    UpdateThreshold { new_k }                    // admin; must keep k ≤ n

  QueryMsg:
    Config                                       // (attestors, threshold)
    AttestationStatus { eth_tx_hash }            // (confirmations_so_far, minted)
    PendingWithdrawals

  State:
    CONFIG { attestors: Set<Addr>, threshold: u32 }
    ATTESTATIONS: Map<EthTxHash, Set<Addr>>      // which attestors confirmed each tx
    PROCESSED_TX: Set<EthTxHash>                 // finalized; idempotency guard
    PENDING_WITHDRAWALS: Map<TxId, WithdrawalRequest>

  Invariants:
    // mint triggers only when ATTESTATIONS[tx].len() >= threshold
    // each attestor can confirm a tx at most once
    // threshold update rejected if new_k > current n
```

mint flow:
```
relayer_i → Attest { eth_tx_hash: H, recipient: R, amount: A }
   ├─ require sender ∈ ATTESTORS
   ├─ require H ∉ PROCESSED_TX
   ├─ require ATTESTATIONS[H] does not already contain sender
   ├─ ATTESTATIONS[H].insert(sender)
   ├─ if ATTESTATIONS[H].len() < threshold: return Ok (not yet)
   └─ else:
       ├─ PROCESSED_TX.insert(H)
       ├─ submsg: cw-usdt.Mint(R, A)
       └─ emit Minted { eth_tx_hash: H, recipient: R, amount: A }
```

withdrawal flow (burn on bostrom → pay on ETH):
```
holder → cw-usdt.Burn { amount, eth_recipient }
   ├─ cw20 burn reduces supply
   ├─ emit WithdrawalRequested { bostrom_sender, eth_recipient, amount, id }
   └─ relayers observe event off-chain, co-sign payout, execute ETH transfer
```

```
cw-usdt (cw20):
  ExecuteMsg:
    cw20 standard (Transfer, Send, Burn, BurnFrom, etc.)
    Mint { recipient, amount }                   // bridge only
    Burn { amount, eth_recipient: String }        // holder withdrawal initiation
  State:
    cw20_base
    BRIDGE: Addr                                 // only address that can call Mint
```

---

## decisions confirmed

- denomination: bridged USDT only
- bridge: threshold k-of-n attestation from deployment; no single-key mode
- buyer authentication: bot provides custodial signing as a UX convenience; contracts accept any valid signed tx; user-controlled signing via [[cyberia/cw-cyber-passport]] when ready
- discount stacking: max(category, audience); not additive
- audience gate: Operator (bot-enforced via telegram group) as initial gate; on-chain allowlist and badge gates available in the same contract from deployment
- registry: single instance; factory + index
- claim representation NF: global cw721 cw-claim with ClaimExt
- claim representation F: cw-coin per (issuance, tier, audience_id, class)
- calendar granularity (NF Slot): 1 hour; interval list storage, O(log N) overlap check
- oracle formula: GIM approach — annual_GR / r_gross; r_gross absorbs OPEX expectations per asset class (see cap rate table in [[cyberia/protocol/marketplace]])
- GR window: trailing 12m realized + forward 12m committed pipeline
- V_implied = 0 for new assets with no revenue history; auto-listing shows reserve_price — correct behavior, not a missing feature
- auto-listing: max(reserve_price, V_implied × (1 + premium_bps / 10_000))
- claim classes NF: both Guaranteed and Flexible supported from deployment; operators choose which to offer per issuance
- preemption compensation: price_paid × (1 + flexible_premium_bps)
- pricing discovery: bonding curve seeds liquidity; limit-order book overlay as later enhancement; curve IS the AMM for F flows
- fungible supply expiry: automatic burn at valid_until
- combinatorial auction: separate module; not required for protocol correctness

## decisions deferred (genuinely open, not simplifications)

- exact dao_bps and master_bps for revenue split — DAO governance decision
- cap_rate_bps defaults per class — DAO config; indicative r_gross table in [[cyberia/protocol/marketplace]]
- initial bridge attestor set and threshold k — operational decision before deploy (minimum: 3-of-5)
- bridge fee on mint — possibly ε for treasury, not required for correctness
- whether seed tier_curves are required or owner may disable them
- tier escalation refund rules for spot downgrades
- whether spot tier-capacity changes grandfather existing holders
- bonding curve shape for F: piecewise linear vs exponential — empirical question; both are correct
- fungible coin cross-audience transfer — risk of audience-bypass arbitrage requires explicit policy decision

---

discover all [[concepts]]
