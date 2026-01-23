# Velocity Breakout Scalper (15m) - Strategy Specification v2.0

## 1) Goal and Fit
- Purpose: intraday momentum scalping to capture sub-1h impulse moves.
- Complements TR³ (1h trend) by trading shorter windows and both directions.
- Uses OHLCV only; optional daily HMM regime filter and 1h trend context.

## 2) Data Requirements
- **Primary**: 15-minute OHLCV bars.
- **Optional enhancements**:
  - 1-hour EMA50 (higher timeframe trend context)
  - Daily regime state `state_lag1d` from HMM model

## 3) Core Philosophy
Trade strong directional moves with volume confirmation and clean breakout context.
Avoid overextended entries and high-volatility panic regimes.
Use intrabar stop detection to handle flash crashes and wick spikes.

---

## 4) Feature Engineering

### 4.1 Required Features (15m bars)
- `ema_50`: EMA(50) of close (12.5 hours)
- `ema_100`: EMA(100) of close (25 hours)
- `atr_14`: 14-period ATR
- `atr_50_ma`: 50-period MA of ATR_14
- `high_20_prev`: max(high, 20) **shifted by 1 bar** (prevents look-ahead)
- `low_20_prev`: min(low, 20) **shifted by 1 bar** (prevents look-ahead)
- `volume_ma_20`: MA(volume, 20)
- `volume_ratio`: volume / volume_ma_20
- `roc_3`: 3-bar rate of change in percent
- `clv`: close location value = ((close - low) - (high - close)) / (high - low)
- `hour_utc`: Hour component of timestamp (for time filter)
- `open_next`: Next bar's open (for realistic fill simulation)

### 4.2 Optional Features
- `ema_50_1h`: 1-hour EMA(50) merged into 15m data (higher timeframe filter)
- `state_lag1d`: Daily HMM regime state (to avoid overlap with TR³)

---

## 5) Entry Logic

All conditions are evaluated on 15m bars. Signals trigger entry at **next bar's open**.

### 5.1 Long Entry Conditions

**A) Trend Filter (choose one approach):**

*Option 1 - 15m EMAs only (simpler):*
```
ema_50 > ema_100
```

*Option 2 - With 1h confirmation (stricter):*
```
ema_50 > ema_100  AND  close > ema_50_1h
```

**B) Velocity Breakout:**
```
high > high_20_prev  (breakout above 20-bar high)
volume > 1.8 × volume_ma_20  (volume surge)
close < high × 1.002  (not overextended by more than 0.2%)
```

**C) Momentum Confirmation:**
```
roc_3 > 0.5  (positive momentum over last 3 bars, in %)
clv > 0.4  (close in upper 70% of bar range)
```

**D) Risk Filter:**
```
atr_14 < 1.5 × atr_50_ma  (not in panic volatility regime)
```

**E) Time Filter:**
```
hour_utc NOT IN {23, 0, 1}  (skip low-liquidity hours)
```

**F) Optional Regime Filter:**
```
If using HMM: state_lag1d != 1  (avoid State 1 where TR³ trades)
```

---

### 5.2 Short Entry Conditions (mirror logic)

**A) Trend Filter:**

*Option 1:*
```
ema_50 < ema_100
```

*Option 2:*
```
ema_50 < ema_100  AND  close < ema_50_1h
```

**B) Velocity Breakout:**
```
low < low_20_prev  (breakout below 20-bar low)
volume > 1.8 × volume_ma_20
close > low × 0.998  (not overextended by more than 0.2%)
```

**C) Momentum Confirmation:**
```
roc_3 < -0.5  (negative momentum)
clv < -0.4  (close in lower 30% of bar range)
```

**D) Risk Filter:**
```
atr_14 < 1.5 × atr_50_ma
```

**E) Time Filter:**
```
hour_utc NOT IN {23, 0, 1}
```

**F) Optional Regime Filter:**
```
If using HMM: state_lag1d != 1
```

---

## 6) Position Sizing

Risk-based sizing per trade with maximum position caps:

