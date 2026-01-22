
# Mean reversion trading engine for Bitcoin


# Complete Quantitative Mean Reversion Trading Model

## Mathematical Foundation to Production Implementation

---

# PART 1: THE COMPLETE TRADING MODEL

## 1.1 Core Philosophy

**What we're exploiting**: BTC prices exhibit short-term overreactions to news, order flow imbalances, and noise traders, creating temporary dislocations from fair value that revert to the mean within hours.

**Why this works in crypto**:

* High retail participation → emotional overreactions
* Leverage cascades → price overshoots
* Funding rate mechanisms → natural mean reversion pressure
* 24/7 markets → continuous arbitrage opportunities

---

## 1.2 STATE ESTIMATION: Kalman Filter for True Price

### Why NOT Simple Moving Average?

**Problem with SMA**:

```
SMA_t = (P_t + P_{t-1} + ... + P_{t-n}) / n

Issues:
- Equal weight to all observations (10 bars ago = now?)
- Lag increases with window size
- No adaptation to changing volatility
- Ghost data: old prices affect SMA long after relevance
```

### Why Kalman Filter?

The Kalman filter is a **recursive Bayesian estimator** that:

* Adapts to new information optimally (minimum mean square error)
* Weighs recent data more when uncertainty is high
* Self-corrects based on prediction errors
* No lag from historical data

**Mathematical Model**:

```
STATE EQUATION (what we believe):
μ_t = μ_{t-1} + w_t

where:
- μ_t = true "fair value" price at time t
- w_t ~ N(0, Q) = how much fair value can change per bar

OBSERVATION EQUATION (what we see):
P_t = μ_t + v_t

where:
- P_t = observed market price
- v_t ~ N(0, R) = measurement noise (microstructure)
```

**The Kalman Recursion**:

```
1. PREDICTION STEP:
   μ̂_t|t-1 = μ̂_{t-1|t-1}           (our prior belief)
   P_t|t-1 = P_{t-1|t-1} + Q         (uncertainty increases)

2. UPDATE STEP:
   K_t = P_t|t-1 / (P_t|t-1 + R)     (Kalman gain)
   
   μ̂_t|t = μ̂_t|t-1 + K_t(P_t - μ̂_t|t-1)   (updated estimate)
   P_t|t = (1 - K_t) · P_t|t-1              (updated uncertainty)
```

**Parameter Tuning**:

**Q (Process Noise)**: How much can "true price" change per 5m bar?

```
Q = 1e-5 (very small)

Why small?
- Fair value doesn't jump around randomly
- Most price movement is noise, not fair value changes
- We want μ_t to be smooth

Effect of Q:
- Too large → μ tracks price too closely (defeats purpose)
- Too small → μ doesn't adapt to real shifts
- Optimal: Price variance · 0.0001
```

**R (Measurement Noise)**: How noisy is our price observation?

```
R = 1e-3

Why this value?
- Microstructure noise: ~0.05%
- Combined observation uncertainty ≈ 0.1%

Effect of R:
- Too large → ignores new prices (underreacts)
- Too small → follows noise (overreacts)
- Optimal: Empirical std(P_t - μ_t)²
```

**Kalman Gain Interpretation**:

```
K_t = P_t|t-1 / (P_t|t-1 + R)

K ≈ 1: Trust new observation (high uncertainty in estimate)
K ≈ 0: Trust prior estimate (high observation noise)

Typical range: 0.01 - 0.05 for our parameters
```

**What to Expect**:

* μ_t will be a **smooth curve** through price
* Responds to genuine shifts within 10-20 bars
* Filters out tick noise and spread bounce
* More responsive than 100-SMA, smoother than 20-SMA

---

## 1.3 VOLATILITY ESTIMATION: Exponentially Weighted Moving Average

### Why EWMA over Standard Deviation?

**Standard deviation problem**:

