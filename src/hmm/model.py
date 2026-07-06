"""
Hidden Markov Model for BTC regime detection.

Uses a 3-state Gaussian HMM to classify market regimes:
    - State 0: Mean Reversion
    - State 1: Trending (Longs Only) <- Trade in this regime
    - State 2: Bearish (Shorts/Sit Out)
"""

from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler


# Default HMM configuration
DEFAULT_CONFIG = {
    "n_components": 3,
    "covariance_type": "diag",
    "n_iter": 1500,
    "tol": 1e-4,
    "min_covar": 1e-5,
    "random_state": 42,
    "restarts": 10,
    "min_dwell": 3,
}

# Features used for HMM training
HMM_FEATURES = [
    "Log_Returns",       # Direction (stationary)
    "GKVol_20",          # Garman-Klass volatility
    "VolZ_20",           # Volume z-score
    "EMA_20_slope",      # Trend slope
    "BodyPct",           # Candle body as % of open
    "ClosePosInRange",   # Close position within range
    "CloseOverEMA20",    # Price vs EMA
]


def build_hmm_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build additional OHLCV-derived features for HMM.
    
    Assumes df already has: Log_Returns, GKVol_20, VolZ_20, EMA_20, EMA_20_slope
    """
    df = df.copy()
    
    # Candle body as % of open
    df["BodyPct"] = (df["Close"] - df["Open"]) / df["Open"].replace(0, np.nan)
    
    # Position of close within day's range [-0.5, +0.5]
    rng = (df["High"] - df["Low"]).replace(0, np.nan)
    df["ClosePosInRange"] = ((df["Close"] - df["Low"]) / rng) - 0.5
    
    # Distance from 20d EMA
    df["CloseOverEMA20"] = (df["Close"] / df["EMA_20"]) - 1.0
    
    # Drop rows with NaN in features
    df = df.dropna(subset=HMM_FEATURES + ["Close"]).copy()
    
    return df


def compute_priors(
    k: int,
    self_bias: float = 5.0,
    concentration: float = 50.0,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute Dirichlet priors for HMM start and transition probabilities.
    
    Args:
        k: Number of states
        self_bias: Favor staying in same state (stickiness)
        concentration: Overall prior strength
    
    Returns:
        (startprob_prior, transmat_prior)
    """
    trans = np.full((k, k), 1.0, dtype=float)
    np.fill_diagonal(trans, self_bias)
    trans *= (concentration / k)
    
    start = np.full(k, concentration / k, dtype=float)
    return start, trans


def lengths_by_year(idx: pd.DatetimeIndex) -> list[int]:
    """Get sequence lengths grouped by year for HMM training."""
    idx_naive = idx.tz_convert(None) if idx.tz is not None else idx
    g = pd.Series(1, index=idx_naive).groupby(idx_naive.to_period("Y")).sum()
    return g.astype(int).tolist()


def fit_hmm(
    X: np.ndarray,
    lengths: list[int],
    k: int = 3,
    seed: int = 42,
    config: Optional[dict] = None,
) -> GaussianHMM:
    """
    Fit a Gaussian HMM with sticky priors.
    
    Args:
        X: Scaled feature matrix
        lengths: Sequence lengths for multi-sequence training
        k: Number of states
        seed: Random seed
        config: Optional config overrides
    
    Returns:
        Fitted GaussianHMM
    """
    cfg = {**DEFAULT_CONFIG, **(config or {})}
    sp, tp = compute_priors(k, self_bias=1.8)
    
    model = GaussianHMM(
        n_components=k,
        covariance_type=cfg["covariance_type"],
        n_iter=cfg["n_iter"],
        tol=cfg["tol"],
        random_state=seed,
        min_covar=cfg["min_covar"],
        startprob_prior=sp,
        transmat_prior=tp,
    )
    model.fit(X, lengths=lengths)

    # hmmlearn 0.3.x bug: for covariance_type="diag" the covars_ property
    # returns (k, n, n) diagonal matrices, but _log_multivariate_normal_density_diag
    # expects (k, n_features) plain variances — so predict() fails with a broadcast
    # error.  Fix: build proper (k, n, n) full-diagonal matrices from the raw
    # _covars_ (which is (k, n)) and switch the model to covariance_type="full".
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
    sp, tp = compute_priors(k, self_bias=1.8)
    
    # Robustly infer covariance type from the actual shape
    # This fixes mismatch where type="diag" but shape is (k, n, n)
    if prev_model.covars_.ndim == 3:
        cov_type = "full"
    else:
        cov_type = "diag"
    
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
    # Bypass validation by setting private attributes if needed,
    # or ensure we set them in order.
    # hmmlearn uses _covars_ internally
    model.startprob_ = prev_model.startprob_.copy()
    model.transmat_ = prev_model.transmat_.copy()
    model.means_ = prev_model.means_.copy()
    
    # Bypass property setter validation which is flaky during init
    model._covars_ = prev_model.covars_.copy()
    
    # Now fit properly on full data (it will use these as init due to init_params="")
    model.fit(X, lengths=lengths)
    return model


