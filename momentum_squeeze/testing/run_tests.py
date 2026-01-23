import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import traceback

# Import the backtest class
from backtest import VolatilitySqueezeBT

def run_simple_backtest():
    """Run a simple backtest and print results"""
    print("\n" + "="*80)
    print("RUNNING SIMPLE BACKTEST")
    print("="*80)
    
    try:
        # Load and align data
        print("\n1. Loading and aligning data...")
        df_hourly, df_daily = VolatilitySqueezeBT.load_and_align_data(
            './momentum_squeeze/data/btc_1h.csv', 
            './momentum_squeeze/data/btc_1d.csv'
        )
        
        print(f"✓ Data loaded successfully")
        print(f"  Hourly records: {len(df_hourly)}")
        print(f"  Daily records: {len(df_daily)}")
        print(f"  Date range: {df_hourly.index.min().date()} to {df_hourly.index.max().date()}")
        
        # Initialize backtest
        print("\n2. Initializing backtest...")
        bt = VolatilitySqueezeBT(
            initial_capital=2000, 
            base_risk=0.025, 
            max_positions=2
        )
        print(f"✓ Backtest initialized with ${bt.initial_capital} capital")
        
        # Run backtest
        print("\n3. Running backtest (this may take a minute)...")
        results = bt.run_backtest(
            df_hourly, 
            df_daily, 
            start_date='2020-01-01'  # Start from 2020
        )
        print(f"✓ Backtest completed")
        
        # Print results
        print("\n" + "="*80)
        print("BACKTEST RESULTS")
        print("="*80)
        print(f"Initial Capital:     ${bt.initial_capital:,.2f}")
        print(f"Final Equity:        ${results['final_equity']:,.2f}")
        print(f"Total Return:        {results['total_return_pct']:.2f}%")
        print(f"Max Drawdown:        {results['max_drawdown_pct']:.2f}%")
        print(f"Number of Trades:    {results['num_trades']}")
        print(f"Win Rate:            {results['win_rate_pct']:.2f}%")
        
        if results['num_trades'] > 0:
            print(f"Average Win:         {results['avg_win_pct']:.2f}%")
            print(f"Average Loss:        {results['avg_loss_pct']:.2f}%")
        
        print("="*80)
        
        # Show sample trades
        if len(results['trades']) > 0:
            print("\n" + "="*80)
            print("SAMPLE TRADES (Last 10)")
            print("="*80)
            trades_display = results['trades'][['entry_time', 'entry_price', 'exit_time', 'exit_price', 'pnl_pct', 'exit_reason']].tail(10)
            print(trades_display.to_string())
            print("="*80)
        
        # Plot equity curve
        print("\n4. Generating charts...")
        plot_results(results)
        print("✓ Charts displayed")
        
        return results
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        return None


