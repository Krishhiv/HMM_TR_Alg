import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys

class WalkForwardTester:
    def __init__(self, df_hourly, df_daily, train_months=12, test_months=3):
        """
        Walk-forward testing framework with automatic data alignment
        
        Args:
            df_hourly: Hourly OHLCV data
            df_daily: Daily OHLCV data
            train_months: Training window in months
            test_months: Testing window in months
        """
        self.df_hourly = df_hourly
        self.df_daily = df_daily
        self.train_months = train_months
        self.test_months = test_months
        
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
        df_h.columns = df_h.columns.str.lower()
        df_h['date'] = pd.to_datetime(df_h['date'])
        df_h = df_h.set_index('date').sort_index()
        
        # Load daily data
        df_d = pd.read_csv(daily_path)
        df_d.columns = df_d.columns.str.lower()
        df_d['date'] = pd.to_datetime(df_d['date'])
        df_d = df_d.set_index('date').sort_index()
        
        # Find overlapping date range
        hourly_start = df_h.index.min()
        hourly_end = df_h.index.max()
        daily_start = df_d.index.min()
        daily_end = df_d.index.max()
        
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
        
        df_h = df_h[aligned_start:aligned_end]
        df_d = df_d[aligned_start:aligned_end]
        
        if len(df_h) == 0 or len(df_d) == 0:
            raise ValueError("No overlapping data between hourly and daily datasets!")
        
        return df_h, df_d
        
    def generate_windows(self):
        """Generate train/test windows"""
        windows = []
        start_date = self.df_hourly.index.min()
        end_date = self.df_hourly.index.max()
        
        # Calculate total months available
        total_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        min_required = self.train_months + self.test_months
        
        if total_months < min_required:
            raise ValueError(f"Not enough data! Need {min_required} months, have {total_months} months")
        
        current_date = start_date
        
        while current_date < end_date:
            train_start = current_date
            train_end = current_date + pd.DateOffset(months=self.train_months)
            test_start = train_end
            test_end = test_start + pd.DateOffset(months=self.test_months)
            
            # Stop if we don't have enough data for a full test period
            if test_end > end_date:
                # Check if we have at least 1 month of test data
                remaining_months = (end_date.year - test_start.year) * 12 + (end_date.month - test_start.month)
                if remaining_months >= 1:
                    test_end = end_date
                else:
                    break
            
            windows.append({
                'train_start': train_start,
                'train_end': train_end,
                'test_start': test_start,
                'test_end': test_end
            })
            
            # Move to next window (advance by test_months)
            current_date = test_end
            
            if test_end >= end_date:
                break
        
        return windows
    
    def optimize_parameters(self, df_h_train, df_d_train, param_grid, bt_class):
        """
        Simple parameter optimization on training data
        
        Args:
            df_h_train: Training hourly data
            df_d_train: Training daily data
            param_grid: Dictionary of parameters to test
            bt_class: Backtest class to use
        """
        best_sharpe = -np.inf
        best_params = None
        
        for base_risk in param_grid.get('base_risk', [0.025]):
            for max_positions in param_grid.get('max_positions', [2]):
                bt = bt_class(
                    initial_capital=2000,
                    base_risk=base_risk,
                    max_positions=max_positions
                )
                
                try:
                    results = bt.run_backtest(df_h_train, df_d_train)
                    
                    # Calculate Sharpe ratio (annualized)
                    equity_curve = results['equity_curve']['equity']
                    returns = equity_curve.pct_change().dropna()
                    
                    if len(returns) > 0 and returns.std() > 0:
                        sharpe = returns.mean() / returns.std() * np.sqrt(365 * 24)
                    else:
                        sharpe = -999
                    
                    if sharpe > best_sharpe:
                        best_sharpe = sharpe
                        best_params = {
                            'base_risk': base_risk,
                            'max_positions': max_positions,
                            'sharpe': sharpe,
                            'return': results['total_return_pct']
                        }
                except Exception as e:
                    print(f"  Error with params {base_risk}, {max_positions}: {str(e)}")
                    continue
        
        return best_params if best_params else {'base_risk': 0.025, 'max_positions': 2, 'sharpe': 0, 'return': 0}
    
    def run_walk_forward(self, bt_class, optimize=True, param_grid=None):
        """
        Run walk-forward analysis
        
        Args:
            bt_class: Backtest class to use (e.g., VolatilitySqueezeBT)
            optimize: Whether to optimize parameters on training data
            param_grid: Parameter grid for optimization
        """
        if param_grid is None:
            param_grid = {
                'base_risk': [0.01, 0.025, 0.05],
                'max_positions': [1, 2, 3]
            }
        
        try:
            windows = self.generate_windows()
        except ValueError as e:
            print(f"Error generating windows: {e}")
            return None
        
        results = []
        
        print(f"\n{'='*60}")
        print(f"WALK-FORWARD ANALYSIS")
        print(f"{'='*60}")
        print(f"Total windows: {len(windows)}")
        print(f"Train period: {self.train_months} months")
        print(f"Test period: {self.test_months} months")
        print(f"{'='*60}\n")
        
        for i, window in enumerate(windows):
            print(f"\nWindow {i+1}/{len(windows)}")
            print(f"  Train: {window['train_start'].date()} to {window['train_end'].date()}")
            print(f"  Test:  {window['test_start'].date()} to {window['test_end'].date()}")
            
            # Split data with safety checks
            df_h_train = self.df_hourly[window['train_start']:window['train_end']]
            df_d_train = self.df_daily[window['train_start']:window['train_end']]
            df_h_test = self.df_hourly[window['test_start']:window['test_end']]
            df_d_test = self.df_daily[window['test_start']:window['test_end']]
            
            # Verify we have data
            if len(df_h_train) == 0 or len(df_d_train) == 0:
                print(f"  WARNING: No training data in this window, skipping...")
                continue
            
            if len(df_h_test) == 0 or len(df_d_test) == 0:
                print(f"  WARNING: No test data in this window, skipping...")
                continue
            
            # Optimize on training data
            if optimize:
                print(f"  Optimizing parameters...")
                best_params = self.optimize_parameters(df_h_train, df_d_train, param_grid, bt_class)
                print(f"  Best params: risk={best_params['base_risk']}, positions={best_params['max_positions']}")
                print(f"  Train Sharpe: {best_params['sharpe']:.2f}, Return: {best_params['return']:.2f}%")
                
                bt_test = bt_class(
                    initial_capital=2000,
                    base_risk=best_params['base_risk'],
                    max_positions=best_params['max_positions']
                )
            else:
                bt_test = bt_class(initial_capital=2000)
                best_params = {'base_risk': 0.025, 'max_positions': 2}
            
            # Run test
            try:
                test_results = bt_test.run_backtest(df_h_test, df_d_test)
                
                results.append({
                    'window': i + 1,
                    'train_start': window['train_start'],
                    'train_end': window['train_end'],
                    'test_start': window['test_start'],
                    'test_end': window['test_end'],
                    'base_risk': best_params['base_risk'],
                    'max_positions': best_params['max_positions'],
                    'train_return': best_params.get('return', 0),
                    'train_sharpe': best_params.get('sharpe', 0),
                    'test_return': test_results['total_return_pct'],
                    'test_drawdown': test_results['max_drawdown_pct'],
                    'test_trades': test_results['num_trades'],
                    'test_winrate': test_results['win_rate_pct']
                })
                
                print(f"  Test Return: {test_results['total_return_pct']:.2f}%")
                print(f"  Test Drawdown: {test_results['max_drawdown_pct']:.2f}%")
                print(f"  Test Trades: {test_results['num_trades']}")
            
            except Exception as e:
                print(f"  ERROR in test period: {str(e)}")
                continue
        
        if len(results) == 0:
            print("\nNo valid results generated!")
            return None
        
        return pd.DataFrame(results)


