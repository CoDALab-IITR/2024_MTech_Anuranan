Calculating SPI:
done on r-studio.
install.packages(SPEI)
library(SPEI)
setwd("Directory") # give directory
Loc<-read.csv("file_name.csv", header=TRUE) # replace with file location
spi6<-spi(Loc$PCRP,6) # decides the SPEI value is calculated for how many months.
vals<-spi6$fitted
Loc$spi6 = vals
write.csv(Loc,"file_name.csv") # replace with store file location