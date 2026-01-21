# Mean Reversion Engine — End-to-End Development Plan (with ML Logistic Regression)

This document converts your notebook spec into a **fully reproducible** development roadmap:  
**data → features → labels (N = 16..21) → logistic regression training + calibration → model persistence → walk-forward testing → backtest + risk/execution**.

---

## 0) Strategy Spec Freeze (prevent code drift)

### Timeframes & Routing
- **Execution timeframe:** 15m bars.
- **Global gatekeeper:** 1D HMM state from **previous day**:
  - If `HMM_{D-1} == CHOP` → Mean Reversion (MR) engine allowed
  - Else → MR engine disabled (sit in cash or let your trend engine run, but **never both**)

### Core Definitions (as per notes)

#### (A) Daily VWAP (reset 00:00 UTC)
Use a consistent price definition (`close` or `typical_price`) and never change it later.

\[
VWAP_t = \frac{\sum_i (price_i \cdot volume_i)}{\sum_i volume_i}
\]

Implementation note: compute cumulative sums per UTC day:
- `cum_pv = cumsum(price * volume)`
- `cum_v  = cumsum(volume)`
- `vwap   = cum_pv / cum_v`

#### (B) Normalized Spread
Let \(D_t = Price_t - VWAP_t\). Define \(\sigma_t\) as rolling std of \(D_t\) over 100 bars:

\[
\sigma_t = \mathrm{Std}(D_{t-99:t})
\]

\[
S_t = \frac{Price_t - VWAP_t}{\sigma_t} = \frac{D_t}{\sigma_t}
\]

Purpose: “How many sigmas away from fair value.”

#### (C) Spread Velocity
\[
\Delta S_t = S_t - S_{t-1}
\]

Purpose: distinguish slow drift vs momentum spike.

#### (D) Volatility Percentile
Let \(ATR_t\) be ATR(14) on 15m bars. Define \(V_t\) as percentile rank of ATR over last 500 bars:

\[
V_t = \mathrm{PercentileRank}(ATR_t \;\text{within}\; ATR_{t-499:t})
\]

Use either 0..1 or 0..100 scaling, but lock it.

Purpose: detect local volatility explosions (possible regime shift) regardless of 1D HMM.

#### (E) Time Decay / Inventory Risk
Define a VWAP “touch” event on bar \(t\):

\[
\text{touch}_t = \mathbb{1}\{Low_t \le VWAP_t \le High_t\}
\]

Then:

\[
Z_t =
\begin{cases}
0, & \text{if touch}_t = 1 \\
Z_{t-1} + 1, & \text{otherwise}
\end{cases}
\]

Purpose: the longer price stays away from VWAP, the more likely a new trend forms.

---

## 1) ML: Logistic Regression for \(P(\text{reversion})\)

### Model Form
Use logistic regression to estimate probability that price **reverts (touches VWAP)** within next \(N\) bars:

\[
P(\text{reversion}) = \sigma\!\left(\beta_0 + \beta_1 S_t + \beta_2 \Delta S_t + \beta_3 V_t + \beta_4 Z_t\right)
\]

where the sigmoid:

\[
\sigma(x) = \frac{1}{1 + e^{-x}}
\]

### N Horizon Requirement
You specified: **N = 16 to 21** (15m bars). That is 4h to 5.25h.

Two acceptable implementations:

**Option A (recommended):** train one model per \(N\)  
Train 6 models: \(N \in \{16,17,18,19,20,21\}\).  
At runtime define:
- \(P = \mathrm{mean}(P_N)\) **or**
- \(P = \max(P_N)\)

Pick one rule and keep it fixed.

**Option B:** choose a single best \(N\) per walk-forward fold  
Evaluate each \(N\) on validation/test and pick the best out-of-sample.  
Simpler runtime, but more “selection” complexity.

---

## 2) EV Filter (trade-quality gate)

Your EV rule:

\[
EV = P \cdot AvgGain - (1-P)\cdot AvgLoss
\]

Define these explicitly for implementation:
- **AvgGain:** distance from entry to VWAP (in price units)
- **AvgLoss:** distance from entry to stop (in price units)

Then require:
- `P(reversion) > 0.50`
- `EV > 0`

---

## 3) Entry & Execution Logic (single position)

### Primary Entry Conditions
Enter only if **all** are true:
1. `HMM_{D-1} == CHOP`  
2. `P(reversion) > 0.50`  
3. `EV > 0`  
4. Exhaustion confirmation (example):
   - If \(S_t > +2\), require \(\Delta S_t < 0\) (short bias)
   - If \(S_t < -2\), require \(\Delta S_t > 0\) (long bias)

### Directional Bias
- If \(S_t > +2.0\) → **SHORT**
- If \(S_t < -2.0\) → **LONG**

### Execution Assumption (must be locked)
Pick one and keep it:
- Signal computed on 15m close, enter at next bar open (**recommended** to reduce lookahead)
- Or enter on same bar close (optimistic)

