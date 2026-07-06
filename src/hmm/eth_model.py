"""
ETH-specific Hidden Markov Model for regime detection.

Uses a 3-state Gaussian HMM tuned for ETH dynamics:
    - State 0: Sideways (ranging/consolidating)
    - State 1: Bullish (trending up)
    - State 2: Bearish (trending down)

Key differences from BTC model:
    - Lower state stickiness (ETH switches regimes faster)
    - Adjusted date splits (ETH has shorter trading history)
    - Different min_dwell (faster transitions)
"""

from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler


# ETH-specific configuration
DEFAULT_CONFIG = {
    "n_components": 3,
    "covariance_type": "diag",
    "n_iter": 500,
    "tol": 1e-3,
    "min_covar": 1e-5,
    "random_state": 42,
    "restarts": 5,
    "min_dwell": 1,  # Reduced from 2 - allow faster transitions
}

# Features for ETH HMM - DIRECTIONAL features FIRST (priority order matters)
# Features for ETH HMM - OPTIMIZED (Set 7 from optimization)
HMM_FEATURES = [
    "CumRet_10d",        # Short-term momentum
    "CumRet_30d",        # Medium-term momentum (Key signal)
    "TrendScore",        # Distance from Moving Averages
]

# State labels for ETH
STATE_LABELS = {
    0: "Sideways",
    1: "Bullish", 
    2: "Bearish",
}


def compute_daily_features(df: pd.DataFrame, n: int = 20) -> pd.DataFrame:
    """Compute daily features for HMM training with better directional signals."""
    df = df.copy()
    
    # Log returns
    df["Log_Returns"] = np.log(df["Close"] / df["Close"].shift(1))
    df["Abs_Return"] = np.abs(df["Log_Returns"])
    df["Squared_Return"] = df["Log_Returns"] ** 2
    
    # Garman-Klass volatility
    gk_var_bar = (
        0.5 * (np.log(df["High"] / df["Low"]) ** 2)
        - (2 * np.log(2) - 1) * (np.log(df["Close"] / df["Open"]) ** 2)
    )
    df[f"GKVol_{n}"] = np.sqrt(gk_var_bar.rolling(window=n, min_periods=n).mean())
    
    # Volume z-score
    vol_mean = df["Volume"].rolling(window=n, min_periods=n).mean()
    vol_std = df["Volume"].rolling(window=n, min_periods=n).std()
    df[f"VolZ_{n}"] = (df["Volume"] - vol_mean) / vol_std
    
    # EMA
    df["EMA_10"] = df["Close"].ewm(span=10, adjust=False).mean()
    df["EMA_20"] = df["Close"].ewm(span=20, adjust=False).mean()
    df["EMA_50"] = df["Close"].ewm(span=50, adjust=False).mean()
    
    # Candle body as % of open
    df["BodyPct"] = (df["Close"] - df["Open"]) / df["Open"].replace(0, np.nan)
    
    # Position of close within day's range
    rng = (df["High"] - df["Low"]).replace(0, np.nan)
    df["ClosePosInRange"] = ((df["Close"] - df["Low"]) / rng) - 0.5
    
    # ===== NEW DIRECTIONAL FEATURES =====
    
    # Cumulative returns (key directional signal)
    df["CumRet_10d"] = df["Log_Returns"].rolling(10).sum()
    df["CumRet_20d"] = df["Log_Returns"].rolling(20).sum()
    df["CumRet_30d"] = df["Log_Returns"].rolling(30).sum()  # Strongest trend signal
    
    # Trend score: how far price is from moving averages
    # Positive = bullish (price above MAs), Negative = bearish
    df["TrendScore"] = (
        (df["Close"] / df["EMA_10"] - 1) * 0.5 +
        (df["Close"] / df["EMA_20"] - 1) * 0.3 +
        (df["Close"] / df["EMA_50"] - 1) * 0.2
    )
    
    # Momentum z-score: recent 5d return vs 20d std
    ret_5d = df["Log_Returns"].rolling(5).sum()
    ret_std = df["Log_Returns"].rolling(20).std()
    df["MomentumZ"] = ret_5d / ret_std.replace(0, np.nan)
    
    return df


