# Holdout Test (Option A)

This uses the same HMM + TR^3 logic as:
- `HMM-1d/btc_1d_hmm.py`
- `TRADING-MODELS/TR_MODEL_2.py`

It trains the HMM on Train+Val only, then tests on the unseen Test window.

## Run
From repo root:
```
python walkforward/run_holdout.py
```

Optional overrides:
```
python walkforward/run_holdout.py \
  --train-end 2019-12-31 \
  --val-end 2021-12-31 \
  --daily-csv MAIN-DATASETS/btc_1d_main.csv \
  --hourly-csv TRADING-MODELS/btc_1h_features_PRIME.csv
```

## Outputs
- `walkforward/outputs/trade_log_holdout.csv`
- `walkforward/outputs/summary.txt`

## Verify
- Check that `trade_log_holdout.csv` only contains dates after `val-end`.
- Review `summary.txt` for headline metrics.
