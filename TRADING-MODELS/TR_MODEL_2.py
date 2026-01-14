import pandas as pd
import numpy as np
from math import sqrt

# === USER SETTINGS ===
CSV_PATH = "./TRADING-MODELS/btc_1h_features_PRIME.csv"  # change if needed
FEE_BPS_PER_SIDE = 0.0                             # e.g., 5 = 0.05% per side
START_CAPITAL = 1.0

# === TR³ (Thrust–Retention–Ride) parameters ===
TR3 = {
    "regime_col": "D1_State_lag1d",
    "allowed_regime": 1,

    # --- ENTRY (unchanged) ---
    "donchian_period": 20,
    "adx_min": 14,
    "r2_min": 0.10,
    "clv_min": 0.55,
    "thrust_atr_mult": 0.50,

    # Trend structure
    "ema_fast": 50,
    "ema_slow": 200,

    # --- EXITS (original defaults kept + new knobs) ---
    "clv_fail_max": 0.35,
    "fail_level_atr": 0.25,
    "trail_atr_n": 14,
    "trail_atr_mult": 2.5,
    "no_progress_hours": 12,
    "no_progress_atr": 0.50,
    "time_stop_hours": 24 * 7,

    # NEW: disable fail-to-hold exits after this advance (in ATRs) to let winners run
    "fth_disable_after_atr": 0.5,   # e.g., after +0.5×ATR from entry, ignore CLV/fail_level exits

    # NEW: breakeven activation once price advances this much (in ATRs)
    "be_activate_atr": 0.75,   # was 0.5  → arm a bit later
    "be_cushion_atr": -0.02,    # was 0.05 → scratch closer to zero
    "be_disable_after_atr": 1.0,   # NEW: turn BE off after +1×ATR
    "be_one_bar_delay": True,      # set BE slightly below entry by 0.05×ATR to avoid micro whips

    # NEW: ratcheting trail — widen trail as the trade gets more in-the-money
    "trail_mult_base": 2.5,         # up to +1×ATR
    "trail_mult_1": 3.5,            # between +1×ATR and +2×ATR
    "trail_mult_2": 4.5,            # beyond +2×ATR

    # NEW: soften EMA break if well in profit (avoid premature exits)
    "ema_break_relax_after_atr": 1.0,  # relax after +1×ATR
    "ema_break_cushion_atr": 0.25      # require Close < EMA50 - 0.25×ATR to trigger
}

def ema(series, span):
    return series.ewm(span=span, adjust=False).mean()

