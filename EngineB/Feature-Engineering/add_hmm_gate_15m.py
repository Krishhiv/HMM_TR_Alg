import argparse
from pathlib import Path

import pandas as pd


def _find_state_column(df: pd.DataFrame) -> str:
    candidates = ["State", "state", "HMM_State", "hmm_state", "regime", "State_K3"]
    for col in candidates:
        if col in df.columns:
            return col
    raise ValueError(f"Could not find HMM state column. Available: {df.columns.tolist()}")


def _find_date_column(df: pd.DataFrame) -> str:
    candidates = ["Date", "date", "timestamp", "time"]
    for col in candidates:
        if col in df.columns:
            return col
    raise ValueError(f"Could not find date column. Available: {df.columns.tolist()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Add D1_State_lag1d to 15m scored dataset.")
    parser.add_argument(
        "--scored-file",
        default="EngineB/Data/BTC-USD_15m_lr_scored.csv",
        help="15m scored CSV to update.",
    )
    parser.add_argument(
        "--daily-states-file",
        default="outputs/btc_1d_with_states_compact.csv",
        help="Daily BTC HMM states CSV.",
    )
    parser.add_argument(
        "--out-file",
        default="EngineB/Data/BTC-USD_15m_lr_scored.csv",
        help="Output CSV (can overwrite input).",
    )
    args = parser.parse_args()

    scored = pd.read_csv(args.scored_file)
    scored["Date"] = pd.to_datetime(scored["Date"], utc=True, errors="coerce")
    scored = scored.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    daily = pd.read_csv(args.daily_states_file)
    date_col = _find_date_column(daily)
    state_col = _find_state_column(daily)

    daily[date_col] = pd.to_datetime(daily[date_col], utc=True, errors="coerce")
    daily = daily.dropna(subset=[date_col]).sort_values(date_col).reset_index(drop=True)
    daily["day"] = daily[date_col].dt.date
    daily["D1_State_lag1d"] = daily[state_col].shift(1)

    state_map = daily.set_index("day")["D1_State_lag1d"].to_dict()
    scored["day"] = scored["Date"].dt.date
    scored["D1_State_lag1d"] = scored["day"].map(state_map)
    scored = scored.drop(columns=["day"])

    out_path = Path(args.out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    scored.to_csv(out_path, index=False)
    print(f"[saved] {out_path}")


if __name__ == "__main__":
    main()
