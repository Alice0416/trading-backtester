import pandas as pd
from data.fetch_data import get_data
from strategies.momentum import momentum_strategy
from backtest.engine import backtest
from reports.visualization import plot_strategy

# Download market data
data = get_data("AAPL")

# Apply strategy
strategy_data = momentum_strategy(data)

# Backtest
final_value = backtest(strategy_data)
print(f"Final Portfolio Value: ${final_value:.2f}")

# Visualize results
plot_strategy(strategy_data)

