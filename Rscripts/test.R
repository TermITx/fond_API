library(data.table)
print("Pozvana R skripta...")
Sys.sleep(2)
dt_3 <- data.table("A" = rnorm(5), 
                   "B" = rpois(5, 5), 
                   "C" = rbinom(5, 2, .6))
fwrite(dt_3, "test_folder/test_R.csv")
Sys.sleep(2)