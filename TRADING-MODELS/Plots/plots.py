import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from pathlib import Path

# --- Load trade log ---
path = './TRADING-MODELS/TR_Model_Log_2.csv'
tl = pd.read_csv(path)

# Parse datetimes
for c in ["entry_time", "exit_time"]:
    tl[c] = pd.to_datetime(tl[c], utc=True, errors="coerce")

# Drop any malformed rows
tl = tl.dropna(subset=["entry_time", "exit_time"]).reset_index(drop=True)

# Choose return column
ret_col = "net_ret" if "net_ret" in tl.columns else "gross_ret"
if ret_col not in tl.columns:
    raise ValueError("Trade log is missing both 'net_ret' and 'gross_ret'.")

# Build an hourly index spanning the trade history
t0 = tl["entry_time"].min().floor("H")
t1 = tl["exit_time"].max().ceil("H")
idx = pd.date_range(t0, t1, freq="H", tz="UTC")

# Hourly return series (additive per hour), to be compounded
r = pd.Series(0.0, index=idx)

# Spread each trade's return evenly (geometric) across its holding hours
Hs   = tl["holding_hours"].to_numpy() if "holding_hours" in tl.columns else None
rets = tl[ret_col].to_numpy()
entries = tl["entry_time"].to_numpy()
exits   = tl["exit_time"].to_numpy()

# Fallback if holding_hours missing: compute from timestamps
if Hs is None or np.isnan(Hs).any():
    Hs = (tl["exit_time"] - tl["entry_time"]).dt.total_seconds().values / 3600.0

for e_time, x_time, H, R in zip(entries, exits, Hs, rets):
    # Map to index
    try:
        e_loc = idx.get_indexer([pd.Timestamp(e_time)])
        x_loc = idx.get_indexer([pd.Timestamp(x_time)])
    except Exception:
        continue
    e_idx = int(e_loc[0])
    x_idx = int(x_loc[0])
    if e_idx == -1 or x_idx == -1:
        # If mapping fails, put the entire return at the nearest hourly exit time
        nearest = idx.get_indexer([pd.Timestamp(x_time)], method="nearest")[0]
        r.iloc[nearest] += R
        continue

    H_int = int(round(H)) if pd.notna(H) else (x_idx - e_idx)
    if H_int <= 0:
        # place entire return on exit bar
        r.iloc[x_idx] += R
        continue

    # per-hour geometric return so that (1+rh)^H_int = 1+R
    rh = (1.0 + R) ** (1.0 / H_int) - 1.0
    end_idx = min(e_idx + H_int, len(r))
    r.iloc[e_idx:end_idx] += rh  # no overlap in this strategy; safe to add

# Equity curve
equity = (1.0 + r).cumprod()

# Drawdown (underwater) series
rolling_max = equity.cummax()
drawdown = (equity / rolling_max) - 1.0

# Save equity series
eq_df = pd.DataFrame({
    "timestamp": equity.index,
    "equity": equity.values,
    "drawdown": drawdown.values
})
eq_csv_path = "./TRADING-MODELS/TR3_equity_timeseries_2.csv"
eq_df.to_csv(eq_csv_path, index=False)

# Plot (single chart, multiple lines; no subplots, no color settings)
plt.figure(figsize=(11, 5.5))
plt.plot(equity.index, equity.values, label="Equity (base=1.0)")
plt.plot(drawdown.index, drawdown.values, label="Drawdown (underwater)")
plt.title("TR³ State-1 Strategy — Equity & Drawdown")
plt.xlabel("Time (UTC)")
plt.ylabel("Equity / Drawdown")
plt.legend()
plt.tight_layout()

fig_path = "./TRADING-MODELS/TR3_equity_curve_2.png"
plt.savefig(fig_path, dpi=160)
plt.show()

fig_path, eq_csv_path
