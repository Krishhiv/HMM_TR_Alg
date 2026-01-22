# Mean Reversion (EngineB) Development Plan

Scope: Only /EngineB for the mean reversion algorithm. This plan covers data collection through walk-forward analysis and optimization, based on EngineB/Notes/MEAN_REVERSION.md.

---

## 0) Current State (Already Done)

- Data collection scripts exist:
  - EngineB/Data-Collection/coinbase_5m_btc.py
  - EngineB/Data-Collection/coinbase_15m_btc.py
- Historical datasets already present:
  - EngineB/Data/BTC-USD_5m.csv
  - EngineB/Data/BTC-USD_15m.csv
  - EngineB/Data/metadata.json
- Strategy specification and math reference exist:
  - EngineB/Notes/MEAN_REVERSION.md

---

## 1) Data Collection (5m + 15m OHLCV)

Goal: Ensure consistent, complete OHLCV datasets as far back as possible.

Tasks:
- Verify data coverage, earliest timestamp, and gaps in EngineB/Data/BTC-USD_5m.csv and EngineB/Data/BTC-USD_15m.csv.
- Confirm schema: Date, Open, High, Low, Close, Volume (UTC).
- Ensure data timestamps are strictly increasing and aligned to 5m/15m boundaries.
- Add lightweight validation reporting (row counts, coverage, missing bars).

Deliverables:
- A small validation script in EngineB/Data-Collection (or EngineB/Feature-Engineering) that prints coverage metrics.
- Updated metadata.json with earliest and latest timestamps for both datasets.

---

## 2) Data Cleaning + QA

Goal: Produce cleaned datasets for modeling, with gap handling and sanity checks.

Tasks:
- Remove duplicates, sort by Date, and enforce consistent frequency.
- Forward-fill OHLC on missing bars, set missing Volume to 0.
- Validate OHLC integrity (High >= max(Open, Close), Low <= min(Open, Close)).
- Flag extreme 5m returns (e.g., abs(return) > 10%) for review.
- Generate a QA report (missing bars, outliers, invalid rows).

Deliverables:
- EngineB/Feature-Engineering/clean_ohlcv.py (or similar).
- Cleaned outputs in EngineB/Data (e.g., BTC-USD_5m_clean.csv, BTC-USD_15m_clean.csv).
- QA summary log or JSON report.

---

## 3) Feature Engineering

Goal: Build signal inputs (fair value, volatility, z-score, Hurst regime).

Features to implement from MEAN_REVERSION.md:
- Kalman filter fair value (mu_t) on 5m close.
- EWMA volatility (sigma_t) on 5m using lambda = 0.94.
- Z-score: (Close - mu_t) / sigma_t.
- Hurst exponent on 15m series (100-bar window, rolling).
- Liquidity/execution cost proxy:
  - range_pct = (High - Low) / Close
  - liquidity_cost_proxy = max(0.0002, 0.10 * range_pct)

Tasks:
- Decide storage format (CSV or Parquet) and output location.
- Ensure 15m Hurst values are aligned to 5m bars (forward-fill or merge-asof).

Deliverables:
- EngineB/Feature-Engineering/mean_reversion_features.py
- EngineB/Data/BTC-USD_5m_features.(csv|parquet)

---

## 4) Signal Generation + Rules Engine

Goal: Implement entry/exit logic exactly as specified.

Entry rules (from MEAN_REVERSION.md):
- Long when Z_t < -2.0, Z_{t-1} >= -2.0, liquidity_cost_proxy < 0.10%, Hurst_15m < 0.50, bars_since_last_trade > 12, no open position.
- Short when Z_t > +2.0, Z_{t-1} <= +2.0, same filters.

Exit rules:
- Target exit at Z_t > +0.5 (long) or Z_t < -0.5 (short).
- Stop at Z_t < -2.8 (long) or Z_t > +2.8 (short).
- Time stop at 6 hours (72 bars on 5m).

Deliverables:
- EngineB/Trading-Model/mean_reversion_signals.py (signal generator).
- Optional: EngineB/Trading-Model/position_logic.py (state machine for entry/exit).

---

## 5) Backtesting Engine

Goal: Event-driven backtest for 5m bars with costs and rule fidelity.

Core requirements:
- Single position at a time.
- Costs: maker/taker slippage model or fixed cost per trade.
- Track trades, equity curve, drawdowns.
- Log entries/exits with reasons (TARGET, STOP, TIME).

Metrics:
- Win rate, avg win/loss, profit factor.
- Sharpe (trade-based or bar-based returns).
- Max drawdown and average hold time.

Deliverables:
- EngineB/Trading-Model/mean_reversion_backtest.py
- EngineB/Outputs/backtest_trades.csv
- EngineB/Outputs/backtest_metrics.json

---

## 6) Walk-Forward Analysis

Goal: Evaluate parameter stability and out-of-sample performance.

Baseline grid (from MEAN_REVERSION.md):
- z_entry: [1.8, 2.0, 2.2]
- z_exit: [0.3, 0.5, 0.7]
- z_stop: [2.5, 2.8, 3.0]

Framework:
- In-sample: 6 months; Out-of-sample: 2 months; Step: 1 month.
- Optimize on in-sample Sharpe or profit factor with min trade count.
- Test on OOS and aggregate results.

Deliverables:
- EngineB/Walkforward/mean_reversion_wfo.py
- EngineB/Outputs/wfo_summary.json
- EngineB/Outputs/wfo_trades.csv

---

## 7) Optimization + Robustness

Goal: Avoid overfitting and validate real-world assumptions.

Tasks:
- Sensitivity tests on costs (increase by 2x/3x).
- Stress tests on missing bars and data gaps.
- Parameter stability analysis across windows.
- Evaluate alternative Hurst thresholds (0.45, 0.50, 0.55).

Deliverables:
- EngineB/Outputs/robustness_report.md
- EngineB/Outputs/parameter_stability.csv

---

## 8) Reporting + Reproducibility

Goal: Ensure consistent and repeatable runs.

Tasks:
- Single entry script (e.g., EngineB/Trading-Model/run_mean_reversion_pipeline.py).
- Save config JSON for each run.
- Log data version hashes (file sizes + timestamps).

Deliverables:
- EngineB/Outputs/run_config.json
- EngineB/Outputs/run_log.txt

---

## 9) Optional Extensions (Later)

- Live trading scaffolding (not in scope now).
- Multi-exchange data reconciliation.
- Dynamic thresholding using regime-conditioned Z_entry.