def calc_atr(df, n=14):
    hl = df["High"] - df["Low"]
    hc = (df["High"] - df["Close"].shift(1)).abs()
    lc = (df["Low"]  - df["Close"].shift(1)).abs()
    tr = pd.concat([hl, hc, lc], axis=1).max(axis=1)
    return tr.rolling(n, min_periods=n).mean()

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    required = [
        "Open","High","Low","Close",
        "MOM_donchian20_up","MOM_ema50",
        "ADX14","R2_ema50","MR_rsi14",
        TR3["regime_col"]
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")

    # Helpers if absent
    if "EMA200" not in df.columns:
        df["EMA200"] = ema(df["Close"], TR3["ema_slow"])
    if "ATR14" not in df.columns:
        df["ATR14"] = calc_atr(df, TR3["trail_atr_n"])

    # CLV (Close Location Value)
    rng = (df["High"] - df["Low"]).replace(0, np.nan)
    df["CLV"] = ((df["Close"] - df["Low"]) / rng).fillna(0.5)

    # === (1) Build a sanitized open-to-open return series ===
    df["ret_oo_raw"] = df["Open"].pct_change()

    bad_price = (
        (df["Open"] <= 0) | (df["High"] <= 0) | (df["Low"] <= 0) | (df["Close"] <= 0) |
        (df["High"] < df["Low"])
    )
    # generous spike cap for BTC 1h; adjust if needed
    spike = df["ret_oo_raw"].abs() > 0.40

    df["valid_bar"] = (~bad_price) & (~spike)
    df["ret_oo"] = 0.0
    ok = df["valid_bar"] & (~df["ret_oo_raw"].isna())
    df.loc[ok, "ret_oo"] = df.loc[ok, "ret_oo_raw"]
    df["ret_oo"] = df["ret_oo"].fillna(0.0)

    # Clean regime ints
    df[TR3["regime_col"]] = df[TR3["regime_col"]].ffill().fillna(1).astype(int)
    return df

def print_return_spikes(df, ret_col="ret_oo", cap=0.40, top=10):
    if ret_col not in df.columns:
        return
    s = df[ret_col].copy()
    spikes = s[s.abs() > cap]
    if spikes.empty:
        print(f"No {ret_col} spikes > {cap:.0%}.")
        return
    print(f"Top {min(top, len(spikes))} {ret_col} spikes (>|{cap:.0%}|):")
    show = spikes.abs().sort_values(ascending=False).head(top).index
    print(df.loc[show, ["Date","Open","High","Low","Close",ret_col]].to_string(index=False))

def simulate_tr3(df: pd.DataFrame):
    """TR³: enter at t open using t-1 signals; long-only; State 1 only; junk-bar safe."""
    R = TR3
    regcol = R["regime_col"]

    # ENTRY at t open (evaluate conditions on t-1)
    thrust = (df["Close"] - df["Close"].shift(1)) >= (R["thrust_atr_mult"] * df["ATR14"])
    breakout = df["Close"] > df["MOM_donchian20_up"]

    cond_now = (
        df["valid_bar"] &
        (df[regcol] == R["allowed_regime"]) &
        (df["MOM_ema50"] > df["EMA200"]) &
        (df["Close"] > df["MOM_ema50"]) &
        ((breakout) | (thrust)) &
        (df["CLV"] >= R["clv_min"]) &
        (df["ADX14"] >= R["adx_min"]) &
        (df["R2_ema50"] >= R["r2_min"])
    )
    entry_sig = cond_now.shift(1).fillna(False).astype(bool)

    in_pos = False
    trades = []
    pos = np.zeros(len(df), dtype=float)
    fee = FEE_BPS_PER_SIDE / 10000.0

    # optional exposure scaler / guardrail
    LEVERAGE = 1.0
    MAX_LOSS_CAP = 0.08

    entry_price = None
    entry_time = None
    entry_bar_high = None
    high_since_entry = None
    entry_reg = None

    # breakeven arming timestamp (per-trade memory)
    be_armed_since = None

    cols = [
        "entry_time","entry_price","exit_time","exit_price",
        "gross_ret","net_ret","holding_hours","regime","strategy","exit_reason"
    ]

    for i in range(1, len(df)):
        if not in_pos:
            if entry_sig.iat[i]:
                in_pos = True
                j = i - 1  # signal bar
                entry_time = df["Date"].iat[i]
                entry_price = df["Open"].iat[i]
                entry_bar_high = df["High"].iat[j]
                high_since_entry = df["High"].iat[j]
                entry_reg = int(df[regcol].iat[j])
                be_armed_since = None  # reset BE state on new trade
        else:
            j = i - 1  # evaluate exits on t-1

            # If t-1 is an invalid bar, skip making decisions on it
            if not bool(df["valid_bar"].iat[j]):
                pos[i] = 1.0
                continue

            # --- update running stats ---
            hh = df["High"].iat[j]
            if pd.notna(hh):
                high_since_entry = max(high_since_entry, hh)

            close_j = df["Close"].iat[j]
            ema50_j = df["MOM_ema50"].iat[j]
            atr_j = df["ATR14"].iat[j] if pd.notna(df["ATR14"].iat[j]) else None
            clv_j = df["CLV"].iat[j]

            # progress in ATR terms since entry
            advance_atr = ((high_since_entry - entry_price) / atr_j) if (atr_j is not None and atr_j > 0) else 0.0

            exit_now, reason = False, "rule"

            # -------- Disable fail-to-hold once trade has proven itself --------
            use_fth = not (advance_atr >= R.get("fth_disable_after_atr", np.inf))

            # -------- Breakeven logic (arming, delay, disable after strong progress) --------
            # Arm BE once we have some advance and before the disable threshold
            can_arm_be = (atr_j is not None) and (advance_atr >= R.get("be_activate_atr", np.inf)) \
                         and (advance_atr < R.get("be_disable_after_atr", np.inf))
            if (be_armed_since is None) and can_arm_be:
                be_armed_since = df["Date"].iat[j]

            # If we've advanced enough, disable BE entirely
            if advance_atr >= R.get("be_disable_after_atr", np.inf):
                be_armed_since = None

            # Active this bar?
            if be_armed_since is not None:
                if R.get("be_one_bar_delay", True):
                    be_active = (df["Date"].iat[j] - be_armed_since) >= pd.Timedelta(hours=1)
                else:
                    be_active = True
            else:
                be_active = False

            be_level = None
            if be_active and (atr_j is not None):
                be_level = entry_price - R.get("be_cushion_atr", 0.0) * atr_j  # small cushion under entry

            # -------- Ratcheting ATR trail --------
            if atr_j is not None:
                if advance_atr >= 2.0:
                    trail_mult = R.get("trail_mult_2", R.get("trail_atr_mult", 2.5))
                elif advance_atr >= 1.0:
                    trail_mult = R.get("trail_mult_1", R.get("trail_atr_mult", 2.5))
                else:
                    trail_mult = R.get("trail_mult_base", R.get("trail_atr_mult", 2.5))
                trail = high_since_entry - trail_mult * atr_j
            else:
                trail = None

            # -------- Order of exits --------
            # (i) Early fail-to-hold (only before we have enough advance)
            if use_fth:
                if clv_j <= R["clv_fail_max"]:
                    exit_now, reason = True, "fth_clv"
                elif (atr_j is not None) and (close_j < (entry_bar_high - R["fail_level_atr"] * atr_j)):
                    exit_now, reason = True, "fth_level"

            # (ii) Breakeven (after advance, protect capital)
            if (not exit_now) and (be_level is not None) and (close_j < be_level):
                exit_now, reason = True, "breakeven"

            # (iii) Chandelier trail (ratcheting)
            if (not exit_now) and (trail is not None) and (close_j < trail):
                exit_now, reason = True, "trail_atr"

            # (iv) Trend break (EMA50) — relaxed if well in profit
            if not exit_now:
                if (advance_atr >= R.get("ema_break_relax_after_atr", np.inf)) and (atr_j is not None):
                    # require cushion below EMA50 if nicely ahead
                    if close_j < (ema50_j - R.get("ema_break_cushion_atr", 0.0) * atr_j):
                        exit_now, reason = True, "ema50_relaxed"
                else:
                    if close_j < ema50_j:
                        exit_now, reason = True, "ema50_break"

            # (v) No-progress stop
            if not exit_now and (df["Date"].iat[j] - entry_time) >= pd.Timedelta(hours=R["no_progress_hours"]):
                if (atr_j is None) or ((high_since_entry - entry_price) < (R["no_progress_atr"] * atr_j)):
                    exit_now, reason = True, "no_progress"

            # (vi) Time stop
            if not exit_now and (df["Date"].iat[j] - entry_time) >= pd.Timedelta(hours=R["time_stop_hours"]):
                exit_now, reason = True, "time_stop"

            if exit_now:
                exit_time = df["Date"].iat[i]
                exit_price = df["Open"].iat[i]
                gross_ret = (exit_price / entry_price) - 1.0
                net_ret = ((exit_price * (1 - fee)) / (entry_price * (1 + fee)) - 1.0) if fee > 0 else gross_ret

                # exposure scaler + max loss cap
                net_ret *= LEVERAGE
                net_ret = max(net_ret, -MAX_LOSS_CAP)

                trades.append({
                    "entry_time": entry_time, "entry_price": entry_price,
                    "exit_time": exit_time,   "exit_price": exit_price,
                    "gross_ret": gross_ret,   "net_ret": net_ret,
                    "holding_hours": (exit_time - entry_time) / pd.Timedelta(hours=1),
                    "regime": entry_reg, "strategy": "TR3", "exit_reason": reason
                })
                in_pos = False
                # reset state
                entry_price = entry_time = entry_bar_high = high_since_entry = None
                entry_reg = None
                be_armed_since = None

        pos[i] = 1.0 if in_pos else 0.0

    # Close any open position on last bar's open
    if in_pos:
        i = len(df) - 1
        exit_time = df["Date"].iat[i]
        exit_price = df["Open"].iat[i]
        gross_ret = (exit_price / entry_price) - 1.0
        net_ret = ((exit_price * (1 - fee)) / (entry_price * (1 + fee)) - 1.0) if fee > 0 else gross_ret
        net_ret *= LEVERAGE
        net_ret = max(net_ret, -MAX_LOSS_CAP)
        trades.append({
            "entry_time": entry_time, "entry_price": entry_price,
            "exit_time": exit_time,   "exit_price": exit_price,
            "gross_ret": gross_ret,   "net_ret": net_ret,
            "holding_hours": (exit_time - entry_time) / pd.Timedelta(hours=1),
            "regime": 1, "strategy": "TR3", "exit_reason": "eod_close"
        })

    trade_log = pd.DataFrame(trades, columns=cols)
    strat_rets = pd.Series(pos, index=df.index) * df["ret_oo"]
    return trade_log, strat_rets


def metrics(df: pd.DataFrame, trade_log: pd.DataFrame) -> dict:
    """
    Computes equity/metrics from trade-based hourly reconstruction (unchanged),
    and ALSO returns alternate win-rate/profit-factor views that treat tiny
    breakeven (BE) exits as flat for reporting only. Equity math is not altered.
    """
    dates = df["Date"]
    # hourly series of zeros
    r = pd.Series(0.0, index=dates)

    if trade_log is None or len(trade_log) == 0:
        # no trades → flat equity
        equity = (1.0 + r).cumprod()
        years = (dates.iloc[-1] - dates.iloc[0]) / pd.Timedelta(days=365.25)
        cagr = equity.iloc[-1] ** (1/years) - 1 if years > 0 else float("nan")
        mu, sd = r.mean(), r.std(ddof=0)
        sharpe = (mu / sd) * sqrt(24 * 365.25) if sd > 0 else float("nan")
        return {
            "CAGR": cagr, "Sharpe": sharpe, "ProfitFactor": float("nan"),
            "WinRate": float("nan"), "FinalEquity": equity.iloc[-1], "NumTrades": 0
        }

    # map trade times to indices on the 1h grid
    idx = pd.Index(dates)
    entry_idx = idx.get_indexer(pd.to_datetime(trade_log["entry_time"]))
    exit_idx  = idx.get_indexer(pd.to_datetime(trade_log["exit_time"]))

    # spread each trade's return evenly (geometric) across its holding hours
    Hs   = trade_log["holding_hours"].to_numpy()
    ret_col = "net_ret" if "net_ret" in trade_log.columns else "gross_ret"
    rets = trade_log[ret_col].astype(float).to_numpy()

    for e, x, H, R in zip(entry_idx, exit_idx, Hs, rets):
        H_int = int(round(H))
        if e < 0 or x < 0 or H_int <= 0:
            # if mapping fails, put whole return on exit bar as a fallback
            if x >= 0:
                r.iloc[x] += R
            continue
        rh = (1.0 + R)**(1.0 / H_int) - 1.0   # per-hour return so that (1+rh)^H = 1+R
        end = min(e + H_int, len(r))
        r.iloc[e:end] += rh

    # equity & metrics from the reconstructed hourly series
    equity = (1.0 + r).cumprod()
    years = (dates.iloc[-1] - dates.iloc[0]) / pd.Timedelta(days=365.25)
    cagr = equity.iloc[-1] ** (1/years) - 1 if years > 0 else float("nan")
    mu, sd = r.mean(), r.std(ddof=0)
    sharpe = (mu / sd) * sqrt(24 * 365.25) if sd > 0 else float("nan")

    # trade-level stats (STRICT, unchanged)
    ret_series = trade_log[ret_col].astype(float)
    gross_profit = ret_series[ret_series > 0].sum()
    gross_loss   = -ret_series[ret_series < 0].sum()
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float("nan")
    win_rate_strict = (ret_series > 0).mean()

    # -------- Alternate reporting (breakeven-aware) --------
    # Treat tiny BE losses as flat for reporting ONLY (does not affect equity)
    EPS_BE = 0.001  # 0.10%; tune to 0.0005–0.0015 if desired
    if "exit_reason" in trade_log.columns:
        is_be = trade_log["exit_reason"].astype(str).eq("breakeven")
    else:
        is_be = pd.Series(False, index=trade_log.index)

    # Alternative WRs
    win_rate_ge0    = (ret_series >= 0).mean()
    win_rate_be_adj = ((ret_series > 0) | (is_be & (ret_series > -EPS_BE))).mean()

    # Reporting PF with tiny BE losses zeroed out (reporting only)
    rep_rets = ret_series.copy()
    mask_be_tiny = is_be & (rep_rets.abs() <= EPS_BE)
    rep_rets.loc[mask_be_tiny] = 0.0
    gp_rep = rep_rets[rep_rets > 0].sum()
    gl_rep = -rep_rets[rep_rets < 0].sum()
    profit_factor_be_adj = (gp_rep / gl_rep) if gl_rep > 0 else float("nan")

    be_count = int(is_be.sum())
    be_near0 = int(mask_be_tiny.sum())
    be_median = float(ret_series[is_be].median()) if be_count > 0 else float("nan")

    return {
        # Core (unchanged)
        "CAGR": cagr,
        "Sharpe": sharpe,
        "ProfitFactor": profit_factor,
        "WinRate": win_rate_strict,
        "FinalEquity": equity.iloc[-1],
        "NumTrades": len(trade_log),

        # Extra reporting (breakeven-aware)
        "WinRate_GE0": win_rate_ge0,
        "WinRate_BEAdj": win_rate_be_adj,
        "ProfitFactor_BEAdj": profit_factor_be_adj,
        "BreakevenCount": be_count,
        "BreakevenNearZeroCount": be_near0,
        "BreakevenMedianRet": be_median,
        "BE_Epsilon": EPS_BE
    }


def main():
    df = load_data(CSV_PATH)
    print_return_spikes(df, "ret_oo", cap=0.40, top=10)
    trade_log, strat_rets = simulate_tr3(df)
    m = metrics(df, trade_log)   # uses trade-based hourly series; ignores strat_rets

    out_path = "./TRADING-MODELS/TR_Model_Log2.csv"
    trade_log.to_csv(out_path, index=False)

    # === Pretty summary & full dump ===
    print("\n=== TR³ — State 1 Trend (1H), Buy/Sell at Open ===")
    print(f"Trades: {m.get('NumTrades', 0)} | Final Equity: {m.get('FinalEquity', float('nan')):.4f}")
    print(f"CAGR: {m.get('CAGR', float('nan')):.2%}")
    print(f"Sharpe (ann.): {m.get('Sharpe', float('nan')):.2f}")
    print(f"Profit Factor: {m.get('ProfitFactor', float('nan')):.2f}")
    print(f"Win Rate (strict >0): {m.get('WinRate', float('nan')):.2%}")
    print(f"Trade Log saved → {out_path}")

    # Breakeven-aware extras (printed only if present)
    if ('ProfitFactor_BEAdj' in m) or ('WinRate_BEAdj' in m):
        print(f"PF (BE-adj): {m.get('ProfitFactor_BEAdj', float('nan')):.2f} | "
              f"WR (>=0): {m.get('WinRate_GE0', float('nan')):.2%} | "
              f"WR (BE-adj): {m.get('WinRate_BEAdj', float('nan')):.2%}")
        print(f"Breakeven trades: {m.get('BreakevenCount', 0)} "
              f"(near-zero: {m.get('BreakevenNearZeroCount', 0)}; "
              f"median ret: {m.get('BreakevenMedianRet', float('nan')):.3%})")
        print(f"BE epsilon used: {m.get('BE_Epsilon', float('nan')):.2%}")

    # Full metrics dict (future-proof: prints any new keys you add later)
    print("\n--- Full metrics dict ---")
    for k, v in m.items():
        if isinstance(v, float):
            if any(s in k.lower() for s in ["cagr", "rate", "wr", "epsilon", "ret"]):
                print(f"{k}: {v:.6%}")
            else:
                print(f"{k}: {v:.6f}")
        else:
            print(f"{k}: {v}")


if __name__ == "__main__":
    main()
