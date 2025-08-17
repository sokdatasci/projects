# Swing Trading Starter: Market Data Pipeline + Indicator Engine

This starter helps you build the **core foundation** for swing trading projects:
1) fetch/clean OHLCV data, 2) compute technical indicators, 3) save enriched datasets,
4) plot basic charts for quick visual inspection.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

# Pull data & compute indicators (example: AAPL, last 2y, daily)
python -m src.data_pipeline --ticker AAPL --period 2y --interval 1d --out data/AAPL_2y_1d.csv

# Plot with indicators
python -m src.plotting --csv data/AAPL_2y_1d.csv --overlay_sma 20 50 --overlay_bbands 20 2
```

> Note: Requires network access for yfinance. If you run in a restricted environment, use it locally.