def align_states(
    model: GaussianHMM, 
    X_sample: np.ndarray,
    feature_idx_for_sort: int = 0
) -> GaussianHMM:
    """
    Permute model states so that State 0 = Lowest Value ... State K-1 = Highest Value.
    Usually sorts by 'Log_Returns' (index 0) to ensure:
      0 = Bearish (Low Return)
      1 = Neutral
      2 = Bullish (High Return)
      
    Actually, conventionally we want:
      0 = Bearish? Or just purely ordered by return?
      
    Let's enforce: Ordered by Mean of feature_idx_for_sort (Log Returns).
    State 0 = Lowest Return (Bearish)
    State K-1 = Highest Return (Bullish)
    """
    means = model.means_[:, feature_idx_for_sort]
    order = np.argsort(means)  # e.g. [2, 0, 1] means state 2 is lowest, 0 is middle, 1 is highest
    
    if np.array_equal(order, np.arange(model.n_components)):
        return model  # Already sorted
        
    # Create new model with permuted parameters
    new_model = GaussianHMM(
        n_components=model.n_components,
        covariance_type=model.covariance_type,
        n_iter=model.n_iter,
        tol=model.tol,
        random_state=model.random_state,
        min_covar=model.min_covar,
        startprob_prior=model.startprob_prior,
        transmat_prior=model.transmat_prior,
        init_params="",
    )
    
    new_model._init(X_sample)

    new_model.startprob_ = model.startprob_[order]
    new_model.transmat_ = model.transmat_[order][:, order]
    new_model.means_ = model.means_[order]
    raw_covars = model.covars_[order]

    if new_model.covariance_type == "full" and raw_covars.ndim == 2:
        raw_covars = np.array([np.diag(c) for c in raw_covars])

    new_model._covars_ = raw_covars

    return new_model


def pick_best_model(
    X: np.ndarray,
    lengths: list[int],
    k: int = 3,
    restarts: int = 5,
    base_seed: int = 42,
) -> GaussianHMM:
    """
    Fit multiple HMMs and return the one with best log-likelihood.
    """
    best, best_ll = None, -np.inf
    seeds = [base_seed + i * 7 for i in range(restarts)]
    
    for s in seeds:
        m = fit_hmm(X, lengths, k=k, seed=s)
        ll = m.score(X, lengths=lengths)
        if ll > best_ll:
            best, best_ll = m, ll
    
    return best