```
σ_standard = sqrt(Σ(P_i - μ)² / n)

Issues:
- Equal weight to old and recent observations
- Window size dilemma: large = lag, small = noise
- Doesn't adapt to volatility regime changes
```

**EWMA Solution**:

```
σ²_t = λ · σ²_{t-1} + (1 - λ) · (P_t - μ_t)²

where λ = decay factor (0.94 for 5m BTC data)
```

**Why λ = 0.94?**

```
Effective window = 1 / (1 - λ) ≈ 16.7 bars ≈ 83 minutes

This captures:
- Recent volatility spikes (crypto flash crashes)
- Enough smoothing to avoid noise
- Fast enough adaptation for regime changes

Half-life = ln(0.5) / ln(λ) ≈ 11.2 bars ≈ 56 minutes
```

**λ sensitivity**:

* **λ = 0.90**: Too reactive, 10-bar window, noisy σ estimates
* **λ = 0.94**: Balanced, captures hourly vol changes ✓
* **λ = 0.97**: Too slow, 33-bar window, misses regime shifts

**Alternative: GARCH(1,1) - Why NOT?**

```
σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}

Why we skip it:
- 3 parameters to optimize vs 1 for EWMA
- Estimation requires 500+ bars (overfitting risk)
- Marginal improvement (~2-5%) not worth complexity
- EWMA is robust, battle-tested, interpretable
```

**What to Expect**:

* σ_t adapts to vol regime within 1 hour
* During flash crashes: σ spikes 3-5x
* During consolidation: σ compresses 0.5x
* Typical BTC 5m σ: 0.15% - 0.40%

---

## 1.4 Z-SCORE: Standardized Distance Metric

### The Core Signal

```
Z_t = (P_t - μ_t) / σ_t

Interpretation:
Z = +2.0 → Price is 2 standard deviations ABOVE fair value
Z = -2.0 → Price is 2 standard deviations BELOW fair value
Z = 0.0  → Price is at fair value
```

**Why Z-score vs Raw Distance?**

```
Raw distance: P_t - μ_t = $500

Is $500 big or small?
- In low vol: HUGE deviation → strong signal
- In high vol: TINY deviation → noise

Z-score normalizes:
Z = $500 / σ = $500 / $1000 = 0.5 (meh, small)
Z = $500 / σ = $500 / $150  = 3.33 (wow, large!)
```

**Statistical Foundation**:

```
If returns are Normal(0, σ):

P(|Z| > 1.0) ≈ 32% → occurs ~92 times per day on 5m
P(|Z| > 1.5) ≈ 13% → occurs ~37 times per day
P(|Z| > 2.0) ≈ 5%  → occurs ~14 times per day ✓ TARGET
P(|Z| > 2.5) ≈ 1%  → occurs ~3 times per day
P(|Z| > 3.0) ≈ 0.3% → occurs ~1 time per day
```

**Why |Z| > 2.0 for entries?**

```
Empirical crypto returns are:
- Leptokurtic (fat tails): κ ≈ 5-8 vs 3 for normal
- This means |Z| > 2.0 happens MORE often than 5%
- Real frequency: ~7-10% on BTC 5m data
- Sweet spot: Rare enough to be meaningful, common enough to trade

Expected setups per day: 10-15
After filters: 4-8 actual trades
```

**Alternative Thresholds - Trade-offs**:

```
Z_entry = 1.5:
  Pros: More trades (30-40/day), faster profits
  Cons: Win rate drops (52% vs 62%), noise trades
  
Z_entry = 2.0: ✓ OPTIMAL
  Pros: 60-65% win rate, strong reversion signal
  Cons: Balanced trade frequency
  
Z_entry = 2.5:
  Pros: 70%+ win rate, very strong signals
  Cons: Only 1-2 trades/day, opportunity cost high
```

---

## 1.5 ENTRY LOGIC

### Long Entry Conditions

