from yahoofinancials import YahooFinancials
import yfinance as yf
import pandas as pd
import os
from datetime import date, timedelta, datetime


name="AAPL"
directory = "model/data/quandl"
date_today=0
days_to_subtract=10
for file in os.listdir(directory):
    data_file = pd.read_csv((os.path.join(directory, file)))
    date_today = data_file.tail(1).iloc[0]["Date"]
    date_today = datetime.strptime(date_today, "%Y-%m-%d")
    break
date_start = (date_today- timedelta(days=days_to_subtract)).strftime("%Y-%m-%d")
date_today = date_today.strftime("%Y-%m-%d")
print(date_today)
print(date_start)


