import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class VolatilitySqueezeBT:
    def __init__(self, initial_capital=2000, base_risk=0.025, max_positions=2):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.position = 0
        self.entry_price = 0
        self.highest_price = 0
        self.stop_price = 0
        self.max_equity = initial_capital
        self.base_risk = base_risk
        self.max_positions = max_positions
        self.next_entry_time = None
        
        # Track trades
        self.trades = []
        self.equity_curve = []
    
    @staticmethod
    def load_and_align_data(hourly_path, daily_path):
        """
        Load CSV files and align them properly
        
        Args:
            hourly_path: Path to hourly OHLCV CSV
            daily_path: Path to daily OHLCV CSV
        
        Returns:
            Tuple of (df_hourly, df_daily) with aligned date ranges
        """
        # Load hourly data
        df_h = pd.read_csv(hourly_path)
        df_h.columns = df_h.columns.str.lower()  # Normalize to lowercase
        df_h['date'] = pd.to_datetime(df_h['date'])
        df_h = df_h.set_index('date').sort_index()
        
        # Load daily data
        df_d = pd.read_csv(daily_path)
        df_d.columns = df_d.columns.str.lower()  # Normalize to lowercase
        df_d['date'] = pd.to_datetime(df_d['date'])
        df_d = df_d.set_index('date').sort_index()
        
        # Find overlapping date range
        hourly_start = df_h.index.min()
        hourly_end = df_h.index.max()
        daily_start = df_d.index.min()
        daily_end = df_d.index.max()
        
        # Use the intersection (latest start, earliest end)
        aligned_start = max(hourly_start, daily_start)
        aligned_end = min(hourly_end, daily_end)
        
        print(f"\n{'='*60}")
        print(f"DATA ALIGNMENT")
        print(f"{'='*60}")
        print(f"Hourly data range: {hourly_start.date()} to {hourly_end.date()}")
        print(f"Daily data range:  {daily_start.date()} to {daily_end.date()}")
        print(f"Aligned range:     {aligned_start.date()} to {aligned_end.date()}")
        print(f"Hourly records: {len(df_h)} -> {len(df_h[aligned_start:aligned_end])}")
        print(f"Daily records:  {len(df_d)} -> {len(df_d[aligned_start:aligned_end])}")
        print(f"{'='*60}\n")
        
        # Filter to aligned range
        df_h = df_h[aligned_start:aligned_end]
        df_d = df_d[aligned_start:aligned_end]
        
        # Validate we have data
        if len(df_h) == 0 or len(df_d) == 0:
            raise ValueError("No overlapping data between hourly and daily datasets!")
        
        return df_h, df_d
        
    def calculate_indicators(self, df_hourly, df_daily):
        """Calculate all required indicators"""
        # Hourly indicators
        df_h = df_hourly.copy()
        
        # Bollinger Bands (20-period on hourly)
        df_h['BB_Middle'] = df_h['close'].rolling(20).mean()
        df_h['BB_Std'] = df_h['close'].rolling(20).std()
        df_h['BB_Upper'] = df_h['BB_Middle'] + (2 * df_h['BB_Std'])
        df_h['BB_Lower'] = df_h['BB_Middle'] - (2 * df_h['BB_Std'])
        
        # ATR (14-period on hourly)
        df_h['H-L'] = df_h['high'] - df_h['low']
        df_h['H-PC'] = abs(df_h['high'] - df_h['close'].shift(1))
        df_h['L-PC'] = abs(df_h['low'] - df_h['close'].shift(1))
        df_h['TR'] = df_h[['H-L', 'H-PC', 'L-PC']].max(axis=1)
        df_h['ATR'] = df_h['TR'].rolling(14).mean()
        
        # Bandwidth (for squeeze detection)
        df_h['Bandwidth'] = (df_h['BB_Upper'] - df_h['BB_Lower']) / df_h['BB_Middle']
        df_h['BW_Avg'] = df_h['Bandwidth'].rolling(100).mean()
        df_h['Is_Squeezed'] = df_h['Bandwidth'] < (df_h['BW_Avg'] * 1.1)
        
        # Daily EMA (50-period)
        df_d = df_daily.copy()
        df_d['EMA_50'] = df_d['close'].ewm(span=50, adjust=False).mean()
        
        # Merge daily EMA into hourly data (forward fill for intraday hours)
        df_h = df_h.reset_index()
        df_h['date_only'] = df_h['date'].dt.date
        
        df_d_reset = df_d.reset_index()
        df_d_reset['date_only'] = df_d_reset['date'].dt.date
        df_d_reset = df_d_reset[['date_only', 'EMA_50']]
        
        df_h = df_h.merge(df_d_reset, on='date_only', how='left')
        df_h['EMA_50'] = df_h['EMA_50'].ffill()
        df_h = df_h.set_index('date')
        df_h = df_h.drop('date_only', axis=1)
        
        return df_h
    
    def run_backtest(self, df_hourly, df_daily, start_date=None, end_date=None):
        """Run the backtest"""
        # Reset state
        self.cash = self.initial_capital
        self.position = 0
        self.max_equity = self.initial_capital
        self.trades = []
        self.equity_curve = []
        self.next_entry_time = None
        
        # Calculate indicators
        df = self.calculate_indicators(df_hourly, df_daily)
        
        # Filter by date range if provided
        if start_date:
            df = df[df.index >= start_date]
        if end_date:
            df = df[df.index <= end_date]
        
        # Drop NaN rows from indicator calculation
        df = df.dropna()
        
        if len(df) == 0:
            raise ValueError("No data available after filtering and indicator calculation!")
        
        for timestamp, row in df.iterrows():
            price = row['close']
            
            # Update equity
            if self.position > 0:
                position_value = self.position * price
                equity = self.cash + position_value
            else:
                equity = self.cash
            
            self.equity_curve.append({'timestamp': timestamp, 'equity': equity})
            
            # Update max equity for drawdown calculation
            if equity > self.max_equity:
                self.max_equity = equity
            
            # Calculate current drawdown and adjust risk
            current_drawdown = (self.max_equity - equity) / self.max_equity
            risk_multiplier = 1.0 if current_drawdown < 0.15 else 0.5
            current_risk = self.base_risk * risk_multiplier
            
            # Skip if we're in cooldown period
            if self.next_entry_time and timestamp < self.next_entry_time:
                continue
            
            # ENTRY LOGIC
            if self.position == 0:
                # Check all entry conditions
                daily_trend_ok = price > row['EMA_50']
                is_squeezed = row['Is_Squeezed']
                bb_breakout = price > row['BB_Upper']
                
                if daily_trend_ok and is_squeezed and bb_breakout:
                    # Position sizing based on ATR
                    stop_dist = row['ATR'] * 2.5
                    if stop_dist > 0:
                        quantity = (equity * current_risk) / stop_dist
                        cost = quantity * price
                        
                        if cost <= equity:  # Can afford the position
                            self.position = quantity
                            self.cash -= cost
                            self.entry_price = price
                            self.highest_price = price
                            self.stop_price = price - stop_dist
                            
                            self.trades.append({
                                'entry_time': timestamp,
                                'entry_price': price,
                                'quantity': quantity,
                                'type': 'BUY'
                            })
            
            # EXIT LOGIC
            else:
                # Update highest price
                if price > self.highest_price:
                    self.highest_price = price
                
                # Calculate trailing stop
                profit_pct = (price - self.entry_price) / self.entry_price
                multiplier = 1.5 if profit_pct > 0.02 else 2.5
                trailing_level = self.highest_price - (row['ATR'] * multiplier)
                
                self.stop_price = max(self.stop_price, trailing_level)
                
                # Exit conditions
                if price < self.stop_price or price < row['EMA_50']:
                    # Close position
                    proceeds = self.position * price
                    pnl = proceeds - (self.position * self.entry_price)
                    pnl_pct = (price - self.entry_price) / self.entry_price
                    
                    self.cash += proceeds
                    
                    self.trades[-1].update({
                        'exit_time': timestamp,
                        'exit_price': price,
                        'pnl': pnl,
                        'pnl_pct': pnl_pct * 100,
                        'exit_reason': 'Stop' if price < self.stop_price else 'EMA'
                    })
                    
                    self.position = 0
                    self.next_entry_time = timestamp + timedelta(hours=12)
        
        return self.get_performance_metrics()
    
    def get_performance_metrics(self):
        """Calculate performance statistics"""
        equity_df = pd.DataFrame(self.equity_curve).set_index('timestamp')
        trades_df = pd.DataFrame(self.trades)
        
        final_equity = equity_df['equity'].iloc[-1]
        total_return = (final_equity - self.initial_capital) / self.initial_capital * 100
        
        # Calculate drawdown
        equity_df['Peak'] = equity_df['equity'].cummax()
        equity_df['Drawdown'] = (equity_df['equity'] - equity_df['Peak']) / equity_df['Peak']
        max_drawdown = equity_df['Drawdown'].min() * 100
        
        # Trade statistics
        completed_trades = trades_df[trades_df['pnl'].notna()]
        num_trades = len(completed_trades)
        
        if num_trades > 0:
            win_rate = (completed_trades['pnl'] > 0).sum() / num_trades * 100
            avg_win = completed_trades[completed_trades['pnl'] > 0]['pnl_pct'].mean()
            avg_loss = completed_trades[completed_trades['pnl'] < 0]['pnl_pct'].mean()
        else:
            win_rate = avg_win = avg_loss = 0
        
        return {
            'final_equity': final_equity,
            'total_return_pct': total_return,
            'max_drawdown_pct': max_drawdown,
            'num_trades': num_trades,
            'win_rate_pct': win_rate,
            'avg_win_pct': avg_win,
            'avg_loss_pct': avg_loss,
            'equity_curve': equity_df,
            'trades': completed_trades
        }


