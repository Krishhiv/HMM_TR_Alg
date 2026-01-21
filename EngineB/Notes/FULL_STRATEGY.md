# Mean Reversion Trading Engine for Bitcoin — Codex-Exact Specification

## 0) Scope

### What this spec defines

A single-instrument (BTC) mean-reversion trading system that:

-   Estimates fair value using a **1D Kalman filter** on mid-price.
    
-   Estimates volatility using **EWMA** on log returns.
    
-   Forms a standardized deviation signal (**Z-score**).
    
-   Filters out trending regimes using **15m Hurst exponent**.
    
-   Enters via **limit orders with timeout**, exits via **market orders**.
    
-   Enforces **one position at a time**, cooldown, daily trade cap, and risk sizing.
    

### What this spec does NOT define

-   Any build/development steps, infra, deployment, monitoring, UI, etc.
    
-   Exchange-specific maker/taker fees (unless you add them as parameters).
    
-   Multi-asset portfolios.
    

----------

## 1) Data Requirements and Derived Series

### 1.1 Required 5-minute bar inputs (indexed by time `t`)

For each 5m bar `t`, you must have:

-   `open_t, high_t, low_t, close_t`
    
-   `volume_t` (base units BTC or quote units USD — you must be consistent)
    
-   `bid_t, ask_t` (best bid/ask at decision time; if missing, derive spread using a proxy but **default spec assumes real bid/ask**)
    

### 1.2 Derived 5-minute fields

Define:

-   `mid_t = (bid_t + ask_t) / 2`
    
-   `spread_t = (ask_t - bid_t) / mid_t` (dimensionless; e.g. 0.001 = 0.10%)
    

### 1.3 5-minute log return

For `t > 0`:

-   `r_t = ln(mid_t / mid_{t-1})`
    

### 1.4 15-minute close series for Hurst

Create a 15m series by grouping 5m bars into 15m buckets:

-   Each 15m bucket contains exactly 3 consecutive 5m bars.
    
-   Define `close15_k` as the **mid price of the last 5m bar** in that 15m bucket.
    

This yields a 15m series indexed by `k`.

----------

## 2) Global Parameters (ALL values and units fixed)

### 2.1 Kalman filter parameters (5m)

-   `Q = 1e-5` (process noise variance)
    
-   `R = 1e-3` (measurement noise variance)
    

### 2.2 EWMA volatility parameters (5m returns)

-   `lambda = 0.94`
    
-   EWMA tracks **variance of log returns**, then converts to price-vol.
    

### 2.3 Z-score thresholds

-   `z_entry = 2.0`
    
-   `z_exit = 0.5`
    
-   `z_stop = 2.8`
    

Interpretation: stop triggers when Z moves to `±z_stop` against your position.

### 2.4 Cooldown and limits

-   `cooldown_bars_5m = 12` (12 * 5m = 60 minutes)
    
-   `max_hold_bars_5m = 72` (72 * 5m = 6 hours)
    
-   `max_daily_trades = 6`
    

### 2.5 Liquidity filter

-   `max_spread = 0.0010` (0.10%)
    

### 2.6 Hurst filter parameters (15m)

-   `hurst_window_15m = 100` (100 * 15m = 25 hours)
    
-   `hurst_lag_max = 100`
    
-   Regime thresholds:
    
    -   Hard block: `hurst >= 0.55` ⇒ **NO TRADES**
        
    -   Caution zone: `0.50 <= hurst < 0.55` ⇒ trade allowed but **size scalar = 0.50**
        
    -   Normal zone: `hurst < 0.50` ⇒ trade allowed with **size scalar = 1.00**
        

(These rules eliminate the ambiguity between “<0.50” and “>=0.55” by making it explicit and consistent.)

### 2.7 Execution parameters

**Entry limit offset**

-   `entry_limit_offset = 0.0005` (0.05%)
    
    -   Long limit price: `limit = mid_t * (1 - entry_limit_offset)`
        
    -   Short limit price: `limit = mid_t * (1 + entry_limit_offset)`
        

**Limit timeout**

-   `limit_timeout_bars = 2` (2 * 5m = 10 minutes)
    

**Limit fill model**

-   `limit_fill_rate = 0.77`
    
-   `limit_adverse_selection = 0.0001` (0.01% = 1 bp, applied against you upon fill)
    

Concrete rule:

-   When a limit order is placed, fill occurs with probability `0.77` within the timeout window.
    
-   If filled:
    
    -   Long fill price = `limit_price * (1 + limit_adverse_selection)`
        
    -   Short fill price = `limit_price * (1 - limit_adverse_selection)`
        
-   If not filled within `2` bars: cancel and do not chase.
    

**Market slippage model (percent, not bps)**  
Define `market_slippage(notional_usd)`:

-   if `notional_usd < 10_000`: `0.0002` (0.02%)
    
-   if `10_000 <= notional_usd <= 50_000`: `0.0004` (0.04%)
    
-   if `notional_usd > 50_000`: `0.0008` (0.08%)
    

Market fills:

-   Long exit market fill price = `mid_t * (1 + market_slippage)`
    
-   Short exit market fill price = `mid_t * (1 - market_slippage)`
    

### 2.8 Risk parameters

-   `MAX_PORTFOLIO_HEAT = 0.02` (2% of equity at risk at stops)
    
-   `MAX_SINGLE_TRADE_RISK = 0.005` (0.5% of equity at risk at stop)
    

Since this strategy is **one position at a time**, portfolio heat is automatically satisfied if single-trade risk is satisfied, but keep both checks anyway.

### 2.9 Sizing parameters (Half Kelly + vol adjustment)

-   Rolling trade lookback: `kelly_lookback_trades = 100`
    
-   Half Kelly scalar: `kelly_fraction_multiplier = 0.5`
    
-   Kelly cap: `kelly_cap = 0.20` (20% of equity max notional before risk-stop scaling)
    
-   Target vol for vol-scaling: `target_return_vol = 0.0025` (0.25% per 5m return vol)
    

Vol scalar:

-   `vol_scalar = min(1.0, target_return_vol / max(current_return_vol, 1e-9))`
    

----------

## 3) State Variables (must be tracked exactly)

### 3.1 Strategy state (5m)

-   `position`: one of `{NONE, LONG, SHORT}`
    
-   `entry_price`: float or null
    
-   `entry_z`: float or null
    
-   `bars_held`: integer (0 when opened)
    
-   `bars_since_trade`: integer (increment each bar; reset to 0 on entry attempt _only if filled_)
    
-   `daily_trade_count[date]`: integer
    
-   `realized_trades`: list of closed trades, each containing at least:
    
    -   pnl_pct_net, win/loss flag, entry_time, exit_time, entry_price, exit_price
        

### 3.2 Kalman filter state (5m)

-   `x_hat` = fair value estimate
    
-   `P` = estimate uncertainty
    

### 3.3 EWMA state (5m)

-   `ewma_var` = EWMA variance of log returns
    
-   `current_return_vol = sqrt(ewma_var)`
    
-   `current_price_vol = current_return_vol * mid_t` (price units)
    

### 3.4 Hurst state (15m)

-   Maintain `prices_15m`: rolling list of last `hurst_window_15m` mid closes sampled at 15m.
    
-   If fewer than `hurst_window_15m` points exist, set `hurst = 0.50` (neutral) and proceed.
    

----------

## 4) Indicator Calculations (exact)

## 4.1 Kalman filter (1D random walk, measurement = mid)

Model:

-   State: `x_t = x_{t-1} + w_t`, `w_t ~ N(0, Q)`
    
-   Measurement: `y_t = x_t + v_t`, `v_t ~ N(0, R)`
    
-   Where `y_t = mid_t`
    

Initialization at first bar `t=0`:

-   `x_hat_0 = mid_0`
    
-   `P_0 = R`
    

Update each bar `t >= 1`:

1.  Predict:
    

-   `x_pred = x_hat_{t-1}`
    
-   `P_pred = P_{t-1} + Q`
    

2.  Update:
    

-   `K = P_pred / (P_pred + R)`
    
-   `x_hat_t = x_pred + K * (mid_t - x_pred)`
    
-   `P_t = (1 - K) * P_pred`
    

Fair value at time `t` is `mu_t = x_hat_t`.

----------

## 4.2 EWMA volatility (5m log returns)

Initialization:

-   For the first return that exists (`t=1`), set:
    
    -   `ewma_var_1 = r_1^2`
        

For each `t >= 2`:

-   `ewma_var_t = lambda * ewma_var_{t-1} + (1 - lambda) * r_t^2`
    

Then:

-   `current_return_vol_t = sqrt(ewma_var_t)`
    
-   `current_price_vol_t = current_return_vol_t * mid_t`
    

----------

## 4.3 Z-score (core signal)

For each `t >= 1`, define:

-   `z_t = (mid_t - mu_t) / max(current_price_vol_t, 1e-9)`
    

Also track `z_{t-1}` for fresh-signal logic.

----------

## 4.4 Hurst exponent on 15m series (exact algorithm)

Given 15m price series `p[0..n-1]` (use log prices):

-   `L = min(hurst_lag_max, n-1)`
    
-   For each lag `l` in `{2,3,...,L}`:
    
    -   `tau_l = sqrt( variance( log(p[l:]) - log(p[:-l]) ) )`
        

Fit a linear regression:

-   `x = log(lags)`
    