def compute_priors(
    k: int,
    self_bias: float = 0.8,  # Minimal stickiness - allow free transitions
    concentration: float = 15.0,  # Reduced concentration
) -> tuple[np.ndarray, np.ndarray]:
    """Compute Dirichlet priors for ETH HMM."""
    trans = np.full((k, k), 1.0, dtype=float)
    np.fill_diagonal(trans, self_bias)
    trans *= (concentration / k)
    start = np.full(k, concentration / k, dtype=float)
    return start, trans


def compute_priors_weak(k: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Extremely weak priors - let data speak for itself.
    Use this if sticky priors are causing issues.
    """
    trans = np.ones((k, k), dtype=float)  # Uniform
    start = np.ones(k, dtype=float)  # Uniform
    return start, trans


def lengths_by_year(idx: pd.DatetimeIndex) -> list[int]:
    """Get sequence lengths grouped by year."""
    idx_naive = idx.tz_convert(None) if idx.tz is not None else idx
    g = pd.Series(1, index=idx_naive).groupby(idx_naive.to_period("Y")).sum()
    return g.astype(int).tolist()


def fit_hmm(
    X: np.ndarray,
    lengths: list[int],
    k: int = 3,
    seed: int = 42,
) -> GaussianHMM:
    """Fit a Gaussian HMM with sticky priors."""
    sp, tp = compute_priors(k)
    
    model = GaussianHMM(
        n_components=k,
        covariance_type="diag",
        n_iter=500,
        tol=1e-3,
        random_state=seed,
        min_covar=1e-5,
        startprob_prior=sp,
        transmat_prior=tp,
    )
    model.fit(X, lengths=lengths)

    # hmmlearn 0.3.x bug: same as model.py — build (k, n, n) from _covars_ (k, n)
    # and switch to "full" so predict/score_samples use the correct density path.
    if model.covariance_type == "diag" and model.covars_.ndim == 3:
        model._covars_ = np.array([np.diag(v) for v in model._covars_])
        model.covariance_type = "full"

    return model


def fit_hmm_warm_start(
    X: np.ndarray,
    lengths: list[int],
    prev_model: GaussianHMM,
    k: int = 3,
    seed: int = 42,
) -> GaussianHMM:
    """
    Fit HMM initializing from a previous model (warm start).
    Helps maintain state consistency.
    """
    # Use ETH priors
    sp, tp = compute_priors(k)
    
    # Always use "diag" — that's what all ETH models are trained with.
    # (The old ndim==3 check was incorrect: the covars_ property always returns
    # (k, n, n) for "diag" models in hmmlearn 0.3.x regardless of _covars_ shape.)
    cov_type = prev_model.covariance_type
    
    # Initialize with previous model's parameters
    model = GaussianHMM(
        n_components=k,
        covariance_type=cov_type,
        n_iter=500,
        tol=1e-3,
        random_state=seed,
        min_covar=1e-5,
        startprob_prior=sp,
        transmat_prior=tp,
        init_params="",  # Don't init fresh
    )
    # Initialize correct shape and n_features using internal _init
    model._init(X, lengths=lengths)
    
    # Now overwrite with previous model's params
    model.startprob_ = prev_model.startprob_.copy()
    model.transmat_ = prev_model.transmat_.copy()
    model.means_ = prev_model.means_.copy()
    
    # Bypass property setter validation which is flaky during init
    model._covars_ = prev_model.covars_.copy()
    
    # Now fit properly on full data
    model.fit(X, lengths=lengths)

    if model.covariance_type == "diag" and model.covars_.ndim == 3:
        model._covars_ = np.array([np.diag(v) for v in model._covars_])
        model.covariance_type = "full"

    return model


def pick_best_model(
    X: np.ndarray,
    lengths: list[int],
    k: int = 3,
    restarts: int = 5,
    base_seed: int = 42,
) -> GaussianHMM:
    """Fit multiple HMMs and return best by log-likelihood."""
    best, best_ll = None, -np.inf
    seeds = [base_seed + i * 7 for i in range(restarts)]
    
    for s in seeds:
        m = fit_hmm(X, lengths, k=k, seed=s)
        ll = m.score(X, lengths=lengths)
        if ll > best_ll:
            best, best_ll = m, ll
    
    return best


def decode_states(model: GaussianHMM, X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Decode states using Viterbi algorithm."""
    states = model.predict(X)
    _, gamma = model.score_samples(X)
    return states, gamma


def enforce_min_dwell(path: np.ndarray, gamma: np.ndarray, min_run: int = 2) -> np.ndarray:
    """Replace short state runs with neighbor having higher posterior."""
    p = np.asarray(path, dtype=int).copy()
    n = len(p)
    changed = True
    
    while changed:
        changed = False
        i = 0
        while i < n:
            j = i + 1
            while j < n and p[j] == p[i]:
                j += 1
            run_len = j - i
            
            if run_len < min_run:
                left = p[i - 1] if i > 0 else None
                right = p[j] if j < n else None
                
                cand = []
                if left is not None:
                    cand.append((left, float(gamma[i:j, left].sum())))
                if right is not None:
                    cand.append((right, float(gamma[i:j, right].sum())))
                
                if cand:
                    fill = max(cand, key=lambda t: t[1])[0]
                    p[i:j] = fill
                    changed = True
            i = j
    
    return p


def relabel_states_by_return(df: pd.DataFrame, state_col: str) -> dict:
    """
    Relabel states so that:
        - Highest avg return = Bullish (1)
        - Lowest avg return = Bearish (2)
        - Middle = Sideways (0)
    """
    avg_returns = df.groupby(state_col)["Log_Returns"].mean().sort_values()
    
    # Print diagnostics
    print("\n--- State Relabeling ---")
    for old_state, avg_ret in avg_returns.items():
        print(f"  Original State {old_state}: Avg Return = {avg_ret:.6f}")
    
    old_to_new = {}
    sorted_states = avg_returns.index.tolist()
    
    # Lowest return = Bearish (2)
    old_to_new[sorted_states[0]] = 2
    # Highest return = Bullish (1)
    old_to_new[sorted_states[-1]] = 1
    # Middle = Sideways (0)
    if len(sorted_states) > 2:
        old_to_new[sorted_states[1]] = 0
    
    # Print mapping
    print("  Mapping:")
    for old, new in old_to_new.items():
        print(f"    {old} → {new} ({STATE_LABELS[new]})")
    
    return old_to_new


def plot_states_chart(
    df: pd.DataFrame,
    state_col: str,
    out_path: Path,
    title: str = "ETH Daily Price with HMM Regimes",
):
    """Plot price chart as colored line by HMM states."""
    colors = {
        0: "#FFA500",  # Orange - Sideways
        1: "#00AA00",  # Green - Bullish
        2: "#CC0000",  # Red - Bearish
    }
    
    fig, ax = plt.subplots(figsize=(16, 8))
    
    # Plot line segments colored by state
    dates = df.index.to_numpy()
    prices = df["Close"].to_numpy()
    states = df[state_col].to_numpy()
    
    # Draw segments
    for i in range(len(dates) - 1):
        state = int(states[i]) if not np.isnan(states[i]) else 0
        ax.plot(
            [dates[i], dates[i + 1]],
            [prices[i], prices[i + 1]],
            color=colors.get(state, "#888888"),
            linewidth=1.2,
            solid_capstyle="round",
        )
    
    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color=colors[0], lw=2, label=STATE_LABELS[0]),
        Line2D([0], [0], color=colors[1], lw=2, label=STATE_LABELS[1]),
        Line2D([0], [0], color=colors[2], lw=2, label=STATE_LABELS[2]),
    ]
    ax.legend(handles=legend_elements, loc="upper left")
    
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Price (USD)", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_yscale("log")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved plot: {out_path}")


