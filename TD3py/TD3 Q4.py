#
# TD 3 "Sciences du Climat" - Question 4
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

# le système d'équations différentielles
def f(t,y):
    # on renomme les 2 variables
    TA = y[0]
    TS = y[1]
    sigmaTA4 = sigma*TA**4
    sigmaTS4 = sigma*TS**4
    # on en déduit les équations
#############  à compléter   #########
    dTAdt = #...
    dTSdt = #...
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