-   `y = log(tau_l)`
    
-   `slope = polyfit(x, y, 1)[0]`
    

Then:

-   `hurst = 2.0 * slope`
    

Warmup rule:

-   If `len(p) < 20`, set `hurst = 0.50` (neutral)
    
-   Else compute as above (but trading requires window state anyway)
    

----------

## 5) Entry Logic (exact boolean conditions)

The strategy may only enter if `position == NONE`.

### 5.1 Shared entry filters (must ALL pass)

At bar `t`, before generating any entry:

1.  `spread_t < max_spread`
    
2.  `bars_since_trade >= cooldown_bars_5m`
    
3.  `daily_trade_count[date(t)] < max_daily_trades`
    
4.  Hurst regime condition:
    
    -   If `hurst >= 0.55`: **BLOCK** (no trade)
        
    -   Else allowed; compute `hurst_size_scalar`:
        
        -   if `hurst < 0.50`: `hurst_size_scalar = 1.00`
            
        -   else (`0.50 <= hurst < 0.55`): `hurst_size_scalar = 0.50`
            

### 5.2 Fresh-signal condition (must be satisfied)

A signal is “fresh” only if it **crossed** the entry threshold this bar.

Long fresh condition:

-   `z_t < -z_entry` AND `z_{t-1} >= -z_entry`
    

Short fresh condition:

-   `z_t > +z_entry` AND `z_{t-1} <= +z_entry`
    

### 5.3 Long entry

Generate `LONG_SIGNAL` if:

-   All shared filters pass AND long fresh condition holds.
    

### 5.4 Short entry

Generate `SHORT_SIGNAL` if:

-   All shared filters pass AND short fresh condition holds.
    

----------

## 6) Exit Logic (exact)

Exit checks only if `position != NONE`.

### 6.1 Target exit (mean reversion complete)

If `position == LONG`:

-   Exit if `z_t >= +z_exit`
    

If `position == SHORT`:

-   Exit if `z_t <= -z_exit`
    

### 6.2 Stop exit (mean reversion failed)

If `position == LONG`:

-   Stop if `z_t <= -z_stop`
    

If `position == SHORT`:

-   Stop if `z_t >= +z_stop`
    

### 6.3 Time stop

If `bars_held > max_hold_bars_5m`: exit immediately (market).

### 6.4 Exit priority (if multiple triggers occur same bar)

Apply in this exact order:

1.  Stop exit
    
2.  Target exit
    
3.  Time stop
    

(Stops always win.)

----------

## 7) Position Sizing (exact)

Compute size ONLY at the moment you are about to place an entry order.

### 7.1 Compute Kelly fraction from last N closed trades

Let `T = last kelly_lookback_trades closed trades`.  
If `len(T) < 20`, set `kelly = 0.05` (5%) as bootstrap.  
Else:

-   `p = win_rate = (# trades with pnl_pct_net > 0) / len(T)`
    
-   `avg_win = mean(pnl_pct_net | pnl_pct_net > 0)`
    
-   `avg_loss = abs(mean(pnl_pct_net | pnl_pct_net < 0))`
    
-   `b = avg_win / max(avg_loss, 1e-9)`
    
-   `kelly = (p*(b+1) - 1) / max(b, 1e-9)`
    
-   Clamp: `kelly = clamp(kelly, 0.0, kelly_cap)`
    

Half Kelly:

-   `base_fraction = kelly_fraction_multiplier * kelly`
    

### 7.2 Volatility scalar

At time `t`:

-   `vol_scalar = min(1.0, target_return_vol / max(current_return_vol_t, 1e-9))`
    

### 7.3 Total notional fraction before stop-risk scaling

-   `fraction = base_fraction * vol_scalar * hurst_size_scalar`
    
-   Clamp: `fraction = clamp(fraction, 0.0, kelly_cap)`
    

Target notional:

-   `target_notional = equity_t * fraction`
    

### 7.4 Stop-based risk scaling (must satisfy MAX_SINGLE_TRADE_RISK)

To compute stop distance, convert z-stop into a **stop price** using current `mu_t` and `current_price_vol_t`.

At entry time (same bar `t`), define:

-   `sigma_price = current_price_vol_t`
    
-   Long stop price: `stop_price_long = mu_t - z_stop * sigma_price`
    
-   Short stop price: `stop_price_short = mu_t + z_stop * sigma_price`
    

Approximate stop distance using intended fill price `fill_est`:

-   Long stop distance: `stop_dist = fill_est - stop_price_long`
    
-   Short stop distance: `stop_dist = stop_price_short - fill_est`  
    If `stop_dist <= 0`, block trade (do not enter).
    

Risk dollars allowed:

-   `risk_dollars = MAX_SINGLE_TRADE_RISK * equity_t`
    

