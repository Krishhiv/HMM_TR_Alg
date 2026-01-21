import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def compute_metrics(trades: pd.DataFrame) -> dict:
    if trades.empty:
        return {}
    df = trades.copy()
    df["exit_time"] = pd.to_datetime(df["exit_time"], utc=True, errors="coerce")
    df = df.dropna(subset=["exit_time"]).sort_values("exit_time")

    daily_rets = df.set_index("exit_time")["net_ret_scaled"].resample("D").sum().fillna(0.0)
    equity = (1 + daily_rets).cumprod()
    total_ret = equity.iloc[-1] - 1
    years = (daily_rets.index[-1] - daily_rets.index[0]).days / 365.25
    cagr = (1 + total_ret) ** (1 / years) - 1 if years > 0 else float("nan")

    ann_vol = daily_rets.std() * np.sqrt(365)
    sharpe = (daily_rets.mean() / daily_rets.std()) * np.sqrt(365) if daily_rets.std() > 0 else float("nan")

    downside = daily_rets[daily_rets < 0]
    sortino = (daily_rets.mean() / downside.std()) * np.sqrt(365) if downside.std() > 0 else float("nan")

    rolling_max = equity.cummax()
    drawdown = (equity - rolling_max) / rolling_max
    max_dd = drawdown.min()
    calmar = cagr / abs(max_dd) if max_dd < 0 else float("nan")

    win_rate = (df["net_ret_scaled"] > 0).mean()
    profits = df.loc[df["net_ret_scaled"] > 0, "net_ret_scaled"].sum()
    losses = df.loc[df["net_ret_scaled"] < 0, "net_ret_scaled"].sum()
    profit_factor = (profits / abs(losses)) if losses < 0 else float("nan")

    return {
        "Total Return": total_ret,
        "CAGR": cagr,
        "Max Drawdown": max_dd,
        "Sharpe Ratio": sharpe,
        "Sortino Ratio": sortino,
        "Calmar Ratio": calmar,
        "Profit Factor": profit_factor,
        "Win Rate": win_rate,
        "Annual Volatility": ann_vol,
    }


def simulate_engine_b(
    df: pd.DataFrame,
    base_risk: float,
    p_threshold: float,
    stop_sigma: float,
    emergency_sigma: float,
    vol_pause_pct: float,
    timeout_bars: int,
    use_hmm_gate: bool,
) -> pd.DataFrame:
    trades = []
    in_pos = False
    side = None
    entry_time = None
    entry_price = None
    entry_spread = None
    entry_sigma = None
    entry_prob = None
    entry_risk = None
    cooldown = 0

    for i in range(len(df) - 1):
        row = df.iloc[i]
        next_row = df.iloc[i + 1]

        if cooldown > 0:
            cooldown -= 1

        if not in_pos:
            if cooldown > 0:
                continue
            if use_hmm_gate and row.get("D1_State_lag1d", 0) != 0:
                continue

            if row["vol_pct_500"] > vol_pause_pct:
                cooldown = 16
                continue

            spread = row["spread"]
            spread_vel = row["spread_vel"]
            prob = row["P_16"]
            sigma = row["sigma_100"]

            if not np.isfinite([spread, spread_vel, prob, sigma]).all():
                continue

            if prob <= p_threshold:
                continue

            # Exhaustion confirmation and direction
            if spread > 2.0 and spread_vel < 0:
                side = "short"
            elif spread < -2.0 and spread_vel > 0:
                side = "long"
            else:
                continue

            avg_gain = abs(row["Close"] - row["vwap"])
            avg_loss = stop_sigma * sigma
            if avg_loss <= 0:
                continue
            ev = prob * avg_gain - (1 - prob) * avg_loss
            if ev <= 0:
                continue

            edge = ev / avg_loss
            risk_factor = base_risk * max(0.0, min(edge, 1.0))
            if risk_factor <= 0:
                continue

            entry_time = next_row["Date"]
            entry_price = next_row["Open"]
            entry_spread = spread
            entry_sigma = sigma
            entry_prob = prob
            entry_risk = risk_factor
            in_pos = True
            entry_index = i + 1
            continue

        # Exit logic
        spread_now = row["spread"]
        prob_now = row["P_16"]

        exit_reason = None
        exit_price = row["Close"]

        if np.isfinite(spread_now) and abs(spread_now) > emergency_sigma:
            exit_reason = "emergency_sigma"
        elif np.isfinite(spread_now) and abs(spread_now) >= stop_sigma:
            exit_reason = "stop_sigma"
        elif row.get("touch_vwap", 0) == 1 or (np.isfinite(spread_now) and spread_now == 0):
            exit_reason = "vwap_touch"
        elif np.isfinite(prob_now) and prob_now < p_threshold:
            exit_reason = "edge_decay"
        elif (row["Date"] - entry_time) >= pd.Timedelta(minutes=15 * timeout_bars):
            exit_reason = "timeout"

        if exit_reason:
            if side == "long":
                net_ret = (exit_price - entry_price) / entry_price
            else:
                net_ret = (entry_price - exit_price) / entry_price

            trades.append(
                {
                    "entry_time": entry_time,
                    "exit_time": row["Date"],
                    "side": side,
                    "entry_price": entry_price,
                    "exit_price": exit_price,
                    "net_ret": net_ret,
                    "net_ret_scaled": net_ret * entry_risk,
                    "risk_factor": entry_risk,
                    "entry_spread": entry_spread,
                    "entry_sigma": entry_sigma,
                    "entry_prob": entry_prob,
                    "exit_reason": exit_reason,
                    "holding_bars": (row["Date"] - entry_time) / pd.Timedelta(minutes=15),
                }
            )

            in_pos = False
            side = None
            entry_time = None
            entry_price = None
            entry_spread = None
            entry_sigma = None
            entry_prob = None
            entry_risk = None

    return pd.DataFrame(trades)


