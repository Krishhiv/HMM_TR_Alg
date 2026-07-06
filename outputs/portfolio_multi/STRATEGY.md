# HMM-TR3 Multi-Asset Momentum Portfolio: Full Description

A regime-aware, long-only momentum strategy run independently on BTC and ETH and combined into one portfolio. Each asset uses the same unified engine: a daily Hidden Markov Model decides when the market is tradeable, an hourly momentum system (TR3) decides what to trade, and three risk overlays decide how large. The two sleeves are then blended 50/50.

Everything is walk-forward and causal: no parameter is fit on the test window, and every signal for time T uses only data available before T. Results cover 2022-01 to 2026-07, out-of-sample.

---

## 1. Why a portfolio (the core idea)

A single-asset momentum strategy is capped by its own drawdowns, because there is nothing to diversify against. The insight here: the same proven edge, run on a second asset, produces decorrelated strategy returns even though the underlying prices are highly correlated.

- BTC / ETH price correlation: 0.83 (crypto moves together)
- BTC / ETH strategy-return correlation: 0.25

The strategy returns decorrelate because the two momentum sleeves trend on different clocks and are rarely both in-market at once. Combining two imperfectly-correlated sleeves (Sharpe 1.18 and 1.13) yields a portfolio Sharpe of 1.46, higher than either sleeve, with a drawdown lower than either. That is the closest thing to a free lunch in finance.

---

## 2. Data

| Layer | Timeframe | Purpose |
|-------|-----------|---------|
| Regime | 1D | HMM regime classification (per asset) |
| Trading | 1H | TR3 entries, exits, position management |

Instruments: BTC-USD and ETH-USD spot. Backtest window 2022-01 to 2026-07, out-of-sample (each HMM's initial training ends 2021-12-31). Only an hourly OHLCV file is required per asset; daily bars and all features are derived from it.

---

## 3. The unified engine (identical for every asset)

The key architectural principle: the HMM is fit, not hand-tuned. The same configuration is applied to every asset; the EM algorithm calibrates the model to each asset's own data automatically. No per-asset feature selection or parameter search. Cross-asset generalization is the built-in overfitting check.

### 3a. Regime detection: daily Gaussian HMM
A 3-state HMM classifies each day using 7 features (log returns, Garman-Klass vol, volume z-score, EMA slope, candle body, close-in-range, close-vs-EMA20). States are sorted by mean return, so state 0 is bearish and state 2 is euphoric. TR3 trades only state 1, the sustainable grind-up regime. On ETH, this state shows a forward return of +0.54%/day (55.8% up-days) versus negative for both other states, a clean economic separation. The state for day T is decoded from data up to T-1 (sliding causal Viterbi); the HMM is retrained every 30 days on a trailing 730-day window, warm-started from the prior model.

### 3b. Entry: TR3 (Thrust, Retention, Ride)
Hourly long entries require, on the signal bar: regime state 1, EMA50 > EMA200, price > EMA50, a Donchian-20 breakout or ATR thrust, plus close-location, ADX and R2 filters. Entry executes on the next bar's open.

### 3c. Exit stack
Layered: failed-thrust stops, ATR trailing stop (widening 2.5x to 4.5x), EMA50 trend-break, breakeven lock, and time/no-progress stops. This yields the signature low-win-rate / high-payoff profile (many small losses, few large winners).

---

## 4. Risk overlays (all causal)

Applied per sleeve, in order:

1. ECT (Equity-Curve Throttle): tracks the sleeve's own equity vs its 40-trade SMA; cuts size to 0.5x when equity falls 0.5% below the SMA, else 1.3x. De-risks during the strategy's own losing streaks.

2. Vol-Target (de-risk only): scales daily position by min(target / realized_vol, 1.0), where realized_vol is 20-day annualized, lagged 1 day. BTC target 0.40, ETH target 0.50. Never levers above 1.0x, so it only ever reduces risk. This is the primary drawdown-reduction lever.

3. min-dwell regime smoothing (ETH only): delays a regime switch until the new state persists 2 days, filtering the HMM's jumpy false-positive flips. Cuts ETH regime switches 68% (624 to 197), which alone took ETH's raw drawdown from -22.5% to -15.5%; vol-targeting then reduced it further.

---

## 5. Portfolio construction

The two vol-targeted sleeve return streams are aligned to their common window and combined at fixed 50/50 capital weight. No dynamic optimization, just a static, robust split. Sensitivity testing shows 30/70 through 70/30 all give Sharpe in the low-to-mid 1.4s, so the exact weight is not a fitted knob.

---

## 6. Results (2022-01 to 2026-07, out-of-sample)

| Metric | BTC | ETH | Portfolio |
|--------|-----|-----|-----------|
| Total Return | 126.8% | 143.6% | 140.8% |
| CAGR | 19.9% | 21.8% | 21.5% |
| Sharpe | 1.18 | 1.13 | 1.46 |
| Sortino | 1.30 | 1.13 | 1.89 |
| Calmar | 2.02 | 1.69 | 2.52 |
| Max Drawdown | -9.8% | -12.9% | -8.5% |
| Annual Vol | 16.4% | 18.8% | 14.0% |

Per-year handoff: BTC drives 2023 (+63%), ETH drives 2025 (+91%); the portfolio has only two mildly negative years (2022 at -2.7%, 2026 year-to-date at -2.3%). See METRICS.txt for the full table and portfolio_chart.png for equity/drawdown curves.

The portfolio beats both sleeves on Sharpe (1.46 vs 1.18 / 1.13) and on drawdown (-8.5% vs -9.8% / -12.9%), the direct benefit of the low 0.25 strategy correlation.

---

## 7. Robustness

Validated in scripts/overfitting_test.py (data through 2026-07):
- 80-config parameter grid: Sharpe 1.29 to 1.49, 72% clear Sharpe 1.40, a broad plateau rather than an overfit spike.
- 5,000-resample block bootstrap: Sharpe 5th percentile 0.79, median 1.47, P(Sharpe > 1.0) = 88%.
- Sub-period split: both halves profitable and balanced (Sharpe 1.55 and 1.39).

---

## 8. Reproduce

```bash
python scripts/run_portfolio_multi.py   # build the portfolio
python scripts/overfitting_test.py      # robustness suite
```

## 9. Limitations

- Single-cycle sample (~4.5 yrs); unseen regimes untested. 2026 year-to-date is mildly negative.
- Both sleeves are crypto: diversification is within-crypto, not market-neutral.
- Long-only; no short side, no participation in bear markets beyond sitting out.
- Net of a per-bar cost model; excludes funding/borrow and large-size slippage.
