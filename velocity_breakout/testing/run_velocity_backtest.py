import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from velocity_breakout.feature_eng.feature_engineering import (  # noqa: E402
    merge_1h_ema_to_15m,
    merge_daily_regime,
)


def _default_config() -> dict:
    return {
        "volume_mult": 1.8,
        "roc_threshold": 0.5,
        "clv_threshold": 0.4,
        "atr_vol_mult": 1.5,
        "stop_atr_mult": 2.0,
        "target1_atr_mult": 1.5,
        "target2_atr_mult": 3.0,
        "trail_atr_mult": 1.2,
        "donchian_lookback": 20,
        "overext_long": 0.002,
        "overext_short": 0.002,
        "catastrophic_atr_mult": 4.0,
    }


def _load_features(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    cols = {c: c.strip().lower() for c in df.columns}
    df = df.rename(columns=cols)
    if "date" in df.columns and "timestamp" not in df.columns:
        df = df.rename(columns={"date": "timestamp"})
    if "timestamp" not in df.columns:
        raise ValueError(f"Missing timestamp column in {path}")
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    df = df.sort_values("timestamp").reset_index(drop=True)
    return df


def _add_breakout_levels(df: pd.DataFrame, lookback: int) -> pd.DataFrame:
    out = df.copy()
    out["high_20_prev"] = out["high"].rolling(lookback).max().shift(1)
    out["low_20_prev"] = out["low"].rolling(lookback).min().shift(1)
    if "open_next" not in out.columns:
        out["open_next"] = out["open"].shift(-1)
    return out


def _load_tr3_trade_log(
    daily_csv: Path,
    hourly_csv: Path,
    train_end: str,
    val_end: str,
    min_dwell: int,
) -> pd.DataFrame:
    from walkforward import run_holdout_ect as ect

    df = pd.read_csv(daily_csv)
    if "Date" not in df.columns:
        raise ValueError("Expected a 'Date' column in daily CSV.")
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.set_index("Date").sort_index()

    need = [
        "Open", "High", "Low", "Close", "Volume", "Log_Returns",
        "GKVol_20", "VolZ_20", "EMA_20", "EMA_20_slope",
    ]
    missing = [c for c in need if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in daily CSV: {missing}")

    df = ect.build_compact_features(df)

    train_mask = df.index <= pd.Timestamp(train_end, tz="UTC")
    val_mask = (df.index > pd.Timestamp(train_end, tz="UTC")) & (df.index <= pd.Timestamp(val_end, tz="UTC"))
    test_mask = df.index > pd.Timestamp(val_end, tz="UTC")

    df_tr, df_va, df_te = df.loc[train_mask], df.loc[val_mask], df.loc[test_mask]
    if df_tr.empty or df_va.empty or df_te.empty:
        raise ValueError("One of Train/Val/Test is empty; adjust train-end or val-end.")

    X_tr, X_va, X_te = df_tr[ect.FEATURES].values, df_va[ect.FEATURES].values, df_te[ect.FEATURES].values
    scaler = ect.StandardScaler().fit(X_tr)
    Xs_tr, Xs_va, Xs_te = scaler.transform(X_tr), scaler.transform(X_va), scaler.transform(X_te)

    len_tr = ect.lengths_by_year(df_tr.index)
    len_trv = ect.lengths_by_year(pd.concat([df_tr, df_va]).index)

    ect.pick_best_model(Xs_tr, len_tr, k=3)
    Xs_trv = np.vstack([Xs_tr, Xs_va])
    final = ect.fit_hmm(Xs_trv, len_trv, k=3, seed=101)

    st_trv, g_trv = ect.decode(final, Xs_trv)
    st_te, g_te = ect.decode(final, Xs_te)

    if min_dwell and min_dwell > 1:
        st_trv = ect.enforce_min_dwell_gamma(st_trv, g_trv, min_run=min_dwell)
        st_te = ect.enforce_min_dwell_gamma(st_te, g_te, min_run=min_dwell)

    last_trv_state = st_trv[-1]
    last_trv_day = pd.concat([df_tr, df_va]).index[-1]
    st_series = pd.Series(st_te, index=df_te.index)
    st_series = pd.concat([pd.Series([last_trv_state], index=[last_trv_day]), st_series])
    lag_states = st_series.shift(1)

    h = pd.read_csv(hourly_csv)
    if "Date" not in h.columns:
        raise ValueError("Hourly CSV must have a 'Date' column.")
    h["Date"] = pd.to_datetime(h["Date"], utc=True, errors="coerce")
    h = h.dropna(subset=["Date"]).sort_values("Date")
    h = h.set_index("Date")
    h_test = h.loc[(h.index > pd.Timestamp(val_end, tz="UTC"))].copy()
    if h_test.empty:
        raise ValueError("No hourly data in test window.")

    day_idx = h_test.index.normalize()
    h_test["D1_State_lag1d"] = day_idx.map(lag_states.to_dict())
    h_test = h_test.dropna(subset=["D1_State_lag1d"]).copy()
    date_col = h_test.index.tz_convert("UTC").tz_localize(None)
    h_test = h_test.reset_index(drop=True)
    h_test.insert(0, "Date", pd.to_datetime(date_col))

    tr_df = ect.load_data_df(h_test)
    trade_log, _ = ect.simulate_tr3(tr_df)
    return trade_log


def _compute_hmm_lag_states(
    daily_csv: Path,
    train_end: str,
    val_end: str,
    min_dwell: int,
) -> pd.Series:
    from walkforward import run_holdout_ect as ect

    df = pd.read_csv(daily_csv)
    if "Date" not in df.columns:
        raise ValueError("Expected a 'Date' column in daily CSV.")
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.set_index("Date").sort_index()

    need = [
        "Open", "High", "Low", "Close", "Volume", "Log_Returns",
        "GKVol_20", "VolZ_20", "EMA_20", "EMA_20_slope",
    ]
    missing = [c for c in need if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in daily CSV: {missing}")

    df = ect.build_compact_features(df)

    train_mask = df.index <= pd.Timestamp(train_end, tz="UTC")
    val_mask = (df.index > pd.Timestamp(train_end, tz="UTC")) & (df.index <= pd.Timestamp(val_end, tz="UTC"))
    test_mask = df.index > pd.Timestamp(val_end, tz="UTC")

    df_tr, df_va, df_te = df.loc[train_mask], df.loc[val_mask], df.loc[test_mask]
    if df_tr.empty or df_va.empty or df_te.empty:
        raise ValueError("One of Train/Val/Test is empty; adjust train-end or val-end.")

    X_tr, X_va, X_te = df_tr[ect.FEATURES].values, df_va[ect.FEATURES].values, df_te[ect.FEATURES].values
    scaler = ect.StandardScaler().fit(X_tr)
    Xs_tr, Xs_va, Xs_te = scaler.transform(X_tr), scaler.transform(X_va), scaler.transform(X_te)

    len_tr = ect.lengths_by_year(df_tr.index)
    len_trv = ect.lengths_by_year(pd.concat([df_tr, df_va]).index)

    ect.pick_best_model(Xs_tr, len_tr, k=3)
    Xs_trv = np.vstack([Xs_tr, Xs_va])
    final = ect.fit_hmm(Xs_trv, len_trv, k=3, seed=101)

    st_trv, g_trv = ect.decode(final, Xs_trv)
    st_te, g_te = ect.decode(final, Xs_te)

    if min_dwell and min_dwell > 1:
        st_trv = ect.enforce_min_dwell_gamma(st_trv, g_trv, min_run=min_dwell)
        st_te = ect.enforce_min_dwell_gamma(st_te, g_te, min_run=min_dwell)

    last_trv_state = st_trv[-1]
    last_trv_day = pd.concat([df_tr, df_va]).index[-1]
    st_series = pd.Series(st_te, index=df_te.index)
    st_series = pd.concat([pd.Series([last_trv_state], index=[last_trv_day]), st_series])
    return st_series.shift(1)


def _build_tr3_intervals(trade_log: pd.DataFrame) -> list[tuple[pd.Timestamp, pd.Timestamp]]:
    intervals = []
    for _, row in trade_log.iterrows():
        entry = pd.to_datetime(row["entry_time"], utc=True)
        exit_ = pd.to_datetime(row["exit_time"], utc=True)
        if pd.isna(entry) or pd.isna(exit_):
            continue
        intervals.append((entry, exit_))
    intervals.sort(key=lambda x: x[0])
    return intervals


def _tr3_active_at(ts: pd.Timestamp, intervals: list[tuple[pd.Timestamp, pd.Timestamp]], idx: int) -> tuple[bool, int]:
    n = len(intervals)
    while idx < n and ts >= intervals[idx][1]:
        idx += 1
    if idx < n and intervals[idx][0] <= ts < intervals[idx][1]:
        return True, idx
    return False, idx


def _position_size(
    equity: float,
    price: float,
    atr_14: float,
    tr3_active: bool,
    tr3_reduce: float,
    max_position_pct: float,
    stop_atr_mult: float,
) -> float:
    risk_per_trade = 0.008
    stop_distance = stop_atr_mult * atr_14
    if stop_distance <= 0:
        return 0.0
    dollar_risk = equity * risk_per_trade
    size_btc = dollar_risk / stop_distance
    position_value = size_btc * price
    position_value = min(position_value, equity * max_position_pct)
    size_btc = position_value / price
    if tr3_active:
        size_btc *= tr3_reduce
    return size_btc


def _long_entry_ok(row: pd.Series, use_1h_ema: bool, use_regime: bool, cfg: dict) -> bool:
    if row["ema_50"] <= row["ema_100"]:
        return False
    if use_1h_ema and (pd.isna(row.get("ema_50_1h")) or row["close"] <= row["ema_50_1h"]):
        return False
    if row["high"] <= row["high_20_prev"]:
        return False
    if row["volume"] <= cfg["volume_mult"] * row["volume_ma_20"]:
        return False
    if row["close"] >= row["high"] * (1 + cfg["overext_long"]):
        return False
    if row["roc_3"] <= cfg["roc_threshold"]:
        return False
    if row["clv"] <= cfg["clv_threshold"]:
        return False
    if row["atr_14"] >= cfg["atr_vol_mult"] * row["atr_50_ma"]:
        return False
    if row["hour_utc"] in {23, 0, 1}:
        return False
    if use_regime and row.get("state_lag1d") == 1:
        return False
    return True


def _short_entry_ok(row: pd.Series, use_1h_ema: bool, use_regime: bool, cfg: dict) -> bool:
    if row["ema_50"] >= row["ema_100"]:
        return False
    if use_1h_ema and (pd.isna(row.get("ema_50_1h")) or row["close"] >= row["ema_50_1h"]):
        return False
    if row["low"] >= row["low_20_prev"]:
        return False
    if row["volume"] <= cfg["volume_mult"] * row["volume_ma_20"]:
        return False
    if row["close"] <= row["low"] * (1 - cfg["overext_short"]):
        return False
    if row["roc_3"] >= -cfg["roc_threshold"]:
        return False
    if row["clv"] >= -cfg["clv_threshold"]:
        return False
    if row["atr_14"] >= cfg["atr_vol_mult"] * row["atr_50_ma"]:
        return False
    if row["hour_utc"] in {23, 0, 1}:
        return False
    if use_regime and row.get("state_lag1d") == 1:
        return False
    return True


def run_backtest(
    df: pd.DataFrame,
    mode: str,
    tr3_intervals: list[tuple[pd.Timestamp, pd.Timestamp]] | None,
    use_1h_ema: bool,
    use_regime: bool,
    block_same_direction: bool,
    cfg: dict,
    out_dir: Path,
    write_output: bool = True,
) -> pd.DataFrame:
    equity = 100000.0
    daily_trade_count = 0
    daily_pnl = 0.0
    daily_loss_limit_hit = False
    current_day = None
    day_start_equity = equity

    max_positions = 2
    max_daily_trades = 8
    max_daily_loss_pct = 0.03
    tr3_reduce = 0.6
    max_position_pct = 0.30

    positions = []
    trades = []
    tr3_idx = 0

    for i, row in df.iterrows():
        ts = row["timestamp"]
        if pd.isna(row["open_next"]):
            continue

        day = ts.normalize()
        if current_day is None or day != current_day:
            current_day = day
            daily_trade_count = 0
            daily_pnl = 0.0
            daily_loss_limit_hit = False
            day_start_equity = equity

        # Check exits first
        for pos in positions[:]:
            pos["bars_held"] += 1
            direction = pos["direction"]
            entry_price = pos["entry_price"]
            entry_atr = pos["entry_atr"]
            size = pos["size"]

            # Track high/low close for trailing
            if direction == 1:
                pos["highest_close"] = max(pos["highest_close"], row["close"])
            else:
                pos["lowest_close"] = min(pos["lowest_close"], row["close"])

            exit_price = None
            exit_reason = None
            exit_size = size

            # Stop loss (intrabar)
            stop_distance = cfg["stop_atr_mult"] * entry_atr
            if direction == 1:
                stop_price = entry_price - stop_distance
                if row["low"] <= stop_price:
                    exit_price = min(stop_price, row["open_next"])
                    exit_reason = "stop_loss"
                elif (entry_price - row["low"]) >= (cfg["catastrophic_atr_mult"] * entry_atr):
                    exit_price = row["open_next"]
                    exit_reason = "catastrophic_wick"
            else:
                stop_price = entry_price + stop_distance
                if row["high"] >= stop_price:
                    exit_price = max(stop_price, row["open_next"])
                    exit_reason = "stop_loss"
                elif (row["high"] - entry_price) >= (cfg["catastrophic_atr_mult"] * entry_atr):
                    exit_price = row["open_next"]
                    exit_reason = "catastrophic_wick"

            # Profit targets
            if exit_price is None:
                target_1 = cfg["target1_atr_mult"] * entry_atr
                target_2 = cfg["target2_atr_mult"] * entry_atr
                if direction == 1:
                    if (not pos["target_1_hit"]) and (row["close"] >= entry_price + target_1):
                        exit_price = row["open_next"]
                        exit_reason = "target_1"
                        exit_size = size * 0.5
                        pos["size"] = size - exit_size
                        pos["target_1_hit"] = True
                    elif row["close"] >= entry_price + target_2:
                        exit_price = row["open_next"]
                        exit_reason = "target_2"
                else:
                    if (not pos["target_1_hit"]) and (row["close"] <= entry_price - target_1):
                        exit_price = row["open_next"]
                        exit_reason = "target_1"
                        exit_size = size * 0.5
                        pos["size"] = size - exit_size
                        pos["target_1_hit"] = True
                    elif row["close"] <= entry_price - target_2:
                        exit_price = row["open_next"]
                        exit_reason = "target_2"

            # Trailing stop (after target 1)
            if exit_price is None and pos["target_1_hit"]:
                trail_distance = cfg["trail_atr_mult"] * entry_atr
                if direction == 1:
                    trail = pos["highest_close"] - trail_distance
                    if row["close"] < trail:
                        exit_price = row["open_next"]
                        exit_reason = "trailing_stop"
                else:
                    trail = pos["lowest_close"] + trail_distance
                    if row["close"] > trail:
                        exit_price = row["open_next"]
                        exit_reason = "trailing_stop"

            # Time stop
            if exit_price is None and pos["bars_held"] > 32:
                profit = (row["close"] - entry_price) * direction
                if profit <= 0:
                    exit_price = row["open_next"]
                    exit_reason = "time_stop"

            # Trend reversal
            if exit_price is None:
                if direction == 1 and row["ema_50"] < row["ema_100"]:
                    exit_price = row["open_next"]
                    exit_reason = "trend_reversal"
                elif direction == -1 and row["ema_50"] > row["ema_100"]:
                    exit_price = row["open_next"]
                    exit_reason = "trend_reversal"

            # Regime override
            if exit_price is None and use_regime and row.get("state_lag1d") == 1:
                exit_price = row["open_next"]
                exit_reason = "regime_override"

            if exit_price is not None:
                pnl = (exit_price - entry_price) * direction * exit_size
                equity += pnl
                daily_pnl += pnl
                trades.append(
                    {
                        "entry_time": pos["entry_time"],
                        "exit_time": ts,
                        "direction": "LONG" if direction == 1 else "SHORT",
                        "entry_price": entry_price,
                        "exit_price": exit_price,
                        "size_btc": exit_size,
                        "pnl": pnl,
                        "reason": exit_reason,
                    }
                )
                if exit_reason != "target_1":
                    positions.remove(pos)

        # Daily loss gate
        if not daily_loss_limit_hit:
            if (daily_pnl / day_start_equity) < -max_daily_loss_pct:
                daily_loss_limit_hit = True

        # Entries
        if daily_loss_limit_hit or daily_trade_count >= max_daily_trades:
            continue

        tr3_active = False
        if mode == "with_tr" and tr3_intervals is not None:
            tr3_active, tr3_idx = _tr3_active_at(ts, tr3_intervals, tr3_idx)

        if len(positions) < max_positions and _long_entry_ok(row, use_1h_ema, use_regime, cfg):
            if not (block_same_direction and tr3_active):
                size = _position_size(
                    equity,
                    row["open_next"],
                    row["atr_14"],
                    tr3_active,
                    tr3_reduce,
                    max_position_pct,
                    cfg["stop_atr_mult"],
                )
                if size > 0:
                    positions.append(
                        {
                            "direction": 1,
                            "entry_time": ts,
                            "entry_price": row["open_next"],
                            "entry_atr": row["atr_14"],
                            "size": size,
                            "target_1_hit": False,
                            "highest_close": row["close"],
                            "lowest_close": row["close"],
                            "bars_held": 0,
                        }
                    )
                    daily_trade_count += 1

        if len(positions) < max_positions and _short_entry_ok(row, use_1h_ema, use_regime, cfg):
            size = _position_size(
                equity,
                row["open_next"],
                row["atr_14"],
                tr3_active,
                tr3_reduce,
                max_position_pct,
                cfg["stop_atr_mult"],
            )
            if size > 0:
                positions.append(
                    {
                        "direction": -1,
                        "entry_time": ts,
                        "entry_price": row["open_next"],
                        "entry_atr": row["atr_14"],
                        "size": size,
                        "target_1_hit": False,
                        "highest_close": row["close"],
                        "lowest_close": row["close"],
                        "bars_held": 0,
                    }
                )
                daily_trade_count += 1

    trades_df = pd.DataFrame(trades)
    if write_output:
        out_dir.mkdir(parents=True, exist_ok=True)
        trades_df.to_csv(out_dir / "velocity_trades.csv", index=False)
    return trades_df


def _daily_pnl_from_trades(trades_df: pd.DataFrame) -> pd.Series:
    trades = trades_df.copy()
    trades["exit_time"] = pd.to_datetime(trades["exit_time"], utc=True)
    trades = trades.sort_values("exit_time")
    return trades.groupby(trades["exit_time"].dt.normalize())["pnl"].sum()


def _daily_returns_from_tr3(trade_log: pd.DataFrame) -> pd.Series:
    tr3 = trade_log.copy()
    tr3["exit_time"] = pd.to_datetime(tr3["exit_time"], utc=True)
    tr3 = tr3.dropna(subset=["exit_time", "net_ret"])
    grouped = tr3.groupby(tr3["exit_time"].dt.normalize())["net_ret"]
    daily_ret = grouped.apply(lambda s: (1 + s).prod() - 1)
    return daily_ret


def _metrics_from_equity(daily_equity: pd.Series, initial_equity: float) -> dict:
    if daily_equity.empty:
        return {
            "Trades": 0,
            "TotalReturn": float("nan"),
            "CAGR": float("nan"),
            "MaxDrawdown": float("nan"),
            "Sharpe": float("nan"),
            "Sortino": float("nan"),
            "Calmar": float("nan"),
            "WinRate": float("nan"),
        }

    annualization = 365.0
    total_return = (daily_equity.iloc[-1] / initial_equity) - 1.0
    years = max(
        (daily_equity.index[-1] - daily_equity.index[0]).total_seconds()
        / (365.25 * 24 * 3600),
        1e-9,
    )
    cagr = (daily_equity.iloc[-1] / initial_equity) ** (1 / years) - 1.0

    daily_rets = daily_equity.pct_change().dropna()
    if daily_rets.std() > 0:
        sharpe = (daily_rets.mean() / daily_rets.std()) * np.sqrt(annualization)
    else:
        sharpe = float("nan")

    downside = daily_rets[daily_rets < 0]
    if downside.std() > 0:
        sortino = (daily_rets.mean() / downside.std()) * np.sqrt(annualization)
    else:
        sortino = float("nan")

    rolling_max = daily_equity.cummax()
    drawdown = (daily_equity - rolling_max) / rolling_max
    max_dd = drawdown.min()
    calmar = cagr / abs(max_dd) if max_dd < 0 else float("nan")

    return {
        "TotalReturn": total_return,
        "CAGR": cagr,
        "MaxDrawdown": max_dd,
        "Sharpe": sharpe,
        "Sortino": sortino,
        "Calmar": calmar,
    }


def _compute_metrics(
    trades_df: pd.DataFrame,
    initial_equity: float = 100000.0,
) -> dict:
    if trades_df.empty:
        return {
            "Trades": 0,
            "TotalReturn": float("nan"),
            "CAGR": float("nan"),
            "MaxDrawdown": float("nan"),
            "Sharpe": float("nan"),
            "Sortino": float("nan"),
            "Calmar": float("nan"),
            "WinRate": float("nan"),
        }

    trades = trades_df.copy()
    trades["exit_time"] = pd.to_datetime(trades["exit_time"], utc=True)
    trades = trades.sort_values("exit_time")

    daily_pnl = _daily_pnl_from_trades(trades)
    daily_equity = (daily_pnl.cumsum() + initial_equity).asfreq("D", method="ffill")
    metrics = _metrics_from_equity(daily_equity, initial_equity)
    win_rate = (trades["pnl"] > 0).mean()

    return {
        "Trades": len(trades),
        "WinRate": win_rate,
        **metrics,
    }


def _compute_combined_metrics(
    trades_df: pd.DataFrame,
    tr3_trade_log: pd.DataFrame,
    initial_equity: float = 100000.0,
) -> dict:
    if trades_df.empty and tr3_trade_log.empty:
        return {
            "Trades": 0,
            "TotalReturn": float("nan"),
            "CAGR": float("nan"),
            "MaxDrawdown": float("nan"),
            "Sharpe": float("nan"),
            "Sortino": float("nan"),
            "Calmar": float("nan"),
            "WinRate": float("nan"),
        }

    velocity_daily_pnl = _daily_pnl_from_trades(trades_df)
    tr3_daily_ret = _daily_returns_from_tr3(tr3_trade_log)

    idx = velocity_daily_pnl.index.union(tr3_daily_ret.index)
    idx = idx.sort_values()
    equity = []
    eq = initial_equity
    for day in idx:
        ret = float(tr3_daily_ret.get(day, 0.0))
        pnl = float(velocity_daily_pnl.get(day, 0.0))
        eq = eq * (1 + ret) + pnl
        equity.append(eq)

    combined_equity = pd.Series(equity, index=idx).asfreq("D", method="ffill")
    metrics = _metrics_from_equity(combined_equity, initial_equity)
    win_rate = (trades_df["pnl"] > 0).mean() if not trades_df.empty else float("nan")

    return {
        "Trades": len(trades_df),
        "WinRate": win_rate,
        **metrics,
    }


def _config_from_args(args: argparse.Namespace) -> dict:
    cfg = _default_config()
    cfg["volume_mult"] = args.volume_mult
    cfg["roc_threshold"] = args.roc_threshold
    cfg["clv_threshold"] = args.clv_threshold
    cfg["atr_vol_mult"] = args.atr_vol_mult
    cfg["stop_atr_mult"] = args.stop_atr_mult
    cfg["target1_atr_mult"] = args.target1_atr_mult
    cfg["target2_atr_mult"] = args.target2_atr_mult
    cfg["trail_atr_mult"] = args.trail_atr_mult
    cfg["donchian_lookback"] = args.donchian_lookback
    cfg["overext_long"] = args.overext_long
    cfg["overext_short"] = args.overext_short
    cfg["catastrophic_atr_mult"] = args.catastrophic_atr_mult
    return cfg


def _prepare_breakout_cache(df: pd.DataFrame, lookbacks: list[int]) -> dict:
    cache = {}
    for lb in lookbacks:
        high_prev = df["high"].rolling(lb).max().shift(1)
        low_prev = df["low"].rolling(lb).min().shift(1)
        cache[lb] = (high_prev, low_prev)
    return cache


def _optimize_configs(
    df: pd.DataFrame,
    mode: str,
    tr3_intervals: list[tuple[pd.Timestamp, pd.Timestamp]] | None,
    use_1h_ema: bool,
    use_regime: bool,
    block_same_direction: bool,
    base_cfg: dict,
    out_dir: Path,
    max_samples: int | None,
    seed: int,
    weight_return: float,
    weight_sharpe: float,
) -> tuple[dict, dict]:
    import time

    grid = {
        "volume_mult": [1.6, 1.8, 2.0],
        "roc_threshold": [0.4, 0.6, 0.8],
        "clv_threshold": [0.35, 0.4, 0.45],
        "stop_atr_mult": [1.5, 2.0, 2.5],
        "target1_atr_mult": [1.0, 1.5, 1.8],
        "target2_atr_mult": [2.5, 3.0, 3.5],
        "trail_atr_mult": [1.0, 1.2, 1.4],
        "donchian_lookback": [15, 20, 25],
    }

    keys = list(grid.keys())
    values = [grid[k] for k in keys]
    combos = []
    for v0 in values[0]:
        for v1 in values[1]:
            for v2 in values[2]:
                for v3 in values[3]:
                    for v4 in values[4]:
                        for v5 in values[5]:
                            for v6 in values[6]:
                                for v7 in values[7]:
                                    combos.append((v0, v1, v2, v3, v4, v5, v6, v7))

    if max_samples is not None and max_samples < len(combos):
        rng = np.random.default_rng(seed)
        combos = list(rng.choice(combos, size=max_samples, replace=False))

    breakout_cache = _prepare_breakout_cache(df, grid["donchian_lookback"])

    best_cfg = base_cfg.copy()
    best_metrics = {}
    best_score = -np.inf
    start_ts = time.time()
    total = len(combos)

    for idx, combo in enumerate(combos, start=1):
        cfg = base_cfg.copy()
        for k, v in zip(keys, combo):
            cfg[k] = v

        df_work = df.copy()
        high_prev, low_prev = breakout_cache[cfg["donchian_lookback"]]
        df_work["high_20_prev"] = high_prev
        df_work["low_20_prev"] = low_prev

        trades_df = run_backtest(
            df_work,
            mode,
            tr3_intervals,
            use_1h_ema,
            use_regime,
            block_same_direction,
            cfg,
            out_dir,
            write_output=False,
        )
        metrics = _compute_metrics(trades_df)
        score = (metrics["TotalReturn"] * weight_return) + (metrics["Sharpe"] * weight_sharpe)
        if score > best_score:
            best_score = score
            best_cfg = cfg
            best_metrics = metrics
            print(
                f"[opt] {idx}/{total} new best score={best_score:.4f} "
                f"return={metrics['TotalReturn']:.2%} sharpe={metrics['Sharpe']:.2f}"
            )
        if idx % 50 == 0:
            elapsed = time.time() - start_ts
            rate = idx / elapsed if elapsed > 0 else 0.0
            eta = (total - idx) / rate if rate > 0 else float("inf")
            print(f"[opt] {idx}/{total} checked | {rate:.2f} cfg/s | ETA {eta/60:.1f} min")

    return best_cfg, best_metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="Velocity Breakout backtest runner.")
    parser.add_argument("--features-15m", default="velocity_breakout/data/feature_engineered/BTC-USD_15m_features.csv")
    parser.add_argument("--features-1h", default="velocity_breakout/data/feature_engineered/BTC-USD_1h_features.csv")
    parser.add_argument("--mode", choices=["independent", "with_tr"], default="independent")
    parser.add_argument("--use-1h-ema", action="store_true", help="Enable 1h EMA50 confirmation filter.")
    parser.add_argument(
        "--no-regime-filter",
        action="store_false",
        dest="use_regime_filter",
        help="Disable HMM state_lag1d filter (enabled by default).",
    )
    parser.add_argument("--block-same-direction", action="store_true", help="Skip longs if TR3 is active.")
    parser.add_argument(
        "--daily-csv",
        default="MAIN-DATASETS/btc_1d_main.csv",
        help="Daily CSV used to train/validate/test the HMM regime model.",
    )
    parser.add_argument("--tr3-daily-csv", default="MAIN-DATASETS/btc_1d_main.csv")
    parser.add_argument("--tr3-hourly-csv", default="TRADING-MODELS/btc_1h_features_TR.csv")
    parser.add_argument("--train-end", default="2019-12-31")
    parser.add_argument("--val-end", default="2021-12-31")
    parser.add_argument("--min-dwell", type=int, default=3)
    parser.add_argument("--out-dir", default="velocity_breakout/testing/outputs")
    parser.add_argument("--optimize", action="store_true", help="Optimize parameters on train+val window.")
    parser.add_argument("--optimize-max", type=int, default=None, help="Max parameter combos to sample.")
    parser.add_argument("--optimize-seed", type=int, default=42)
    parser.add_argument("--opt-weight-return", type=float, default=1.0)
    parser.add_argument("--opt-weight-sharpe", type=float, default=1.0)

    parser.add_argument("--volume-mult", type=float, default=1.8)
    parser.add_argument("--roc-threshold", type=float, default=0.5)
    parser.add_argument("--clv-threshold", type=float, default=0.4)
    parser.add_argument("--atr-vol-mult", type=float, default=1.5)
    parser.add_argument("--stop-atr-mult", type=float, default=2.0)
    parser.add_argument("--target1-atr-mult", type=float, default=1.5)
    parser.add_argument("--target2-atr-mult", type=float, default=3.0)
    parser.add_argument("--trail-atr-mult", type=float, default=1.2)
    parser.add_argument("--donchian-lookback", type=int, default=20)
    parser.add_argument("--overext-long", type=float, default=0.002)
    parser.add_argument("--overext-short", type=float, default=0.002)
    parser.add_argument("--catastrophic-atr-mult", type=float, default=4.0)
    args = parser.parse_args()

    val_end_ts = pd.Timestamp(args.val_end, tz="UTC")

    df_15m = _load_features(Path(args.features_15m))
    cfg = _config_from_args(args)
    df_15m = _add_breakout_levels(df_15m, cfg["donchian_lookback"])

    if args.use_1h_ema:
        df_1h = _load_features(Path(args.features_1h))
        df_15m = merge_1h_ema_to_15m(df_15m, df_1h)

    if args.use_regime_filter:
        lag_states = _compute_hmm_lag_states(
            Path(args.daily_csv),
            args.train_end,
            args.val_end,
            args.min_dwell,
        )
        df_daily = pd.DataFrame(
            {
                "timestamp": pd.to_datetime(lag_states.index, utc=True),
                "state_lag1d": lag_states.values,
            }
        ).dropna(subset=["state_lag1d"])
        df_15m = merge_daily_regime(df_15m, df_daily, regime_col="state_lag1d")

    df_trainval = df_15m[df_15m["timestamp"] <= val_end_ts].copy()
    df_test = df_15m[df_15m["timestamp"] > val_end_ts].copy()

    tr3_intervals = None
    if args.mode == "with_tr":
        trade_log = _load_tr3_trade_log(
            Path(args.tr3_daily_csv),
            Path(args.tr3_hourly_csv),
            args.train_end,
            args.val_end,
            args.min_dwell,
        )
        tr3_intervals = _build_tr3_intervals(trade_log)

    if args.optimize:
        cfg, opt_metrics = _optimize_configs(
            df_trainval,
            args.mode,
            tr3_intervals,
            args.use_1h_ema,
            args.use_regime_filter,
            args.block_same_direction,
            cfg,
            Path(args.out_dir),
            args.optimize_max,
            args.optimize_seed,
            args.opt_weight_return,
            args.opt_weight_sharpe,
        )
        df_test = _add_breakout_levels(df_test, cfg["donchian_lookback"])
        print("Best config (train+val):")
        for k in sorted(cfg.keys()):
            print(f"  {k}: {cfg[k]}")
        if opt_metrics:
            print(
                f"Train+Val Return: {opt_metrics['TotalReturn']:.2%} | "
                f"Sharpe: {opt_metrics['Sharpe']:.2f}"
            )

    trades_df = run_backtest(
        df_test,
        args.mode,
        tr3_intervals,
        args.use_1h_ema,
        args.use_regime_filter,
        args.block_same_direction,
        cfg,
        Path(args.out_dir),
    )

    print(f"Trades: {len(trades_df)}")
    if not trades_df.empty:
        if args.mode == "with_tr" and tr3_intervals is not None:
            trade_log = _load_tr3_trade_log(
                Path(args.tr3_daily_csv),
                Path(args.tr3_hourly_csv),
                args.train_end,
                args.val_end,
                args.min_dwell,
            )
            combined = _compute_combined_metrics(trades_df, trade_log, initial_equity=100000.0)
            print("Combined (Velocity + TR3) Metrics:")
            print(f"Total Return: {combined['TotalReturn']:.2%}")
            print(f"CAGR: {combined['CAGR']:.2%}")
            print(f"Max Drawdown: {combined['MaxDrawdown']:.2%}")
            print(f"Sharpe: {combined['Sharpe']:.2f}")
            print(f"Sortino: {combined['Sortino']:.2f}")
            print(f"Calmar: {combined['Calmar']:.2f}")
            print(f"Win Rate: {combined['WinRate']:.2%}")
            print(f"Trades: {combined['Trades']}")
        metrics = _compute_metrics(trades_df, initial_equity=100000.0)
        print("Velocity Metrics:")
        print(f"Total Return: {metrics['TotalReturn']:.2%}")
        print(f"CAGR: {metrics['CAGR']:.2%}")
        print(f"Max Drawdown: {metrics['MaxDrawdown']:.2%}")
        print(f"Sharpe: {metrics['Sharpe']:.2f}")
        print(f"Sortino: {metrics['Sortino']:.2f}")
        print(f"Calmar: {metrics['Calmar']:.2f}")
        print(f"Win Rate: {metrics['WinRate']:.2%}")
        print(f"Trades: {metrics['Trades']}")
        print(f"Output: {Path(args.out_dir) / 'velocity_trades.csv'}")


if __name__ == "__main__":
    main()
