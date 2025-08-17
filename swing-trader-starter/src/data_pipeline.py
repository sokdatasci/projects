import argparse, numpy as np, pandas as pd

def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = (delta.clip(lower=0)).ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()

def sma(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window).mean()

def macd(close: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    macd_line = ema(close, fast) - ema(close, slow)
    signal_line = ema(macd_line, signal)
    hist = macd_line - signal_line
    return macd_line, signal_line, hist

def bollinger_bands(close: pd.Series, window: int = 20, num_std: float = 2.0):
    mid = sma(close, window)
    std = close.rolling(window).std()
    upper = mid + num_std * std
    lower = mid - num_std * std
    return upper, mid, lower

def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    close = df["Close"]
    df["SMA20"] = sma(close, 20)
    df["SMA50"] = sma(close, 50)
    df["EMA20"] = ema(close, 20)
    df["RSI14"] = rsi(close, 14)
    m, s, h = macd(close, 12, 26, 9)
    df["MACD"], df["MACD_SIGNAL"], df["MACD_HIST"] = m, s, h
    u, m, l = bollinger_bands(close, 20, 2.0)
    df["BB_UPPER"], df["BB_MID"], df["BB_LOWER"] = u, m, l
    return df

def fetch_ohlcv_yf(ticker: str, period: str = "2y", interval: str = "1d") -> pd.DataFrame:
    import yfinance as yf
    df = yf.download(ticker, period=period, interval=interval, auto_adjust=True, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df.rename_axis("Date").reset_index()
    return df.dropna(subset=["Close"]).copy()

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--period", default="2y")
    ap.add_argument("--interval", default="1d")
    ap.add_argument("--out", default="data/output.csv")
    args = ap.parse_args()

    df = fetch_ohlcv_yf(args.ticker, args.period, args.interval)
    df = compute_indicators(df)
    df.to_csv(args.out, index=False)
    print(f"Saved enriched data to {args.out} with shape {df.shape}")

if __name__ == "__main__":
    main()
