# HMM-TR3: Regime-Filtered Crypto Momentum Portfolio

A quantitative trading system that combines Hidden Markov Model regime detection with a momentum breakout strategy (TR3), layered risk overlays, and multi-asset diversification across BTC and ETH.

Everything is walk-forward and causal: the model is retrained on a rolling window and never sees future data. All results below are out-of-sample from 2022-01 onward, on data through 2026-07.

---

## Headline Results (2022-01 to 2026-07, out-of-sample)

| Metric | BTC sleeve | ETH sleeve | Portfolio (50/50) |
|---|---|---|---|
| CAGR | 19.9% | 21.8% | 21.5% |
| Sharpe | 1.18 | 1.13 | 1.46 |
| Sortino | 1.30 | 1.13 | 1.89 |
| Max Drawdown | -9.8% | -12.9% | -8.5% |
| Annual Vol | 16.4% | 18.8% | 14.0% |
| Total Return | 126.8% | 143.6% | 140.8% |

The portfolio beats both of its sleeves on Sharpe (1.46 vs 1.18 / 1.13) and drawdown (-8.5% vs -9.8% / -12.9%). That is the diversification benefit of combining two momentum sleeves whose strategy returns correlate just 0.25 (vs 0.83 for the underlying assets), because they trend on different clocks.

---

## How It Works

```
   Daily OHLCV                         Hourly OHLCV
        |                                    |
        v                                    v
+-------------------+              +----------------------+
|  3-State Gaussian |  regime      |   TR3 momentum entry |
|  HMM (walk-fwd)   |------------->|   (Donchian / thrust |
|  state 1 = trade  |  (lagged)    |    breakout + filters|
+-------------------+              +----------+-----------+
                                              | per-trade returns
                                              v
                              +------------------------------+
                              |  Risk overlays (all causal): |
                              |   - ECT equity-curve throttle|
                              |   - Vol-target sizing        |
                              |   - min-dwell regime smooth  |
                              +--------------+---------------+
                                              |
                     +------------------------+------------------------+
                     v                                                 v
              BTC sleeve                                         ETH sleeve
                     +----------------- 50 / 50 blend -------------------+
                                              |
                                              v
                                     Diversified portfolio
```

### 1. Regime detection: daily Gaussian HMM
A 3-state HMM classifies each day using 7 volatility/trend features. States are labeled by mean return (0 = bearish, 2 = euphoric); TR3 is only permitted to trade state 1, the sustainable grind-up regime, which shows the cleanest forward returns. The state for day T is decoded from data up to T-1 (no lookahead) and retrained every 30 days on a trailing 730-day window.

### 2. Entry: TR3 (Thrust, Retention, Ride)
Hourly long entries fire on a Donchian-20 breakout or ATR thrust, gated by trend structure (EMA50 > EMA200, price > EMA50), close-location, ADX and R2. The profile is low win-rate / high payoff: many small losses funded by a few large winners.

### 3. Risk overlays (all causal, no lookahead)
- ECT: throttles position size when the strategy's own equity falls below its 40-trade SMA.
- Vol-target: scales size down when the asset's realized vol is elevated (min(target/realized_vol, 1.0), de-risk only). BTC target 0.40, ETH 0.50.
- min-dwell smoothing (ETH): delays regime switches until a new state persists 2 days, cutting HMM churn 68% and roughly halving the raw drawdown.

### 4. Portfolio
Per-sleeve vol-targeted returns are combined 50/50. Low strategy correlation lifts portfolio Sharpe above either sleeve and cuts the drawdown below both.

---

## Robustness

Validated with [scripts/overfitting_test.py](scripts/overfitting_test.py):

- Parameter sensitivity: across 80 overlay configs (vol-targets x weight), Sharpe stays in 1.29 to 1.49 (median 1.43), with 72% clearing Sharpe 1.40 and 86% clearing CAGR 20%. A broad plateau, not a knife-edge peak.
- Monte-Carlo block bootstrap (5,000 resamples): Sharpe 5th percentile 0.79, median 1.47; P(Sharpe > 1.0) = 88%.
- Sub-period stability: both halves profitable and balanced (Sharpe 1.55 and 1.39).

The HMM + TR3 engine is genuinely walk-forward out-of-sample. Known limitations: single-cycle sample (~4.5 yrs), and both sleeves share crypto beta, so diversification is within crypto, not market-neutral. 2026 year-to-date has been mildly negative (-2.3%), a reminder the edge is not guaranteed.

---

## Project Structure

```
HMM_TR_Alg/
├── src/
│   ├── data/            # Coinbase downloader
│   ├── features/        # daily_features.py, hourly_features.py
│   ├── hmm/             # model.py  (unified, asset-agnostic HMM)
│   ├── strategy/        # tr3_engine.py
│   └── backtest/        # metrics.py
├── scripts/
│   ├── run_holdout_ect.py     # TR3 + ECT core (shared engine)
│   ├── run_btc_strategy.py    # walk-forward runner (any asset)
│   ├── run_portfolio.py       # single-asset runner + vol-target
│   ├── run_portfolio_multi.py # BTC+ETH combined portfolio
│   └── overfitting_test.py    # robustness suite
├── data/
│   ├── raw/             # BTC/ETH 1h + 1d OHLCV
│   └── processed/       # engineered feature files
├── outputs/             # equity curves, charts, metrics, reports
├── requirements.txt
└── README.md
```

---

## Usage

```bash
# Install
pip install -r requirements.txt

# Refresh raw data to the latest available (Coinbase)
python -c "from src.data.coinbase_downloader import download_daily; download_daily()"

# Single-asset BTC (vol-targeted)
python scripts/run_portfolio.py --vol-target 0.40 --vol-max-scale 1.0 \
    --out-dir outputs/portfolio_voltarget40

# Single-asset ETH (same engine, just different data)
python scripts/run_portfolio.py \
    --daily data/processed/eth_1d_features.csv \
    --hourly data/processed/eth_1h_features_tr.csv \
    --out-dir outputs/portfolio_eth

# Combined BTC + ETH portfolio (the headline result)
python scripts/run_portfolio_multi.py

# Robustness / overfitting suite
python scripts/overfitting_test.py
```

### Adding a new asset
The HMM is fit, not hand-tuned: the same unified spec applies to any asset. To add one:
1. Drop an hourly OHLCV CSV in `data/raw/` (daily is resampled from it).
2. Generate features with `src/features/daily_features.py` and `src/features/hourly_features.py`.
3. Run it through `run_portfolio.py`, with no per-asset model tuning.

---

## Key Design Principles

- No lookahead: every signal for time T uses only data available before T; the HMM is retrained walk-forward.
- Unified spec: one model configuration across all assets; cross-asset generalization is the built-in overfitting check.
- De-risk, don't lever: overlays only ever reduce exposure (max scale 1.0), so they cannot manufacture surprise losses.
- Diversify an edge that exists: the momentum edge is validated per-asset first; the portfolio just harvests its low cross-asset correlation.

---

*Research/education only. Not investment advice. Past performance does not guarantee future results.*
