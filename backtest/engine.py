def backtest(data, initial_cash=10000):
    """Simple Backtesting Engine"""
    cash = initial_cash
    shares = 0

    for i in range(1, len(data)):
        if data["Signal"].iloc[i-1] == 0 and data["Signal"].iloc[i] == 1:
            shares = cash / data["Close"].iloc[i]
            cash = 0
        elif data["Signal"].iloc[i-1] == 1 and data["Signal"].iloc[i] == 0:
            cash = shares * data["Close"].iloc[i]
            shares = 0

    portfolio_value = cash + shares * data["Close"].iloc[-1]
    return portfolio_value

