import yfinance as yf
import pandas as pd
import os

def get_data(ticker, start="2020-01-01", end="2023-01-01"):
    """Download historical stock data and save it as a CSV file."""
    data = yf.download(ticker, start=start, end=end)

    # Ensure the 'data' directory exists
    os.makedirs("data", exist_ok=True)

    # Save data
    file_path = f"data/{ticker}.csv"
    data.to_csv(file_path)
    print(f"Data saved successfully at {file_path}")

    return data

if __name__ == "__main__":
    get_data("AAPL")