def main() -> None:
    parser = argparse.ArgumentParser(description="Engine B mean reversion holdout simulator.")
    parser.add_argument(
        "--file",
        default="EngineB/Data/BTC-USD_15m_lr_scored.csv",
        help="Scored 15m dataset with P_16.",
    )
    parser.add_argument("--out-dir", default="EngineB/Outputs/engine_b", help="Output directory.")
    parser.add_argument("--base-risk", type=float, default=0.005, help="Base risk per trade (fraction of equity).")
    parser.add_argument("--p-threshold", type=float, default=0.50, help="Probability threshold.")
    parser.add_argument("--stop-sigma", type=float, default=3.5, help="Stop in S-space.")
    parser.add_argument("--emergency-sigma", type=float, default=4.0, help="Emergency sigma exit.")
    parser.add_argument("--vol-pause-pct", type=float, default=0.95, help="Volatility percentile pause.")
    parser.add_argument("--timeout-bars", type=int, default=32, help="Timeout in 15m bars.")
    parser.add_argument("--use-hmm-gate", action="store_true", help="Require D1_State_lag1d == 0.")
    args = parser.parse_args()

    df = pd.read_csv(args.file)
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    required = [
        "Open",
        "High",
        "Low",
        "Close",
        "vwap",
        "sigma_100",
        "spread",
        "spread_vel",
        "touch_vwap",
        "time_since_vwap",
        "vol_pct_500",
        "P_16",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if args.use_hmm_gate and "D1_State_lag1d" not in df.columns:
        print("[warn] D1_State_lag1d missing; HMM gate disabled.")
        args.use_hmm_gate = False

    trades = simulate_engine_b(
        df,
        base_risk=args.base_risk,
        p_threshold=args.p_threshold,
        stop_sigma=args.stop_sigma,
        emergency_sigma=args.emergency_sigma,
        vol_pause_pct=args.vol_pause_pct,
        timeout_bars=args.timeout_bars,
        use_hmm_gate=args.use_hmm_gate,
    )

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    trade_path = out_dir / "engine_b_trades.csv"
    trades.to_csv(trade_path, index=False)

    metrics = compute_metrics(trades)
    summary_path = out_dir / "engine_b_summary.txt"
    with open(summary_path, "w") as f:
        f.write("Engine B Holdout Summary\n")
        f.write(f"Trades: {len(trades)}\n")
        for k, v in metrics.items():
            if k in ["Total Return", "CAGR", "Max Drawdown", "Win Rate", "Annual Volatility"]:
                f.write(f"{k}: {v:.2%}\n")
            else:
                f.write(f"{k}: {v:.2f}\n")

    print(f"[saved] trades -> {trade_path}")
    print(f"[saved] summary -> {summary_path}")


if __name__ == "__main__":
    main()
