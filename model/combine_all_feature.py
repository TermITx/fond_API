import datetime as dt
import numpy as np
import pandas as pd
import os

def get_names_of_features(dira):
    lista = os.listdir(dira)
    return [(i.replace("features_", "").replace(".csv", ""), dira + "/" + i) for i in lista]


def combine_all_features():
    df_base = pd.read_csv("model/data/quandl_cpd_126lbw.csv")
    df_base.to_csv("model/data/quandl_cpd_126lbw_backup1.csv")
    useful = ["autoarima_sd_126_Lo95"   ,         "autoarima_1_126_PointForecast" ,  
    "autoarima_last_126_PointForecast" ,"q75_close_divergence_50"    ,     
    "close_above_vwap_50",
    "ema_above_sma200",
    "close_above_sma22",
    "close_above_vwap_20",
    "lm_std2_126",
    "sharpe_126",
    "q1_close_divergence_100",
    "q50_close_divergence_100",
    "q75_close_divergence_50",
    "rolling_mode_200",
    "rolling_mode_500",
    "backcusum_rejections_10_126",
    "exuber_126_2_sadf",
    "exuber_126_2_bsadf",
    "autoarima_1_126_Lo80",
    "autoarima_1_126_Hi95",
    "autoarima_last_126_Lo80",
    "autoarima_sd_126_Hi95",
    "volume_rate_126"
    "percent_rank_126",
    "bbands_mavg_126",
    "skew_126",
    "sd_parkinson_126"
    ]
    useful+= ["date", "symbol"]
    stocks = get_names_of_features("model/data/m_features")


    df_final = pd.DataFrame()
    for tup in stocks:
        if (tup[0] not in ["PCG",  "RF", "SPY", "SWN", "T", "TELL", "WBD"]):
            continue
        if (tup[0][0] ==  "."):
            continue
        print(tup[1])
        curr_stock = pd.read_csv(tup[1])
        curr_stock["date"] = curr_stock.apply(lambda x: (dt.datetime.strptime(x["date"], '%Y-%m-%d') - dt.timedelta(days=1)).strftime('%Y-%m-%d'), axis=1)
        curr_stock = curr_stock[curr_stock.columns.intersection(useful)]
        df_a = df_base
        df_b= curr_stock
        df_a = df_a.merge(df_b, how='inner', left_on=['date', 'ticker'], right_on=['date', 'symbol'])
        df_a=df_a.drop("symbol", axis=1)
        df_a=df_a.dropna(how='any',axis=0) 
        df_final = pd.concat([df_final, df_a], axis=0)

    df_final.to_csv("model/data/quandl_cpd_126lbw.csv", index=False)