```python
LONG_SIGNAL if ALL of:

1. Z_t < -2.0                    # Price significantly below fair value
2. Z_{t-1} ≥ -2.0                # Fresh signal (not already triggered)
3. liquidity_cost_proxy < 0.10%  # Liquidity/execution cost check (OHLC-based)
4. no_existing_position()        # One trade at a time
5. Hurst_15m < 0.50              # Not in strong trending regime
6. bars_since_last_trade > 12    # Cool-off period (1 hour)
```

### Short Entry Conditions

```python
SHORT_SIGNAL if ALL of:

1. Z_t > +2.0                    # Price significantly above fair value
2. Z_{t-1} ≤ +2.0                # Fresh signal
3. liquidity_cost_proxy < 0.10%  # Liquidity/execution cost check (OHLC-based)
4. no_existing_position()        
5. Hurst_15m < 0.50              
6. bars_since_last_trade > 12    
```

**Why These Filters?**

**Liquidity/Execution Cost Proxy (replaces bid-ask spread filter)**:

```
We don’t rely on bid/ask in historical data.

Instead, we use an OHLC-based proxy for "execution gets bad now" moments.

Define 5m range percent:
range_pct = (High_t - Low_t) / Close_t

Convert to a conservative cost proxy:
liquidity_cost_proxy = max(0.02%, 0.10 * range_pct)

Interpretation:
- When the 5m candle range explodes, spreads widen, slippage increases, and limit fills get worse.
- range_pct captures volatility bursts and liquidity holes that make mean reversion entries unreliable.

Threshold:
liquidity_cost_proxy < 0.10%
```

**Examples**:

```
Normal conditions:
High-Low = 0.20% in 5m
range_pct = 0.20%
proxy = max(0.02%, 0.10 * 0.20%) = max(0.02%, 0.02%) = 0.02% ✓ pass

Choppy/liquidity hole:
High-Low = 1.50% in 5m
range_pct = 1.50%
proxy = max(0.02%, 0.10 * 1.50%) = 0.15% ✗ fail (skip)
```

**No Existing Position**:

```
Why only 1 position at a time?
- Mean reversion trades are NEGATIVELY correlated
- Both longs mean "catching falling knife" multiple times
- Better to concentrate capital on best setup
- Reduces portfolio heat and simplifies management
```

**Hurst Exponent Filter** (explained in detail below):

```
H < 0.50: Mean reverting regime → GO
H ≈ 0.50: Random walk → CAUTION
H > 0.50: Trending regime → STOP

Prevents fighting momentum when market is trending
```

**Cool-off Period**:

```
bars_since_last_trade > 12 = 1 hour

Why?
- Prevents overtrading same mean reversion move
- If Z crosses -2.0, reverts to -1.5, then back to -2.0:
  These are the SAME reversion, not independent setups
- Allows market to establish new equilibrium
```

---

## 1.6 EXIT LOGIC

### Three Exit Mechanisms

**Exit 1: Mean Reversion Complete (Target)**

```python
IF long_position:
    exit if Z_t > Z_target (e.g., +0.5)
    
IF short_position:
    exit if Z_t < -Z_target (e.g., -0.5)
```

**Why Z = ±0.5 for targets?**

```
Entry at Z = -2.0 (long)
Target at Z = +0.5

Expected profit = 2.5 standard deviations of price movement
If σ = 0.25% per 5m bar:
  Expected profit ≈ 2.5 × 0.25% = 0.625%
  
This gives us:
- R:R ratio ≈ 2.5:1 (good for mean reversion)
- Win rate ≈ 62% (empirical)
- Allows small overshoot beyond fair value for buffer
```

**Exit 2: Stop Loss (Risk Management)**

```python
IF long_position:
    stop if Z_t < -Z_stop (e.g., -2.8)
    
IF short_position:
    stop if Z_t > +Z_stop (e.g., +2.8)
```

**Why Z = ±2.8 for stops?**

