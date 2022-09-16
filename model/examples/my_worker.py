import argparse
import os
import subprocess
import multiprocessing
from datetime import date, timedelta, datetime
import pandas as pd
from pathlib import Path

import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)



from model.settings.default import (
    QUANDL_TICKERS,
    CPD_QUANDL_OUTPUT_FOLDER,
    CPD_DEFAULT_LBW,
)

def main(lookback_window_length: int):
    days_to_subtract = 2 * 365
    
    date_today = 0
    # if not os.path.exists(CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length)):
    #     os.mkdir(CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length))

    
    directory = "model/data/quandl"
    file = "AAPL.csv"
    #for file in os.listdir(directory):
    data_file = pd.read_csv((os.path.join(directory, file)))
    date_today = data_file.tail(1).iloc[0]["Date"]
    date_today = datetime.strptime(date_today, "%Y-%m-%d")
    date_start = (date_today- timedelta(days=days_to_subtract)).strftime("%Y-%m-%d")
    date_today = (date_today+  timedelta(days=1)) .strftime("%Y-%m-%d")
    
    print(date_today)

    QUANDL_TICKERS = ['AAL','AAPL','AMD','AMZN','APA','BAC','BEN','BMY','BSX','C','CCL','CL','CLF','CMCSA','CSCO','CSX','CVX','DAL','DIS','ET','FCX','FTI','GM','HBAN','INTC','JPM','KO','LUMN','MRK','MRO','MSFT','MU','NEE','NFLX','NVDA','NYCB','OXY','PCG','PFE','PLUG','QCOM','RF','RIG','SIRI','SPY','SWN','T','TELL','UEC','VZ','WBA','WBD','WFC','WU','X','XOM']





    for i in range(0, len(QUANDL_TICKERS), 2):
        
        new_tickers = QUANDL_TICKERS[i:i+2]
        processes=[]
     
    
        for ticker in new_tickers:
           
            original_path = f'{os.path.join( CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length), ticker + ".csv")}'
            tmp_path = f'{os.path.join( CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length), ticker +  "tmp"+  ".csv")}'
            if (not(os.path.isfile(tmp_path))):
                Path(tmp_path).touch()
            

        
            command = ["python", "-m", "model.examples.cpd_quandl" , f'{ticker}', tmp_path,  date_start ,date_today, f"{lookback_window_length}"]
            process = subprocess.Popen(command)
            processes.append(process)

        for process in processes:
            process.wait()
        
        for ticker in new_tickers:
               
            original_path = f'{os.path.join( CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length), ticker + ".csv")}'
            tmp_path = f'{os.path.join( CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length), ticker +  "tmp"+  ".csv")}'

            df1 = pd.read_csv(tmp_path)
            df2 = pd.read_csv(original_path)
            df3=pd.concat([df2, df1], axis=0, ignore_index=True).drop_duplicates( keep= "last", ignore_index=False, subset='date')
            if ("Unnamed: 0" in df3.columns):
                df3.drop("Unnamed: 0", inplace=True, axis=1)
            df3.to_csv(original_path, index=False)

        
        

    
    




if __name__ == "__main__":

    def get_args():
        """Returns model.settings from command line."""

        parser = argparse.ArgumentParser(
            description="Run changepoint detection module for all tickers"
        )
        parser.add_argument(
            "lookback_window_length",
            metavar="l",
            type=int,
            nargs="?",
            default=CPD_DEFAULT_LBW,
            help="CPD lookback window length",
        )
        return [
            parser.parse_known_args()[0].lookback_window_length,
        ]

    main(*get_args())