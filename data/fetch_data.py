import yfinance as yf
import pandas as pd

def get_data(ticker, start="2020-01-01", end="2023-01-01"):
    """Download historical stock data."""
    data = yf.download(ticker, start=start, end=end)
    data.to_csv(f"data/{ticker}.csv")
    return data

if __name__ == "__main__":
    get_data("AAPL")

