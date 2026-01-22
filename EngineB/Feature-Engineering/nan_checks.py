import numpy as np
import pandas as pd

FILE5 = "EngineB/Data/Feature-Engineered/BTC-USD_5m_features.csv"
FILE15 = "EngineB/Data/Feature-Engineered/BTC-USD_15m_features.csv"

df5 = pd.read_csv(FILE5)
df15 = pd.read_csv(FILE15)

df5["Date"] = pd.to_datetime(df5["Date"], utc=True).dt.tz_convert(None)
df15["Date"] = pd.to_datetime(df15["Date"], utc=True).dt.tz_convert(None)

# Define which columns must be present for your strategy
needed5 = ["FairValue", "EWMAVol", "ZScore", "LiquidityCostProxy", "Hurst15m"]
needed15 = ["Hurst15m"]

mask5 = df5[needed5].apply(pd.to_numeric, errors="coerce").isna().any(axis=1)
mask15 = df15[needed15].apply(pd.to_numeric, errors="coerce").isna().any(axis=1)

def nan_diagnostics(df, mask, name):
    idx = np.flatnonzero(mask.to_numpy())
    print(f"\n{name} NaN rows: {len(idx)} / {len(df)}")

    if len(idx) == 0:
        return

    print("First NaN index:", idx[0], "Date:", df.loc[idx[0], "Date"])
    print("Last  NaN index:", idx[-1], "Date:", df.loc[idx[-1], "Date"])

    # Are they a contiguous prefix?
    is_prefix = np.all(idx == np.arange(idx[0], idx[-1] + 1)) and idx[0] == 0
    print("Contiguous prefix starting at 0:", is_prefix)

    # If not prefix, show some scattered examples
    if not is_prefix:
        print("Sample NaN rows (index, Date):")
        for j in idx[:10]:
            print(j, df.loc[j, "Date"])
        if len(idx) > 10:
            print("...")

nan_diagnostics(df5, mask5, "5m (needed features)")
nan_diagnostics(df15, mask15, "15m (needed features)")
