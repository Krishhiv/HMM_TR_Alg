import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import LineCollection
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# -----------------------------
# Config
# -----------------------------
TRAIN_END  = "2019-12-31"
VAL_END    = "2021-12-31"
K_CANDIDATES = (3,)
RESTARTS   = 5
MAX_ITER   = 500
RANDOM_SEED = 42

# -----------------------------
# Load
# -----------------------------
df = pd.read_csv('./MAIN-DATASETS/btc_1d_main.csv')
if "Date" not in df.columns:
    raise ValueError("Expected a 'Date' column.")
df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
df = df.set_index("Date").sort_index()

need = ["Open","High","Low","Close","Volume",
        "Log_Returns","GKVol_20","VolZ_20","EMA_20","EMA_20_slope"]
missing = [c for c in need if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns: {missing}")

# -----------------------------
# Build compact OHLCV-derived features (stationary)
# -----------------------------
eps = 1e-12
# Candle body as % of open (directional, scale-free)
df["BodyPct"] = (df["Close"] - df["Open"]) / (df["Open"].replace(0, np.nan))
# Position of close within the day's range [-0.5, +0.5]
rng = (df["High"] - df["Low"]).replace(0, np.nan)
df["ClosePosInRange"] = ((df["Close"] - df["Low"]) / rng) - 0.5
# Distance from 20d EMA (positioning)
df["CloseOverEMA20"] = (df["Close"] / df["EMA_20"]) - 1.0

# Feature set: direction, vol, volume pressure, trend slope, and two candle/position features
FEATURES = [
    "Log_Returns",          # direction (stationary)
    "GKVol_20",             # volatility (from OHLC)
    "VolZ_20",              # volume pressure
    "EMA_20_slope",         # trend slope
    "BodyPct",              # OHLC candle shape
    "ClosePosInRange",      # OHLC position-of-close
    "CloseOverEMA20",       # price position vs EMA
]

df = df.dropna(subset=FEATURES + ["Close"]).copy()

# -----------------------------
# Splits (by date, no leakage)
# -----------------------------
train_mask = df.index <= pd.Timestamp(TRAIN_END, tz="UTC")
val_mask   = (df.index > pd.Timestamp(TRAIN_END, tz="UTC")) & (df.index <= pd.Timestamp(VAL_END, tz="UTC"))
test_mask  = df.index > pd.Timestamp(VAL_END, tz="UTC")

df_tr, df_va, df_te = df.loc[train_mask], df.loc[val_mask], df.loc[test_mask]
if df_tr.empty or df_va.empty or df_te.empty:
    raise ValueError("One of Train/Val/Test is empty; adjust TRAIN_END or VAL_END.")

X_tr, X_va, X_te = df_tr[FEATURES].values, df_va[FEATURES].values, df_te[FEATURES].values

# Standardize on TRAIN only
scaler = StandardScaler().fit(X_tr)
Xs_tr, Xs_va, Xs_te = scaler.transform(X_tr), scaler.transform(X_va), scaler.transform(X_te)

# -----------------------------
# Sequence lengths by calendar year (stabilizes priors)
# -----------------------------
def lengths_by_year(idx_utc):
    idx_naive = idx_utc.tz_convert(None) if idx_utc.tz is not None else idx_utc
    g = pd.Series(1, index=idx_naive).groupby(idx_naive.to_period("Y")).sum()
    return g.astype(int).tolist()

len_tr  = lengths_by_year(df_tr.index)
len_va  = lengths_by_year(df_va.index)
len_trv = lengths_by_year(pd.concat([df_tr, df_va]).index)

# -----------------------------
# Priors to avoid brittle transitions
# -----------------------------
def priors(k, self_bias=5.0, concentration=50.0):
    """
    Dirichlet pseudo-counts for start and transition priors.
    - self_bias > 1 favors staying in the same state.
    - concentration scales how strongly the prior influences learning.
    """
    trans = np.full((k, k), 1.0, dtype=float)
    np.fill_diagonal(trans, self_bias)   # stickiness
    trans *= (concentration / k)         # overall strength of the prior

    start = np.full(k, concentration / k, dtype=float)  # roughly uniform but strong
    return start, trans


def fit_hmm(X, lengths, k, seed):
    sp, tp = priors(k, self_bias=1.8)
    model = GaussianHMM(
        n_components=k,
        covariance_type="diag", ###
        n_iter=MAX_ITER,
        tol=1e-3,
        random_state=seed,
        min_covar=1e-5, ###
        startprob_prior=sp,
        transmat_prior=tp,
    )
    model.fit(X, lengths=lengths)
    return model

def n_params_diag(k, d):
    # start (k-1) + trans k*(k-1) + means k*d + diag vars k*d
    return (k-1) + k*(k-1) + 2*k*d

def bic(model, X, lengths=None):
    ll = model.score(X, lengths=lengths)
    n = len(X)
    d = model.means_.shape[1]
    p = n_params_diag(model.n_components, d)
    return -2*ll + p*np.log(n), ll

# -----------------------------
# Model selection (K=3 fixed)
# -----------------------------
cands = []
seeds = [RANDOM_SEED + i*7 for i in range(RESTARTS)]
best, best_ll = None, -np.inf
for s in seeds:
    m = fit_hmm(Xs_tr, len_tr, k=3, seed=s)
    ll = m.score(Xs_tr, lengths=len_tr)
    if ll > best_ll:
        best, best_ll = m, ll

b, vll = bic(best, Xs_va, lengths=len_va)
print(f"K=3  Val-LL={vll:.1f}  BIC={b:.1f}")
best_k, best_tr_model = 3, best
print(f"Selected K={best_k}")

# -----------------------------
# Refit on Train+Val, then decode all
# -----------------------------
Xs_trv = np.vstack([Xs_tr, Xs_va])
final = fit_hmm(Xs_trv, len_trv, best_k, seed=101)

def decode(model, X):
    states = model.predict(X)        # Viterbi path
    _, gamma = model.score_samples(X)  # smoothed posteriors (analysis only)
    return states, gamma

def enforce_min_dwell_gamma(path, gamma, min_run=10):
    """
    Replace any run shorter than min_run by the neighbor with higher
    posterior mass over that window. Repeats until no short runs remain.
    """
    import numpy as np
    p = np.asarray(path, dtype=int).copy()
    n = len(p)
    changed = True
    while changed:                      # multi-pass to collapse chains of shorts
        changed = False
        i = 0
        while i < n:
            j = i + 1
            while j < n and p[j] == p[i]:
                j += 1
            run_len = j - i
            if run_len < min_run:
                left  = p[i-1] if i > 0 else None
                right = p[j]   if j < n else None

                # choose neighbor by posterior mass over the short window
                cand = []
                if left  is not None: cand.append((left , float(gamma[i:j, left ].sum())))
                if right is not None: cand.append((right, float(gamma[i:j, right].sum())))
                if cand:
                    fill = max(cand, key=lambda t: t[1])[0]
                    p[i:j] = fill
                    changed = True
            i = j
    return p


st_tr, g_tr = decode(final, Xs_tr)
st_va, g_va = decode(final, Xs_va)
st_te, g_te = decode(final, Xs_te)

# >>> dwell smoothing goes here (BEFORE building states_full) <<<
MIN_DWELL = 3  # try 7–10 first; 30 is very strong and may over-smooth
st_tr = enforce_min_dwell_gamma(st_tr, g_tr, min_run=MIN_DWELL)
st_va = enforce_min_dwell_gamma(st_va, g_va, min_run=MIN_DWELL)
st_te = enforce_min_dwell_gamma(st_te, g_te, min_run=MIN_DWELL)



states_full = pd.Series(
    np.concatenate([st_tr, st_va, st_te]),
    index=pd.Index(df_tr.index.tolist() + df_va.index.tolist() + df_te.index.tolist(), name="Date"),
    name=f"State_K{best_k}"
)

out = df.join(states_full)

# -----------------------------
# Quick sanity diagnostics
# -----------------------------
occ = states_full.value_counts(normalize=True).sort_index()
print("\nOccupancy by state:\n", occ.round(4))
print("\nStart probs (π):", final.startprob_)
print("Trans matrix (A):\n", pd.DataFrame(final.transmat_))

# -----------------------------
# Plot: ONE price line, colored by state
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

# Build line segments
x = mdates.date2num(out.index.to_pydatetime())
y = out["Close"].to_numpy()
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Assign a color per segment using the state at the segment's start
state_at_seg = out[f"State_K{best_k}"].to_numpy()[:-1]
palette = plt.cm.tab10.colors  # 10 distinct colors
state_colors = [palette[s % len(palette)] for s in state_at_seg]

lc = LineCollection(segments, colors=state_colors, linewidth=1.6)
ax.add_collection(lc)

ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min() * 0.95, y.max() * 1.05)
ax.set_title(f"BTC-USD Daily Close — colored by HMM states (K={best_k})")
ax.set_xlabel("Date"); ax.set_ylabel("Close (USD)")
ax.grid(True, alpha=0.3)

# Optional: legend swatches (no extra price lines)
from matplotlib.lines import Line2D
legend_elems = [Line2D([0], [0], color=palette[s % len(palette)], lw=2, label=f"State {s}") for s in range(best_k)]
ax.legend(handles=legend_elems, loc="best")

plt.tight_layout()
Path("outputs").mkdir(exist_ok=True)
plt.savefig("outputs/btc_1d_colored_states.png", dpi=140)
plt.show()

# Save labeled data
df_out = out[[f"State_K{best_k}", "Close"] + FEATURES].copy()
df_out.to_csv("outputs/btc_1d_with_states_compact.csv")
print("Saved outputs/btc_1d_colored_states.png and outputs/btc_1d_with_states_compact.csv")