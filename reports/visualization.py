import matplotlib.pyplot as plt

def plot_strategy(data):
    plt.figure(figsize=(12,6))
    plt.plot(data["Close"], label="Stock Price")
    plt.plot(data["Short_MA"], label="Short MA", linestyle="--")
    plt.plot(data["Long_MA"], label="Long MA", linestyle="--")
    plt.legend()
    plt.title("Trading Strategy Performance")
    plt.show()
