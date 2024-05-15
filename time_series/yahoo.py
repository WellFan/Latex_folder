import yfinance as yf
import pandas as pd
df = yf.download('NG=F', start='2009-05-14', end='2024-05-14')
df.to_csv('data.csv')