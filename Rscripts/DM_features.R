#ODAVDE
library(finfeatures)
library(data.table)
names <- c('KO','MRK','MSFT','NYCB','PCG','RF','SPY','SWN','T','TELL','WBD','WU','XOM')
a<-0.0
print("Krecemo")
for (name in names){
  input_file <- read.csv(file = paste(c('model/data/quandl',name,'.csv'),collapse=""))
  input_file <- tail(input_file,n=300)
  input_file[6] <- NULL
  colnames(input_file) <- c('datetime','open','high','low','close','volume')
  input_file['symbol'] = name
  ohlcv <- Ohlcv$new(input_file, date_col = "datetime")
  num_rows <- nrow(ohlcv$X)
  
  RollingGpdInit = OhlcvFeatures$new(windows = 126, quantile_divergence_window =  c(50, 100))
  ohlcv_features = RollingGpdInit$get_ohlcv_features(ohlcv)
  
  backcusum <- RollingBackcusum$new(
    windows = 126,
    workers = 2L,
    at = 1:nrow(ohlcv$X),
    lag = 1L,
    na_pad = TRUE,
    simplify = FALSE
  )
  backcusum_features = backcusum$get_rolling_features(ohlcv)
  head(backcusum_features)
  
  exuber <- RollingExuber$new(
    windows = 126,
    workers = 2L,
    at = 1:nrow(ohlcv$X),
    lag = 1L,
    na_pad = TRUE,
    simplify = FALSE,
    exuber_lag = 2L
  )
  exuber_features = exuber$get_rolling_features(ohlcv)
  
  RollingForecatsInstance = RollingForecats$new(windows = 126,
                                                workers = 2L,
                                                lag = 1L,
                                                at = 1:nrow(ohlcv$X),
                                                na_pad = TRUE,
                                                simplify = FALSE,
                                                forecast_type = "autoarima",
                                                h = 22)
  forcats_features = RollingForecatsInstance$get_rolling_features(ohlcv)
  
  
  features <- Reduce(function(x, y) merge(x, y, by = c("symbol", "date"), all.x = TRUE, all.y = FALSE),
                     list(ohlcv_features, backcusum_features, exuber_features,forcats_features))
  
  appendFile <- read.csv(file = paste(c('model/data/m_features/features_',name,'.csv'),collapse=""))
  rbind(appendFile,tail(features,n=1))
  write.csv(features,paste(c('model/data/m_features/features_',name,'.csv'),collapse=""), row.names = FALSE)
  
  print(paste(c('Završen ',name),collapse=""))
  a<-a+1
  posto <- a/length(names)*100
  print(paste(c(posto,'%'),collapse=""))
}