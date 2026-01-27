"""
Unified Coinbase OHLCV downloader for BTC and multi-asset data.

Supports 1D and 1H granularities with resumable monthly downloads.
"""

import math
import time
from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import Optional

import requests
import pandas as pd


BASE_URL = "https://api.exchange.coinbase.com"
USER_AGENT = "hmm-trading-system/1.0"

# Default paths
DATA_DIR = Path(__file__).parent.parent.parent / "data"
RAW_DIR = DATA_DIR / "raw"
CACHE_DIR = DATA_DIR / "cache"


def _make_session() -> requests.Session:
    """Create a session with headers."""
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def _get_with_retries(
    session: requests.Session,
    url: str,
    params: dict,
    timeout: int = 30,
    max_retries: int = 6,
    base_sleep: float = 1.5,
) -> requests.Response:
    """GET with exponential backoff on transient errors."""
    attempt = 0
    while True:
        try:
            r = session.get(url, params=params, timeout=timeout)
            if r.status_code in (429, 500, 502, 503, 504):
                raise requests.HTTPError(f"Transient HTTP {r.status_code}", response=r)
            r.raise_for_status()
            return r
        except Exception as e:
            attempt += 1
            if attempt > max_retries:
                raise
            sleep_s = min(base_sleep * (2 ** (attempt - 1)), 15.0)
            print(f"[retry] attempt {attempt}/{max_retries} after error: {e}. Sleeping {sleep_s:.1f}s ...")
            time.sleep(sleep_s)


def _fetch_candles(
    session: requests.Session,
    product: str,
    start_dt: datetime,
    end_dt: datetime,
    granularity_s: int,
    timeout: int = 30,
) -> pd.DataFrame:
    """
    Fetch candles from Coinbase for a single window.
    Max 300 candles per call.
    """
    url = f"{BASE_URL}/products/{product}/candles"
    params = {
        "start": start_dt.replace(tzinfo=timezone.utc).isoformat(),
        "end": end_dt.replace(tzinfo=timezone.utc).isoformat(),
        "granularity": granularity_s,
    }
    r = _get_with_retries(session, url, params, timeout=timeout)
    data = r.json()
    if not data:
        return pd.DataFrame(columns=["time", "low", "high", "open", "close", "volume"])
    
    df = pd.DataFrame(data, columns=["time", "low", "high", "open", "close", "volume"])
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df = df.sort_values("time")
    return df


