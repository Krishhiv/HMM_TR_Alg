import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) Load + clean
df = pd.read_csv('./TRADING-MODELS/TR_Model_Log3_mc_runs.csv')

# Make sure Sharpe is numeric
sharpe = pd.to_numeric(df['Sharpe'], errors='coerce')

# Drop NaNs and non-finite values
sharpe = sharpe.replace([np.inf, -np.inf], np.nan).dropna()

# (Optional but common) remove runs with no trades if Sharpe=0 was a placeholder:
# If you have a 'Trades' column, do: sharpe = sharpe[df['Trades'] > 0]

# 2) (Optional) Winsorize to reduce extreme tails that can distort the bell curve
low, high = np.percentile(sharpe, [1, 99])   # trim at 1st/99th percentiles
sharpe_w = sharpe.clip(lower=low, upper=high)

# 3) Summary stats
mu = sharpe_w.mean()
sigma = sharpe_w.std(ddof=1)
p5, p50, p95 = np.percentile(sharpe_w, [5, 50, 95])

print(f"n={len(sharpe_w)}  mean={mu:.3f}  std={sigma:.3f}  "
      f"P5={p5:.3f}  median={p50:.3f}  P95={p95:.3f}")

# 4) Pick a sensible bin count (Freedman–Diaconis rule) for a smoother histogram
def fd_bins(x):
    x = np.asarray(x)
    iqr = np.subtract(*np.percentile(x, [75, 25]))
    if iqr == 0:
        return 30
    bin_width = 2 * iqr * (len(x) ** (-1/3))
    if bin_width <= 0:
        return 30
    return max(10, int(np.ceil((x.max() - x.min()) / bin_width)))

bins = fd_bins(sharpe_w)

# 5) Plot histogram (density) + fitted normal PDF
fig = plt.figure(figsize=(10, 6))
# Histogram as density
counts, bin_edges, _ = plt.hist(sharpe_w, bins=bins, density=True, alpha=0.6)

# Normal PDF using fitted mean/std
x = np.linspace(sharpe_w.min(), sharpe_w.max(), 400)
pdf = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-0.5*((x - mu)/sigma)**2)
plt.plot(x, pdf, linewidth=2, label='Fitted Normal PDF')

plt.title('Distribution of Sharpe over Monte Carlo Runs')
plt.xlabel('Sharpe')
plt.ylabel('Density')
plt.grid(True)
plt.legend()
plt.show()

# 6) (Optional) Quick normality sanity check: Q–Q plot
import scipy.stats as st  # if not available, skip this block
fig = plt.figure(figsize=(6, 6))
st.probplot(sharpe_w, dist="norm", sparams=(mu, sigma), plot=plt)
plt.title('Q–Q Plot for Sharpe')
plt.grid(True)
plt.show()
