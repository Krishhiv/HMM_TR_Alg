import numpy as np
import pandas as pd
from pathlib import Path
from math import sqrt
from datetime import datetime

# =========================
# Metrics (your formulas)
# =========================
def max_drawdown(equity_curve: np.ndarray) -> float:
    peaks = np.maximum.accumulate(equity_curve)
    dd = equity_curve / peaks - 1.0
    return dd.min() if len(dd) else 0.0

def profit_factor_from_returns(rets: np.ndarray) -> float:
    gains = rets[rets > 0].sum()
    losses = -rets[rets < 0].sum()
    return np.nan if losses == 0 else gains / losses

def ann_stats_from_trades_exact(trade_rets: np.ndarray, start_ts: pd.Timestamp, end_ts: pd.Timestamp) -> dict:
    """
    Matches your earlier formulas:
      years   = (dates[-1] - dates[0]) / 365.25 days
      CAGR    = equity[-1] ** (1/years) - 1
      Sharpe  = (mu/sd) * sqrt(24 * 365.25)  (ddof=0)
      WinRate = (ret > 0).mean()   # strict
      PF      = gross_profit / gross_loss    # strict
    """
    n = len(trade_rets)
    if n == 0:
        return dict(CAGR=np.nan, Sharpe=np.nan, PF=np.nan, WinRate=np.nan, MDD=np.nan, Trades=0)

    years = (end_ts - start_ts) / pd.Timedelta(days=365.25)
    years = float(years) if years > 0 else np.nan

    equity = np.cumprod(1 + trade_rets)
    cagr = equity[-1] ** (1 / years) - 1 if years and years > 0 and equity[-1] > 0 else np.nan

    mu = np.mean(trade_rets)
    sd = np.std(trade_rets, ddof=0)
    sharpe = (mu / sd) * sqrt(24 * 365.25) if sd > 0 else np.nan

    pf = profit_factor_from_returns(trade_rets)
    winrate_strict = (trade_rets > 0).mean()
    mdd = max_drawdown(equity)

    return dict(CAGR=cagr, Sharpe=sharpe, PF=pf, WinRate=winrate_strict, MDD=mdd, Trades=n)

# =========================
# Bootstrap samplers
# =========================
def bootstrap_sample(trade_rets: np.ndarray, n_trades: int) -> np.ndarray:
    return np.random.choice(trade_rets, size=n_trades, replace=True)

def block_bootstrap_sample(trade_rets: np.ndarray, n_trades: int, avg_block=5) -> np.ndarray:
    if avg_block < 1:
        avg_block = 1
    n = len(trade_rets)
    out = []
    p = 1.0 / avg_block  # geometric parameter
    while len(out) < n_trades:
        start = np.random.randint(0, n)
        L = max(1, np.random.geometric(p))
        block = trade_rets[start : min(start + L, n)]
        out.extend(block.tolist())
    return np.array(out[:n_trades])

def monte_carlo_exact(
    trade_rets: np.ndarray,
    start_ts: pd.Timestamp,
    end_ts: pd.Timestamp,
    n_runs: int = 5000,
    sampler: str = "block",
    avg_block: int = 4,
    random_state: int | None = 42,
):
    np.random.seed(random_state)
    n_trades = len(trade_rets)
    rows = []
    for _ in range(n_runs):
        sample = (
            block_bootstrap_sample(trade_rets, n_trades, avg_block=avg_block)
            if sampler == "block"
            else bootstrap_sample(trade_rets, n_trades)
        )
        rows.append(ann_stats_from_trades_exact(sample, start_ts, end_ts))
    return pd.DataFrame(rows)

def summarize(df_stats: pd.DataFrame) -> pd.DataFrame:
    pct = [5, 10, 25, 50, 75, 90, 95]
    out = pd.DataFrame({
        "CAGR":   np.percentile(df_stats["CAGR"].dropna(), pct) if df_stats["CAGR"].notna().any() else [np.nan]*7,
        "Sharpe": np.percentile(df_stats["Sharpe"].dropna(), pct) if df_stats["Sharpe"].notna().any() else [np.nan]*7,
        "PF":     np.percentile(df_stats["PF"].dropna(), pct) if df_stats["PF"].notna().any() else [np.nan]*7,
        "WinRate":np.percentile(df_stats["WinRate"].dropna(), pct) if df_stats["WinRate"].notna().any() else [np.nan]*7,
        "MDD":    np.percentile(df_stats["MDD"].dropna(), pct) if df_stats["MDD"].notna().any() else [np.nan]*7,
    }, index=[f"{p}%" for p in pct])
    return out

