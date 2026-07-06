# HMM-TR³ — Regime-Filtered Crypto Momentum Portfolio

A quantitative trading system that combines **Hidden Markov Model regime detection** with a **momentum breakout strategy (TR³)**, layered risk overlays, and **multi-asset diversification** across BTC and ETH.

Everything is **walk-forward and causal** — the model is retrained on a rolling window and never sees future data. All results below are out-of-sample from 2022-01 onward.

---

## Headline Results (2022-01 → 2025-09, out-of-sample)

| Metric | BTC sleeve | ETH sleeve | **Portfolio (50/50)** |
|---|---|---|---|
| CAGR | 21.4% | 29.9% | **26.3%** |
| Sharpe | 1.22 | 1.40 | **1.68** |
| Sortino | 1.47 | 1.58 | **2.58** |
| Max Drawdown | -9.8% | -9.6% | **-7.2%** |
| Annual Vol | 17.0% | 20.0% | **14.5%** |

The portfolio beats **both** of its sleeves on Sharpe *and* drawdown — the diversification benefit of two momentum sleeves whose **strategy returns correlate just 0.23** (vs 0.83 for the underlying assets), because they trend on different clocks.

**vs the original single-asset BTC baseline:** Sharpe 1.15 → **1.68** (+46%), Max DD -12.6% → **-7.2%** (43% shallower), CAGR 23.8% → **26.3%**.

---

## How It Works

```
   Daily OHLCV                         Hourly OHLCV
        │                                    │
        ▼                                    ▼
┌───────────────────┐              ┌──────────────────────┐
│  3-State Gaussian │  regime      │   TR³ momentum entry │
│  HMM (walk-fwd)   │─────────────▶│   (Donchian / thrust │
│  state 1 = trade  │  (lagged)    │    breakout + filters│
└───────────────────┘              └──────────┬───────────┘
                                              │ per-trade returns
                                              ▼
                              ┌──────────────────────────────┐
                              │  Risk overlays (all causal):  │
                              │   • ECT  equity-curve throttle│
                              │   • Vol-target position sizing│
                              │   • min-dwell regime smoothing│
                              └──────────────┬───────────────┘
                                              │
                     ┌────────────────────────┴───────────────────────┐
                     ▼                                                 ▼
              BTC sleeve                                         ETH sleeve
                     └───────────────── 50 / 50 blend ──────────────────┘
                                              │
                                              ▼
                                     Diversified portfolio
```

### 1. Regime detection — daily Gaussian HMM
A 3-state HMM classifies each day using 7 volatility/trend features. States are labeled by mean return (0 = bearish, 2 = euphoric); TR³ is only permitted to trade **state 1** — the sustainable "grind-up" regime, which shows the cleanest forward returns. The state for day *T* is decoded from data up to *T-1* (no lookahead) and retrained every 30 days on a trailing 730-day window.

### 2. Entry — TR³ (Thrust · Retention · Ride)
Hourly long entries fire on a **Donchian-20 breakout or ATR thrust**, gated by trend structure (EMA50 > EMA200, price > EMA50), close-location, ADX and R². The profile is low win-rate / high payoff — many small losses funded by a few large winners.

### 3. Risk overlays (all causal, no lookahead)
- **ECT** — throttles position size when the strategy's own equity falls below its 40-trade SMA.
- **Vol-target** — scales size down when the asset's realized vol is elevated (`min(target/realized_vol, 1.0)`, de-risk only). BTC target 0.40, ETH 0.50.
- **min-dwell smoothing** (ETH) — delays regime switches until a new state persists 2 days, cutting HMM churn 68% and halving the drawdown.

### 4. Portfolio
Per-sleeve vol-targeted returns are combined 50/50. Low strategy correlation lifts portfolio Sharpe above either sleeve and cuts the drawdown below both.

---

## Robustness

Validated with [`scripts/overfitting_test.py`](scripts/overfitting_test.py):

- **Parameter sensitivity** — across **80 overlay configs** (vol-targets × weight), Sharpe stays in **1.51–1.71** and **100%** clear Sharpe 1.5 / CAGR 20%. The result is a broad plateau, not a knife-edge peak.
- **Monte-Carlo block bootstrap** (5,000 resamples) — Sharpe 5th percentile **0.96**, median 1.70; P(Sharpe > 1.0) = 94%.
- **Sub-period stability** — both halves profitable (Sharpe 1.20 and 2.06).

The HMM + TR³ engine is genuinely walk-forward OOS. Known limitations: short single-cycle sample (~3.7 yrs), and both sleeves share crypto beta — diversification is *within* crypto, not market-neutral.

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
│   ├── run_holdout_ect.py     # TR³ + ECT core (shared engine)
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
The HMM is **fit**, not hand-tuned — the same unified spec applies to any asset. To add one:
1. Drop an hourly OHLCV CSV in `data/raw/` (daily is resampled from it).
2. Generate features with `src/features/daily_features.py` and `src/features/hourly_features.py`.
3. Run it through `run_portfolio.py` — no per-asset model tuning.

---

## Key Design Principles

- **No lookahead** — every signal for time *T* uses only data available before *T*; the HMM is retrained walk-forward.
- **Unified spec** — one model configuration across all assets; cross-asset generalization is the built-in overfitting check.
- **De-risk, don't lever** — overlays only ever *reduce* exposure (max scale 1.0), so they can't manufacture surprise losses.
- **Diversify an edge that exists** — the momentum edge is validated per-asset first; the portfolio just harvests its low cross-asset correlation.

---

*Research/education only. Not investment advice. Past performance does not guarantee future results.*
