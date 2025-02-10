import ccxt

exchange = ccxt.binance()
markets = exchange.load_markets()
ticker = exchange.fetch_ticker('BTC/USDT')
print(ticker)