def diagnose_regimes(df: pd.DataFrame, state_col: str) -> pd.DataFrame:
    """Generate regime diagnostics with directional metrics."""
    diag = df.groupby(state_col).agg({
        "Log_Returns": ["mean", "std", "count"],
        "GKVol_20": "mean",
        "VolZ_20": "mean",
        "CumRet_20d": "mean",  # Check if states align with trend
        "TrendScore": "mean",  # Should be positive for bullish, negative for bearish
    }).round(4)
    
    diag.columns = ["AvgReturn", "StdReturn", "Days", "AvgVol", "AvgVolZ", 
                    "AvgCumRet20", "AvgTrendScore"]
    diag["Label"] = diag.index.map(STATE_LABELS)
    diag["Pct"] = (diag["Days"] / diag["Days"].sum() * 100).round(1)
    
    return diag


class ETHRegimeDetector:
    """ETH-specific regime detector using HMM."""
    
    def __init__(
        self,
        train_end: str = "2020-12-31",  # ETH DeFi summer was 2020
        val_end: str = "2022-12-31",
        k: int = 3,
        min_dwell: int = 2,  # Allow single-day switches (was 2)
    ):
        self.train_end = train_end
        self.val_end = val_end
        self.k = k
        self.min_dwell = min_dwell
        
        self.scaler = None
        self.model = None
        self.state_mapping = None
    
    def fit(self, df: pd.DataFrame) -> "ETHRegimeDetector":
        """Fit HMM on training + validation data."""
        # Compute features
        df = compute_daily_features(df)
        df = df.dropna(subset=HMM_FEATURES + ["Close"]).copy()
        
        # Split by date
        train_mask = df.index <= pd.Timestamp(self.train_end, tz="UTC")
        val_mask = (
            (df.index > pd.Timestamp(self.train_end, tz="UTC")) &
            (df.index <= pd.Timestamp(self.val_end, tz="UTC"))
        )
        
        df_tr = df.loc[train_mask]
        df_va = df.loc[val_mask]
        
        if df_tr.empty or df_va.empty:
            raise ValueError("Train or Val split is empty")
        
        # Scale features
        X_tr = df_tr[HMM_FEATURES].values
        X_va = df_va[HMM_FEATURES].values
        
        self.scaler = StandardScaler().fit(X_tr)
        Xs_tr = self.scaler.transform(X_tr)
        Xs_va = self.scaler.transform(X_va)
        
        # Train on Train+Val
        Xs_trv = np.vstack([Xs_tr, Xs_va])
        len_trv = lengths_by_year(pd.concat([df_tr, df_va]).index)
        
        self.model = pick_best_model(Xs_trv, len_trv, k=self.k)
        
        return self
    
    def predict(self, df: pd.DataFrame, relabel: bool = True) -> pd.Series:
        """
        Predict states using Viterbi (full sequence).
        
        WARNING: Has subtle lookahead on test data.
        For realistic backtests, use predict_online() instead.
        """
        if self.model is None:
            raise ValueError("Model not fitted")
        
        df = compute_daily_features(df)
        df = df.dropna(subset=HMM_FEATURES + ["Close"]).copy()
        
        X = df[HMM_FEATURES].values
        Xs = self.scaler.transform(X)
        
        states, gamma = decode_states(self.model, Xs)
        
        if self.min_dwell > 1:
            states = enforce_min_dwell(states, gamma, min_run=self.min_dwell)
        
        result = pd.Series(states, index=df.index, name=f"State_K{self.k}")
        
        # Relabel states by average return
        if relabel and self.state_mapping:
            result = result.map(self.state_mapping)
        elif relabel:
            df_temp = df.copy()
            df_temp["state"] = result
            self.state_mapping = relabel_states_by_return(df_temp, "state")
            result = result.map(self.state_mapping)
        
        return result
    
    def predict_online(self, df: pd.DataFrame, lookback: int = 60) -> pd.Series:
        """
        Predict states day-by-day without lookahead (realistic for live trading).
        
        For each day t, only data up to day t-1 is used for prediction.
        This simulates what you'd actually know at market open on day t.
        
        Args:
            df: Daily DataFrame with required features
            lookback: Number of days to use for each prediction (rolling window)
        
        Returns:
            Series of states indexed by date (state known at market open)
        """
        if self.model is None:
            raise ValueError("Model not fitted")
        
        df = compute_daily_features(df)
        df = df.dropna(subset=HMM_FEATURES + ["Close"]).copy()
        
        X = df[HMM_FEATURES].values
        Xs = self.scaler.transform(X)
        
        n = len(Xs)
        states = np.zeros(n, dtype=int)
        
        for t in range(n):
            # Use lookback window ending at YESTERDAY (t-1), not today
            start = max(0, t - lookback)
            X_window = Xs[start:t]  # Excludes today's observation
            
            if len(X_window) == 0:
                # First day: no prior data, use neutral state
                states[t] = 0
            else:
                window_states = self.model.predict(X_window)
                states[t] = window_states[-1]
        
        result = pd.Series(states, index=df.index, name=f"State_K{self.k}_online")
        
        # Apply state mapping if available
        if self.state_mapping:
            result = result.map(self.state_mapping)
        
        return result
    
    def save_model(self, out_dir: Path) -> None:
        """
        Save trained model artifacts.
        
        Saves: model.pkl, scaler.pkl, state_mapping.pkl, config.json
        """
        import pickle
        import json
        
        if self.model is None:
            raise ValueError("Model not fitted")
        
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        
        with open(out_dir / "model.pkl", "wb") as f:
            pickle.dump(self.model, f)
        
        with open(out_dir / "scaler.pkl", "wb") as f:
            pickle.dump(self.scaler, f)
        
        with open(out_dir / "state_mapping.pkl", "wb") as f:
            pickle.dump(self.state_mapping, f)
        
        config = {
            "train_end": self.train_end,
            "val_end": self.val_end,
            "k": self.k,
            "min_dwell": self.min_dwell,
            "features": HMM_FEATURES,
            "state_labels": STATE_LABELS,
        }
        with open(out_dir / "config.json", "w") as f:
            json.dump(config, f, indent=2)
        
        print(f"Saved ETH model to: {out_dir}")
    
    @classmethod
    def load_model(cls, model_dir: Path) -> "ETHRegimeDetector":
        """Load a previously saved model."""
        import pickle
        import json
        
        model_dir = Path(model_dir)
        
        with open(model_dir / "config.json", "r") as f:
            config = json.load(f)
        
        detector = cls(
            train_end=config["train_end"],
            val_end=config["val_end"],
            k=config["k"],
            min_dwell=config["min_dwell"],
        )
        
        with open(model_dir / "model.pkl", "rb") as f:
            detector.model = pickle.load(f)
        
        with open(model_dir / "scaler.pkl", "rb") as f:
            detector.scaler = pickle.load(f)
        
        with open(model_dir / "state_mapping.pkl", "rb") as f:
            detector.state_mapping = pickle.load(f)
        
        print(f"Loaded ETH model from: {model_dir}")
        return detector


