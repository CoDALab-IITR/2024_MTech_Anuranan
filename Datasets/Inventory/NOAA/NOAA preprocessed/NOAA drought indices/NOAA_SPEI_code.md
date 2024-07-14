Calculating SPEI:
done on r-studio.
install.packages(SPEI)
library(SPEI)
setwd("Directory") # give directory
Loc<-read.csv("file_name.csv", header=TRUE) # replace with file location
Loc$PET<-hargreaves(Tmin = Loc$tmin,Tmax = Loc$tmax,lat = latitude) # give latitude value
CWBAL<-Loc$PCRP-Loc$PET
spei6<-spei(CWBAL,6) # decides the SPEI value is calculated for how many months.
vals<-spei6$fitted
Loc$Spei6 = vals
write.csv(Loc,"file_name.csv") # replace with store file location