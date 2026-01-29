# HMM-TR3 Strategy Specification (V2 Standard)

This document preserves the exact configurations used to achieve the **22.95% CAGR** portfolio result (Backtest Period: 2022-2025).

## 1. BTC Strategy Configuration
- **Asset**: Bitcoin (BTC)
- **HMM Model Type**: Gaussian HMM (3-state)
- **HMM Features**: 
  - `Log_Returns`
  - `GKVol_20` (Garman-Klass Volatility)
  - `VolZ_20` (Volatility Z-Score)
  - `EMA_20_slope`
  - `BodyPct`
  - `ClosePosInRange`
  - `CloseOverEMA20`
- **TR3 Strategy Parameters**: Standard Baseline
- **Risk Management (ECT)**:
  - `risk_high`: **1.3x** (Aggressive Bullish Exposure)
  - `risk_low`: 0.5x
  - `window`: 40 trades

## 2. ETH Strategy Configuration
- **Asset**: Ethereum (ETH)
- **HMM Model Type**: Gaussian HMM (3-state)
- **HMM Features (Optimized for ETH)**:
  - `Log_Returns`
  - `GKVol_20`
  - `VolZ_20`
  - `EMA_20_slope`
  - `BodyPct`
  - `ClosePosInRange`
  - **`CumRet_30d`** (Critical Alpha driver for ETH)
- **TR3 Strategy Parameters**: Standard Baseline
- **Risk Management (ECT)**:
  - `risk_high`: 1.0x
  - `risk_low`: 0.5x
  - `window`: 30 trades

## 3. Portfolio Orchestration
- **Simulation Mode**: Walk-Forward (30-day Retraining)
- **Allocation Logic**: Dynamic Capital Efficiency
  - **100% BTC**: When only BTC signal is active.
  - **100% ETH**: When only ETH signal is active.
  - **70% BTC / 30% ETH**: When BOTH signals are active (Weighted to favor BTC's higher Sharpe).
  - **100% Cash**: When neither signal is active.
- **Return Engine**: Geometric compounding with corrected signal-bar shift.

## 4. Final Performance Metrics (2022-2025)
| Metric | Result |
| :--- | :--- |
| **Total Return** | 128.35% |
| **CAGR** | 22.95% |
| **Max Drawdown** | -13.35% |
| **Sharpe Ratio** | 1.05 |