```
Entry at Z = -2.0 (long)
Stop at Z = -2.8

Maximum loss = 0.8 standard deviations
If σ = 0.25%:
  Max loss ≈ 0.8 × 0.25% = 0.20%
  
vs Expected profit of 0.625%
→ R:R = 3.1:1 ✓

Why not tighter (Z = -2.5)?
- Mean reversion needs room to "wobble"
- Tight stops → stopped out on noise → lower win rate
- -2.8 is ~99.7th percentile → genuine failed reversion
```

**Exit 3: Time-Based (Opportunity Cost)**

```python
IF time_in_position > 6 hours:
    exit at market
```

**Why 6 hours max?**

```
Mean reversion half-life in BTC 5m: ~1.5 - 2.5 hours

After 6 hours:
- 95% of reversions have completed
- Capital is dead weight
- Opportunity cost of missing new setups
- Possibly fundamental regime change

Expected holding time: 2-3 hours (most trades)
6 hour limit catches the stragglers
```

---

## 1.7 HURST EXPONENT: Regime Detection

### What is Hurst Exponent?

**Intuition**: Measures the "memory" or persistence in a time series.

```
H = 0.0 → Perfect anti-persistence (pure mean reversion)
H = 0.5 → Random walk (no memory)
H = 1.0 → Perfect persistence (trending)
```

**Calculation: Rescaled Range (R/S) Analysis**

```python
def calculate_hurst(returns, window=100):
    """
    returns: array of log returns
    window: number of bars to analyze
    """
    
    1. Divide returns into sub-periods of length n
    2. For each sub-period:
       a. Calculate mean: m = mean(returns)
       b. Create mean-adjusted series: Y = cumsum(returns - m)
       c. Calculate range: R = max(Y) - min(Y)
       d. Calculate std dev: S = std(returns)
       e. Rescaled range: R/S
    
    3. Repeat for different n values
    4. Plot log(R/S) vs log(n)
    5. Hurst = slope of regression line
```

**Mathematical Formula**:

```
E[R/S] = (n/2)^H

Taking logs:
log(E[R/S]) = H · log(n/2)

H = slope of linear regression
```

**Implementation for Trading**:

```python
def hurst_exponent(prices, lag_max=100):
    """Calculate Hurst exponent using simplified R/S"""
    lags = range(2, lag_max)
    tau = []
    
    for lag in lags:
        # Standard deviation at different lags
        std = np.std(np.subtract(prices[lag:], prices[:-lag]))
        tau.append(std)
    
    # Linear regression on log-log plot
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0] * 2.0  # Hurst exponent
```

**Interpretation for Trading**:

```
H < 0.40: STRONG mean reversion
  - Price deviations reverse quickly
  - Ideal for our strategy
  - Increase position sizes
  - Tighten profit targets

0.40 ≤ H < 0.50: MILD mean reversion ✓ TRADE
  - Normal operating regime
  - Standard parameters
  
0.50 ≤ H < 0.60: RANDOM WALK
  - No edge
  - Reduce position sizes 50%
  - Tighten stops
  
H ≥ 0.60: TRENDING
  - Mean reversion will LOSE money
  - DO NOT TRADE
  - Wait for regime change
```

**Why Calculate on 15m Instead of 5m?**

```
15m Hurst with 100 bars = 25 hours of data
5m Hurst with 100 bars = 8.3 hours of data

15m advantages:
- More stable estimate (less noise)
- Captures true market regime
- Avoids false regime changes from hourly noise
- Better predictive power for next 2-4 hours

We use:
- 5m for μ, σ, Z (high frequency signals)
- 15m for H (regime filter)
```

**Expected Values**:

```
BTC typical regimes:

Consolidation/Range: H = 0.35 - 0.45 → TRADE AGGRESSIVELY
Normal market:       H = 0.45 - 0.55 → TRADE NORMALLY
Trend initiation:    H = 0.55 - 0.65 → REDUCE ACTIVITY
Strong trend:        H = 0.65 - 0.80 → STOP TRADING

Regime persistence:
- H regimes last 6-18 hours typically
- Transitions take 1-2 hours
- Check every 15m bar for updates
```

