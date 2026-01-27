"""
Centralized configuration for HMM Trading System.

All paths, parameters, and train/val/test splits in one place.
"""

from pathlib import Path
from dataclasses import dataclass, field


# Project root
PROJECT_ROOT = Path(__file__).parent

# Data paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
CACHE_DIR = DATA_DIR / "cache"

# Output paths
OUTPUT_DIR = PROJECT_ROOT / "outputs"
MODELS_DIR = OUTPUT_DIR / "models"
LOGS_DIR = OUTPUT_DIR / "logs"
PLOTS_DIR = OUTPUT_DIR / "plots"
REPORTS_DIR = OUTPUT_DIR / "reports"


@dataclass
class DataConfig:
    """Data file paths."""
    
    # Raw data
    btc_1d_raw: Path = RAW_DIR / "btc_1d_coinbase.csv"
    btc_1h_raw: Path = RAW_DIR / "btc_1h_coinbase.csv"
    
    # Processed data
    btc_1d_features: Path = PROCESSED_DIR / "btc_1d_features.csv"
    btc_1d_states: Path = PROCESSED_DIR / "btc_1d_with_states.csv"
    btc_1h_features: Path = PROCESSED_DIR / "btc_1h_features.csv"
    btc_1h_features_tr: Path = PROCESSED_DIR / "btc_1h_features_tr.csv"


@dataclass
class HMMConfig:
    """HMM training configuration."""
    
    # Train/Val/Test splits
    train_end: str = "2019-12-31"
    val_end: str = "2021-12-31"
    
    # Model parameters
    n_components: int = 3
    covariance_type: str = "diag"
    n_iter: int = 500
    restarts: int = 5
    random_seed: int = 42
    
    # Post-processing
    min_dwell: int = 3  # Minimum state duration in days
    
    # State labels
    state_labels: dict = field(default_factory=lambda: {
        0: "Mean Reversion",
        1: "Trending (Longs Only)",
        2: "Bearish (Sit Out)",
    })


@dataclass
class TR3Config:
    """TR³ strategy configuration."""
    
    # Regime filter
    regime_col: str = "D1_State_lag1d"
    allowed_regime: int = 1  # Only trade in State 1
    
    # Entry conditions
    donchian_period: int = 20
    adx_min: float = 14
    r2_min: float = 0.10
    clv_min: float = 0.55
    thrust_atr_mult: float = 0.75
    ema_fast: int = 50
    ema_slow: int = 200
    
    # Exit: Fail-to-hold
    clv_fail_max: float = 0.35
    fail_level_atr: float = 0.25
    fth_disable_after_atr: float = 0.5
    
    # Exit: Breakeven
    be_activate_atr: float = 0.75
    be_cushion_atr: float = -0.02
    be_disable_after_atr: float = 1.0
    be_one_bar_delay: bool = True
    
    # Exit: Trailing stop
    trail_atr_n: int = 14
    trail_mult_base: float = 2.5
    trail_mult_1: float = 3.5
    trail_mult_2: float = 4.5
    
    # Exit: EMA break
    ema_break_relax_after_atr: float = 1.0
    ema_break_cushion_atr: float = 0.25
    
    # Exit: Time-based
    no_progress_hours: int = 12
    no_progress_atr: float = 0.50
    time_stop_hours: int = 168  # 7 days
    
    # Risk management
    fee_bps: float = 0.0
    max_loss_cap: float = 0.08
    leverage: float = 1.0


@dataclass
class BacktestConfig:
    """Backtesting configuration."""
    
    # Date ranges
    train_end: str = "2019-12-31"
    val_end: str = "2021-12-31"
    
    # Output
    save_trade_log: bool = True
    save_equity_curve: bool = True
    
    # Monte Carlo
    mc_runs: int = 1000
    mc_confidence: float = 0.95


# Asset universe for multi-asset support
ELITE10_SYMBOLS = [
    "BTC-USD",
    "ETH-USD",
    "SOL-USD",
    "AVAX-USD",
    "DOT-USD",
    "LINK-USD",
    "AAVE-USD",
    "POL-USD",
    "LTC-USD",
    "NEAR-USD",
]

ASSET_ROLES = {
    "BTC-USD": "Anchor — Primary trend setter",
    "ETH-USD": "Proxy — Altseason leader",
    "SOL-USD": "High-Beta — Extreme thrust potential",
    "AVAX-USD": "Ecosystem — Regime-responsive",
    "DOT-USD": "Interoperability — Different cycle",
    "LINK-USD": "Infrastructure — Relative strength",
    "AAVE-USD": "DeFi Bluechip — Non-correlated signals",
    "POL-USD": "Exchange — Trends when flat",
    "LTC-USD": "Legacy — Clean Donchian breakouts",
    "NEAR-USD": "Wildcard — High volatility",
}


# Default instances
data_config = DataConfig()
hmm_config = HMMConfig()
tr3_config = TR3Config()
backtest_config = BacktestConfig()