def plot_results(results):
    """Plot backtest results"""
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))
    
    # Equity curve
    axes[0].plot(results['equity_curve'].index, results['equity_curve']['equity'], 
                linewidth=2, color='#2E86AB')
    axes[0].fill_between(results['equity_curve'].index, 
                         results['equity_curve']['equity'], 
                         2000, alpha=0.3, color='#2E86AB')
    axes[0].axhline(y=2000, color='red', linestyle='--', alpha=0.5, 
                   label='Initial Capital', linewidth=1.5)
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
    
    # Returns distribution
    if len(results['trades']) > 0:
        returns = results['trades']['pnl_pct'].values
        axes[2].hist(returns, bins=30, edgecolor='black', alpha=0.7, color='#A23B72')
        axes[2].axvline(x=0, color='red', linestyle='--', linewidth=2, label='Break Even')
        axes[2].axvline(x=returns.mean(), color='green', linestyle='--', linewidth=2, 
                       label=f'Mean: {returns.mean():.2f}%')
        axes[2].set_title('Trade Returns Distribution', fontsize=14, fontweight='bold')
        axes[2].set_xlabel('Return (%)')
        axes[2].set_ylabel('Frequency')
        axes[2].legend()
        axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def run_walk_forward():
    """Run walk-forward analysis"""
    print("\n" + "="*80)
    print("RUNNING WALK-FORWARD ANALYSIS")
    print("="*80)
    
    try:
        from walkforward import WalkForwardTester
        
        # Load and align data
        print("\n1. Loading and aligning data...")
        df_hourly, df_daily = WalkForwardTester.load_and_align_data(
            './momentum_squeeze/data/btc_1h.csv', 
            './momentum_squeeze/data/btc_1d.csv'
        )
        
        # Create walk-forward tester
        print("\n2. Setting up walk-forward test...")
        wft = WalkForwardTester(
            df_hourly, 
            df_daily, 
            train_months=12,  # 12 months training
            test_months=3     # 3 months testing
        )
        print(f"✓ Walk-forward setup complete")
        
        # Run walk-forward analysis
        print("\n3. Running walk-forward analysis...")
        print("   (This will take several minutes...)")
        
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
            print(wf_results[['window', 'base_risk', 'max_positions', 'test_return', 
                             'test_drawdown', 'test_trades', 'test_winrate']].to_string())
            
            # Summary statistics
            print("\n" + "="*80)
            print("SUMMARY STATISTICS")
            print("="*80)
            print(f"Number of Windows:        {len(wf_results)}")
            print(f"Average Test Return:      {wf_results['test_return'].mean():.2f}%")
            print(f"Median Test Return:       {wf_results['test_return'].median():.2f}%")
            print(f"Std Dev of Returns:       {wf_results['test_return'].std():.2f}%")
            print(f"Best Window Return:       {wf_results['test_return'].max():.2f}%")
            print(f"Worst Window Return:      {wf_results['test_return'].min():.2f}%")
            print(f"Average Max Drawdown:     {wf_results['test_drawdown'].mean():.2f}%")
            print(f"Worst Drawdown:           {wf_results['test_drawdown'].min():.2f}%")
            print(f"Average Win Rate:         {wf_results['test_winrate'].mean():.2f}%")
            print(f"Total Trades:             {wf_results['test_trades'].sum()}")
            print(f"Positive Windows:         {(wf_results['test_return'] > 0).sum()}/{len(wf_results)}")
            
            # Calculate compound return
            cumulative_returns = (1 + wf_results['test_return'] / 100).prod() - 1
            print(f"Compound Return:          {cumulative_returns * 100:.2f}%")
            print("="*80)
            
            # Plot
            plot_walk_forward_results(wf_results)
            
            return wf_results
        else:
            print("\n❌ No valid walk-forward results generated")
            return None
            
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        return None


def plot_walk_forward_results(wf_results):
    """Plot walk-forward results"""
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
                marker='o', linewidth=2, markersize=6, color='#2E86AB')
    axes[2].axhline(y=1, color='black', linestyle='--', alpha=0.5)
    axes[2].fill_between(wf_results['window'], wf_results['cumulative_return'], 1, 
                        alpha=0.3, color='#2E86AB')
    axes[2].set_title('Cumulative Returns Across Windows', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Window')
    axes[2].set_ylabel('Cumulative Return (1 = Break Even)')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("\n" + "="*80)
    print("VOLATILITY SQUEEZE STRATEGY - TEST RUNNER")
    print("="*80)
    
    while True:
        print("\nSelect test to run:")
        print("1. Simple Backtest (2020-present)")
        print("2. Walk-Forward Analysis (12-month train, 3-month test)")
        print("3. Both")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            run_simple_backtest()
        elif choice == "2":
            run_walk_forward()
        elif choice == "3":
            run_simple_backtest()
            input("\nPress Enter to continue to walk-forward analysis...")
            run_walk_forward()
        elif choice == "4":
            print("\nExiting...")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1-4.")
        
        print("\n" + "="*80)