import pandas as pd

FILE5  = "EngineB/Data/Feature-Engineered/BTC-USD_5m_features.csv"
FILE15 = "EngineB/Data/Feature-Engineered/BTC-USD_15m_features.csv"

OUT5  = "EngineB/Data/Feature-Engineered/BTC-USD_5m_features_clean.csv"
OUT15 = "EngineB/Data/Feature-Engineered/BTC-USD_15m_features_clean.csv"

# Your verified warmup sizes
CUT5 = 600
CUT15 = 199

df5 = pd.read_csv(FILE5)
df15 = pd.read_csv(FILE15)

df5_clean = df5.iloc[CUT5:].reset_index(drop=True)
df15_clean = df15.iloc[CUT15:].reset_index(drop=True)

df5_clean.to_csv(OUT5, index=False)
df15_clean.to_csv(OUT15, index=False)

print("Wrote:", OUT5, "rows:", len(df5_clean))
print("Wrote:", OUT15, "rows:", len(df15_clean))

needed5 = ["FairValue","EWMAVol","ZScore","LiquidityCostProxy","Hurst15m"]
needed15 = ["Hurst15m"]

print("5m remaining NaN rows:", df5_clean[needed5].isna().any(axis=1).sum())
print("15m remaining NaN rows:", df15_clean[needed15].isna().any(axis=1).sum())
