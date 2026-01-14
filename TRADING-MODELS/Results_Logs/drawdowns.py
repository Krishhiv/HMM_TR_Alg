import pandas as pd
import numpy as np

df = pd.read_csv('./TRADING-MODELS/Results_Logs/TR_Model_Log3.csv')

r = pd.to_numeric(df['net_ret'], errors='coerce').fillna(0.0)

equity = (1 + r).cumprod()
rolling_max = equity.cummax()
drawdown = equity / rolling_max - 1.0
max_drawdown = drawdown.min()

dd_trough_idx = drawdown.idxmin()
dd_peak_idx = equity.loc[:dd_trough_idx].idxmax()

print(f"Maximum Drawdown (peak-to-trough): {max_drawdown:.2%}")
print(f"MDD peak row index: {dd_peak_idx}, trough row index: {dd_trough_idx}")

loss_mask = r < 0
run_id = (loss_mask != loss_mask.shift()).cumsum()
losing_run_lengths = loss_mask.groupby(run_id).sum()
longest_losing_streak = int(losing_run_lengths[loss_mask.groupby(run_id).any()].max() or 0)

print(f"Longest losing streak (count): {longest_losing_streak}")

run_sums = r.where(loss_mask).groupby(run_id).sum()
losing_run_sums = run_sums[loss_mask.groupby(run_id).any()]
worst_losing_streak_sum = float(losing_run_sums.min() or 0.0)

print(f"Worst losing streak sum: {worst_losing_streak_sum:.4f} ({worst_losing_streak_sum:.2%})")