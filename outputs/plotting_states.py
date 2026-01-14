# plot_1d_states_colored.py
# ------------------------------------------------------------
# Plot BTC-USD Daily Close colored by HMM states from a CSV that
# already contains the state labels.
#
# Color map (requested):
#   State 0 -> yellow
#   State 1 -> green
#   State 2 -> red
#
# Input:  ./outputs/btc_1d_with_states_compact.csv
#   Must have columns: Date, Close, and one state column whose
#   name starts with 'State' (e.g., 'State_K3').
#
# Output: ./outputs/btc_1d_colored_states.png
#
# Usage:
#   python plot_1d_states_colored.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from pathlib import Path

# -----------------------------
# Config
# -----------------------------
CSV_PATH   = "./outputs/btc_1d_with_states_compact.csv"
DATE_COL   = "Date"
CLOSE_COL  = "Close"
STATE_COL  = None         # set to the exact name if you want; otherwise auto-detect
PLOT_LAST_DAYS = None     # e.g., 900 to show ~2.5y. Use None for full history.

OUT_DIR = Path("./outputs")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PNG = OUT_DIR / "btc_1d_colored_states.png"

# Color mapping
COLOR_MAP = {
    0: "yellow",
    1: "green",
    2: "red",
}
COLOR_DEFAULT = (0.6, 0.6, 0.6, 0.9)  # for any unexpected state id

# -----------------------------
# Load & prepare
# -----------------------------
df = pd.read_csv(CSV_PATH)
if DATE_COL not in df.columns:
    # assume first column is the datetime if unnamed
    df.rename(columns={df.columns[0]: DATE_COL}, inplace=True)

# parse datetimes to UTC-aware, then drop tz for Matplotlib
df[DATE_COL] = pd.to_datetime(df[DATE_COL], utc=True, errors="coerce")
df = df.dropna(subset=[DATE_COL, CLOSE_COL]).set_index(DATE_COL).sort_index()
if df.index.tz is not None:
    idx = df.index.tz_convert("UTC").tz_localize(None)
    df.index = idx

# find state column if not provided
if STATE_COL is None:
    state_candidates = [c for c in df.columns if c.lower().startswith("state")]
    if not state_candidates:
        raise ValueError("No state column found. Expect a column starting with 'State'.")
    STATE_COL = state_candidates[-1]  # pick the last one if multiple exist

# ensure numeric state labels (int)
df = df.dropna(subset=[STATE_COL]).copy()
df[STATE_COL] = pd.to_numeric(df[STATE_COL], errors="coerce").astype(int)

# Optional window for plotting
if PLOT_LAST_DAYS:
    cut = df.index.max() - pd.Timedelta(days=int(PLOT_LAST_DAYS))
    df = df.loc[df.index >= cut]

# -----------------------------
# Build colored line segments
# -----------------------------
x = mdates.date2num(df.index.to_pydatetime())
y = df[CLOSE_COL].to_numpy()

# segments between consecutive points
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# color by state at the start of each segment
seg_states = df[STATE_COL].to_numpy()[:-1]
seg_colors = [COLOR_MAP.get(int(s), COLOR_DEFAULT) for s in seg_states]

# -----------------------------
# Plot
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))
lc = LineCollection(segments, colors=seg_colors, linewidth=1.4)
ax.add_collection(lc)

ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min() * 0.98, y.max() * 1.02)
ax.set_title(f"BTC-USD Daily Close — colored by HMM states ({STATE_COL})")
ax.set_xlabel("Date")
ax.set_ylabel("Close (USD)")
ax.grid(True, alpha=0.3)

# Format x-axis as dates
locator   = mdates.AutoDateLocator(minticks=3, maxticks=10)
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.figure.autofmt_xdate()

# Legend swatches
uniq_states = sorted(pd.unique(df[STATE_COL]))
handles = []
for s in uniq_states:
    color = COLOR_MAP.get(int(s), COLOR_DEFAULT)
    handles.append(Line2D([0], [0], color=color, lw=2, label=f"State {int(s)}"))
ax.legend(handles=handles, loc="best")

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150)
plt.show()
print(f"Saved plot to: {OUT_PNG.resolve()}")