def download_range(
    product: str,
    start: datetime,
    end: datetime,
    granularity_s: int,
    session: Optional[requests.Session] = None,
    calls_per_sec: float = 2.0,
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Download OHLCV data for a date range, paginating as needed.
    
    Args:
        product: Coinbase product ID (e.g., 'BTC-USD')
        start: Start datetime (UTC)
        end: End datetime (UTC)
        granularity_s: Candle granularity in seconds (3600=1h, 86400=1d)
        session: Optional requests session
        calls_per_sec: Rate limit
        verbose: Print progress
    
    Returns:
        DataFrame with columns: Open, High, Low, Close, Volume
        Indexed by UTC datetime
    """
    session = session or _make_session()
    max_span = granularity_s * 300  # Max 300 candles per request
    chunks = []
    cursor = start
    
    total_secs = max(0, (end - start).total_seconds())
    est_calls = math.ceil(total_secs / max_span) if total_secs > 0 else 0
    sleep_s = 1.0 / calls_per_sec if calls_per_sec > 0 else 0.0
    done = 0
    
    while cursor <= end:
        window_end = min(end, cursor + timedelta(seconds=max_span - granularity_s))
        df = _fetch_candles(session, product, cursor, window_end, granularity_s)
        if not df.empty:
            chunks.append(df)
        done += 1
        if verbose:
            print(f"[{product}] [{done}/{est_calls}] {cursor.date()} → {window_end.date()}  rows:{len(df)}")
        cursor = window_end + timedelta(seconds=granularity_s)
        if sleep_s > 0:
            time.sleep(sleep_s)
    
    if not chunks:
        return pd.DataFrame(columns=["Open", "High", "Low", "Close", "Volume"])
    
    all_df = pd.concat(chunks, ignore_index=True)
    all_df = all_df.drop_duplicates(subset=["time"]).set_index("time").sort_index()
    out = all_df.rename(columns={
        "open": "Open", "high": "High", "low": "Low", "close": "Close", "volume": "Volume"
    })[["Open", "High", "Low", "Close", "Volume"]]
    return out


def download_daily(
    product: str = "BTC-USD",
    start: str = "2015-01-01",
    end: Optional[str] = None,
    out_csv: Optional[Path] = None,
) -> pd.DataFrame:
    """Download daily OHLCV data."""
    if end is None:
        end = datetime.now(timezone.utc).date().isoformat()
    
    start_dt = datetime.fromisoformat(start).replace(tzinfo=timezone.utc)
    end_dt = datetime.fromisoformat(end).replace(tzinfo=timezone.utc)
    
    df = download_range(product, start_dt, end_dt, granularity_s=86400)
    
    if out_csv:
        out_csv.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(out_csv, float_format="%.8f")
        print(f"Saved: {out_csv}")
    
    return df


def download_hourly_monthly(
    product: str = "BTC-USD",
    start: str = "2015-08-09",
    end: Optional[str] = None,
    cache_dir: Optional[Path] = None,
    resume: bool = True,
) -> pd.DataFrame:
    """
    Download hourly data month-by-month (resumable).
    
    Args:
        product: Coinbase product ID
        start: Start date (ISO format)
        end: End date (ISO format), defaults to now
        cache_dir: Directory for monthly cache files
        resume: Skip existing monthly files
    
    Returns:
        Merged DataFrame of all months
    """
    if end is None:
        end = datetime.now(timezone.utc).isoformat()
    
    if cache_dir is None:
        cache_dir = CACHE_DIR / "1h_months"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
    if start_dt.tzinfo is None:
        start_dt = start_dt.replace(tzinfo=timezone.utc)
    
    end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
    if end_dt.tzinfo is None:
        end_dt = end_dt.replace(tzinfo=timezone.utc)
    
    session = _make_session()
    
    # Iterate months
    cur = datetime(start_dt.year, start_dt.month, 1, tzinfo=timezone.utc)
    while cur <= end_dt:
        next_m = (cur.replace(day=28) + timedelta(days=4)).replace(day=1)
        m_end = min(end_dt, next_m - timedelta(seconds=1))
        m_start = max(cur, start_dt)
        
        out_path = cache_dir / f"{product}_1h_{cur.strftime('%Y-%m')}.csv"
        if resume and out_path.exists():
            print(f"[resume] Skip {out_path.name}")
            cur = next_m
            continue
        
        df_m = download_range(product, m_start, m_end, granularity_s=3600, session=session)
        df_m.to_csv(out_path, float_format="%.8f")
        time.sleep(0.2)
        cur = next_m
    
    # Merge all months
    files = sorted(cache_dir.glob(f"{product}_1h_*.csv"))
    if not files:
        return pd.DataFrame(columns=["Open", "High", "Low", "Close", "Volume"])
    
    dfs = [pd.read_csv(p, parse_dates=["time"], index_col="time") for p in files]
    merged = pd.concat(dfs).sort_index()
    merged = merged[~merged.index.duplicated(keep="last")]
    return merged


# Multi-asset support for elite10
ELITE10_SYMBOLS = [
    "BTC-USD", "ETH-USD", "SOL-USD", "AVAX-USD", "DOT-USD",
    "LINK-USD", "AAVE-USD", "POL-USD", "LTC-USD", "NEAR-USD",
]


def download_elite10_hourly(
    start: str = "2020-01-01",
    end: Optional[str] = None,
    out_dir: Optional[Path] = None,
) -> dict[str, pd.DataFrame]:
    """Download 1H data for the curated elite10 universe."""
    if out_dir is None:
        out_dir = RAW_DIR / "elite10"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    results = {}
    for symbol in ELITE10_SYMBOLS:
        print(f"\n=== Downloading {symbol} ===")
        cache_dir = CACHE_DIR / f"1h_months_{symbol.replace('-', '_').lower()}"
        df = download_hourly_monthly(symbol, start=start, end=end, cache_dir=cache_dir)
        
        out_csv = out_dir / f"{symbol.replace('-', '_')}_1h.csv"
        df.to_csv(out_csv, float_format="%.8f")
        results[symbol] = df
        print(f"Saved: {out_csv} ({len(df)} rows)")
    
    return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Download OHLCV data from Coinbase",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m src.data.coinbase_downloader --product BTC-USD
  python -m src.data.coinbase_downloader --product ETH-USD --start 2017-06-01
  python -m src.data.coinbase_downloader --product SOL-USD --no-resume
  python -m src.data.coinbase_downloader --elite10  # Download all 10 assets
        """,
    )
    parser.add_argument(
        "--product",
        default="BTC-USD",
        help="Coinbase product ID (e.g., BTC-USD, ETH-USD)",
    )
    parser.add_argument(
        "--start",
        default="2015-01-01",
        help="Start date (YYYY-MM-DD). ETH starts ~2017-06, SOL ~2020",
    )
    parser.add_argument(
        "--end",
        default=None,
        help="End date (YYYY-MM-DD), defaults to now",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Re-download all months (don't skip existing cache)",
    )
    parser.add_argument(
        "--elite10",
        action="store_true",
        help="Download all Elite10 assets (ignores --product)",
    )
    args = parser.parse_args()
    
    if args.elite10:
        # Download all Elite10 assets
        print("Downloading Elite10 universe...")
        download_elite10_hourly(start=args.start, end=args.end)
    else:
        # Download single product
        product = args.product
        symbol_lower = product.replace("-", "_").lower()
        
        # Daily
        print(f"\n{'='*50}")
        print(f"Downloading {product} Daily (1D)")
        print(f"{'='*50}")
        daily_csv = RAW_DIR / f"{symbol_lower}_1d_coinbase.csv"
        df_1d = download_daily(product, start=args.start, end=args.end, out_csv=daily_csv)
        print(f"1D: {len(df_1d)} rows | {df_1d.index.min()} → {df_1d.index.max()}")
        
        # Hourly
        print(f"\n{'='*50}")
        print(f"Downloading {product} Hourly (1H) - Monthly Chunks")
        print(f"{'='*50}")
        cache_dir = CACHE_DIR / f"1h_months_{symbol_lower}"
        df_1h = download_hourly_monthly(
            product,
            start=args.start,
            end=args.end,
            cache_dir=cache_dir,
            resume=not args.no_resume,
        )
        hourly_csv = RAW_DIR / f"{symbol_lower}_1h_coinbase.csv"
        df_1h.to_csv(hourly_csv, float_format="%.8f")
        print(f"\n1H: {len(df_1h)} rows | {df_1h.index.min()} → {df_1h.index.max()}")
        print(f"Saved: {hourly_csv}")
        
        # Summary
        print(f"\n{'='*50}")
        print("DOWNLOAD COMPLETE")
        print(f"{'='*50}")
        print(f"Daily:  {daily_csv}")
        print(f"Hourly: {hourly_csv}")