# Example usage:
if __name__ == "__main__":
    # Load and align your data automatically
    df_hourly, df_daily = VolatilitySqueezeBT.load_and_align_data(
        'btcusd_1h.csv', 
        'btcusd_1d.csv'
    )
    
    # Run backtest
    bt = VolatilitySqueezeBT(initial_capital=2000, base_risk=0.025, max_positions=2)
    results = bt.run_backtest(df_hourly, df_daily, start_date='2020-01-01')
    
    # Print results
    print(f"\n{'='*60}")
    print(f"BACKTEST RESULTS")
    print(f"{'='*60}")
    print(f"Final Equity: ${results['final_equity']:.2f}")
    print(f"Total Return: {results['total_return_pct']:.2f}%")
    print(f"Max Drawdown: {results['max_drawdown_pct']:.2f}%")
    print(f"Number of Trades: {results['num_trades']}")
    print(f"Win Rate: {results['win_rate_pct']:.2f}%")
    if results['num_trades'] > 0:
        print(f"Avg Win: {results['avg_win_pct']:.2f}%")
        print(f"Avg Loss: {results['avg_loss_pct']:.2f}%")
    print(f"{'='*60}\n")
    
    # Show trade details
    if len(results['trades']) > 0:
        print("Recent Trades:")
        print(results['trades'][['entry_time', 'entry_price', 'exit_time', 'exit_price', 'pnl_pct', 'exit_reason']].tail(10))
    
    # Plot equity curve
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(2, 1, figsize=(14, 8))
    
    # Equity curve
    axes[0].plot(results['equity_curve'].index, results['equity_curve']['equity'], linewidth=2)
    axes[0].fill_between(results['equity_curve'].index, 
                         results['equity_curve']['equity'], 
                         2000, alpha=0.3)
    axes[0].axhline(y=2000, color='r', linestyle='--', alpha=0.5, label='Initial Capital')
    axes[0].set_title('Equity Curve', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Equity ($)')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Drawdown
    axes[1].fill_between(results['equity_curve'].index, 
                         results['equity_curve']['Drawdown'] * 100, 
                         0, color='red', alpha=0.3)
    axes[1].plot(results['equity_curve'].index, 
                results['equity_curve']['Drawdown'] * 100, 
                color='darkred', linewidth=2)
    axes[1].set_title('Drawdown', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Drawdown (%)')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()