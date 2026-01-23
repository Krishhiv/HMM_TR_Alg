# Velocity Breakout Scalper - Development Plan

## Phase 0: Setup and Data
1) Confirm data coverage: 2+ years of 15m BTC OHLCV.
2) Validate data hygiene: missing bars, timezone alignment, splits/rollover.
3) Generate 1h EMA reference series (align to 15m bars).
4) Optional: join daily HMM regime state `D1_State_lag1d`.

## Phase 1: Feature Engineering
1) Implement EMA_50_15m, EMA_100_15m.
2) Implement ATR_14_15m and ATR_50_MA.
3) Implement Donchian 20 high/low.
4) Implement Volume_MA_20 and Volume_Ratio.
5) Implement ROC_3 and CLV.
6) Implement UTC hour and time filter mask.

## Phase 2: Signal Generation
1) Encode long and short condition sets as boolean masks.
2) Apply time filter (skip 23, 0, 1 UTC).
3) Emit signal: 1 = long, -1 = short, 0 = none.
4) Add optional HMM regime gate for entries/exits.

## Phase 3: Trade Engine
1) Entry at next bar open after signal.
2) Position sizing with risk_per_trade = 0.8% and 30% cap.
3) Implement all exits:
   - Stop loss at 2.0 * Entry_ATR
   - Target_1 at 1.5 * Entry_ATR (scale out 50%)
   - Target_2 at 3.0 * Entry_ATR (exit remainder)
   - Trailing stop at 1.2 * Entry_ATR after Target_1
   - Time stop after 32 bars if not profitable
   - Trend reversal EMA cross
4) Enforce portfolio limits:
   - max positions = 2
   - max daily trades = 8
   - max daily loss = -3%
5) Daily reset at 00:00 UTC.

## Phase 4: Backtest and Validation
1) Run baseline backtest across full history.
2) Validate metrics (Sharpe > 1.0, PF > 1.3).
3) Confirm trade logs and rule adherence.
4) Check sensitivity to slippage and fee assumptions.

## Phase 5: Optimization and Robustness
1) Parameter sweeps:
   - ATR stop multiplier (1.5-2.5)
   - Volume threshold (1.5-2.2)
   - ROC threshold (0.3-0.8)
   - Donchian lookback (15-30)
2) Walk-forward analysis (6-month windows).
3) Stress test 2022 bear market and high-volatility windows.
4) Compare IS vs OOS degradation (<20% target).

## Phase 6: Paper Trading
1) Run 4-week paper test.
2) Track fills, slippage, trade duration, win rate.
3) Validate correlation with TR3 (<0.3 target).
4) Adjust risk caps if daily loss limit hit frequently.

## Phase 7: Live Rollout
1) Start with 10% capital allocation.
2) Scale after 50+ trades with stable metrics.
3) Weekly monitoring and retraining checks.
4) Pause if Sharpe < 0.8 or drawdown breaches policy.

## Deliverables
- Feature engineering module.
- Signal generation module.
- Trade engine with exits and risk limits.
- Backtest report with metrics and equity curve.
- Sensitivity and walk-forward summary.

