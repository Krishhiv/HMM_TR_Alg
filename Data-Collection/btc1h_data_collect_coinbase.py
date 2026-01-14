import math
import time
import pathlib
import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

# ----------------------------
# Config
# ----------------------------
BASE      = "https://api.exchange.coinbase.com"
PRODUCT   = "BTC-USD"
GRAN_S    = 3600                   # 1 hour
USER_AGENT = "btc-1h-downloader/1.0"

DATA_DIR      = pathlib.Path("data_coinbase_btc")
MONTH_DIR_1H  = DATA_DIR / "1h_months"
DATA_DIR.mkdir(parents=True, exist_ok=True)
MONTH_DIR_1H.mkdir(parents=True, exist_ok=True)


# ----------------------------
# HTTP helpers
# ----------------------------
def _make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def _get_with_retries(session: requests.Session, url: str, params: dict,
                      timeout=30, max_retries=6, base_sleep=1.5):
    """GET with simple retry/backoff on 429/5xx/errors."""
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


def _fetch_candles(session: requests.Session,
                   product: str,
                   start_dt: datetime,
                   end_dt: datetime,
                   granularity_s: int,
                   timeout=30) -> pd.DataFrame:
    """
    One request to Coinbase /candles endpoint.
    Returns ascending DataFrame with columns: time, low, high, open, close, volume.
    NOTE: Max 300 candles per call; keep (end - start) <= granularity_s * 300.
    """
    url = f"{BASE}/products/{product}/candles"
    params = {
        "start": start_dt.replace(tzinfo=timezone.utc).isoformat(),
        "end":   end_dt.replace(tzinfo=timezone.utc).isoformat(),
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


# ----------------------------
# Pagination over a date range
# ----------------------------
def _download_range(session: requests.Session,
                    product: str,
                    start: datetime,
                    end: datetime,
                    granularity_s: int,
                    calls_per_sec: float = 2.0,
                    progress_prefix: str = "") -> pd.DataFrame:
    """
    Paginates [start, end] into windows of <=300 candles (Coinbase limit).
    Returns UTC-indexed OHLCV DataFrame: Open, High, Low, Close, Volume.
    """
    max_span = granularity_s * 300
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
        if progress_prefix:
            print(f"{progress_prefix} [{done}/{est_calls}] {cursor.date()} → {window_end.date()}  rows:{len(df)}")
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


# ----------------------------
# Month iteration & probing
# ----------------------------
def _month_bounds_iter(start_dt: datetime, end_dt: datetime):
    """Yield (month_start, month_end) pairs across [start_dt, end_dt] in UTC."""
    # Start at the 1st of the start month to keep clean month files,
    # but we'll clamp the first fetch to start_dt later.
    cur = datetime(start_dt.year, start_dt.month, 1, tzinfo=timezone.utc)
    end_m = datetime(end_dt.year, end_dt.month, 1, tzinfo=timezone.utc)
    while cur <= end_m:
        next_m = (cur.replace(day=28) + timedelta(days=4)).replace(day=1)
        month_end = min(end_dt, next_m - timedelta(seconds=1))
        yield cur, month_end
        cur = next_m


def _month_has_data(session: requests.Session,
                    product: str,
                    m_start: datetime,
                    m_end: datetime,
                    granularity_s: int,
                    calls_per_sec: float = 2.0) -> bool:
    """
    Probe a month using up to 3 safe 24h windows (start, mid, end).
    Returns True iff any probe returns non-empty.
    """
    sleep_s = 1.0 / calls_per_sec if calls_per_sec > 0 else 0.0
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
        if sleep_s:
            time.sleep(sleep_s)
    return False


def find_first_data_month(session: requests.Session,
                          product: str,
                          start_dt: datetime,
                          end_dt: datetime,
                          granularity_s: int,
                          calls_per_sec: float = 2.0):
    for m_start, m_end in _month_bounds_iter(start_dt, end_dt):
        if _month_has_data(session, product, m_start, m_end, granularity_s, calls_per_sec=calls_per_sec):
            return m_start
    return None


# ----------------------------
# Public functions
# ----------------------------
def _parse_iso_utc(s: str) -> datetime:
    """Parse an ISO string to a timezone-aware UTC datetime."""
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = dt.astimezone(timezone.utc)
    return dt


def download_btc_usd_1h_monthly(start="2015-08-09T00:00:00+00:00",
                                end=None,
                                calls_per_sec: float = 2.0,
                                resume: bool = True):
    """
    Download BTC-USD 1h candles month-by-month (resumable).
    The very first month is clamped to start at `start` exactly.
    """
    if end is None:
        end = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
    start_dt = _parse_iso_utc(start)
    end_dt   = _parse_iso_utc(end)
    session  = _make_session()

    # 1) Discover first month that has any data in [start_dt, end_dt]
    first_m = find_first_data_month(session, PRODUCT, start_dt, end_dt, GRAN_S, calls_per_sec=calls_per_sec)
    if first_m is None:
        print("No 1h data found in the requested range.")
        return

    # 2) Download from first_m to end_dt (clamp first month to start_dt)
    cur = first_m
    while cur <= end_dt:
        next_m = (cur.replace(day=28) + timedelta(days=4)).replace(day=1)
        m_end = min(end_dt, next_m - timedelta(seconds=1))

        # Clamp the first month's start to the requested start_dt
        m_start_effective = max(cur, start_dt)

        out_path = MONTH_DIR_1H / f"{PRODUCT}_1h_{cur.strftime('%Y-%m')}.csv"
        if resume and out_path.exists():
            print(f"[resume] Skip {out_path.name}")
            cur = next_m
            continue

        df_m = _download_range(session, PRODUCT, m_start_effective, m_end, GRAN_S,
                               calls_per_sec=calls_per_sec,
                               progress_prefix=f"1h {cur.strftime('%Y-%m')}")
        df_m.to_csv(out_path, float_format="%.8f")
        time.sleep(0.2)  # tiny pause between months
        cur = next_m


def merge_1h_months(out_csv=DATA_DIR / "btc_usd_1h_merged.csv") -> pd.DataFrame:
    files = sorted(MONTH_DIR_1H.glob(f"{PRODUCT}_1h_*.csv"))
    if not files:
        print("No monthly files to merge yet.")
        return pd.DataFrame(columns=["Open", "High", "Low", "Close", "Volume"])
    dfs = [pd.read_csv(p, parse_dates=["time"], index_col="time") for p in files]
    df = pd.concat(dfs).sort_index()
    df = df[~df.index.duplicated(keep="last")]
    df.to_csv(out_csv, float_format="%.8f")
    return df


# ----------------------------
# CLI
# ----------------------------
if __name__ == "__main__":
    START = "2015-08-09T00:00:00+00:00"  # exact UTC start
    END   = None  # to "now" UTC

    print("Downloading BTC-USD 1h (month-by-month, resumable) ...")
    download_btc_usd_1h_monthly(start=START, end=END, calls_per_sec=2.0, resume=True)

    print("\nMerging monthly files ...")
    df_1h = merge_1h_months()
    if not df_1h.empty:
        print("Merged 1h:", df_1h.shape, "| range:", df_1h.index.min(), "→", df_1h.index.max())
    else:
        print("Merged 1h: (no data)")
