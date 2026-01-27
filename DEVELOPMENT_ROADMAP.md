# Development Roadmap: Next Phase

## Decision: Where to Start?

### Option A: Build a Short Model
**Idea**: Trade State 2 (bearish regime) with a mirrored or new short strategy.

| Pros | Cons |
|------|------|
| Uses existing infrastructure (same asset) | Shorting crypto has different dynamics (funding rates, liquidation) |
| Currently sitting out State 2 — money left on table | Mean reversion (State 0) is harder to trade |
| Diversifies return stream (profit in down markets) | Need to validate if bearish regime is reliable for shorts |
| HMM already labels State 2 as "Shorts/Sit Out" | Asymmetric risk profile (unlimited loss potential) |
| | Exchange/counterparty risk on short positions |

### Option B: Expand Asset Class (ETH first)
**Idea**: Apply existing TR³ (long-only) to ETH, using BTC regime as filter.

| Pros | Cons |
|------|------|
| Lower risk increment — proven strategy, new data | Need data pipeline for each asset |
| Already planned in original DEVELOPMENT_PLAN.md | Each asset may need parameter tuning |
| Validates cross-asset thesis before adding complexity | Correlation during crashes limits diversification |
| Faster to validate — same backtest infra | More monitoring overhead |
| ETH often leads "Altseason" — different timing vs BTC | |

---

## Recommendation: Start with Option B (ETH Expansion)

**Reasoning:**

1. **Lower execution risk**: You're scaling a proven strategy, not building new mechanics
2. **Validates core thesis**: The development plan assumes BTC regime filters other assets — this tests that assumption
3. **Faster feedback loop**: Same backtest code, just new data
4. **Foundation for shorts**: Once multi-asset works, shorting becomes one strategy change vs N×M complexity
5. **Shorting needs more research**: Funding rates, exchange risk, liquidation mechanics — this deserves its own focused iteration

**Recommended sequence:**
```
Phase 1: ETH with BTC regime filter (this doc)
    ↓
Phase 2: Validate on 2-3 more assets (SOL, LINK, AVAX)
    ↓
Phase 3: Short model research & development
    ↓
Phase 4: Full Elite10 universe
```

---

## Phase 1: ETH Expansion Plan

### Goals
- Apply TR³ long-only strategy to ETH-USD
- Use lagged BTC 1D HMM regime as the filter (same as BTC strategy)
- Validate whether BTC regime transfers to ETH trading
- Establish patterns for adding future assets

### Assumptions
- ETH 1H data available from Coinbase (already downloaded in `data/raw/elite10/`)
- Same TR³ parameters initially (can tune later)
- Same HMM (BTC-based) — we're testing if BTC regime works for ETH

---

### Step 1: Data Validation
**Goal**: Confirm ETH data quality and coverage.

- [ ] Check `data/raw/elite10/ETH-USD_1h.csv` for:
  - Date range overlap with BTC test period (2022+)
  - No large gaps in hourly bars
  - OHLCV sanity (no negative prices, High ≥ Low)
- [ ] Note any data gaps or issues

### Step 2: Feature Engineering for ETH
**Goal**: Generate 1H features for ETH (same as BTC).

- [ ] Run `src/features/hourly_features.py` on ETH data
- [ ] Merge BTC daily HMM states into ETH 1H data (`D1_State_lag1d`)
- [ ] Output: `data/processed/eth_1h_features.csv`

### Step 3: Run ETH Backtest
**Goal**: Apply TR³ to ETH using BTC regime filter.

- [ ] Modify `scripts/run_holdout.py` to accept asset parameter
- [ ] Run holdout test on ETH (2022+ out-of-sample)
- [ ] Output: `outputs/logs/trade_log_eth_holdout.csv`

### Step 4: Compare Results
**Goal**: Determine if BTC regime filter helps ETH.

| Metric | ETH (with BTC filter) | ETH (no filter) | BTC baseline |
|--------|----------------------|-----------------|--------------|
| CAGR | | | |
| Sharpe | | | |
| Win Rate | | | |
| Profit Factor | | | |
| Max Drawdown | | | |
| Trades | | | |

Key questions:
- Does filtering ETH trades by BTC State 1 improve metrics?
- Does ETH show different regime timing than BTC?
- Are there enough trades in the test period?

### Step 5: Decision Gate
Based on results:

| Outcome | Action |
|---------|--------|
| ETH metrics comparable to BTC | Proceed to add SOL/AVAX |
| ETH metrics significantly worse | Investigate: parameter tuning, ETH-specific HMM? |
| Too few trades | Consider relaxing filters or shorter holding periods |

---

## Future Phases (Out of Scope for Phase 1)

### Phase 2: Expand to 3-5 Assets
- Add SOL, LINK, AVAX, LTC
- Same pattern: BTC regime filter, TR³ long-only
- Build portfolio-level logic (max positions, correlation limits)

### Phase 3: Short Model Development
- Research: Funding rates, exchange mechanics, liquidation risk
- Backtest State 2 characteristics (duration, volatility, trend strength)
- Design: Mirrored TR³ vs. separate short strategy
- Risk management: Tighter stops, position sizing adjustments

### Phase 4: Full Elite10 + Shorts
- 10 assets × 2 directions = 20 potential signal sources
- Portfolio optimization, walk-forward re-tuning
- Live paper trading simulation

---

## Success Criteria for Phase 1

✅ ETH backtest runs cleanly with BTC regime filter  
✅ Metrics documented and compared to BTC baseline  
✅ At least 50+ trades in test period for statistical relevance  
✅ Decision made: proceed to Phase 2 or iterate on ETH  

---

## Timeline Estimate

| Step | Effort |
|------|--------|
| Data validation | 1 hour |
| Feature engineering | 1-2 hours |
| Run backtest | 30 min |
| Analyze & compare | 1-2 hours |
| **Total** | **~4-5 hours** |

---

## Notes

- Keep BTC HMM fixed for now — don't retrain on ETH data
- Use same TR³ parameters initially — tune only if needed
- Document any ETH-specific quirks (e.g., more volatile, different ATR scale)
