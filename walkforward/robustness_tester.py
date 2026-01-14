import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_robustness_test(file_path):
    df = pd.read_csv(file_path)
    ret_col = "net_ret_scaled" if "net_ret_scaled" in df.columns else "net_ret"
    rets = df[ret_col].values
    
    print(f"Analyzing: {file_path}")
    print(f"Total Trades: {len(rets)}")
    print("-" * 30)

    # 1. Profit Concentration (Pareto Test)
    sorted_rets = np.sort(rets)[::-1]
    total_profit = np.sum(sorted_rets[sorted_rets > 0])
    cumulative_profit = np.cumsum(sorted_rets[sorted_rets > 0])
    trades_for_80pct = np.argwhere(cumulative_profit >= total_profit * 0.8)[0][0] + 1
    print(f"[CONCENTRATION] {trades_for_80pct} trades ({(trades_for_80pct/len(rets))*100:.1f}%) generate 80% of total profit.")

    # 2. "Bad Luck" Test - Removing top 5% of trades
    num_to_remove = int(len(rets) * 0.05)
    bad_luck_rets = np.sort(rets)[:-num_to_remove]
    bl_equity = np.cumprod(1 + bad_luck_rets)[-1] - 1
    print(f"[STRESS TEST] Removing top 5% of winners: Total Return drops to {bl_equity*100:.2f}%")

    # 3. Monte Carlo Simulation (5,000 paths)
    iterations = 5000
    mc_drawdowns = []
    mc_returns = []
    
    for _ in range(iterations):
        # Shuffle with replacement
        shuffled = np.random.choice(rets, size=len(rets), replace=True)
        equity = np.cumprod(1 + shuffled)
        peak = np.maximum.accumulate(equity)
        dd = (equity - peak) / peak
        mc_drawdowns.append(np.min(dd))
        mc_returns.append(equity[-1] - 1)

    print(f"[MONTE CARLO] Median Max Drawdown: {np.median(mc_drawdowns)*100:.2f}%")
    print(f"[MONTE CARLO] 95th Percentile Max DD: {np.percentile(mc_drawdowns, 5)*100:.2f}%")
    print(f"[MONTE CARLO] Probability of DD > 20%: {(np.array(mc_drawdowns) < -0.20).mean()*100:.2f}%")
    
    # 4. Outlier Analysis (Robustness of edge)
    expectancy = np.mean(rets)
    std_dev = np.std(rets)
    print(f"[RELIABILITY] Trade Expectancy: {expectancy*100:.4f}% +/- {std_dev*100:.2f}%")

    # Plotting for visual confirmation
    plt.figure(figsize=(10, 5))
    plt.hist(mc_drawdowns, bins=50, color='salmon', alpha=0.7)
    plt.axvline(np.percentile(mc_drawdowns, 5), color='red', linestyle='--', label='95% Confidence Limit')
    plt.title("Distribution of Max Drawdowns (Monte Carlo)")
    plt.xlabel("Max Drawdown")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig("robustness_report.png")
    print("-" * 30)
    print("Report image saved as 'robustness_report.png'")

if __name__ == "__main__":
    import sys
    file = sys.argv[1] if len(sys.argv) > 1 else "walkforward/outputs/trade_log_holdout_ect.csv"
    run_robustness_test(file)