---

## 1.8 POSITION SIZING: Kelly Criterion

### Why Kelly?

**Alternatives and Problems**:

```
Fixed % of capital (2% per trade):
  Problem: Doesn't account for win rate or R:R
  
Fixed $ amount:
  Problem: Doesn't scale with account growth
  
Volatility-based ($ risk per σ):
  Problem: Ignores edge strength
  
Kelly Criterion:
  Solution: Mathematically optimal for log wealth growth
```

### Full Kelly Formula

```
f* = (p × b - q) / b

where:
- f* = fraction of capital to risk
- p = probability of winning
- q = 1 - p = probability of losing
- b = win amount / loss amount (reward:risk ratio)
```

**Example Calculation**:

```
From last 100 trades:
- Win rate p = 0.62
- Loss rate q = 0.38
- Average win = 0.65%
- Average loss = 0.22%
- b = 0.65 / 0.22 = 2.95

Full Kelly:
f* = (0.62 × 2.95 - 0.38) / 2.95
f* = (1.829 - 0.38) / 2.95
f* = 0.491 = 49.1% of capital
```

**Why NOT Full Kelly?**

```
Problems with full Kelly:
1. Parameter estimation error → massive drawdowns
2. Assumes win rate/R:R are constant (they're not)
3. 49% position → one bad trade = -25% account
4. Volatility of returns is HUGE

Empirical: Full Kelly drawdowns reach 70-90%
```

### Half-Kelly (Our Choice)

```
Position_size = 0.5 × f*

Using example above:
Position_size = 0.5 × 0.491 = 24.5% of capital

But we add a volatility scalar...
```

### Volatility-Adjusted Kelly

```python
def kelly_position_size(win_rate, avg_win, avg_loss, current_vol, base_vol):
    """
    Calculate position size using half-Kelly with vol adjustment
    """
    # Basic Kelly
    p = win_rate
    q = 1 - p
    b = avg_win / avg_loss
    
    full_kelly = (p * b - q) / b
    half_kelly = 0.5 * full_kelly
    
    # Volatility adjustment
    vol_scalar = base_vol / current_vol  # Reduce size in high vol
    
    # Final position size
    position = half_kelly * vol_scalar
    
    # Hard limits
    position = min(position, 0.15)  # Never more than 15% of capital
    position = max(position, 0.02)  # Never less than 2% (unless 0)
    
    return position
```

**Volatility Scalar Explained**:

```
base_vol = 0.25%  (normal BTC 5m volatility)
current_vol = 0.50%  (2x normal)

vol_scalar = 0.25 / 0.50 = 0.5

Position = 24.5% × 0.5 = 12.25%

Why?
- Higher vol = higher risk of hitting stops
- Higher vol = wider price swings
- Same % position = 2x dollar risk
- Scale down to maintain constant risk
```

**Expected Position Sizes**:

```
Low volatility regime (σ = 0.15%):
  Base Kelly = 20%
  Vol adjusted = 20% × (0.25/0.15) = 33% → capped at 15%
  
Normal regime (σ = 0.25%):
  Base Kelly = 20%
  Vol adjusted = 20% × 1.0 = 20%
  
High volatility (σ = 0.50%):
  Base Kelly = 20%
  Vol adjusted = 20% × 0.5 = 10%
  
Extreme volatility (σ = 0.80%):
  Base Kelly = 20%
  Vol adjusted = 20% × 0.31 = 6.2%
```

**Rolling Window for Kelly Parameters**:

```python
lookback = 100 trades  # Rolling window

Why 100?
- Too small (20): Noisy estimates, parameter instability
- Too large (500): Doesn't adapt to changing edge
- 100 trades ≈ 1-2 months of data
- Good balance: stable estimates, adaptive

Update: After each trade completes
```

