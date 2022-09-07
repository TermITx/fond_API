import os

CPD_LBWS = [10, 21, 63, 126, 256]
CPD_DEFAULT_LBW = 21
BACKTEST_AVERAGE_BASIS_POINTS = [None, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
USE_KM_HYP_TO_INITIALISE_KC = True

CPD_QUANDL_OUTPUT_FOLDER = lambda lbw: os.path.join( 
    "model/data", f"quandl_cpd_{(lbw if lbw else 'none')}lbw"
)

CPD_QUANDL_OUTPUT_FOLDER_DEFAULT = CPD_QUANDL_OUTPUT_FOLDER(CPD_DEFAULT_LBW)

FEATURES_QUANDL_FILE_PATH = lambda lbw: os.path.join( 
    "model/data", f"quandl_cpd_{(lbw if lbw else 'none')}lbw.csv"
)

FEATURES_QUANDL_FILE_PATH_DEFAULT = FEATURES_QUANDL_FILE_PATH(CPD_DEFAULT_LBW)

QUANDL_TICKERS = ['AAPL',

 'F',
 'AMD',
 'INTC',
 'T',

 'NVDA',

 'BAC',
 'CMCSA',
 'VZ',

 
 'SWN',
 'MSFT',
 'SIRI',

 'XOM',

 


 
 'PFE',
 'WFC',

 'BMY',
 'PCG',

 


 'AAL',
 'WBD',
 'CLF',
 'X',
 
 'CCL',
 
 'C',
 

 'CSCO',
 'KO',
 
 'HBAN',
 'OXY',

 'TELL',

 
 
 
 'FCX',
 'DIS',
 'MU',
 'GM',
 'RIG',
 'ET',
 'NFLX',
 'PLUG',
 'CSX',
 'MRK',
 'LUMN',
 'BSX',
 
 'CL',
 'NEE',
 'JPM',
 'CVX',
 'MRO',
 'UEC',
 
 
 'FTI',
 
 'QCOM',
 'AMZN',
 'DAL',
 


 'WU',
 'APA',

 'NYCB',

 'BEN',

 'RF',
 'WBA',
 "SPY"

]


ALL_QUANDL_CODES = ['AAPL',

 'F',
 'AMD',
 'INTC',
 'T',

 'NVDA',

 'BAC',
 'CMCSA',
 'VZ',

 
 'SWN',
 'MSFT',
 'SIRI',

 'XOM',

 


 
 'PFE',
 'WFC',

 'BMY',
 'PCG',

 


 'AAL',
 'WBD',
 'CLF',
 'X',
 
 'CCL',
 
 'C',
 

 'CSCO',
 'KO',
 
 'HBAN',
 'OXY',

 'TELL',

 
 
 
 'FCX',
 'DIS',
 'MU',
 'GM',
 'RIG',
 'ET',
 'NFLX',
 'PLUG',
 'CSX',
 'MRK',
 'LUMN',
 'BSX',
 
 'CL',
 'NEE',
 'JPM',
 'CVX',
 'MRO',
 'UEC',
 
 
 'FTI',
 
 'QCOM',
 'AMZN',
 'DAL',
 


 'WU',
 'APA',

 'NYCB',

 'BEN',

 'RF',
 'WBA',
 "SPY"

]


COMMODITIES_TICKERS = [
    "CC=F",
    "CL=F",
    "CT=F",
    "ES=F",
    "GC=F",
    "GF=F",
    "HE=F",
    "HG=F",
    "HO=F",
    "KC=F",
    "KE=F",
    "LBS=F",
    "LE=F",
    "MGC=F",
    "NG=F",
    "NQ=F",
    "OJ=F",
    "PA=F",
    "PL=F",
    "RB=F",
    "RTY=F",
    "SB=F",
    "SI=F",
    "SIL=F",
    "YM=F",
    "ZB=F",
    "ZC=F",
    "ZF=F",
    "ZL=F",
    "ZM=F",
    "ZN=F",
    "ZO=F",
    "ZR=F",
    "ZS=F",
    "ZT=F",
    "BZ=F",
    "B0=F",
    "EURUSD=X",
    "JPY=X",
    "GBPUSD=X",
    "AUDUSD=X",
    "NZDUSD=X",
    "EURJPY=X",
    "GBPJPY=X",
    "EURGBP=X",
    "EURCAD=X",
    "EURSEK=X",
    "EURCHF=X",
    "EURHUF=X",
    "EURJPY=X",
    "CNY=X",
    "HKD=X",
    "SGD=X",
    "INR=X",
    "MXN=X",
    "PHP=X",
    "IDR=X",
    "THB=X",
    "MYR=X",
    "ZAR=X",
    "RUB=X",
    "^GSPC",
    "^DJI",
    "^IXIC",
    "^NYA",
    "^XAX",
    "^BUK100P",
    "^RUT",
    "^VIX",
    "^FTSE",
    "^GDAXI",
    "^FCHI",
    "^STOXX50E",
    "^N100",
    "^BFX",
    "IMOEX.ME",
    "^N225",
    "^HSI",
    "000001.SS",
    "399001.SZ",
    "^STI",
    "^AXJO",
    "^AORD",
    "^BSESN",
    "^JKSE",
    "^KLSE",
    "^NZ50",
    "^KS11",
    "^TWII",
    "^GSPTSE",
    "^BVSP",
    "^MXX",
    "^IPSA",
    "^MERV",
    "^TA125.TA",
    "^CASE30",
    "^JN0U.JO",
]

OTHER_TICKERS = [
    "ES=F",
    "YM=F",
    "NQ=F",
    "RTY=F",
    "ZB=F",
    "ZN=F",
    "ZF=F",
    "ZT=F",
    "GC=F",
    "MGC=F",
    "SI=F",
    "SIL=F",
    "PL=F",
    "HG=F",
    "PA=F",
    "CL=F",
    "HO=F",
    "NG=F",
    "RB=F",
    "BZ=F",
    "B0=F",
    "ZC=F",
    "ZO=F",
    "KE=F",
    "ZR=F",
    "ZM=F",
    "ZL=F",
    "ZS=F",
    "GF=F",
    "HE=F",
    "LE=F",
    "CC=F",
    "KC=F",
    "CT=F",
    "LBS=F",
    "OJ=F",
    "SB=F",
]


PINNACLE_DATA_FOLDER = "/nfs/data/files/DAILY/PINNACLE/CLCDATA/"
PINNACLE_DATA_CUT = "RAD"

PINNACLE_ASSETS = [
    "AN",
    "BN",
    "CA",
    "CC",
    "CN",
    "DA",
    "DT",
    "DX",
    "EN",
    "ER",
    "ES",
    "FB",
    "FN",
    "GI",
    "JN",
    "JO",
    "KC",
    "KW",
    "LB",
    "LX",
    "MD",
    "MP",
    "NK",
    "NR",
    "SB",
    "SC",
    "SN",
    "SP",
    "TY",
    "UB",
    "US",
    "XU",
    "XX",
    "YM",
    "ZA",
    "ZC",
    "ZF",
    "ZG",
    "ZH",
    "ZI",
    "ZK",
    "ZL",
    "ZN",
    "ZO",
    "ZP",
    "ZR",
    "ZT",
    "ZU",
    "ZW",
    "ZZ",
]

# TODO get rid of the ones not used get
PINNACLE_ASSET_CLASS_MAPPING = {
    "TY": "FI",
    "US": "FI",
    "FB": "FI",
    "UB": "FI",
    "DT": "FI",
    "ZA": "CM",
    "ZC": "CM",
    "ZG": "CM",
    "ZL": "CM",
    "ZW": "CM",
    "ZI": "CM",
    "ZP": "CM",
    "ZR": "CM",
    "ZZ": "CM",
    "KW": "CM",
    "ZT": "CM",
    "ZF": "CM",
    "ZK": "CM",
    "GI": "CM",
    "ZO": "CM",
    "ZH": "CM",
    "NR": "CM",
    "ZN": "CM",
    "ZU": "CM",
    "LB": "CM",
    "JO": "CM",
    "KC": "CM",
    "CC": "CM",
    "SB": "CM",
    "DA": "CM",
    "NK": "FX",
    "DX": "FX",
    "AN": "FX",
    "BN": "FX",
    "SN": "FX",
    "JN": "FX",
    "FN": "FX",
    "CN": "FX",
    "MP": "FX",
    "ER": "EQ",
    "XX": "EQ",
    "YM": "EQ",
    "ES": "EQ",
    "EN": "EQ",
    "SC": "EQ",
    "SP": "EQ",
    "MD": "EQ",
    "CA": "EQ",
    "XU": "EQ",
    "LX": "EQ",
    "AD": "FX",
    "AP": "FI",
    "AX": "EQ",
    "BC": "CM",
    "BG": "CM",
    "BO": "CM",
    "CB": "FX",
    "CL": "CM",
    "CT": "CM",
    "C_": "CM",
    "FA": "FI",
    "FC": "CM",
    "FX": "FX",
    "GC": "CM",
    "GS": "FI",
    "HG": "CM",
    "HO": "CM",
    "HS": "EQ",
    "LC": "CM",
    "LH": "CM",
    "MW": "CM",
    "NG": "CM",
    "O_": "CM",
    "PA": "CM",
    "PL": "CM",
    "RB": "CM",
    "SF": "FX",
    "SI": "CM",
    "SM": "CM",
    "S_": "CM",
    "TA": "FI",
    "TD": "FI",
    "TU": "FI",
    "UA": "FI",
    "W_": "CM",
    "ZB": "CM",
    "ZM": "CM",
    "ZS": "CM",
}