require(tgcd)

temps <- read.csv("/home/ferna96/Documents/BecaIB/code/tld_curves/temps.csv")
tld_data <- read.csv("/home/ferna96/Documents/BecaIB/code/tld_curves/rest_raw_16-02.csv")
tld_data <- tld_data[,7]

tgcd(cbind(temps, tld_data),, npeak=5, model="wo", nstart=9, 
    outfile = '/home/ferna96/Documents/BecaIB/code/peaks_curves/19-02/tld_7') 

head(dd1$comp.sig)
dd1$pars
dd1$sp
dd1$FOM

temps <- read.csv("/home/ferna96/Documents/BecaIB/code/tld_curves/temps.csv")

tld_data <- read.csv("/home/ferna96/Documents/BecaIB/code/tld_curves/rest_raw_26-02.csv")
tld_data <- tld_data[,15]
#four peaks
knPars <-
cbind(c(2, 4.8, 7.3, 0.27), # Im
c(1.8, 2, 2.2, 1.5), # E
c( 530, 590, 605, 699), # Tm
c( 0.1, 0.1, 0.1, 0.1)) # R
tgcd(cbind(temps, tld_data),npeak=4, model="wo", inisPAR=knPars, edit.inis = FALSE,
    outfile = '/home/ferna96/Documents/BecaIB/code/peaks_curves/26-02/tld_15') 

#five peaks
'''
knPars <-
cbind(c(1.65, 2, 4.8, 7.3, 0.27), # Im
c(1.64, 1.8, 2, 2.2, 1.5), # E
c(500, 530, 590, 605, 699), # Tm
c(0.1, 0.1, 0.1, 0.1, 0.1)) # R
'''
