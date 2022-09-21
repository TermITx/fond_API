from os import popen
import subprocess
import time
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import datetime

import model.call_model as model
import model.examples.my_worker as my_worker
import model.combine_all_feature as combine_all_features
PATH = "Rscripts"

def call_R_script(name : str):
    subprocess.call ("Rscript --vanilla " + PATH + name +  ".R", shell=True)
    return {"Status":"Success"}

def get_position(strategy : str):
    print(strategy)
    if strategy == 'DM':
        print("uso")
        R_script_name = 'DM_features'
        ##Poziv yahoo finance-a za danasnje OHLCV podatke
        ##call_yahoo()
        ##Ovdje pozvati prvo izgradnju featura s R skriptom
        #subprocess.call ("Rscript --vanilla " + PATH +  + R_script_name +".R", shell=True)
        process = subprocess.Popen(["Rscript", "--vanilla",PATH,R_script_name ,".R"])
        process.wait()
        ##Pricekaj da se generiraju featurei
        #time.sleep(1)
        ##Zatim pozvati poziciju s istim featurima

        #my_worker.main(21)
        #my_worker.main(126)
        command = ["python" ,  "-m" ,  "model.examples.create_features_quandl" ,   "126",   "21"]
        process = subprocess.Popen(command)

        # process = subprocess.call ("python " +  "-m " +  "model.examples.create_features_quandl " +   "126 "  + "21 ", shell=True)
        # process.wait()
        combine_all_features.combine_all_features()
        today = datetime.today().strftime("%Y-%m-%d")

        return model.call_model(today)

        

def call_yahoo(tickers=None,date=None):
    if tickers is None:
        #tickers = ['AAL','AAPL','AMD','AMZN','APA','BAC','BEN','BMY','BSX','C','CCL','CL','CLF','CMCSA','CSCO','CSX','CVX','DAL','DIS','ET','FCX','FTI','GM','HBAN','INTC','JPM','KO','LUMN','MRK','MRO','MSFT','MU','NEE','NFLX','NVDA','NYCB','OXY','PCG','PFE','PLUG','QCOM','RF','RIG','SIRI','SPY','SWN','T','TELL','UEC','VZ','WBA','WBD','WFC','WU','X','XOM']
        tickers = ['AAPL', 'AMD', 'T', 'BAC', 'SWN', 'MSFT', 'XOM', 'BMY', 'PCG', 'WBD', 'CCL', 'C', 'KO', 'TELL', 'DIS', 'MRK', 'BSX', 'CL', 'CVX', 'FTI', 'AMZN', 'WU', 'NYCB', 'RF','SPY']
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')

    call_OHLC_prices(tickers)
    call_settle_prices(tickers)

 


def call_OHLC_prices(tickers):
    for name in tickers:
        to_append_OHLCV = pd.read_csv(f'model/data/data_OHLCV/{name}.csv',)


        last_row = to_append_OHLCV.tail(1)
        last_date_in_original_csv = last_row.iloc[0]['Date']
        to_append_yahoo = yf.download(name, 
                                    start=last_date_in_original_csv, 
                                    #end='2021-01-01', 
                                    progress=True)
        last_date_in_yahoo_csv = last_row.iloc[0]['Date']
        to_append_yahoo.reset_index(inplace=True)
        to_append_OHLCV['Date'] = pd.to_datetime(to_append_OHLCV['Date'])
        to_append_OHLCV['Date'] = to_append_OHLCV['Date'].dt.date
        to_append_yahoo['Date'] = to_append_yahoo['Date'].dt.date


        df3=pd.concat([to_append_OHLCV, to_append_yahoo], axis=0, ignore_index=True).drop_duplicates( keep= "last", ignore_index=False, subset='Date')
        
        df3.to_csv(f"model/data/data_OHLCV/{name}.csv", index=False)

def call_settle_prices(tickers):
    for name in tickers:
        to_append_settle = pd.read_csv(f'model/data/quandl/{name}.csv',)

        last_row = to_append_settle.tail(1)
        last_date_in_original_csv = last_row.iloc[0]['Date']
        to_append_yahoo = yf.download(name, 
                                    start=last_date_in_original_csv, 
                                    #end='2021-01-01', 
                                    progress=True)
        last_date_in_yahoo_csv = last_row.iloc[0]['Date']
        to_append_yahoo.reset_index(inplace=True)
        to_append_settle['Date'] = pd.to_datetime(to_append_settle['Date'])
        to_append_settle['Date'] = to_append_settle['Date'].dt.date
        to_append_yahoo['Date'] = to_append_yahoo['Date'].dt.date
        to_append_yahoo = to_append_yahoo.drop(["Open","High","Low","Adj Close","Volume"], axis=1)
        to_append_yahoo.rename(columns={"Close": "Settle", }, inplace=True)
        df3=pd.concat([to_append_settle, to_append_yahoo], axis=0, ignore_index=True).drop_duplicates( keep= "last", ignore_index=False, subset='Date')
        df3.to_csv(f'model/data/quandl/{name}.csv', index=False)


def call_yahoo_from_start(tickers=None,date=None):
    if tickers is None:
        tickers = ['AAL','AAPL','AMD','AMZN','APA','BAC','BEN','BMY','BSX','C','CCL','CL','CLF','CMCSA','CSCO','CSX','CVX','DAL','DIS','ET','FCX','FTI','GM','HBAN','INTC','JPM','KO','LUMN','MRK','MRO','MSFT','MU','NEE','NFLX','NVDA','NYCB','OXY','PCG','PFE','PLUG','QCOM','RF','RIG','SIRI','SPY','SWN','T','TELL','UEC','VZ','WBA','WBD','WFC','WU','X','XOM']
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')

    for name in tickers:

        to_append_OHLCV = pd.DataFrame()
        

        to_append_OHLCV = yf.download(name, 
                            start= "1999-12-31", 
                            end='2021-01-01', 
                            progress=True,)
        
        
        #print(aapl_df[-1:].drop(columns=["Open", "High", ]))
        to_append_OHLCV = to_append_OHLCV.drop(["Open","High","Low","Adj Close","Volume"], axis=1)
        to_append_OHLCV.rename(columns={"Close": "Settle", }, inplace=True)
        to_append_OHLCV.append(to_append_OHLCV)
        to_append_OHLCV.to_csv(f"model/data/quandl/{name}.csv", index=True)
        

if __name__ == "__main__":
    #call_yahoo_from_start()
    #call_yahoo()
    #my_worker.main(21)
    command = ["python" ,  "-m" ,  "model.examples.my_worker" ,    "21"]
    process = subprocess.Popen(command)
    process.wait()
    ##call_R_script("probar")