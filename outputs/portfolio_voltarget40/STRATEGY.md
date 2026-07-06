# BTC HMM-TR3 Strategy — Full Description (Vol-Target 0.40 Configuration)

A regime-aware, long-only momentum strategy on Bitcoin. A daily Hidden Markov
Model decides *when* the market is in a tradeable regime; an hourly momentum
system (**TR3** — Thrust · Retention · Ride) decides *what* to trade; and two
risk overlays (**ECT** + **Vol-Target**) decide *how large* to trade.

Everything is walk-forward and causal — no parameter is fit on the test window,
and every signal for day/bar *T* uses only data available before *T*.

---

## 1. Data

| Layer | Timeframe | Purpose |
|-------|-----------|---------|
| Regime | 1D (daily) OHLCV | HMM regime classification |
| Trading | 1H (hourly) OHLCV | TR3 entries, exits, position management |

Source: BTC-USD spot. Backtest window is **2022-01-01 → 2025-09-05**, fully
out-of-sample (the model's initial training ends 2021-12-31).

---

## 2. Regime Detection — Daily Gaussian HMM

A 3-state Gaussian Hidden Markov Model classifies each day into a market regime.

**Features (7, standardized per training window):**
- `Log_Returns` — daily log return (direction)
- `GKVol_20` — Garman-Klass volatility (20d)
- `VolZ_20` — volume z-score (20d)
- `EMA_20_slope` — trend slope
- `BodyPct` — candle body as % of open
- `ClosePosInRange` — close position within the day's range
- `CloseOverEMA20` — price distance from the 20-day EMA

**State labeling:** after each fit, states are sorted ascending by mean
`Log_Returns`, so State 0 = most bearish, State 2 = most bullish. TR3 is only
allowed to enter in **State 1** (the sustainable "grind-up" regime). The
top state (State 2) is the euphoric/blow-off regime, which tends to mean-revert,
so it is deliberately excluded.

**Causality (no lookahead):** the state used for day *T* is decoded with a
sliding Viterbi window ending at day *T-1*. Hourly bars within day *T* inherit
that day's lagged state via `D1_State_lag1d`.

---

## 3. Entry Logic — TR3 (Thrust · Retention · Ride)

On the 1H timeframe, a long entry triggers only when **all** conditions hold on
the signal bar (entry executes on the next bar's open):

1. **Regime gate** — daily HMM state == 1 (bullish grind).
2. **Trend structure** — `EMA50 > EMA200` and `Close > EMA50`.
3. **Momentum trigger** — either a **Donchian(20) breakout** (`Close > 20-bar
   high`) **or** a **thrust** (`Close - prev Close >= 0.75 x ATR14`).
4. **Close-location** — `CLV >= 0.55` (closed in the upper half of the bar).
5. **Trend quality** — `ADX14 >= 14` and `R2(EMA50) >= 0.10`.

The design intent: enter strong, well-structured breakouts inside a confirmed
bull regime — and nothing else.

---

## 4. Exit Logic

Positions are managed with a layered exit stack (observed exit-reason mix in
parentheses):

- **ATR trailing stop** (`trail_atr`, ~22%) — trails the high by an ATR
  multiple that widens as the trade matures (2.5x → 3.5x → 4.5x).
- **Failed-thrust stops** (`fth_level` + `fth_clv`, ~41%) — bails early if the
  breakout immediately fails on price level or weak close-location.
- **Trend-break exits** (`ema50_relaxed` + `ema50_break`, ~30%) — exits when
  price loses the EMA50 (with a relaxed band once the trade is in profit).
- **Breakeven stop** (`breakeven`, ~8%) — moves the stop to entry after ~0.75
  ATR of favorable movement, with a one-bar delay.
- **Time / no-progress stops** — exits stagnant trades (no progress in 12h;
  hard time stop at 7 days).

This produces the strategy's signature: **many small losses, few large wins**
(avg win +3.1% vs avg loss -0.53%, a ~5.9:1 payoff ratio).

---

## 5. Risk Management

Two independent overlays scale position size. Both are causal.

### 5a. ECT — Equity Curve Trading throttle
The strategy trades its own equity curve like a moving-average system:
- Track cumulative equity and its **40-trade SMA**.
- **Warm-up:** first 40 trades run at full size (`risk_high = 1.3`) to build the
  baseline.
- **Live:** if equity falls **0.5% below** its SMA, cut size to `risk_low = 0.5`;
  otherwise stay at 1.3. The 0.5% buffer prevents flip-flopping on noise.

Effect: automatically de-risks during the strategy's own losing streaks and
re-risks when it recovers.

### 5b. Vol-Target 0.40 (de-risk only)
Daily returns are scaled by BTC's realized volatility:

```
scale[T] = min( 0.40 / realized_vol[T-1] , 1.00 )
realized_vol = 20-day close-to-close std, annualized (sqrt 365), lagged 1 day
```

- When BTC's annualized vol is above ~40% (most of the time in crypto), the
  strategy runs below full size.
- The cap at **1.00x** means it **only ever reduces** risk — it never levers up,
  so it cannot manufacture a surprise loss.
- Observed scaling: **0.39x – 1.00x, mean 0.82x**; de-risks on ~66% of days.

This is the overlay that separates this config from the baseline. It trims the
high-volatility tails — most visibly neutralizing the choppy 2025 bleed — at the
cost of shaving some of 2023's euphoric upside.

---

## 6. Walk-Forward Methodology

The strategy is evaluated as it would trade live:

1. **Initial train:** HMM fit on data up to 2021-12-31.
2. **Predict:** classify the next 30 days of regimes causally.
3. **Retrain:** slide the 730-day (2-year) training window forward and refit
   (warm-started from the previous model, with a fresh multi-seed fallback if
   the warm start diverges).
4. **Repeat** monthly through 2025-09-05.

No test-period data ever influences the model. Results are genuinely
out-of-sample.

---

## 7. Results (2022-01-01 → 2025-09-05)

| Metric | Value |
|--------|-------|
| Total Return | **103.81%** (2.04x) |
| CAGR | **21.35%** |
| Sharpe | **1.220** |
| Sortino | 1.469 |
| Calmar | 2.172 |
| Max Drawdown | **-9.83%** |
| Annualized Vol | 16.98% |
| Win Rate | 25.0% |
| Profit Factor | 1.96 |
| Trades | 204 |

**vs Baseline (no vol-target):** total return 119.33% → 103.81%, Sharpe
1.150 → 1.220, Max DD -12.62% → -9.83%. The overlay trades ~15.5 pts of total
return for a ~22% shallower worst drawdown and higher risk-adjusted return.

See `METRICS.txt` for the full metric set and per-year breakdown, and
`equity_chart.png` for the equity/drawdown curves.

---

## 8. Reproduce

```bash
python scripts/run_portfolio.py \
    --vol-target 0.40 \
    --vol-max-scale 1.0 \
    --out-dir outputs/portfolio_voltarget40
```

## 9. Known Limitations

- **Long-only:** no participation on the short side; bear markets are sat out,
  not exploited.
- **Single asset:** BTC only; no diversification.
- **Costs:** net of a per-bar cost model, but excludes exchange funding/borrow
  and slippage on large size.
- **Sharpe ceiling:** this architecture (trend-following a volatile asset) tops
  out near Sharpe ~1.25 under vol-targeting. Crossing ~2.0 would require a
  different alpha source (mean-reversion, funding-rate harvest, or pairs).
