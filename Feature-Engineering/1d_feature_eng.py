import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Loading data
df = pd.read_csv('./data_coinbase_eth/eth_1d.csv')

# Making Date column the index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

print(df.head())
print('')
print('------------------------')
print('')

# Feature engineering (adding required columns)
df['Log_Returns'] = np.log(df['Close']/df['Close'].shift(1))
df.dropna(inplace=True)
df['Abs_Return'] = np.abs(df['Log_Returns'])
df['Squared_Return'] = df['Log_Returns']*df['Log_Returns']

N = 20
TRADING_DAYS = 252 

# Volatility Features - Key for regime detection

# Rolling realized volatility (from squared returns)
#    σ_t = sqrt( (1/N) * Σ r_{t-i}^2 )
df[f'RealizedVol_{N}'] = (
    df['Squared_Return']
    .rolling(window=N, min_periods=N)
    .mean()
    .pipe(np.sqrt)
)


# Parkinson range-based volatility (uses High/Low)
#    σ_P,t = sqrt( (1/(4N ln(2))) * Σ [ ln(High/Low) ]^2 )
hl_log = np.log(df['High'] / df['Low'])
df[f'ParkinsonVol_{N}'] = np.sqrt(
    (hl_log.pow(2).rolling(window=N, min_periods=N).sum()) / (4 * N * np.log(2))
)

# Garman-Klass volatility
#    σ_GK^2 per bar = 0.5 * [ln(High/Low)]^2 - (2ln2 - 1) * [ln(Close/Open)]^2
gk_var_bar = 0.5 * (np.log(df['High'] / df['Low']) ** 2) - (2 * np.log(2) - 1) * (np.log(df['Close'] / df['Open']) ** 2)
df[f'GKVol_{N}'] = np.sqrt(
    gk_var_bar.rolling(window=N, min_periods=N).mean()
)

# VolZ_20 > 0 -> higher-than-average volume
# VolZ_20 < 0 -> lower-than-average volume
df[f'VolZ_{N}'] = (
    (df['Volume'] - df['Volume'].rolling(window=N, min_periods=N).mean())
    / df['Volume'].rolling(window=N, min_periods=N).std()
)

# EMA
df[f'EMA_{N}'] = df['Close'].ewm(span=N, adjust=False).mean()

# EMA Slope
df[f'EMA_{N}_slope'] = df[f'EMA_{N}'].diff()

df.dropna(inplace=True)
print(df.head())

df.to_csv('./Feature-Engineered/eth_1d_eng.csv')