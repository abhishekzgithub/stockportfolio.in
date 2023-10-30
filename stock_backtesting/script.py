import yfinance as yf
symbol="TATAMOTORS.NS"
df=yf.Ticker(symbol).history(period="2y",interval="1d")

print(df.head())

import backtesting