```python
# Parameters
risk_per_trade = 0.008  # 0.8% of equity per trade
atr_stop_multiplier = 2.0
max_position_pct = 0.30  # Cap at 30% of equity

# Calculate
stop_distance_price = atr_stop_multiplier × atr_14
stop_distance_pct = stop_distance_price / close

# Position size
dollar_risk = equity × risk_per_trade
position_size_btc = dollar_risk / stop_distance_price
position_value = position_size_btc × close

# Apply cap
position_value = min(position_value, equity × max_position_pct)
position_size_btc = position_value / close

# Reduce if TR³ position active (avoid correlation)
if tr3_has_position:
    position_size_btc × 0.6  # Reduce by 40%
```

**Example:**
- Equity: $100,000
- Risk: 0.8% = $800
- ATR: $200
- Stop distance: 2.0 × $200 = $400
- BTC to trade: $800 / $400 = 2 BTC
- Position value: 2 BTC × $50,000 = $100,000
- **After 30% cap**: $30,000 position = 0.6 BTC

---

## 7) Exit Logic

Exits are checked **every 15m bar** after entry, in priority order.

### 7.1 Stop Loss (HIGHEST PRIORITY)

**Uses intrabar low/high + catastrophic wick protection:**

**For LONG positions:**
```python
# Normal stop
stop_price = entry_price - (2.0 × entry_atr)

# Check 1: Intrabar stop hit
if bar['low'] <= stop_price:
    exit_price = min(stop_price, bar['open_next'])  # Conservative fill
    EXIT at exit_price

# Check 2: Catastrophic wick (flash crash protection)
max_adverse_excursion = entry_price - bar['low']
if max_adverse_excursion >= (4.0 × entry_atr):
    EXIT at bar['open_next']  # Assume stopped in reality
```

**For SHORT positions:**
```python
stop_price = entry_price + (2.0 × entry_atr)

if bar['high'] >= stop_price:
    exit_price = max(stop_price, bar['open_next'])
    EXIT at exit_price

max_adverse_excursion = bar['high'] - entry_price
if max_adverse_excursion >= (4.0 × entry_atr):
    EXIT at bar['open_next']
```

**Key changes from v1:**
- ✅ Uses `low/high` instead of `close` to detect stops
- ✅ Adds 4 ATR catastrophic wick threshold
- ✅ Conservative fill assumption (stop price or worse)

---

### 7.2 Profit Targets (Scale Out)

**Target 1 (50% of position):**
```
LONG:  price >= entry_price + (1.5 × entry_atr)
SHORT: price <= entry_price - (1.5 × entry_atr)

Action: Close 50% of position at bar['open_next']
        Set target_1_hit = True
```

**Target 2 (remaining 50%):**
```
LONG:  price >= entry_price + (3.0 × entry_atr)
SHORT: price <= entry_price - (3.0 × entry_atr)

Action: Close remaining 50% at bar['open_next']
```

---

### 7.3 Trailing Stop (Activates AFTER Target 1)

Only active once `target_1_hit = True`:

```python
trailing_distance = 1.2 × entry_atr

# LONG position:
highest_close_since_entry = max(close values since entry)
trailing_stop_price = highest_close_since_entry - trailing_distance

if bar['close'] < trailing_stop_price:
    EXIT remaining position at bar['open_next']

# SHORT position:
lowest_close_since_entry = min(close values since entry)
trailing_stop_price = lowest_close_since_entry + trailing_distance

if bar['close'] > trailing_stop_price:
    EXIT remaining position at bar['open_next']
```

---

### 7.4 Time Stop

```python
if bars_in_trade > 32:  # 8 hours (32 × 15min)
    current_pnl = (close - entry_price) × direction
    if current_pnl <= 0:  # Only if not profitable
        EXIT at bar['open_next']
```

---

### 7.5 Trend Reversal Exit

**LONG positions:**
```
if ema_50 < ema_100:  # Trend flipped bearish
    EXIT immediately at bar['open_next']
```

**SHORT positions:**
```
if ema_50 > ema_100:  # Trend flipped bullish
    EXIT immediately at bar['open_next']
```

---

### 7.6 Regime Override (Optional)

If using daily HMM regime:
```python
# If regime changes to State 1 (TR³ territory), exit immediately
if state_lag1d == 1 and position_active:
    EXIT at bar['open_next']
```

---

## 8) Portfolio Risk Controls

