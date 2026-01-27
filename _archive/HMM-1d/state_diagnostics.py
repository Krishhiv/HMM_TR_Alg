# state_diagnostics.py
# ------------------------------------------------------------
# Usage:
#   python state_diagnostics.py \
#       --csv outputs/btc_1d_with_states_compact.csv \
#       --out outputs \
#       --min_run 3 \
#       --plot_dwell
#
# What it prints:
#   - Detected K and the state column name (e.g., "State_K3")
#   - Per-state table: n, occ, mean_ret, vol, ema_slope, close_over_ema, avg_dwell
#   - Short-run share (< min_run)
#   - Transition matrix (counts and row-normalized)
#   - Role mapping (Bearish/Chop/Bullish) by mean return
#
# What it saves:
#   - <out>/state_diagnostics_report.csv
#   - <out>/dwell_hist.png  (only if --plot_dwell)
# ------------------------------------------------------------

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", type=str, default="outputs/btc_1d_with_states_compact.csv",
                   help="Path to CSV with state column + features (from 1d_hmm.py).")
    p.add_argument("--out", type=str, default="outputs", help="Output directory.")
    p.add_argument("--min_run", type=int, default=3, help="Short-run threshold for diagnostics.")
    p.add_argument("--plot_dwell", action="store_true", help="Save a dwell-length histogram.")
    return p.parse_args()

def detect_state_col(df: pd.DataFrame) -> str:
    cand = [c for c in df.columns if c.startswith("State_K")]
    if not cand:
        raise ValueError("No 'State_K*' column found in the CSV.")
    # If multiple, pick the longest name (most specific), else first
    cand.sort(key=len, reverse=True)
    return cand[0]

def dwell_lengths(path_1d: np.ndarray) -> pd.DataFrame:
    p = np.asarray(path_1d, dtype=int).ravel()
    lens, vals = [], []
    i, n = 0, len(p)
    while i < n:
        j = i + 1
        while j < n and p[j] == p[i]:
            j += 1
        lens.append(j - i)
        vals.append(p[i])
        i = j
    return pd.DataFrame({"state": vals, "len": lens})

def transition_matrix(states_1d: np.ndarray):
    s = np.asarray(states_1d, dtype=int).ravel()
    uniq = np.unique(s)
    # Map to consecutive ids in case states aren't 0..K-1
    remap = {u: i for i, u in enumerate(sorted(uniq))}
    r = np.array([remap[v] for v in s], dtype=int)
    K = len(uniq)
    T = np.zeros((K, K), dtype=int)
    for a, b in zip(r[:-1], r[1:]):
        T[a, b] += 1
    # Row-normalized (probabilities)
    with np.errstate(divide="ignore", invalid="ignore"):
        P = T / T.sum(axis=1, keepdims=True)
        P = np.nan_to_num(P)
    # Also return the mapping back to original labels
    inv = {v: k for k, v in remap.items()}
    original_order = [inv[i] for i in range(K)]
    return T, P, original_order

def main():
    args = parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.csv, parse_dates=["Date"], infer_datetime_format=True) if "Date" in pd.read_csv(args.csv, nrows=0).columns else pd.read_csv(args.csv)
    state_col = detect_state_col(df)
    S = df[state_col].to_numpy().astype(int).ravel()

    # Optional columns (handle missing gracefully)
    maybe_cols = [
        "Log_Returns", "GKVol_20", "EMA_20_slope", "CloseOverEMA20",
    ]
    present = [c for c in maybe_cols if c in df.columns]
    feat_df = df[present].copy()
    feat_df["_s"] = S

    # Per-state stats
    g = feat_df.groupby("_s", observed=True)
    diag = pd.DataFrame({
        "n": g.size(),
        "occ": g.size() / len(feat_df),
    })

    if "Log_Returns" in present:
        diag["mean_ret"] = g["Log_Returns"].mean()
    if "GKVol_20" in present:
        diag["vol"] = g["GKVol_20"].mean()
    if "EMA_20_slope" in present:
        diag["ema_slope"] = g["EMA_20_slope"].mean()
    if "CloseOverEMA20" in present:
        diag["close_over_ema"] = g["CloseOverEMA20"].mean()

    # Dwell stats
    rl = dwell_lengths(S)
    diag["avg_dwell"] = rl.groupby("state")["len"].mean()

    # Short-run share
    short_share = (rl["len"] < args.min_run).mean()

    # Transition matrix
    T, P, original_states = transition_matrix(S)
    K = len(original_states)

    # Role mapping by mean return (fallback to ema_slope if missing)
    if "mean_ret" in diag.columns:
        order = diag["mean_ret"].sort_values().index.tolist()  # low→high
    elif "ema_slope" in diag.columns:
        order = diag["ema_slope"].sort_values().index.tolist()
    else:
        order = diag["n"].sort_values().index.tolist()

    role_map = {}
    if len(order) >= 3:
        role_map[order[0]] = "Bearish"
        role_map[order[1]] = "Chop"
        role_map[order[2]] = "Bullish"
    else:
        # Generic roles if K != 3
        for i, s in enumerate(order):
            role_map[s] = f"State_{i}"

    diag = diag.sort_index()
    diag["role"] = [role_map.get(s, f"State_{s}") for s in diag.index]

    # Print summary
    print(f"\nDetected state column: {state_col} (K={K})")
    print("\nPer-state diagnostics:")
    print(diag.round(4))

    print(f"\nShort-run share (< {args.min_run} bars): {short_share:.4f}")

    # Pretty transition matrices with original labels as index/cols
    T_df = pd.DataFrame(T, index=original_states, columns=original_states)
    P_df = pd.DataFrame(P, index=original_states, columns=original_states)

    print("\nTransition counts (rows→cols, original state labels):")
    print(T_df)
    print("\nRow-normalized transition probs:")
    print(P_df.round(4))

    # Save a compact report
    report = diag.copy()
    report.index.name = "state"
    report.reset_index().to_csv(out_dir / "state_diagnostics_report.csv", index=False)
    print(f"\nSaved: {out_dir / 'state_diagnostics_report.csv'}")

    # Optional dwell histogram
    if args.plot_dwell:
        plt.figure(figsize=(7,4))
        for s in sorted(rl["state"].unique()):
            plt.hist(rl.loc[rl["state"]==s, "len"], bins=30, alpha=0.5, label=f"state {s}")
        plt.xlabel("Run length (bars)")
        plt.ylabel("Count")
        plt.title("Dwell length distribution by state")
        plt.legend()
        plt.tight_layout()
        plt.savefig(out_dir / "dwell_hist.png", dpi=140)
        plt.close()
        print(f"Saved: {out_dir / 'dwell_hist.png'}")

if __name__ == "__main__":
    main()
