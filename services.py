import subprocess
import time
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import datetime

PATH = "C:/Users/Karlo/Desktop/"

def call_R_script(name : str):
    subprocess.call ("Rscript --vanilla " + PATH + name +  ".R", shell=True)
    return {"Status":"Success"}

def get_position(strategy : str):
    if strategy == 'DM':
        R_script_name = 'DM_features'
        ##Ovdje pozvati prvo izgradnju featura s R skriptom
        subprocess.call ("Rscript --vanilla " + PATH +  + R_script_name +".R", shell=True)
        ##Pricekaj da se generiraju featurei
        time.sleep(1)
        ##Zatim pozvati poziciju s istim featurima

        pass

def call_yahoo(tickers=None,date=None):
    if tickers is None:
        tickers = ['AAL','AAPL','AMD','AMZN','APA','BAC','BEN','BMY','BSX','C','CCL','CL','CLF','CMCSA','CSCO','CSX','CVX','DAL','DIS','ET','FCX','FTI','GM','HBAN','INTC','JPM','KO','LUMN','MRK','MRO','MSFT','MU','NEE','NFLX','NVDA','NYCB','OXY','PCG','PFE','PLUG','QCOM','RF','RIG','SIRI','SPY','SWN','T','TELL','UEC','VZ','WBA','WBD','WFC','WU','X','XOM']
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')

    for name in tickers:
        aapl_df = yf.download(name, 
                            start=date, 
                            #end='2021-01-01', 
                            progress=True,
        )
        to_append = pd.read_csv(f'{name}.csv')
        to_append.append(aapl_df[-1:])
        to_append.to_csv(f"{name}.csv")
if __name__ == "__main__":
    call_R_script("probar")