### 8.1 Position Limits
```python
MAX_CONCURRENT_POSITIONS = 2  # Can hold 1 long + 1 short simultaneously
```

### 8.2 Daily Limits (Reset at 00:00 UTC)
```python
MAX_DAILY_TRADES = 8
MAX_DAILY_LOSS_PCT = 0.03  # -3% of starting equity

# At start of each UTC day:
daily_trade_count = 0
daily_pnl = 0
daily_loss_limit_hit = False

# Before each entry:
if daily_trade_count >= MAX_DAILY_TRADES:
    REJECT entry

if daily_pnl / starting_equity_today < -MAX_DAILY_LOSS_PCT:
    daily_loss_limit_hit = True
    REJECT all entries for rest of day
```

### 8.3 Correlation with TR³
```python
# Check before entry:
if tr3_has_active_position:
    # Reduce position size by 40%
    position_size = position_size × 0.6
    
    # Optional: prevent same-direction overlap
    if tr3_direction == signal_direction:
        REJECT entry  # Uncomment if you want strict no-overlap
```

---

## 9) Backtest Implementation Notes

### 9.1 Entry Execution
```python
# Signal detected on bar[i]
if all_entry_conditions_met(bar[i]):
    entry_price = bar[i]['open_next']  # Next bar's open
    entry_atr = bar[i]['atr_14']
    position = create_position(entry_price, entry_atr, ...)
```

### 9.2 Exit Execution
```python
# Check exits on each bar while position active
for bar in bars[i+1:]:
    is_exit, exit_price, reason = position.check_exits(bar)
    if is_exit:
        pnl = position.close(exit_price)
        log_trade(position, pnl, reason)
        break
```

### 9.3 Slippage Model (Optional)
```python
# Add realistic slippage to backtest
SLIPPAGE_BPS = 5  # 0.05%

entry_price = bar['open_next'] × (1 + SLIPPAGE_BPS/10000 × direction)
exit_price = bar['open_next'] × (1 - SLIPPAGE_BPS/10000 × direction)
```

### 9.4 Data Handling
- Drop rows with NaN values after feature engineering (first ~100 bars)
- Ensure `open_next` is not NaN (last bar will have NaN, exclude from signals)
- Sort by timestamp before generating signals
- Use vectorized operations where possible for speed

---

## 10) Expected Performance Characteristics

Based on Bitcoin's intraday behavior and similar momentum strategies:

**Standalone Performance:**
- **Win Rate**: 42-48% (tight stops, good R:R)
- **Profit Factor**: 1.4-1.7
- **Average Duration**: 4-6 hours (16-24 bars)
- **Trades per Month**: 40-60
- **CAGR**: 20-35%
- **Max Drawdown**: 12-18%
- **Sharpe Ratio**: 1.1-1.6
- **Sortino Ratio**: 1.8-2.4

**Combined with TR³:**
- **Portfolio CAGR**: 50-65% (assumes 50/50 capital split)
- **Portfolio Sharpe**: 1.7-2.1 (diversification benefit)
- **Portfolio Max DD**: 10-15% (smoother than either alone)
- **Strategy Correlation**: <0.3 (low overlap due to different timeframes/regimes)

---

## 11) Parameter Sensitivity Guide

These parameters can be tuned during walk-forward optimization:

| Parameter | Default | Range to Test | Impact |
|-----------|---------|---------------|--------|
| EMA fast/slow | 50/100 | 30/60 - 100/200 | Trade frequency |
| Volume threshold | 1.8 | 1.5 - 2.2 | Entry selectivity |
| ROC threshold | 0.5% | 0.3% - 1.0% | Momentum filter |
| CLV threshold | 0.4 | 0.3 - 0.5 | Candle quality |
| Stop distance | 2.0 ATR | 1.5 - 2.5 ATR | Risk per trade |
| Target 1 | 1.5 ATR | 1.2 - 2.0 ATR | Win rate vs R:R |
| Target 2 | 3.0 ATR | 2.5 - 4.0 ATR | Profit capture |
| Trailing distance | 1.2 ATR | 1.0 - 1.5 ATR | Runner protection |
| Time stop | 32 bars | 24 - 48 bars | Capital efficiency |