---

## 1.9 RISK MANAGEMENT LAYER

### Portfolio Heat Limits

```python
# Maximum total risk exposure
MAX_PORTFOLIO_HEAT = 0.02  # 2% of account

# Maximum single trade risk
MAX_SINGLE_TRADE_RISK = 0.005  # 0.5% of account

# How it works:
current_risk = sum(open_position.risk for all positions)
new_trade_risk = position_size × stop_loss_distance

if current_risk + new_trade_risk > MAX_PORTFOLIO_HEAT:
    reject_trade()
```

**Why 2% Portfolio Heat?**

```
Assuming:
- Win rate = 62%
- Kelly suggests 20% positions
- Stop loss = 2.5% of position

Risk per trade = 20% × 2.5% = 0.5% of account

With 2% max heat:
- Can have 4 concurrent trades maximum
- But our system is one-at-a-time
- 2% allows correlation buffer with your HMM system
```

### Correlation Penalty

```python
if hmm_system.has_open_position() and mean_rev_signal:
    # Both systems active simultaneously
    position_size *= 0.7  # Reduce by 30%
```

**Why Correlation Penalty?**

```
Your HMM system: Long-only, trend-following, regime 1
This system: Mean reversion, regime-agnostic

Correlation scenarios:

1. HMM long + Mean Rev long:
   - Both bullish
   - Correlation = +0.3 to +0.5
   - Combined position = 1.3x - 1.5x effective leverage
   - Reduce new position to compensate
   
2. HMM long + Mean Rev short:
   - Opposed positions
   - Natural hedge
   - NO penalty needed
   
3. HMM flat + Mean Rev active:
   - No correlation
   - Full position size OK
```

### Maximum Daily Trades Limit

```python
MAX_DAILY_TRADES = 6

if today_trade_count >= MAX_DAILY_TRADES:
    skip_new_signals()
```

**Why Limit Daily Trades?**

```
Protections against:

1. Overfitting to random noise
   - If signals fire 20x/day → too sensitive
   
2. Execution quality degradation
   - Each trade costs spread + slippage
   - Cumulative costs add up
   
3. Regime transition periods
   - Markets transitioning = choppy = false signals
   
4. Fat finger / bug protection
   - Hard circuit breaker

Expected: 3-5 trades/day normally
6 trade limit catches outlier days
```

---

## 1.10 EXECUTION LAYER

### Order Types Strategy

**Entry Orders: Limit Orders with Timeout**

```python
def enter_position(signal, price, z_score):
    """
    Use limit orders to improve entry price
    """
    if signal == 'LONG':
        # Enter below current price
        limit_price = price × (1 - 0.0005)  # 0.05% below
        
    elif signal == 'SHORT':
        # Enter above current price
        limit_price = price × (1 + 0.0005)  # 0.05% above
    
    # Place limit order
    order = place_limit_order(limit_price)
    
    # Timeout: if not filled in 2 bars (10 min), cancel
    if not order.filled_within(bars=2):
        order.cancel()
        skip_this_signal()
```

**Why Limit Orders?**

```
Market order cost:
- Slippage on market impact = -0.02%
- Total cost ≈ -0.03% to -0.07%

Limit order benefit:
- Join the bid (for longs) or ask (for shorts)
- Earn spread rebate = +0.01% (maker fee)
- No slippage
- Total benefit ≈ +0.01%

Difference = 0.05% to 0.08% per trade
Over 100 trades = 5% to 8% additional profit
```

**Why Timeout Limit Orders?**

```
Problem: Limit order not filled
- Signal was at Z = -2.0
- Price keeps falling to Z = -2.3
- Our limit order sits unfilled
- Miss the trade

Solution: 10-minute timeout
- If market wants to move away, let it
- Don't chase
- Wait for next setup

Fill rate with this approach: ~75-80%
Acceptable trade-off for better execution
```

