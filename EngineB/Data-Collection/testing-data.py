import pandas as pd
import numpy as np
import statsmodels.api as sm #type: ignore
from statsmodels.tsa.stattools import adfuller #type: ignore

def run_suitability_audit(file_path):
    print(f"--- Starting Suitability Audit: {file_path} ---")
    
    # 1. LOAD DATA
    # Using your specific column names
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    
    # ==========================================
    # PHASE 1: DATA INTEGRITY CHECKS
    # ==========================================
    print("\n[PHASE 1: INTEGRITY]")
    
    # Check for missing 15m bars (Critical for Velocity calculation)
    expected_range = pd.date_range(start=df['Date'].min(), end=df['Date'].max(), freq='15min')
    missing_bars = len(expected_range) - len(df)
    print(f"Missing 15m Bars: {missing_bars} ({missing_bars/len(expected_range):.4%})")
    
    # Check for zero volume (Can break VWAP calculation)
    zero_vol = (df['Volume'] == 0).sum()
    print(f"Zero Volume Bars: {zero_vol} ({zero_vol/len(df):.4%})")
    
    # Check for extreme price gaps
    max_gap = df['Close'].pct_change().abs().max()
    print(f"Max 15m Price Gap: {max_gap:.2%}")

    # ==========================================
    # FEATURE ENGINEERING (FOR TESTS)
    # ==========================================
    # Calculate Daily VWAP anchored to UTC Daily Open
    df['DayDate'] = df['Date'].dt.date
    df['PV'] = df['Close'] * df['Volume']
    
    grouped = df.groupby('DayDate')
    df['cum_pv'] = grouped['PV'].cumsum()
    df['cum_vol'] = grouped['Volume'].cumsum()
    df['vwap'] = df['cum_pv'] / df['cum_vol']
    
    # Calculate Normalized Spread (S_t)
    df['diff'] = df['Close'] - df['vwap']
    # 100-period rolling window for standard deviation normalization
    df['rolling_std'] = df['diff'].rolling(window=100).std()
    df['spread'] = df['diff'] / df['rolling_std']
    
    # Drop NaNs created by rolling windows for clean stats
    test_series = df['spread'].dropna()

    # ==========================================
    # PHASE 2: STATISTICAL SUITABILITY
    # ==========================================
    print("\n[PHASE 2: STATISTICAL SUITABILITY]")

    # 1. ADF TEST (Stationarity)
    # Testing the 'spread' error because price is non-stationary
    adf_result = adfuller(test_series)
    print(f"ADF Statistic: {adf_result[0]:.4f}")
    print(f"ADF p-value: {adf_result[1]:.4e}")
    if adf_result[1] < 0.05:
        print("RESULT: Stationarity Confirmed (Mean Reversion is mathematically viable).")
    else:
        print("RESULT: FAIL - Series is non-stationary (Trend/Random Walk).")

    # 2. HURST EXPONENT (Mean Reversion Strength)
    # Goal: < 0.5 (Ideal: 0.3 - 0.45)
    def get_hurst(series):
        lags = range(2, 100)
        tau = [np.sqrt(np.std(np.subtract(series[lag:], series[:-lag]))) for lag in lags]
        poly = np.polyfit(np.log(lags), np.log(tau), 1)
        return poly[0] * 2.0

    hurst = get_hurst(test_series.values)
    print(f"Hurst Exponent: {hurst:.4f}")
    if hurst < 0.5:
        print(f"RESULT: Mean Reverting Tendency (Strength: {0.5 - hurst:.4f})")
    else:
        print("RESULT: FAIL - Trending or Random Walk.")

    # 3. HALF-LIFE OF REVERSION
    # Formula: Half-life = -log(2) / beta
    y = test_series.diff()
    x = test_series.shift(1)
    df_hl = pd.DataFrame({"y": y, "x": x}).dropna()
    x = sm.add_constant(df_hl["x"])
    model = sm.OLS(df_hl["y"], x).fit()
    beta = model.params.iloc[1]
    
    if beta < 0:
        halflife = -np.log(2) / beta
        print(f"Half-Life: {halflife:.2f} bars ({(halflife * 15) / 60:.2f} hours)")
        # Guidance for the Logistic Regression N parameter
        print(f"Recommended N (Look-ahead): {int(np.ceil(halflife * 1.5))} to {int(np.ceil(halflife * 2))} bars")
    else:
        print("Half-Life: Infinite (Series does not mean-revert)")

    print("\n--- Audit Complete ---")

# Run the audit on your 15m file
run_suitability_audit('./EngineB/Data/BTC-USD_15m.csv')
