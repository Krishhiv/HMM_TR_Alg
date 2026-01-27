import numpy as np
import pandas as pd

# assumes you have a DataFrame `out` (or `df`) indexed by Date with columns:
# 'Close','Log_Returns','GKVol_20','VolZ_20','EMA_20_slope','BodyPct','ClosePosInRange','CloseOverEMA20'
# and a state column like 'State_K4'. Adjust names if different.

df_states = pd.read_csv('./outputs/btc_1d_with_states_compact.csv')
state_col = next(c for c in df_states.columns if c.startswith('State_K'))
feat_cols = ['Log_Returns','GKVol_20','VolZ_20','EMA_20_slope','BodyPct','ClosePosInRange','CloseOverEMA20']

# forward 1-day log return (no leakage for analysis)
df_states['FwdRet_1d'] = df_states['Log_Returns'].shift(-1)

summary = (
    df_states
    .groupby(state_col)
    .agg(
        n=('Close','size'),
        occ=('Close',lambda s: len(s)/len(df_states)),
        mean_ret=('Log_Returns','mean'),
        fwd1d=('FwdRet_1d','mean'),
        ret_std=('Log_Returns','std'),
        GKVol=('GKVol_20','mean'),
        VolZ=('VolZ_20','mean'),
        EMA_slope=('EMA_20_slope','mean'),
        BodyPct=('BodyPct','mean'),
        ClosePos=('ClosePosInRange','mean'),
        PosVsEMA=('CloseOverEMA20','mean'),
    )
).round(4)
print('')
print('')
print(summary)
print('')
print('')
