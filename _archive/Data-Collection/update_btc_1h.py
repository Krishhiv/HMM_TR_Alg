#!/usr/bin/env python3
"""
Update BTC-USD 1h CSV to the latest available candles.
Reads data/coinbase_1h/BTC-USD_1h.csv and appends new rows.
"""

from __future__ import annotations

import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
import requests
import pandas as pd


BASE = "https://api.exchange.coinbase.com"
PRODUCT = "BTC-USD"
GRAN_S = 3600
USER_AGENT = "btc-1h-updater/1.0"


def _make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def _get_with_retries(session: requests.Session, url: str, params: dict,
                      timeout=30, max_retries=6, base_sleep=1.5):
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


def _fetch_candles(session: requests.Session, start_dt: datetime, end_dt: datetime) -> pd.DataFrame:
    url = f"{BASE}/products/{PRODUCT}/candles"
    params = {
        "start": start_dt.replace(tzinfo=timezone.utc).isoformat(),
        "end": end_dt.replace(tzinfo=timezone.utc).isoformat(),
        "granularity": GRAN_S,
    }
    r = _get_with_retries(session, url, params, timeout=30)
    data = r.json()
    if not data:
        return pd.DataFrame(columns=["time", "low", "high", "open", "close", "volume"])
    df = pd.DataFrame(data, columns=["time", "low", "high", "open", "close", "volume"])
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df = df.sort_values("time")
    return df


def _download_range(session: requests.Session, start: datetime, end: datetime, sleep_s: float = 0.5) -> pd.DataFrame:
    max_span = GRAN_S * 300
    chunks = []
    cursor = start
    while cursor <= end:
        window_end = min(end, cursor + timedelta(seconds=max_span - GRAN_S))
        df = _fetch_candles(session, cursor, window_end)
        if not df.empty:
            chunks.append(df)
        cursor = window_end + timedelta(seconds=GRAN_S)
        if sleep_s > 0:
            time.sleep(sleep_s)
    if not chunks:
        return pd.DataFrame(columns=["Open", "High", "Low", "Close", "Volume"])
    all_df = pd.concat(chunks, ignore_index=True)
    all_df = all_df.drop_duplicates(subset=["time"]).set_index("time").sort_index()
    out = all_df.rename(columns={
        "open": "Open", "high": "High", "low": "Low", "close": "Close", "volume": "Volume"
    })[["Open", "High", "Low", "Close", "Volume"]]
    out.index.name = "Date"
    return out


def forward_fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    full_idx = pd.date_range(df.index.min(), df.index.max(), freq="h", tz="UTC")
    df = df.reindex(full_idx)
    df[["Open", "High", "Low", "Close"]] = df[["Open", "High", "Low", "Close"]].ffill()
    df["Volume"] = df["Volume"].fillna(0.0)
    df.index.name = "Date"
    return df


def main():
    path = Path("data/coinbase_1h/BTC-USD_1h.csv")
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}")

    df = pd.read_csv(path)
    if "Date" not in df.columns:
        raise ValueError("Expected a 'Date' column in BTC-USD_1h.csv.")
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.dropna(subset=["Date"]).set_index("Date").sort_index()

    last_ts = df.index.max()
    next_ts = last_ts + pd.Timedelta(hours=1)
    end_ts = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)

    if next_ts > end_ts:
        print("BTC-USD_1h.csv is already up to date.")
        return

    session = _make_session()
    new_df = _download_range(session, next_ts.to_pydatetime(), end_ts, sleep_s=0.5)
    if new_df.empty:
        print("No new data returned.")
        return

    combined = pd.concat([df, new_df]).sort_index()
    combined = combined[~combined.index.duplicated(keep="last")]
    combined = forward_fill_missing(combined)
    combined.reset_index().to_csv(path, index=False)
    print(f"Updated {path} to {combined.index.max()}")


if __name__ == "__main__":
    main()
