import pandas as pd

def analyze_stock_csv(filename: str) -> str:
    try:
        df = pd.read_csv(filename, parse_dates=["Date"], index_col="Date")

        # Drop rows with missing values
        df.dropna(inplace=True)

        # Daily returns
        df["Daily Return"] = df["Close"].pct_change()
        avg_return = df["Daily Return"].mean()
        volatility = df["Daily Return"].std()

        # Moving averages
        df["50MA"] = df["Close"].rolling(window=50).mean()
        df["200MA"] = df["Close"].rolling(window=200).mean()

        summary = f"""
📊 Stock Analysis Summary for {filename}:

• Average Daily Return: {avg_return:.4f}
• Volatility (Std Dev of Return): {volatility:.4f}
• Latest Close Price: {df['Close'][-1]:.2f}
• 50-Day Moving Average: {df['50MA'][-1]:.2f}
• 200-Day Moving Average: {df['200MA'][-1]:.2f}
"""
        return summary.strip()

    except Exception as e:
        return f"❌ Error during analysis: {e}"
