import pandas as pd
import matplotlib.pyplot as plt


def load_equity_curve(csv_path: str, ret_col: str) -> pd.Series:
    df = pd.read_csv(csv_path)
    df["exit_time"] = pd.to_datetime(df["exit_time"], errors="coerce")
    df = df.dropna(subset=["exit_time"]).sort_values("exit_time")
    daily_rets = df.set_index("exit_time")[ret_col].resample("D").sum().fillna(0.0)
    equity = (1.0 + daily_rets).cumprod()
    return equity


def main():
    raw_path = "walkforward/outputs/trade_log_holdout_raw.csv"
    ect_path = "walkforward/outputs/trade_log_holdout_ect.csv"

    raw_eq = load_equity_curve(raw_path, "net_ret")
    ect_eq = load_equity_curve(ect_path, "net_ret_scaled")

    plt.figure(figsize=(10, 5.5))
    plt.plot(raw_eq.index, raw_eq.values, label="Raw (net_ret)")
    plt.plot(ect_eq.index, ect_eq.values, label="ECT (net_ret_scaled)")
    plt.title("Equity Curve: Raw vs ECT")
    plt.xlabel("Date")
    plt.ylabel("Equity (base=1.0)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