---

## 4) Risk Management & Safety Brakes

### Emergency Brake (trend breakout / missed regime change)
Hard stop:

\[
|S_t| > 4.0 \Rightarrow \text{exit immediately}
\]

### Volatility Spike Pause
If \(V_t > 95\%\) percentile, cease new entries for **4 hours** (16 bars).

---

## 5) Exit Logic

Exit if any triggers (recommended priority order):
1. **Emergency:** \(|S_t| > 4.0\)
2. **Stop loss:** hard stop at 3.5σ (define this consistently; see below)
3. **Mean reverted:** VWAP touched or \(S_t\) crosses 0
4. **Edge decay:** \(P(\text{reversion}) < 0.50\)
5. **Timeout:** 8 hours (32 bars) without VWAP touch

### Important Consistency Choice: Stop in S-space vs Price-space
Pick one forever (do not mix):
- **S-space stop:** exit if \(|S_t| \ge 3.5\)
- **Price-space stop:** exit if price crosses `entry ± 3.5 * sigma_price`

Where `sigma_price` is \(\sigma_t\), the rolling std of \((Price - VWAP)\).

---

## 6) Development Roadmap (Start → Finish)

### 6.1 Repo Structure + Config Discipline
Create a small package layout:

- `data/` raw and cleaned bars  
- `features/` feature builders (pure functions)
- `labels/` event labeling for \(P(\text{reversion})\)
- `models/` training, calibration, persistence
- `backtest/` event-driven simulator + walk-forward harness
- `configs/` YAML configs for parameters + splits
- `reports/` metrics dumps, plots, fold summaries

Use a single config file for:
- VWAP price choice (close vs typical)
- windows: `sigma_window=100`, `atr_window=14`, `V_window=500`
- entry thresholds: `S_entry=2`, `P_thresh=0.5`, `EV_thresh=0`
- stops: `S_stop=3.5`, `S_emergency=4.0`
- pause & timeout: `entry_pause_bars=16`, `max_hold_bars=32`
- horizons: `N_list = [16,17,18,19,20,21]`

---

## 7) Data Engineering (2018-08-01 → Present)

### 7.1 Acquire + Standardize
- Pull **15m OHLCV** and **1D OHLCV** from the same venue.
- Normalize:
  - UTC timestamps
  - continuous 15m grid (handle missing bars deterministically)
  - remove duplicates
  - sanity checks (OHLC bounds, nonnegative volume)

Deliverables:
- `bars_15m.parquet`
- `bars_1d.parquet`

### 7.2 Align 1D HMM to 15m bars (no lookahead)
- Compute HMM on daily bars.
- Join daily state onto all 15m bars of that day.
- Use previous-day state for decisions: `HMM_{D-1}`.

Deliverable:
- `bars_15m_with_regime.parquet`

---

## 8) Feature Engineering (what the model sees)

Implement features as a deterministic pipeline:

### 8.1 Daily VWAP (00:00 UTC reset)
Per day:
- `cum_pv = cumsum(price * volume)`
- `cum_v = cumsum(volume)`
- `vwap = cum_pv / cum_v`

### 8.2 Spread + Normalization
- \(D_t = Price_t - VWAP_t\)
- \(\sigma_t = \mathrm{rolling\_std}(D_t, 100)\)
- \(S_t = D_t/\sigma_t\)
- \(\Delta S_t = S_t - S_{t-1}\)

### 8.3 Volatility Percentile \(V_t\)
- Compute `ATR(14)` on 15m
- `V_t = percent_rank(ATR_t, window=500)`

### 8.4 Time decay \(Z_t\)
- touch if `low <= vwap <= high`
- `Z_t = 0` on touch else increment

### 8.5 Recommended “low-risk, high-value” extra features (optional)
These often improve calibration without changing core logic:
- \(|S_t|\)
- time-of-day sin/cos features (intraday seasonality)
- volume z-score
- rolling slope / kurtosis on \(D_t\)

Deliverable:
- `features_15m.parquet` (strict column names)

---

## 9) Label Engineering for Logistic Regression (N = 16..21)

You want: probability of VWAP touch within next \(N\) bars.

### 9.1 Base event (touch within horizon)
For each decision bar \(t\), define window \(t+1..t+N\):

\[
\text{touch\_within\_N}(t) = \mathbb{1}\left[\exists k \in [t+1,t+N] : Low_k \le VWAP_k \le High_k \right]
\]

### 9.2 Trading-consistent label (recommended)
To avoid “fake positives” that would stop out before touch:

\[
y_t =
\begin{cases}
1, & \text{if VWAP touched before stop and before } N \\
0, & \text{otherwise}
\end{cases}
\]

This makes \(P(\text{reversion})\) align with “probability of a winning reversion trade,” not just eventual touch.

