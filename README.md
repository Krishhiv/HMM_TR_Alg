# HMM_Det: Regime-Filtered Crypto Trading System

A quantitative trading system that uses **Hidden Markov Models (HMM)** to detect market regimes and applies the **TR³ (Thrust–Retention–Ride)** strategy during favorable conditions.

## Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA PIPELINE                             │
│  Coinbase API → Raw OHLCV → Feature Engineering → HMM States    │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    REGIME DETECTION (HMM)                        │
│  3-State Gaussian HMM on BTC Daily Data:                        │
│    • State 0: Mean Reversion                                    │
│    • State 1: Trending (Longs Only) ✅ Trade here              │
│    • State 2: Bearish (Sit Out)                                 │
└──────────────────────────┬──────────────────────────────────────┘
                           │ Lagged State (1D)
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    TR³ STRATEGY (1H)                             │
│  Entry: Donchian breakout OR ATR thrust + regime filter         │
│  Exits: FTH → Breakeven → Trail → EMA break → Time stop         │
└─────────────────────────────────────────────────────────────────┘
```

## Project Structure

```
HMM_Det/
├── config.py                 # Centralized configuration
├── README.md                 # This file
│
├── src/                      # Source code
│   ├── data/                 # Data collection
│   │   └── coinbase_downloader.py
│   ├── features/             # Feature engineering
│   │   ├── daily_features.py
│   │   └── hourly_features.py
│   ├── hmm/                  # HMM regime detection
│   │   └── model.py
│   ├── strategy/             # Trading strategy
│   │   └── tr3_engine.py
│   ├── backtest/             # Backtesting
│   │   └── metrics.py
│   └── utils/                # Utilities
│
├── scripts/                  # Runnable entry points
│   ├── run_holdout.py        # Out-of-sample backtest
│   ├── run_optimization.py   # Parameter grid search
│   └── run_daily_update.py   # Daily pipeline
│
├── data/
│   ├── raw/                  # Downloaded OHLCV
│   ├── processed/            # Feature-engineered datasets
│   └── cache/                # Monthly download cache
│
└── outputs/
    ├── models/               # Saved HMM models
    ├── logs/                 # Trade logs
    ├── plots/                # Visualizations
    └── reports/              # Summary reports
```

## Quick Start

### 1. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Download Data

```bash
python -m src.data.coinbase_downloader
```

### 3. Generate Features

```bash
python -m src.features.daily_features
python -m src.features.hourly_features
```

### 4. Train HMM & Run Backtest

```bash
python scripts/run_holdout.py
```

## Key Components

### HMM Regime Detection

Uses a 3-state Gaussian HMM trained on daily BTC features:
- **Log returns** (direction)
- **Garman-Klass volatility** (OHLC-based vol)
- **Volume z-score** (volume pressure)
- **EMA slope** (trend direction)
- **Candle body %** (momentum)

Minimum dwell smoothing prevents unrealistic rapid state switches.

### TR³ Strategy

**Entry conditions** (all must be true):
- HMM State = 1 (Trending)
- Price > EMA50 > EMA200
- Donchian breakout OR ATR thrust move
- CLV ≥ 0.55, ADX ≥ 14, R² ≥ 0.10

**Exit tiers**:
1. **Fail-to-hold**: Quick exit if price fails (disabled after +0.5 ATR)
2. **Breakeven**: Protect capital (active 0.75-1.0 ATR advance)
3. **Ratcheting trail**: 2.5 → 3.5 → 4.5 ATR as profit grows
4. **EMA50 break**: Relaxed when in profit
5. **No-progress**: Exit if stalling
6. **Time stop**: 7 days max hold

## Configuration

All parameters centralized in `config.py`:

```python
from config import tr3_config, hmm_config

# Modify TR³ parameters
tr3_config.adx_min = 18
tr3_config.clv_min = 0.60

# Modify HMM settings
hmm_config.train_end = "2020-12-31"
```

## Train/Val/Test Splits

| Split | Period | Purpose |
|-------|--------|---------|
| Train | → 2019-12-31 | Fit HMM and scaler |
| Validation | 2020-01-01 → 2021-12-31 | Model selection |
| Test | 2022-01-01 → | Out-of-sample evaluation |

## License

MIT
