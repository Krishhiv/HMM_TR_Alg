import argparse
import pandas as pd
import numpy as np

def get_max_consecutive_losses(rets):
    """Calculates the longest streak of trades <= 0."""
    is_loss = (rets <= 0).astype(int)
    # This creates a group for every change from win to loss or vice versa
    consecutive = is_loss.groupby((is_loss != is_loss.shift()).cumsum()).cumsum()
    return (consecutive * is_loss).max()

def calculate_professional_metrics(file_path):
    # 1. Load the data
    df = pd.read_csv(file_path)
    df["exit_time"] = pd.to_datetime(df["exit_time"])
    df = df.sort_values("exit_time")

    ret_col = "net_ret_scaled" if "net_ret_scaled" in df.columns else "net_ret"

    # 2. Create Daily Returns (The "Calendar" view)
    # We map trade returns to the day they were realized
    daily_rets = df.set_index("exit_time")[ret_col].resample("D").sum().fillna(0)

    # 3. Cumulative Equity
    cum_equity = (1 + daily_rets).cumprod()

    # 4. Calculation Logic
    total_ret = cum_equity.iloc[-1] - 1
    years = (daily_rets.index[-1] - daily_rets.index[0]).days / 365.25
    cagr = (1 + total_ret) ** (1 / years) - 1

    # Annualized Volatility
    ann_vol = daily_rets.std() * np.sqrt(365)

    # Sharpe Ratio (Risk Free Rate = 0)
    sharpe = (daily_rets.mean() / daily_rets.std()) * np.sqrt(365)

    # Sortino Ratio (Only penalize negative returns)
    downside_rets = daily_rets[daily_rets < 0]
    sortino = (daily_rets.mean() / downside_rets.std()) * np.sqrt(365)

    # Max Drawdown
    rolling_max = cum_equity.cummax()
    drawdown = (cum_equity - rolling_max) / rolling_max
    max_dd = drawdown.min()

    # Calmar Ratio
    calmar = cagr / abs(max_dd)

    # Trade-specific metrics
    win_rate = (df[ret_col] > 0).mean()
    profit_factor = df[df[ret_col] > 0][ret_col].sum() / abs(df[df[ret_col] < 0][ret_col].sum())
    
    max_cons_losses = get_max_consecutive_losses(df[ret_col])
    recovery_factor = total_ret / abs(max_dd) if max_dd != 0 else 0
    expectancy = df[ret_col].mean()

    # Display Results
    print("--- Quant Performance Report (Holdout) ---")
    print(f"Return Column:     {ret_col}")
    print(f"Total Return:      {total_ret*100:.2f}%")
    print(f"CAGR:              {cagr*100:.2f}%")
    print(f"Max Drawdown:      {max_dd*100:.2f}%")
    print(f"Recovery Factor:   {recovery_factor:.2f}") # New
    print(f"Max Cons. Losses:  {max_cons_losses}")    # New
    print(f"Trade Expectancy:  {expectancy*100:.4f}%") # New
    print(f"Sharpe Ratio:      {sharpe:.2f}")
    print(f"Sortino Ratio:     {sortino:.2f}")
    print(f"Calmar Ratio:      {calmar:.2f}")
    print(f"Profit Factor:     {profit_factor:.2f}")
    print(f"Win Rate:          {win_rate*100:.2f}%")
    print(f"Annual Volatility: {ann_vol*100:.2f}%")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="./walkforward/outputs/trade_log_holdout_ect.csv")
    args = parser.parse_args()
    calculate_professional_metrics(args.file)


if __name__ == "__main__":
    main()
