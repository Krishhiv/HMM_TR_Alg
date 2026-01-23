import pandas as pd

df_15m = pd.read_csv('./velocity_breakout/data/feature_engineered/BTC-USD_15m_features.csv')
df_1h = pd.read_csv('./velocity_breakout/data/feature_engineered/BTC-USD_1h_features.csv')

print('15m columns:')
print(df_15m.columns)
print('')
print('1h columns:')
print(df_1h.columns)