# Example usage:
if __name__ == "__main__":
    # Import the backtest class from the other script
    # Make sure the first script is saved as 'backtest.py' or adjust import
    try:
        from backtest import VolatilitySqueezeBT
    except ImportError:
        print("ERROR: Could not import VolatilitySqueezeBT.")
        print("Make sure the backtest script is saved as 'backtest.py'")
        print("Or copy the VolatilitySqueezeBT class into this file")
        sys.exit(1)
    
    # Load and align data
    df_hourly, df_daily = WalkForwardTester.load_and_align_data(
        'btcusd_1h.csv',
        'btcusd_1d.csv'
    )
    
    # Create walk-forward tester
    wft = WalkForwardTester(
        df_hourly, 
        df_daily, 
        train_months=12,  # 12 months training
        test_months=3     # 3 months testing
    )
    
    # Run walk-forward analysis
    wf_results = wft.run_walk_forward(
        bt_class=VolatilitySqueezeBT,
        optimize=True,
        param_grid={
            'base_risk': [0.01, 0.025, 0.05],
            'max_positions': [1, 2]
        }
    )
    
    if wf_results is not None and len(wf_results) > 0:
        # Display results
        print("\n" + "="*80)
        print("WALK-FORWARD RESULTS")
        print("="*80)
        print(wf_results[['window', 'base_risk', 'max_positions', 'test_return', 'test_drawdown', 'test_trades', 'test_winrate']].to_string())
        
        # Summary statistics
        print("\n" + "="*80)
        print("SUMMARY STATISTICS")
        print("="*80)
        print(f"Number of Windows: {len(wf_results)}")
        print(f"Average Test Return: {wf_results['test_return'].mean():.2f}%")
        print(f"Median Test Return: {wf_results['test_return'].median():.2f}%")
        print(f"Std Dev of Returns: {wf_results['test_return'].std():.2f}%")
        print(f"Best Window Return: {wf_results['test_return'].max():.2f}%")
        print(f"Worst Window Return: {wf_results['test_return'].min():.2f}%")
        print(f"Average Max Drawdown: {wf_results['test_drawdown'].mean():.2f}%")
        print(f"Worst Drawdown: {wf_results['test_drawdown'].min():.2f}%")
        print(f"Average Win Rate: {wf_results['test_winrate'].mean():.2f}%")
        print(f"Total Trades: {wf_results['test_trades'].sum()}")
        print(f"Positive Windows: {(wf_results['test_return'] > 0).sum()}/{len(wf_results)}")
        print("="*80)
        
        # Calculate compound return across all windows
        cumulative_returns = (1 + wf_results['test_return'] / 100).prod() - 1
        print(f"\nCompound Return Across All Windows: {cumulative_returns * 100:.2f}%")
        
        # Plot results
        import matplotlib.pyplot as plt
        
        fig, axes = plt.subplots(3, 1, figsize=(14, 10))
        
        # Returns by window
        colors = ['green' if x > 0 else 'red' for x in wf_results['test_return']]
        axes[0].bar(wf_results['window'], wf_results['test_return'], color=colors, alpha=0.7)
        axes[0].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        axes[0].axhline(y=wf_results['test_return'].mean(), color='blue', linestyle='--', 
                       label=f"Mean: {wf_results['test_return'].mean():.2f}%")
        axes[0].set_title('Returns by Walk-Forward Window', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Window')
        axes[0].set_ylabel('Return (%)')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Drawdown by window
        axes[1].bar(wf_results['window'], wf_results['test_drawdown'], color='red', alpha=0.7)
        axes[1].axhline(y=wf_results['test_drawdown'].mean(), color='darkred', linestyle='--',
                       label=f"Mean: {wf_results['test_drawdown'].mean():.2f}%")
        axes[1].set_title('Max Drawdown by Walk-Forward Window', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Window')
        axes[1].set_ylabel('Drawdown (%)')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        # Cumulative returns
        wf_results['cumulative_return'] = (1 + wf_results['test_return'] / 100).cumprod()
        axes[2].plot(wf_results['window'], wf_results['cumulative_return'], 
                    marker='o', linewidth=2, markersize=6)
        axes[2].axhline(y=1, color='black', linestyle='--', alpha=0.5)
        axes[2].fill_between(wf_results['window'], wf_results['cumulative_return'], 1, alpha=0.3)
        axes[2].set_title('Cumulative Returns Across Windows', fontsize=14, fontweight='bold')
        axes[2].set_xlabel('Window')
        axes[2].set_ylabel('Cumulative Return (1 = Break Even)')
        axes[2].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo results to display!")