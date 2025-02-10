import pandas as pd

def momentum_strategy(data, short_window=10, long_window=50):
    """Simple Moving Average (SMA) momentum strategy."""
    data["Short_MA"] = data["Close"].rolling(window=short_window).mean()
    data["Long_MA"] = data["Close"].rolling(window=long_window).mean()
    data["Signal"] = (data["Short_MA"] > data["Long_MA"]).astype(int)
    return data

