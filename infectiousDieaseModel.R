#install.packages("EpiModel)
library("EpiModel")

#calculate equilibrium for DCM
#use ctrl + alt + r to run all

#Kennel
param <- param.dcm(inf.prob= 0.4, inf.prob.g2 = 0.45,  act.rate = 0.7, act.rate.g2 = 0.75,
                   balance = "g1", rec.rate = 1/7, rec.rate.g2 = 1/9)
init <- init.dcm(s.num = 25, i.num = 1, s.num.g2 = 25, i.num.g2 = 1)
control <- control.dcm(type = "SIS", nsteps = 365, verbose = FALSE)
k <- dcm(param,init,control)

init1 <- init.dcm(s.num = 1000, i.num = 1, s.num.g2 = 1000, i.num.g2 = 1)
kb <- dcm(param, init1, control)

#plot graph
#par(mfcol=c(1,2))
plot (kb, main = "Large Model")
plot (k , main = "Kennels")

#calculate equilibirum 
calc_eql(k, nsteps = 365)
