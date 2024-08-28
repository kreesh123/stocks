import yfinance as yf
msft = yf.Ticker("MSFT")
history = msft.history()
print(history[['Open', 'High', 'Low', 'Close']])