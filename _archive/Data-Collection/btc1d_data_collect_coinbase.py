import os
import math
import time
import pathlib
import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

BASE = "https://api.exchange.coinbase.com"
PRODUCT = "BTC-USD"
DATA_DIR = pathlib.Path("data_coinbase_btc")
MONTH_DIR_5M = DATA_DIR / "5m_months"
DATA_DIR.mkdir(parents=True, exist_ok=True)
MONTH_DIR_5M.mkdir(parents=True, exist_ok=True)

def _sess():
    s = requests.Session()
    s.headers.update({"User-Agent": "btc-downloader/1.0"})
    return s

def _fetch_candles(session, product, start_dt, end_dt, granularity_s, timeout=30):
    url = f"{BASE}/products/{product}/candles"
    params = {
        "start": start_dt.replace(tzinfo=timezone.utc).isoformat(),
        "end":   end_dt.replace(tzinfo=timezone.utc).isoformat(),
        "granularity": granularity_s,  # 300=5m, 86400=1d
    }
    r = session.get(url, params=params, timeout=timeout)
    r.raise_for_status()
    data = r.json()  # list of [time, low, high, open, close, volume]
    if not data:
        return pd.DataFrame(columns=["time","low","high","open","close","volume"])
    df = pd.DataFrame(data, columns=["time","low","high","open","close","volume"])
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df = df.sort_values("time")
    return df

def _download_range(session, product, start, end, granularity_s, calls_per_sec=2.0, progress_prefix=""):
    # Coinbase returns max 300 candles per call
    max_span = granularity_s * 300
    chunks = []
    cursor = start

    total_secs = (end - start).total_seconds()
    est_calls = math.ceil(max(0, total_secs) / max_span)
    done = 0
    sleep_s = 1.0 / calls_per_sec if calls_per_sec > 0 else 0.0

    while cursor < end:
        window_end = min(end, cursor + timedelta(seconds=max_span - granularity_s))
        df = _fetch_candles(session, product, cursor, window_end, granularity_s)
        if not df.empty:
            chunks.append(df)
        done += 1
        if progress_prefix:
            print(f"{progress_prefix} [{done}/{est_calls}] {cursor.date()} → {window_end.date()}  rows:{len(df)}")
        cursor = window_end + timedelta(seconds=granularity_s)
        if sleep_s > 0:
            time.sleep(sleep_s)

    if not chunks:
        return pd.DataFrame(columns=["Open","High","Low","Close","Volume"])

    all_df = pd.concat(chunks, ignore_index=True)
    all_df = all_df.drop_duplicates(subset=["time"]).set_index("time").sort_index()
    out = all_df.rename(columns={
        "open":"Open","high":"High","low":"Low","close":"Close","volume":"Volume"
    })[["Open","High","Low","Close","Volume"]]
    return out

def month_iter(start_dt, end_dt):
    cur = datetime(start_dt.year, start_dt.month, 1, tzinfo=timezone.utc)
    end_m = datetime(end_dt.year, end_dt.month, 1, tzinfo=timezone.utc)
    while cur <= end_m:
        # month end = next month minus 1 second
        next_m = (cur.replace(day=28) + timedelta(days=4)).replace(day=1)
        month_end = min(end_dt, next_m - timedelta(seconds=1))
        yield cur, month_end
        cur = next_m

def get_btc_usd_1d(start="2015-01-01", end=None, calls_per_sec=2.0, session=None, out_csv=DATA_DIR/"btc_usd_1d.csv"):
    if end is None:
        end = datetime.utcnow().date().isoformat()
    start_dt = datetime.fromisoformat(start).replace(tzinfo=timezone.utc)
    end_dt   = datetime.fromisoformat(end).replace(tzinfo=timezone.utc)
    session = session or _sess()
    df = _download_range(session, PRODUCT, start_dt, end_dt, 86400, calls_per_sec, progress_prefix="1D")
    df.to_csv(out_csv, float_format="%.8f")
    return df


if __name__ == "__main__":
    # Tip: you can start with a later date to get moving quickly, then widen later.
    START = "2015-01-01"  # Coinbase BTC-USD history is solid from ~2015 onward
    END   = None          # to today (UTC)

    session = _sess()

    print("Downloading BTC-USD 1D ...")
    df_1d = get_btc_usd_1d(start=START, end=END, calls_per_sec=2.0, session=session)
    print("1D:", df_1d.shape, df_1d.index.min(), "→", df_1d.index.max())