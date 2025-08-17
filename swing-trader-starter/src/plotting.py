import argparse, pandas as pd, matplotlib.pyplot as plt

def plot_price_with_overlays(df, sma_list=None, ema_list=None, bbands=False):
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["Close"], label="Close")
    if sma_list:
        for w in sma_list:
            col = f"SMA{w}"
            if col in df.columns:
                plt.plot(df["Date"], df[col], label=col)
    if ema_list:
        for w in ema_list:
            col = f"EMA{w}"
            if col in df.columns:
                plt.plot(df["Date"], df[col], label=col)
    if bbands and all(c in df.columns for c in ["BB_UPPER","BB_MID","BB_LOWER"]):
        plt.plot(df["Date"], df["BB_UPPER"], label="BB_UPPER", linewidth=1)
        plt.plot(df["Date"], df["BB_MID"], label="BB_MID", linewidth=1)
        plt.plot(df["Date"], df["BB_LOWER"], label="BB_LOWER", linewidth=1)
    plt.legend(); plt.title("Price with Overlays")
    plt.xlabel("Date"); plt.ylabel("Price")
    plt.tight_layout(); plt.show()

def plot_rsi(df):
    if "RSI14" not in df.columns: return
    plt.figure(figsize=(12,3.5))
    plt.plot(df["Date"], df["RSI14"], label="RSI14")
    plt.axhline(30, linestyle="--"); plt.axhline(70, linestyle="--")
    plt.title("RSI(14)"); plt.xlabel("Date"); plt.ylabel("RSI")
    plt.tight_layout(); plt.show()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--overlay_sma", nargs="*", type=int, default=[])
    ap.add_argument("--overlay_ema", nargs="*", type=int, default=[])
    ap.add_argument("--overlay_bbands", action="store_true")
    args = ap.parse_args()
    df = pd.read_csv(args.csv, parse_dates=["Date"])
    plot_price_with_overlays(df, sma_list=args.overlay_sma, ema_list=args.overlay_ema, bbands=args.overlay_bbands)
    plot_rsi(df)

if __name__ == "__main__":
    main()
