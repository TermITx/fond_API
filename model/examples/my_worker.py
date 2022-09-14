import argparse
import os
import subprocess
import multiprocessing
from datetime import date, timedelta, datetime
import pandas as pd

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
    for file in os.listdir(directory):
        data_file = pd.read_csv((os.path.join(directory, file)))
        date_today = data_file.tail(1).iloc[0]["Date"]
        date_today = datetime.strptime(date_today, "%Y-%m-%d")
        break
    date_start = (date_today- timedelta(days=days_to_subtract)).strftime("%Y-%m-%d")
    date_today = date_today.strftime("%Y-%m-%d")


    for i in range(0, len(QUANDL_TICKERS), 1):
        
        new_tickers = QUANDL_TICKERS[i:i+1]
        processes=[]
    
        for ticker in new_tickers:
            original_path = f'{os.path.join( CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length), ticker + ".csv")}'
            tmp_path = f'{os.path.join( CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length), ticker +  "tmp"+  ".csv")}'

        #ticker = QUANDL_TICKERS[0]
            command = ["python", "-m", "model.examples.cpd_quandl" , f'{ticker}', tmp_path,  date_start ,date_today, f"{lookback_window_length}"]
            process = subprocess.Popen(command)
            processes.append(process)
        for process in processes:
            process.wait()
        df1 = pd.read_csv(tmp_path)
        print(df1.iloc[0])
        df2 = pd.read_csv(original_path)
        print(df2.iloc[0])
        df3=pd.concat([df2, df1]).drop_duplicates(["date"], keep= "last", ignore_index=True)
        df3.to_csv(original_path)
        

        return
    




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