def train_eth_hmm(
    daily_csv: Path,
    out_dir: Path,
    train_end: str = "2020-12-31",
    val_end: str = "2022-12-31",
) -> pd.DataFrame:
    """
    Train ETH HMM and save results.
    
    Outputs:
        - eth_1d_with_states.csv
        - eth_1d_colored_states.png
        - eth_state_diagnostics.csv
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Load data
    print(f"Loading: {daily_csv}")
    df = pd.read_csv(daily_csv)
    
    # Parse date
    if "time" in df.columns:
        df = df.rename(columns={"time": "Date"})
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.set_index("Date").sort_index()
    
    print(f"Loaded {len(df)} rows: {df.index.min()} → {df.index.max()}")
    
    # Train HMM
    print(f"\nTraining ETH HMM (train_end={train_end}, val_end={val_end})...")
    detector = ETHRegimeDetector(train_end=train_end, val_end=val_end)
    detector.fit(df)
    
    # Predict states for all data
    df = compute_daily_features(df)
    df = df.dropna(subset=HMM_FEATURES + ["Close"]).copy()
    states = detector.predict(df, relabel=True)
    df["State_K3"] = states
    
    # Save CSV
    out_csv = out_dir / "eth_1d_with_states.csv"
    out_df = df.reset_index()
    if pd.api.types.is_datetime64tz_dtype(out_df["Date"]):
        out_df["Date"] = out_df["Date"].dt.tz_convert("UTC").dt.tz_localize(None)
    out_df.to_csv(out_csv, index=False)
    print(f"\nSaved: {out_csv}")
    
    # Plot states
    plot_path = out_dir / "eth_1d_colored_states.png"
    plot_states_chart(df, "State_K3", plot_path)
    
    # Diagnostics
    diag = diagnose_regimes(df, "State_K3")
    diag_path = out_dir / "eth_state_diagnostics.csv"
    diag.to_csv(diag_path)
    print(f"Saved: {diag_path}")
    
    # Print diagnostics
    print("\n" + "=" * 60)
    print("ETH REGIME DIAGNOSTICS")
    print("=" * 60)
    print(diag.to_string())
    print("=" * 60)
    
    return df


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    
    DAILY_CSV = PROJECT_ROOT / "data/raw/eth_usd_1d_coinbase.csv"
    OUT_DIR = PROJECT_ROOT / "outputs"
    
    if DAILY_CSV.exists():
        train_eth_hmm(DAILY_CSV, OUT_DIR)
    else:
        print(f"Input not found: {DAILY_CSV}")
        print("Run: python -m src.data.coinbase_downloader --product ETH-USD --start 2017-06-01")
