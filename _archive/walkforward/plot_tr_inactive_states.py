import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def _find_date_col(df: pd.DataFrame) -> str:
    for col in ["Date", "date", "timestamp", "time"]:
        if col in df.columns:
            return col
    raise ValueError(f"No date column found. Columns: {df.columns.tolist()}")


def _find_state_col(df: pd.DataFrame) -> str:
    for col in ["State_K3", "State", "state", "HMM_State", "hmm_state", "regime"]:
        if col in df.columns:
            return col
    raise ValueError(f"No state column found. Columns: {df.columns.tolist()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Plot BTC 1D states when TR model is inactive.")
    parser.add_argument(
        "--trades",
        default="walkforward/outputs/trade_log_holdout_ect.csv",
        help="TR trade log CSV.",
    )
    parser.add_argument(
        "--states",
        default="outputs/btc_1d_with_states_compact.csv",
        help="BTC 1D HMM states CSV.",
    )
    parser.add_argument(
        "--out",
        default="walkforward/outputs/tr_inactive_states.png",
        help="Output plot path.",
    )
    args = parser.parse_args()

    trades = pd.read_csv(args.trades)
    trades["entry_time"] = pd.to_datetime(trades["entry_time"], utc=True, errors="coerce")
    trades["exit_time"] = pd.to_datetime(trades["exit_time"], utc=True, errors="coerce")
    trades = trades.dropna(subset=["entry_time", "exit_time"]).sort_values("entry_time")

    states = pd.read_csv(args.states)
    date_col = _find_date_col(states)
    state_col = _find_state_col(states)
    states[date_col] = pd.to_datetime(states[date_col], utc=True, errors="coerce")
    states = states.dropna(subset=[date_col]).sort_values(date_col)

    if trades.empty:
        raise ValueError("Trade log is empty; cannot derive inactive periods.")

    # Build daily active mask from trade intervals
    start_day = trades["entry_time"].min().floor("D")
    end_day = trades["exit_time"].max().ceil("D")
    days = pd.date_range(start_day, end_day, freq="D", tz="UTC")
    active = pd.Series(False, index=days)
    for _, row in trades.iterrows():
        s = row["entry_time"].floor("D")
        e = row["exit_time"].floor("D")
        if pd.isna(s) or pd.isna(e):
            continue
        active.loc[s:e] = True

    daily = states.set_index(date_col).reindex(days)
    daily["active"] = active
    daily["inactive"] = ~daily["active"]

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(daily.index, daily[state_col], drawstyle="steps-post", label="BTC 1D State")

    # Shade inactive periods
    for day, inactive in daily["inactive"].items():
        if inactive:
            ax.axvspan(day, day + pd.Timedelta(days=1), color="red", alpha=0.15)

    ax.set_title("BTC 1D HMM States (TR Inactive Periods Shaded)")
    ax.set_ylabel("State")
    ax.set_xlabel("Date")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right")
    fig.tight_layout()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    print(f"[saved] {out_path}")


if __name__ == "__main__":
    main()