Deliverables:
- `labels_N16.parquet` … `labels_N21.parquet`

---

## 10) Train Logistic Regression (time-series safe)

### 10.1 Build training rows
- Filter to the regime you trade: `HMM_{D-1} == CHOP`
- Optionally focus on the relevant zone: `abs(S_t) >= 1.5` or `>= 2.0`

### 10.2 Time-series validation (no random splits)
Use walk-forward / expanding splits. Example:
- Train: 2018-08 → 2020-12
- Validate: 2021-01 → 2021-06
- Roll forward by 3–6 months

### 10.3 Model defaults
Train a sklearn `Pipeline`:
- `StandardScaler` (good for dS, V, Z)
- `LogisticRegression(penalty='l2', C tuned, class_weight='balanced' optional)`

### 10.4 Probability calibration (strongly recommended)
Even logistic can be miscalibrated in time series.
Calibrate using a validation slice:
- isotonic or sigmoid calibration

Track:
- Brier score
- calibration curve / reliability bins

Artifacts per model:
- coefficients
- feature list
- calibration report

---

## 11) Save Models for Instant Reuse (walk-forward & fast testing)

Persist for each \(N\):
- sklearn pipeline (scaler + logistic [+ calibrator])
- metadata JSON:
  - feature names + versions
  - window parameters
  - label definition
  - training start/end
  - git commit hash (optional but ideal)

Use `joblib.dump()`.

Deliverables:
- `models/logreg_N16.joblib` … `models/logreg_N21.joblib`
- `models/logreg_N16.meta.json` …

---

## 12) Backtest Engine (event-driven, matches live rules)

### 12.1 Execution assumptions
Lock these:
- signal computed on bar close
- entry on next bar open
- fee/slippage model (fixed bps is fine at first)

### 12.2 Main loop (single position)
At each bar \(t\):
1) If in position → manage exits
2) Else:
   - if MR disabled (HMM not CHOP) → skip
   - if in vol-spike pause window → skip
   - compute \(P(\text{reversion})\) via loaded model(s)
   - compute EV
   - apply exhaustion rule + `abs(S) >= 2`
   - open position with defined sizing

### 12.3 Trade sizing (Kelly-like, but capped)
You wrote:

\[
Size = BaseRisk \times \frac{P - P_{be}}{1 - P_{be}}
\]

Define breakeven probability:

\[
P_{be} = \frac{AvgLoss}{AvgGain + AvgLoss}
\]

Then enforce:
- `Size = clip(Size, 0, MaxRisk)`
- cap leverage / notional exposure

### 12.4 Exit priority (deterministic)
Recommended order:
1) emergency \(|S| > 4.0\)
2) stop loss (3.5σ)
3) VWAP touch or \(S\) crosses 0
4) \(P < 0.5\)
5) timeout 8h (32 bars)

Outputs:
- trades table
- equity curve
- per-trade diagnostics: entry S, P, EV, V, Z, exit reason

---

## 13) Walk-Forward Testing Harness (the iteration engine)

### 13.1 Walk-forward scheme
Typical:
- Train window: 18–24 months
- Test window: 1–3 months
- Step forward by test window

For each fold:
1) build features + labels using only available history
2) train model(s)
3) save model artifacts
4) backtest on fold test period with saved model
5) store fold metrics

### 13.2 Metrics to track
**ML metrics (test slice):**
- AUC (secondary)
- **Brier score + calibration** (primary)
- precision/recall for candidate region `abs(S) >= 2`

**Trading metrics (test slice):**
- CAGR, Sharpe/Sortino, max drawdown
- win rate, payoff ratio, profit factor
- avg hold time, exits by type
- performance by volatility percentile buckets and time-of-day

Deliverable:
- `reports/walkforward_report.csv` + plots

---

## 14) Iteration & Tuning Order (lowest overfit risk first)

Tune in this order:
1) label definition (touch-before-stop) + N handling
2) calibration & stability checks
3) P threshold (0.50 is a baseline, not a law)
4) entry zone (`abs(S) >= 2` vs 1.8 etc.)
5) exhaustion rule variants
6) risk caps + pause logic (V>95 freeze length)

Only after stable:
- add more features (time-of-day, volume z-score)
- explore regularization / elastic net carefully

---

## 15) Definition of “Done”

You’re done when you have:
- a single command/script that:
  1) builds features from 2018-08-01 → present
  2) builds labels for N=16..21
  3) runs walk-forward training + calibration
  4) saves models per fold
  5) runs fold backtests
  6) produces a final report + trade logs
- plus a “latest model” artifact you can load instantly for paper trading.

---

### Final Notes
Before you code, lock these two choices (they affect everything):
1) Stop definition: **S-space** vs **price-space**  
2) VWAP touch definition: **OHLC crosses VWAP** vs stricter “close near VWAP”

Once locked, do not change them across experiments, or your walk-forward results won’t be comparable.
