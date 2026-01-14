import pandas as pd

df = pd.read_csv('./TRADING-MODELS/btc_1h_features_PRIME.csv')

df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
df = df.dropna(subset=["Date"]).set_index("Date").sort_index()

print(df.index.dtype)           # should be datetime64[ns, UTC]
print("tz:", df.index.tz)       # should be UTC

df = df.loc[:, ~df.columns.str.match(r'^Unnamed(:.*)?$')]

df.to_csv('./TRADING-MODELS/btc_1h_features_PRIME.csv')