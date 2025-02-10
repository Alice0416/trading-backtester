import pandas as pd
import numpy as np

def mean_reversion_strategy(data, window=20, threshold=1.5):
    """Mean Reversion Strategy using Z-score."""
    data["Mean"] = data["Close"].rolling(window=window).mean()
    data["Std"] = data["Close"].rolling(window=window).std()
    data["Z-score"] = (data["Close"] - data["Mean"]) / data["Std"]

    data["Signal"] = 0
    data.loc[data["Z-score"] > threshold, "Signal"] = -1  # Overbought (sell)
    data.loc[data["Z-score"] < -threshold, "Signal"] = 1  # Oversold (buy)

    return data