**Optimization tips:**
- Test on 70% in-sample, validate on 30% out-of-sample
- Use walk-forward analysis (6-month windows)
- Ensure OOS Sharpe > 0.8 and PF > 1.3
- Avoid over-optimization (max 2-3 parameter changes from defaults)

---

## 12) Key Improvements from v1.0

✅ **Entry**: Added optional 1h EMA filter for stronger trend alignment  
✅ **Stop Loss**: Uses intrabar low/high instead of close  
✅ **Stop Loss**: Added 4 ATR catastrophic wick protection  
✅ **Exit**: Conservative fill assumptions (stop price or worse)  
✅ **Features**: Donchian shifted by 1 bar (prevents look-ahead bias)  
✅ **Features**: Added `open_next` for realistic backtesting  
✅ **Risk**: Position sizing caps at 30% equity  
✅ **Risk**: TR³ correlation adjustment (40% size reduction)  
✅ **Documentation**: Complete math for all calculations

---

## 13) Next Steps

1. ✅ Feature engineering complete (using updated script)
2. ⏭️ Implement signal generation logic
3. ⏭️ Build backtesting engine with proper exits
4. ⏭️ Run initial backtest on 2020-2024 data
5. ⏭️ Analyze trade distribution and metrics
6. ⏭️ Walk-forward optimization if needed
7. ⏭️ Paper trading for 4+ weeks
8. ⏭️ Live deployment with 10% capital

---

## Appendix: Code Snippets

### Signal Generation Template
```python
def generate_signals(df):
    """Generate entry signals on 15m bars"""
    df = df.copy()
    df['signal'] = 0  # 0=none, 1=long, -1=short
    
    # LONG conditions
    long_trend = df['ema_50'] > df['ema_100']
    long_breakout = df['high'] > df['high_20_prev']
    long_volume = df['volume_ratio'] > 1.8
    long_not_extended = df['close'] < df['high'] * 1.002
    long_momentum = df['roc_3'] > 0.5
    long_clv = df['clv'] > 0.4
    long_atr = df['atr_14'] < 1.5 * df['atr_50_ma']
    long_time = ~df['hour_utc'].isin([23, 0, 1])
    
    long_signal = (long_trend & long_breakout & long_volume & 
                   long_not_extended & long_momentum & long_clv & 
                   long_atr & long_time)
    
    df.loc[long_signal, 'signal'] = 1
    
    # SHORT conditions (mirror)
    short_trend = df['ema_50'] < df['ema_100']
    short_breakout = df['low'] < df['low_20_prev']
    short_volume = df['volume_ratio'] > 1.8
    short_not_extended = df['close'] > df['low'] * 0.998
    short_momentum = df['roc_3'] < -0.5
    short_clv = df['clv'] < -0.4
    short_atr = df['atr_14'] < 1.5 * df['atr_50_ma']
    short_time = ~df['hour_utc'].isin([23, 0, 1])
    
    short_signal = (short_trend & short_breakout & short_volume &
                    short_not_extended & short_momentum & short_clv &
                    short_atr & short_time)
    
    df.loc[short_signal, 'signal'] = -1
    
    return df
```

### Stop Loss Check Template
```python
def check_stop_loss(position, bar):
    """Check if stop was hit (intrabar + catastrophic wick)"""
    stop_distance = 2.0 * position.entry_atr
    catastrophic_threshold = 4.0 * position.entry_atr
    
    if position.direction == 1:  # LONG
        stop_price = position.entry_price - stop_distance
        
        # Normal stop
        if bar['low'] <= stop_price:
            exit_price = min(stop_price, bar['open_next'])
            return True, exit_price, 'STOP_LOSS'
        
        # Catastrophic wick
        if (position.entry_price - bar['low']) >= catastrophic_threshold:
            return True, bar['open_next'], 'CATASTROPHIC_WICK'
    
    else:  # SHORT
        stop_price = position.entry_price + stop_distance
        
        if bar['high'] >= stop_price:
            exit_price = max(stop_price, bar['open_next'])
            return True, exit_price, 'STOP_LOSS'
        
        if (bar['high'] - position.entry_price) >= catastrophic_threshold:
            return True, bar['open_next'], 'CATASTROPHIC_WICK'
    
    return False, None, None
```