Max quantity allowed by risk:

-   `qty_risk_max = risk_dollars / stop_dist`
    

Quantity implied by notional:

-   `qty_notional = target_notional / fill_est`
    

Final quantity:

-   `qty = min(qty_notional, qty_risk_max)`
    

If `qty * fill_est < 10` USD (dust), skip trade.

----------

## 8) Execution (exact)

### 8.1 Entry execution (limit with timeout)

If `LONG_SIGNAL` at bar `t`:

-   Place limit order at `limit_price = mid_t * (1 - entry_limit_offset)`
    

If `SHORT_SIGNAL`:

-   Place limit order at `limit_price = mid_t * (1 + entry_limit_offset)`
    

Fill simulation:

-   Over the next `limit_timeout_bars` bars (inclusive), decide fill using Bernoulli(p=limit_fill_rate).
    
-   If filled:
    
    -   Long fill = `limit_price * (1 + limit_adverse_selection)`
        
    -   Short fill = `limit_price * (1 - limit_adverse_selection)`
        
    -   Set `position`, `entry_price`, `entry_z = z_t`, `bars_held = 0`
        
    -   Increment `daily_trade_count[date(t)] += 1`
        
    -   Set `bars_since_trade = 0`
        
-   If not filled:
    
    -   Cancel, do nothing, and **do not** reset cooldown.
        
    -   Keep `bars_since_trade` continuing to increment normally.
        

### 8.2 Exit execution (market)

When an exit triggers at bar `t`, execute a market order using:

-   Determine `slip = market_slippage(notional_usd = qty * mid_t)`
    

If exiting a LONG:

-   `exit_price = mid_t * (1 - slip)` (selling, worse price)
    

If exiting a SHORT:

-   `exit_price = mid_t * (1 + slip)` (buying back, worse price)
    

Then:

-   Realize PnL
    
-   Append trade to `realized_trades`
    
-   Set `position = NONE`, clear entry vars
    
-   Set `bars_since_trade = 0` (because you just traded)
    
-   Continue.
    

(If you prefer “next bar open” execution instead of same-bar mid, you must apply that consistently everywhere; default spec uses same-bar mid for trigger + fill modeling above.)

----------

## 9) Bar-by-Bar Main Loop (deterministic order)

For each 5m bar `t` in chronological order:

1.  Compute `mid_t`, `spread_t`.
    
2.  Update Kalman (`mu_t`).
    
3.  Update EWMA variance and vols (`current_return_vol_t`, `current_price_vol_t`).
    
4.  Compute `z_t`.
    
5.  Update 15m series if this bar completes a 15m bucket; compute `hurst` if enough data else `0.50`.
    
6.  Increment:
    
    -   `bars_since_trade += 1` (unless you reset it due to a filled trade this bar)
        
    -   If `position != NONE`: `bars_held += 1`
        
7.  If in position: evaluate exits in priority order; if exit triggers, execute exit and continue to next bar.
    
8.  If flat: evaluate entry filters + fresh signal; if signal, compute sizing and place limit order (fill is simulated as specified).
    
9.  Store `z_{t-1} = z_t` for next step.
    

----------

## 10) Trade Record Fields (minimum required for backtest + Kelly)

Each closed trade must store:

-   `direction` ∈ {LONG, SHORT}
    
-   `entry_time`, `exit_time`
    
-   `entry_price`, `exit_price`
    
-   `qty`
    
-   `gross_pnl_usd`
    
-   `pnl_pct_net = gross_pnl_usd / equity_at_entry`
    
-   `holding_bars`
    
-   `entry_z`
    
-   `exit_reason` ∈ {STOP, TARGET, TIME}
    

----------

## 11) One-line Default Parameter Summary (for Codex config)

```json
{
  "Q": 1e-5,
  "R": 1e-3,
  "lambda": 0.94,
  "z_entry": 2.0,
  "z_exit": 0.5,
  "z_stop": 2.8,
  "cooldown_bars_5m": 12,
  "max_hold_bars_5m": 72,
  "max_daily_trades": 6,
  "max_spread": 0.0010,
  "hurst_window_15m": 100,
  "hurst_lag_max": 100,
  "hurst_block": 0.55,
  "hurst_full": 0.50,
  "hurst_size_scalar_caution": 0.50,
  "entry_limit_offset": 0.0005,
  "limit_timeout_bars": 2,
  "limit_fill_rate": 0.77,
  "limit_adverse_selection": 0.0001,
  "MAX_PORTFOLIO_HEAT": 0.02,
  "MAX_SINGLE_TRADE_RISK": 0.005,
  "kelly_lookback_trades": 100,
  "kelly_fraction_multiplier": 0.5,
  "kelly_cap": 0.20,
  "target_return_vol": 0.0025
}

```
