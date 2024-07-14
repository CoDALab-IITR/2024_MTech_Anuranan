Calculating RDI:
done on r-studio.
install.packages(SPEI)
install.packages(dplyr)
library(SPEI)
library(dplyr)
setwd("Directory") # give directory
Loc<-read.csv("file_name.csv", header=TRUE)
Loc$PET<-hargreaves(Tmin = Loc$tmin,Tmax = Loc$tmax,lat = latitude) # give latitude value
Loc_alpha<-Loc %>% group_by(Year) %>% summarise(Precipitation = sum(PCRP),PET = sum(PET)) # calculate sum of pcrp, pet
Loc_alpha<-mutate(Loc_alpha, alpha = Precipitation / PET) # calculate alpha
alpha_mean<-mean(Loc_alpha$alpha) # calculate arithmetic mean of alpha
Loc_alpha$RDIn<-Loc_alpha$alpha/alpha_mean # calculate normalised RDI
alpha_sd<-sd(Loc_alpha$alpha) # calculate standardized deviation of alpha
alpha_ln<-log(Loc_alpha$alpha) # calculate natural log of alpha
Loc_alpha$RDIst<-(alpha_ln - alpha_mean) / alpha_sd # calculate standardized RDI
write.csv(Loc_alpha,"file_name.csv") # replace with store file location