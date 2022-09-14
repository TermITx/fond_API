import sys,os,json
from model.mom_trans.momentum_transformer import TftDeepMomentumNetworkModel 
from model.settings.default import QUANDL_TICKERS
from model.mom_trans.model_inputs import ModelFeatures
import pandas as pd


def call_model(today):
    #return {"Result": 5}
    
    experiment_name = "model/results/experiment_quandl_100assets_tft_cp12621_len252_notime_div_v1/2016-2023"
    hp_directory = os.path.join(experiment_name + "/best_hyperparameters.json")
    checkpoint_path = "model/results/experiment_quandl_100assets_tft_cp12621_len252_notime_div_v1/2016-2023/best/checkpoints"
    params = {}
    hiperparameters={}
    with open('model/results/experiment_quandl_100assets_tft_cp12621_len252_notime_div_v1/2016-2023/fixed_params.json') as json_file:
        params = json.load(json_file)
    with open('model/results/experiment_quandl_100assets_tft_cp12621_len252_notime_div_v1/2016-2023/best_hyperparameters.json') as json_file:
        hiperparameters = json.load(json_file)

    features_file_path = "model/data/quandl_cpd_126lbw.csv"

    print("123")




    raw_data = pd.read_csv(features_file_path, index_col=0, parse_dates=True)
    print(len(raw_data["ticker"].unique()))
    raw_data["date"] = raw_data["date"].astype("datetime64[ns]")
    train_interval = [2001, 2003, 2023]
    changepoint_lbws = [126, 21]
    ASSET_CLASS_MAPPING = dict(zip(QUANDL_TICKERS, ["COMB"] * len(QUANDL_TICKERS)))
    print("uso")
    model_features = ModelFeatures(
        raw_data,
        params["total_time_steps"],
        start_boundary=train_interval[0],
        test_boundary=train_interval[1],
        test_end=train_interval[2],
        changepoint_lbws=changepoint_lbws,
        split_tickers_individually=params["split_tickers_individually"],
        train_valid_ratio=params["train_valid_ratio"],
        add_ticker_as_static=(params["architecture"] == "TFT"),
        time_features=params["time_features"],
        lags=params["force_output_sharpe_length"],
        asset_class_dictionary=ASSET_CLASS_MAPPING,
        )

    model = TftDeepMomentumNetworkModel(
        experiment_name,
        experiment_name  + "novo",
        #hp_minibatch_size,
        **params,
        #**model_features.input_params,
        **{
            "column_definition": model_features.get_column_definition(),
            "num_encoder_steps": 0,  # TODO artefact
            "stack_size": 1,
            "num_heads": 4,  # TODO to fixed params
        },
    )
    a = model.load_model(hiperparameters)
    m = a.load_weights("model/results/experiment_quandl_100assets_tft_cp12621_len252_notime_div_v1/2016-2023/best/checkpoints/checkpoint")
    res = model.get_positions(
        model_features.test_sliding,
        a,
        sliding_window=True,
        years_geq=train_interval[1],
        years_lt=train_interval[2],
    )

    res[0].to_csv("test_api.csv", index=None)
    print(res[0].tail(1))
    return res[0].loc[res[0]['time'] == today]


if __name__ == '__main__':
    call_model()
    




    



