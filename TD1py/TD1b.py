#
# TD 1 "Sciences du Climat" - Question 3
# pour ce 2nd problème, on explore l'influence de F et de la condition initiale sur S1
#
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#
# les paramètres
#
Smoy = 35.0
mu = 6
delta = 8
tau = 10
Vol = 300
T1r = 5
T2r = 20
S1r = 34.3

#
# le système d'équations différentielles, avec F en paramètre
#
def f2(t,y,F):
# on renomme les variables pronostiques et on en déduit les variables diagnostiques
    T1 = y[0]
    T2 = y[1]
    S1 = y[2]
#############  à compléter   #########
    S2 = #...
    m  = #...
# et les équations d'évolution
    dT1dt = #...
    dT2dt = #...
    dS1dt = #...
#######################################
    return [dT1dt, dT2dt, dS1dt]


#
# on s'intéresse à la circulation océanique m final en fonction de F et de la condition initiale sur S1
#
def mfinal2(S1i,F):
    tfinal = 1000
    sol2 = solve_ivp(lambda t, y: f2(t,y,F), [0, tfinal], [10,10,S1i], rtol = 1e-7)
    
    #plt.plot(sol2.t,mfunc(sol2.y))
    #plt.show()

    yfinal = sol2.y[:,-1]
    T1final = yfinal[0]
    T2final = yfinal[1]
    S1final = yfinal[2]
#############  à compléter   #########
    S2final = #...
    mfinal  = #...
#######################################
    return mfinal

#
# ... quelques valeurs de m final en fonction de S1_initial et de F
#
print("35 & -0.032 : ",mfinal2(35,-0.032))
print("35 & -0.031 : ",mfinal2(35,-0.031))
print("34 & -0.031 : ",mfinal2(34,-0.031))


#
# de façon un peu plus systématique, plot la fonction m(F) pour quelques valeus de S1_initial 
#
nrun = 20
xf = np.linspace(0.025,0.035,nrun)   # les valeurs de -F
xm350 = np.array([mfinal2(35,-f) for f in xf])
xm345 = np.array([mfinal2(34.5,-f) for f in xf])
xm340 = np.array([mfinal2(34,-f) for f in xf])

plt.scatter(xf,xm350)
plt.scatter(xf,xm345)
plt.scatter(xf,xm340)
plt.show()
