# Development Plan: Live-Sim TR^3 on Top-25 Crypto

## Goals
- Update market data daily and simulate live trades (paper trading only).
- Use lagged BTC 1D HMM regime as a filter for TR^3 across top-25 market-cap assets.
- Log metrics and optimize the model with guardrails to avoid overfitting.

## Assumptions (Confirmed)
- Data source: Coinbase preferred (Binance acceptable fallback); use Coinbase as primary.
- Universe: Top-25 by market cap, refreshed weekly; exclude stablecoins (USDT, USDC, etc.).
- Trading timeframe: 1h; execution at bar open.
- Fees/slippage: use average assumptions (simple fixed bps per side + modest slippage).
- Optimization cadence: every 2 weeks.

## Phase 0 — Requirements Lock-In
- Universe definition:
  - Source of top-25 market-cap list.
  - Refresh schedule: weekly.
  - Exclusions: stablecoins (USDT, USDC, etc.).
- Data vendor decision:
  - Coinbase primary; Binance fallback if Coinbase coverage is missing.
  - Ensure 1h + 1d OHLCV coverage for all top-25 assets.
  - Define fallback behavior if a symbol lacks data.
- Execution model:
  - Entry/exit prices (bar open).
  - Fees and slippage model with average assumptions.
  - Treatment of gaps and missing bars.

## Phase 1 — Data Pipeline (Daily Updates)
- Scheduler:
  - Use a daily job runner (cron/launchd) to trigger updates.
- Ingestion:
  - Pull latest 1h and 1d OHLCV for all symbols.
  - Store raw data per asset (CSV/Parquet/SQLite).
- QA checks:
  - Deduplicate timestamps.
  - Validate continuous hourly grids.
  - Report missing bars and anomalies.

## Phase 2 — Feature + Regime Pipeline
- Daily feature generation:
  - Compute BTC 1d features used for HMM.
  - Compute 1h feature set for all assets (MR/MOM/LVBB + PRIME).
- Regime model:
  - Train BTC HMM on a rolling window.
  - Output a lagged BTC state series (no lookahead).
- Merge regime into each asset:
  - Add `D1_State_lag1d` into each asset’s 1h dataset.

## Phase 3 — Strategy Engine (Live Simulation)
- Signal generation:
  - Apply TR^3 rules per asset using lagged BTC regime.
  - Enforce rule that signals use t-1 data, execute at t open.
- Paper execution layer:
  - Simulated broker: order, fill, fee, slippage.
  - Position tracking per asset and portfolio-level exposure.
- Risk management:
  - Portfolio rules (confirmed):
    - Volatility-scaled sizing using ATR; risk 0.5% to 1.0% of capital per trade.
    - Position size: if stop is 2 x ATR, size so stop loss equals 1% of equity.
    - Max open positions: 10 (target range 8 to 12).
    - Selection priority when oversubscribed: pick top 10 by 24h relative strength.
    - Per-trade risk cap: never exceed 1.5% risk on a single entry.
    - Global halt: stop new entries if equity drawdown reaches 15% from ATH.
    - Correlation cap: limit to 3 positions per sector/category.

## Phase 4 — Metrics and Logging
- Daily metrics:
  - Per-asset stats: CAGR, Sharpe, PF, WR, MDD, trade count.
  - Portfolio stats: equity curve, exposure, drawdown.
- Audit logs:
  - Save signals, fills, trade logs, and per-bar PnL.
  - Record a daily run snapshot for reproducibility.

## Phase 5 — Optimization Framework
- Objective:
  - Optimize TR^3 thresholds against PF/MDD/Sharpe and trade count.
- Procedure:
  - Rolling walk-forward evaluation.
  - Separate train/validation windows to avoid leakage.
- Guardrails:
  - Stability checks across multiple market regimes.
  - Penalties for overly brittle parameter sets.
  - Re-optimize every 2 weeks.

## Phase 6 — Reporting and Ops
- Reporting:
  - Daily summary report (CSV + text).
  - Weekly recap: best/worst assets, regime distribution, signal stats.
- Alerts:
  - Data gaps, failed updates, abnormal volatility spikes.
- Documentation:
  - Operational runbook for updates, re-optimization, and review.

## Deliverables
- End-to-end daily pipeline (data → features → regime → signals → trades).
- Paper trading engine with portfolio-aware logs.
- Metrics dashboard outputs and Monte Carlo resampling for robustness.
- Optimization loop with walk-forward validation.
