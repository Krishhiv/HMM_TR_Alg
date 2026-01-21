from __future__ import annotations

import argparse
import json
import math
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
import requests


BASE = "https://api.exchange.coinbase.com"
GRAN_S = 300  # 5m
USER_AGENT = "btc-5m-downloader/1.0"

ASSETS = ["BTC-USD"]


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
            if r.status_code == 404:
                return r
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


def _product_exists(session: requests.Session, product: str) -> bool:
    url = f"{BASE}/products/{product}"
    r = _get_with_retries(session, url, params={}, timeout=15)
    if r.status_code == 404:
        return False
    try:
        r.raise_for_status()
    except Exception:
        return False
    return True


def _fetch_candles(session: requests.Session, product: str,
                   start_dt: datetime, end_dt: datetime,
                   granularity_s: int, timeout=30) -> pd.DataFrame:
    url = f"{BASE}/products/{product}/candles"
    params = {
        "start": start_dt.replace(tzinfo=timezone.utc).isoformat(),
        "end": end_dt.replace(tzinfo=timezone.utc).isoformat(),
        "granularity": granularity_s,
    }
    r = _get_with_retries(session, url, params, timeout=timeout)
    if r.status_code == 404:
        return pd.DataFrame(columns=["time", "low", "high", "open", "close", "volume"])
    data = r.json()
    if not data:
        return pd.DataFrame(columns=["time", "low", "high", "open", "close", "volume"])
    df = pd.DataFrame(data, columns=["time", "low", "high", "open", "close", "volume"])
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df = df.sort_values("time")
    return df


def _download_range(session: requests.Session, product: str,
                    start: datetime, end: datetime,
                    granularity_s: int,
                    sleep_s: float = 0.5) -> pd.DataFrame:
    max_span = granularity_s * 300
    chunks = []
    cursor = start
    total_secs = max(0, (end - start).total_seconds())
    est_calls = math.ceil(total_secs / max_span) if total_secs > 0 else 0
    done = 0
    while cursor <= end:
        window_end = min(end, cursor + timedelta(seconds=max_span - granularity_s))
        df = _fetch_candles(session, product, cursor, window_end, granularity_s)
        if not df.empty:
            chunks.append(df)
        done += 1
        print(f"[{product}] fetch {done}/{est_calls} {cursor.date()} → {window_end.date()} rows:{len(df)}")
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
    out.index.name = "Date"
    return out


def _month_bounds_iter(start_dt: datetime, end_dt: datetime):
    cur = datetime(start_dt.year, start_dt.month, 1, tzinfo=timezone.utc)
    end_m = datetime(end_dt.year, end_dt.month, 1, tzinfo=timezone.utc)
    while cur <= end_m:
        next_m = (cur.replace(day=28) + timedelta(days=4)).replace(day=1)
        month_end = min(end_dt, next_m - timedelta(seconds=1))
        yield cur, month_end
        cur = next_m


def _month_has_data(session: requests.Session, product: str,
                    m_start: datetime, m_end: datetime,
                    granularity_s: int) -> bool:
    one_day = timedelta(days=1)
    probes = [
        (m_start, min(m_end, m_start + one_day - timedelta(seconds=granularity_s))),
    ]
    mid = m_start + (m_end - m_start) / 2
    mid_start = datetime(mid.year, mid.month, mid.day, tzinfo=timezone.utc)
    probes.append((mid_start, min(m_end, mid_start + one_day - timedelta(seconds=granularity_s))))
    end_start = max(m_start, m_end - one_day + timedelta(seconds=granularity_s))
    probes.append((end_start, m_end))
    for a, b in probes:
        df = _fetch_candles(session, product, a, b, granularity_s)
        if not df.empty:
            return True
        time.sleep(0.5)
    return False


def find_first_data_month(session: requests.Session, product: str,
                          start_dt: datetime, end_dt: datetime,
                          granularity_s: int):
    for m_start, m_end in _month_bounds_iter(start_dt, end_dt):
        print(f"[{product}] probing month {m_start.strftime('%Y-%m')} ...")
        if _month_has_data(session, product, m_start, m_end, granularity_s):
            return m_start
    return None


def forward_fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    full_idx = pd.date_range(df.index.min(), df.index.max(), freq="5min", tz="UTC")
    df = df.reindex(full_idx)
    df[["Open", "High", "Low", "Close"]] = df[["Open", "High", "Low", "Close"]].ffill()
    df["Volume"] = df["Volume"].fillna(0.0)
    df.index.name = "Date"
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="EngineB/Data")
    parser.add_argument("--start", default="2015-08-09T00:00:00+00:00")
    parser.add_argument("--sleep", type=float, default=0.5)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    metadata = {}

    session = _make_session()
    start_dt = datetime.fromisoformat(args.start.replace("Z", "+00:00")).astimezone(timezone.utc)
    end_dt = datetime.now(timezone.utc)

    for product in ASSETS:
        out_csv = out_dir / f"{product}_5m.csv"
        if out_csv.exists() and not args.overwrite:
            print(f"[skip] {product} (exists)")
            df = pd.read_csv(out_csv, parse_dates=["Date"])
            metadata[product] = {"start_date": str(df["Date"].iloc[0]), "path": str(out_csv)}
            continue

        if not _product_exists(session, product):
            print(f"[missing] {product} (product not found)")
            metadata[product] = {"start_date": None, "path": str(out_csv), "error": "product_not_found"}
            continue

        first_month = find_first_data_month(session, product, start_dt, end_dt, GRAN_S)
        if first_month is None:
            print(f"[no-data] {product} (no available data)")
            metadata[product] = {"start_date": None, "path": str(out_csv), "error": "no_data"}
            continue

        df = _download_range(session, product, first_month, end_dt, GRAN_S, sleep_s=args.sleep)
        if df.empty:
            print(f"[no-data] {product} (empty after fetch)")
            metadata[product] = {"start_date": None, "path": str(out_csv), "error": "empty"}
            continue

        df = forward_fill_missing(df)
        df.reset_index().to_csv(out_csv, index=False)
        metadata[product] = {"start_date": str(df.index[0]), "path": str(out_csv)}
        print(f"[saved] {product} -> {out_csv}")

    meta_path = out_dir / "metadata.json"
    meta_path.write_text(json.dumps(metadata, indent=2))
    print(f"Saved {meta_path}")


if __name__ == "__main__":
    main()
