import pandas as pd
import numpy as np

def calculate_professional_metrics(file_path):
    # 1. Load the data
    df = pd.read_csv(file_path)
    df['exit_time'] = pd.to_datetime(df['exit_time'])
    df = df.sort_values('exit_time')

    # 2. Create Daily Returns (The "Calendar" view)
    # We map trade returns to the day they were realized
    daily_rets = df.set_index('exit_time')['net_ret'].resample('D').sum().fillna(0)
    
    # 3. Cumulative Equity
    cum_equity = (1 + daily_rets).cumprod()
    
    # 4. Calculation Logic
    total_ret = cum_equity.iloc[-1] - 1
    years = (daily_rets.index[-1] - daily_rets.index[0]).days / 365.25
    cagr = (1 + total_ret)**(1/years) - 1
    
    # Annualized Volatility
    ann_vol = daily_rets.std() * np.sqrt(365)
    
    # Sharpe Ratio (Risk Free Rate = 0)
    sharpe = (daily_rets.mean() / daily_rets.std()) * np.sqrt(365)
    
    # Sortino Ratio (Only penalize negative returns)
    downside_rets = daily_rets[daily_rets < 0]
    sortino = (daily_rets.mean() / downside_rets.std()) * np.sqrt(365)
    
    # Max Drawdown
    rolling_max = cum_equity.cummax()
    drawdown = (cum_equity - rolling_max) / rolling_max
    max_dd = drawdown.min()
    
    # Calmar Ratio
    calmar = cagr / abs(max_dd)
    
    # Trade-specific metrics
    win_rate = (df['net_ret'] > 0).mean()
    profit_factor = df[df['net_ret'] > 0]['net_ret'].sum() / abs(df[df['net_ret'] < 0]['net_ret'].sum())
    
    # Display Results
    print(f"--- Quant Performance Report ---")
    print(f"Total Return:      {total_ret*100:.2f}%")
    print(f"CAGR:              {cagr*100:.2f}%")
    print(f"Max Drawdown:      {max_dd*100:.2f}%")
    print(f"Sharpe Ratio:      {sharpe:.2f}")
    print(f"Sortino Ratio:     {sortino:.2f}")
    print(f"Calmar Ratio:      {calmar:.2f}")
    print(f"Profit Factor:     {profit_factor:.2f}")
    print(f"Win Rate:          {win_rate*100:.2f}%")
    print(f"Annual Volatility: {ann_vol*100:.2f}%")

# Execute
calculate_professional_metrics('./TRADING-MODELS/Results_Logs/TR_Model_Log2.csv')