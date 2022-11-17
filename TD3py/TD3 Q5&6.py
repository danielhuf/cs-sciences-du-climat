#
# TD 3 "Sciences du Climat" - Questions 5 et 6
# équilibre : intégration temporelle
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#les paramètres
swA=67
swS=168
LH=78
SH=24
eta=0.9
sigma=5.67e-8

#les capacités calorifiques
cA=13e+6
cS=210e+6

#les nuages (Question 6)
DeltaHcld = 0
DeltaLcld = 0

co2 = 560

############ on selection la question ICI #######
question = '6'
#################################################

def ew(T):
    return 6.112*np.exp(17.62*(T-273.15)/(243.12+T-273.15))

# le système d'équations différentielles
def f(t,y):
    # on renomme les 2 variables
    TA = y[0]
    TS = y[1]
    swS = 168
    if question=='5a':       # on modifie le CO2, sans rétroaction
#############  à compléter   #########
        eta = #....
######################################
    elif question=='5b':     # on modifie le CO2 et la vapeur d'eau
        #############  à compléter   #########
        eta = #....
######################################
    elif question=='5c':     # on modifie le CO2, la vapeur d'eau et l'albédo de surface
#############  à compléter   #########
        eta = #....
        alphaS = #....
        swS = #....
######################################
    elif question=='6':
        co2 = 280
        DeltaLcld = 0.1  # à modifier = 0 ou 0.1
        DeltaHcld = 0.   # à modifier = 0 ou 0.1
        eta = 0.9+0.03*(np.sqrt(co2/280)-1)+0.05*(ew(TS)/ew(288) - 1)+0.1*DeltaHcld + 0.1*DeltaLcld
        alphaA = 77.0/342 + 0.02*DeltaHcld + 0.125*DeltaLcld
        swS = (168.0/198)*342*(1-67.0/342-alphaA)
    else:
        eta = 0.9
    
    sigmaTA4 = sigma*TA**4
    sigmaTS4 = sigma*TS**4
    # on en déduit les équations
    #############  à compléter .... copier-coller de la question 3  #########
    dTAdt = #....
    dTSdt = #....
    ######################################
    return [dTAdt, dTSdt]

# la condition initiale: par exemple 273 K
y0 = [273,273]
# la durée de l'intégration en secondes. Ici 20 ans.
tfinal = (60*60*24)*365*20

sol = solve_ivp(f, [0, tfinal], y0, rtol = 1e-7)
yfinal = sol.y[:,-1]
TAfinal = yfinal[0]
TSfinal = yfinal[1]
print( "TA, TS = ",TAfinal, ",", TSfinal )

plt.plot(sol.t,sol.y[0])
plt.plot(sol.t,sol.y[1])
plt.show()