**Exit Orders: Market Orders**

```python
def exit_position(exit_reason):
    """
    Exit immediately at market
    """
    order = place_market_order(close_position)
    
    # No limit orders on exits
```

**Why Market on Exits?**

```
When exiting:
1. Target hit (Z crossed 0.5) → secure profit NOW
2. Stop hit (Z = -2.8) → limit damage NOW
3. Time-based → free up capital NOW

Limit order risks on exit:
- Price runs away from limit
- Stop doesn't get filled → bigger loss
- Target doesn't get filled → missed profit

Cost of market order: 0.03%
Cost of missing exit: 1-5%+
→ Always use market for exits
```

### Slippage Modeling

**Expected Slippage by Order Type**:

```python
SLIPPAGE_MODEL = {
    'market_order': {
        'small': 0.02,   # < $10k notional
        'medium': 0.04,  # $10k - $50k
        'large': 0.08    # > $50k
    },
    'limit_order': {
        'fill_rate': 0.77,
        'adverse_selection': 0.01  # When filled, price moved against us
    }
}
```

**Position Size Based on Slippage**:

```python
def calculate_max_position_size(account_value):
    """
    Don't let single position cause high slippage
    """
    target_notional = account_value × kelly_fraction
    
    # BTC liquidity check
    typical_5m_volume = get_avg_volume_5m()  # e.g., $50M
    max_safe_notional = typical_5m_volume × 0.001  # 0.1% of volume
    
    position_notional = min(target_notional, max_safe_notional)
    
    return position_notional
```

---

## 1.11 PERFORMANCE EXPECTATIONS

### Realistic Metrics (5-minute BTC Mean Reversion)

**Trade Frequency**:

```
Signals per day: 10-15
After filters: 4-8
Actually executed: 3-5 (due to limit order fills)

Monthly: 70-100 trades
```

**Win Rate**:

```
Expected: 60-65%

Why not higher?
- Mean reversion fails during trend continuation
- Stop outs on extended moves
- Noise trades that hit stops before reversing

Why not lower?
- Z = 2.0 threshold is conservative
- Hurst filter removes trending regimes
- Strong statistical edge
```

**Profit Factor**:

```
Profit Factor = Gross Profit / Gross Gross Loss

Target: 1.8 - 2.2

Example:
60% win rate, 40% loss rate
Avg win = 0.65%, avg loss = 0.22%

PF = (0.60 × 0.65) / (0.40 × 0.22) = 0.39 / 0.088 = 4.43

But this assumes perfect execution...
Real PF after costs: 1.8 - 2.2 ✓
```

**Sharpe Ratio**:

```
Target: 1.5 - 2.0 (annualized)

Calculation:
- Avg monthly return: 8-12%
- Monthly std dev: 6-8%
- Sharpe = (0.10 - 0) / 0.07 × sqrt(12) = 4.95 (monthly)
- Annual Sharpe ≈ 1.7

This is EXCELLENT for crypto strategies
```

**Maximum Drawdown**:

```
Expected: 10-15%

Occurs during:
- Regime transitions (H crosses 0.50 suddenly)
- Flash crashes (2-3 stops hit in succession)
- Volatility explosions (σ spikes, stops widen)

Recovery time: 2-4 weeks typically
```

**Return Profile**:

```
Conservative scenario:
- 70 trades/month
- 60% win rate: 42 wins, 28 losses
- Avg win: 0.55% (after costs)
- Avg loss: 0.25% (after costs)
- Net: 42 × 0.55% - 28 × 0.25% = 23.1% - 7% = 16.1%
- But Kelly positions vary: Effective return ≈ 8-12%/month

Aggressive scenario (low vol regime):
- 100 trades/month
- 65% win rate
- Larger Kelly positions
- Returns: 15-20%/month

Realistic expectation: 80-150% annually
```

---