def decode_states(
    model: GaussianHMM,
    X: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Decode states using Viterbi algorithm.
    
    Returns:
        (states, gamma) where gamma is the posterior probabilities
    """
    states = model.predict(X)
    _, gamma = model.score_samples(X)
    return states, gamma


def enforce_min_dwell(
    path: np.ndarray,
    gamma: np.ndarray,
    min_run: int = 3,
) -> np.ndarray:
    """
    Replace short state runs with the neighbor having higher posterior mass.
    
    This smooths out unrealistic rapid state switches.
    """
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


def enforce_min_dwell_causal(path: np.ndarray, min_run: int = 3) -> np.ndarray:
    """
    Causal min-dwell filter: delays a state transition until the new state
    has persisted for ``min_run`` consecutive observations. Uses NO future data,
    making it safe for live / walk-forward use.
    """
    p = np.asarray(path, dtype=int)
    if min_run <= 1 or len(p) == 0:
        return p.copy()

    out = p.copy()
    current = out[0]
    pending = None
    pending_count = 0

    for i in range(1, len(out)):
        s = out[i]
        if s == current:
            pending = None
            pending_count = 0
        else:
            if pending is None or pending != s:
                pending = s
                pending_count = 1
            else:
                pending_count += 1
            if pending_count >= min_run:
                current = pending
                pending = None
                pending_count = 0
        out[i] = current

    return out


class BTCRegimeDetector:
    """
    High-level wrapper for BTC regime detection using HMM.
    """
    
    def __init__(
        self,
        train_end: str = "2019-12-31",
        val_end: str = "2021-12-31",
        k: int = 3,
        min_dwell: int = 3,
    ):
        self.train_end = train_end
        self.val_end = val_end
        self.k = k
        self.min_dwell = min_dwell
        
        self.scaler = None
        self.model = None
        self.state_labels = {
            0: "Mean Reversion",
            1: "Trending (Longs)",
            2: "Bearish (Sit Out)",
        }
    
    def fit(self, df: pd.DataFrame) -> "BTCRegimeDetector":
        """
        Fit HMM on training + validation data.
        
        Args:
            df: Daily DataFrame with required features
        """
        # Build features
        df = build_hmm_features(df)
        
        # Split by date
        train_mask = df.index <= pd.Timestamp(self.train_end, tz="UTC")
        val_mask = (
            (df.index > pd.Timestamp(self.train_end, tz="UTC")) &
            (df.index <= pd.Timestamp(self.val_end, tz="UTC"))
        )
        
        df_tr = df.loc[train_mask]
        df_va = df.loc[val_mask]
        
        if df_tr.empty or df_va.empty:
            raise ValueError("Train or Val split is empty. Check dates.")
        
        # Extract features
        X_tr = df_tr[HMM_FEATURES].values
        X_va = df_va[HMM_FEATURES].values
        
        # Fit scaler on training only
        self.scaler = StandardScaler().fit(X_tr)
        Xs_tr = self.scaler.transform(X_tr)
        Xs_va = self.scaler.transform(X_va)
        
        # Train on Train+Val combined
        Xs_trv = np.vstack([Xs_tr, Xs_va])
        len_trv = lengths_by_year(pd.concat([df_tr, df_va]).index)
        
        self.model = pick_best_model(Xs_trv, len_trv, k=self.k)
        
        return self
    
    def predict(self, df: pd.DataFrame) -> pd.Series:
        """
        Predict states for new data using Viterbi (full sequence).
        
        WARNING: This has subtle lookahead when used on test data.
        For realistic backtests, use predict_online() instead.
        """
        if self.model is None:
            raise ValueError("Model not fitted. Call fit() first.")
        
        df = build_hmm_features(df)
        X = df[HMM_FEATURES].values
        Xs = self.scaler.transform(X)
        
        states, gamma = decode_states(self.model, Xs)
        
        if self.min_dwell > 1:
            states = enforce_min_dwell(states, gamma, min_run=self.min_dwell)
        
        return pd.Series(states, index=df.index, name=f"State_K{self.k}")
    
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
            raise ValueError("Model not fitted. Call fit() first.")
        
        df = build_hmm_features(df)
        X = df[HMM_FEATURES].values
        Xs = self.scaler.transform(X)
        
        n = len(Xs)
        states = np.zeros(n, dtype=int)
        
        for t in range(n):
            # Use lookback window ending at YESTERDAY (t-1), not today
            # At market open on day t, we only have data up to day t-1
            start = max(0, t - lookback)
            X_window = Xs[start:t]  # Excludes today's observation
            
            if len(X_window) == 0:
                # First day: no prior data, use neutral state
                states[t] = 0
            else:
                # Predict using only past data
                window_states = self.model.predict(X_window)
                states[t] = window_states[-1]  # Yesterday's state
        
        return pd.Series(states, index=df.index, name=f"State_K{self.k}_online")
    
    def save_model(self, out_dir: Path) -> None:
        """
        Save trained model artifacts for later use.
        
        Saves:
            - model.pkl: Trained GaussianHMM
            - scaler.pkl: StandardScaler
            - config.json: Model configuration
        """
        import pickle
        import json
        
        if self.model is None:
            raise ValueError("Model not fitted. Call fit() first.")
        
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        
        # Save model
        with open(out_dir / "model.pkl", "wb") as f:
            pickle.dump(self.model, f)
        
        # Save scaler
        with open(out_dir / "scaler.pkl", "wb") as f:
            pickle.dump(self.scaler, f)
        
        # Save config
        config = {
            "train_end": self.train_end,
            "val_end": self.val_end,
            "k": self.k,
            "min_dwell": self.min_dwell,
            "features": HMM_FEATURES,
            "state_labels": self.state_labels,
        }
        with open(out_dir / "config.json", "w") as f:
            json.dump(config, f, indent=2)
        
        print(f"Saved model to: {out_dir}")
    
    @classmethod
    def load_model(cls, model_dir: Path) -> "BTCRegimeDetector":
        """
        Load a previously saved model.
        
        Args:
            model_dir: Directory containing model.pkl, scaler.pkl, config.json
        
        Returns:
            BTCRegimeDetector ready for prediction
        """
        import pickle
        import json
        
        model_dir = Path(model_dir)
        
        # Load config
        with open(model_dir / "config.json", "r") as f:
            config = json.load(f)
        
        # Create instance
        detector = cls(
            train_end=config["train_end"],
            val_end=config["val_end"],
            k=config["k"],
            min_dwell=config["min_dwell"],
        )
        
        # Load model
        with open(model_dir / "model.pkl", "rb") as f:
            detector.model = pickle.load(f)
        
        # Load scaler
        with open(model_dir / "scaler.pkl", "rb") as f:
            detector.scaler = pickle.load(f)
        
        print(f"Loaded model from: {model_dir}")
        return detector
    
    def fit_predict(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fit model and return DataFrame with states added."""
        self.fit(df)
        
        df = build_hmm_features(df)
        states = self.predict(df)
        
        return df.join(states)


def train_and_save(
    daily_csv: Path,
    out_csv: Path,
    train_end: str = "2019-12-31",
    val_end: str = "2021-12-31",
) -> pd.DataFrame:
    """
    Train HMM on daily data and save with states.
    """
    # Load
    df = pd.read_csv(daily_csv)
    if "Date" not in df.columns:
        raise ValueError("Expected 'Date' column")
    
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.set_index("Date").sort_index()
    
    # Train and predict
    detector = BTCRegimeDetector(train_end=train_end, val_end=val_end)
    df_with_states = detector.fit_predict(df)
    
    # Save
    out = df_with_states.reset_index()
    if pd.api.types.is_datetime64tz_dtype(out["Date"]):
        out["Date"] = out["Date"].dt.tz_convert("UTC").dt.tz_localize(None)
    
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_csv, index=False)
    
    print(f"Saved: {out_csv}")
    print(f"State distribution:\n{df_with_states[f'State_K{detector.k}'].value_counts(normalize=True)}")
    
    return df_with_states


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    
    DAILY_CSV = PROJECT_ROOT / "data/processed/btc_1d_features.csv"
    OUT_CSV = PROJECT_ROOT / "data/processed/btc_1d_with_states.csv"
    
    if DAILY_CSV.exists():
        train_and_save(DAILY_CSV, OUT_CSV)
    else:
        print(f"Input not found: {DAILY_CSV}")