# =========================
# Runner for one CSV
# =========================
def run_one(csv_path: Path, n_runs=5000, sampler="block", avg_block=4, random_state=42,
            save_runs_csv=True):
    df = pd.read_csv(csv_path)

    # Parse times UTC for consistency (adjust if needed)
    df["entry_time"] = pd.to_datetime(df["entry_time"], errors="coerce", utc=True)
    df["exit_time"]  = pd.to_datetime(df["exit_time"],  errors="coerce", utc=True)

    # Inputs
    if "net_ret" not in df.columns:
        raise ValueError(f"{csv_path.name}: Expected column 'net_ret' in CSV.")
    trade_rets = pd.to_numeric(df["net_ret"], errors="coerce").dropna().values

    if not df["entry_time"].notna().any() or not df["exit_time"].notna().any():
        raise ValueError(f"{csv_path.name}: Need valid 'entry_time' and 'exit_time' to compute years.")
    start_ts = df["entry_time"].min()
    end_ts   = df["exit_time"].max()

    # Baseline (historical)
    baseline = ann_stats_from_trades_exact(trade_rets, start_ts, end_ts)

    # Monte Carlo
    stats_df = monte_carlo_exact(
        trade_rets=trade_rets,
        start_ts=start_ts,
        end_ts=end_ts,
        n_runs=n_runs,
        sampler=sampler,
        avg_block=avg_block,
        random_state=random_state
    )
    summary_df = summarize(stats_df)

    # Tail/targets
    probs = {
        "P(Sharpe≥1.5)": (stats_df["Sharpe"] >= 1.5).mean(),
        "P(Sharpe≥2.0)": (stats_df["Sharpe"] >= 2.0).mean(),
        "P(CAGR≤0)":     (stats_df["CAGR"] <= 0).mean(),
    }

    # Optionally save full runs
    if save_runs_csv:
        out_csv = csv_path.with_name(csv_path.stem + "_mc_runs.csv")
        stats_df.to_csv(out_csv, index=False)

    return baseline, summary_df, probs

# =========================
# Batch over all files & write TXT
# =========================
if __name__ == "__main__":
    # Inputs
    files = [
        Path("./TRADING-MODELS/TR_Model_Log3.csv"),
        Path("./TRADING-MODELS/TR_Model_Log2.csv"),
        Path("./TRADING-MODELS/TR_Model_Log1.csv"),
    ]
    report_path = Path("./TRADING-MODELS/TR_Models_MonteCarlo.txt")

    # MC params (tweak as desired)
    N_RUNS = 5000
    SAMPLER = "block"   # "block" or "bootstrap"
    AVG_BLOCK = 4
    SEED = 42
    SAVE_RUNS = True

    # Build report
    lines = []
    lines.append(f"Monte Carlo Report | {datetime.now().isoformat(timespec='seconds')}\n")
    lines.append(f"Params: n_runs={N_RUNS}, sampler={SAMPLER}, avg_block={AVG_BLOCK}, seed={SEED}\n")

    for f in files:
        lines.append("="*80 + "\n")
        lines.append(f"FILE: {f}\n")
        try:
            baseline, summary_df, probs = run_one(
                f, n_runs=N_RUNS, sampler=SAMPLER, avg_block=AVG_BLOCK,
                random_state=SEED, save_runs_csv=SAVE_RUNS
            )

            # Baseline
            lines.append("BASELINE (Historical; your formulas)\n")
            lines.append(
                "CAGR={CAGR:.6f} | Sharpe={Sharpe:.6f} | PF={PF:.6f} | "
                "WinRate={WinRate:.4f} | MDD={MDD:.4f} | Trades={Trades}\n".format(**baseline)
            )

            # Summary percentiles
            lines.append("\nMONTE CARLO SUMMARY (Percentiles; your formulas)\n")
            with pd.option_context("display.float_format", lambda x: f"{x:0.6f}"):
                lines.append(summary_df.to_string() + "\n")

            # Tail probs
            lines.append("\nTail/Target Probabilities\n")
            lines.append(f"P(Sharpe ≥ 1.5): {probs['P(Sharpe≥1.5)']:.3f}\n")
            lines.append(f"P(Sharpe ≥ 2.0): {probs['P(Sharpe≥2.0)']:.3f}\n")
            lines.append(f"P(CAGR ≤ 0):     {probs['P(CAGR≤0)']:.3f}\n")

        except Exception as e:
            lines.append(f"ERROR processing {f.name}: {e}\n")

    # Write report
    report_path.write_text("".join(lines), encoding="utf-8")
    print(f"Saved report to: {report_path}")
