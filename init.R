my_packages <- c("devtools")
 install_if_missing <- function(p) {
 if(p %in% rownames(installed.packages())==FALSE){
 install.packages(p)}
 }
 
invisible(sapply(my_packages, install_if_missing))
invisible(devtools::install_bitbucket( 'quanttools/QuantTools' ))
invisible(install_github("MislavSag/finfeatures"))