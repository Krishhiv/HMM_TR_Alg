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
    "n_iter": 500,
    "tol": 1e-3,
    "min_covar": 1e-5,
    "random_state": 42,
    "restarts": 5,
    "min_dwell": 3,  # Minimum state duration in days
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
    return model


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
        Predict states for new data.
        
        Args:
            df: Daily DataFrame with required features
        
        Returns:
            Series of state labels indexed by date
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
