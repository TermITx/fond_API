my_packages <- c("devtools",'stats','graphics','grDevices','utils','datasets','methods','base')
 install_if_missing <- function(p) {
 if(p %in% rownames(installed.packages())==FALSE){
 install.packages(p,repos = "http://cran.us.r-project.org")}
 }
 
invisible(sapply(my_packages, install_if_missing))
library('devtools')
invisible(devtools::install_bitbucket( 'quanttools/QuantTools' ))
invisible(install_github("MislavSag/finfeatures"))