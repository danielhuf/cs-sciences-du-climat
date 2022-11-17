#
# TD 1 "Sciences du Climat" - Question 2
#
from scipy.integrate import solve_ivp
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
# le système d'équations différentielles
#
def f(t,y):
# on renomme les variables pronostiques et on en déduit les variables diagnostiques
    T1 = y[0]
    T2 = y[1]
    S1 = y[2]
#############  à compléter   #########
    S2 = ##...
    m  = ##...
# et les équations d'évolution
    dT1dt = ##...
    dT2dt = ##...
    dS1dt = ##...
#######################################
    return [dT1dt, dT2dt, dS1dt]

#
# la condition initiale: 10°C, 10°C et 35‰
#
y0 = [10,10,35]
tfinal = 1000

#
# on intègre l'équation différentielle y' = f(y,t)
#
sol = solve_ivp(f, [0, tfinal], y0, rtol = 1e-7)

#
# on s'intéresse à la valeur finale (supposée être "l'équilibre")
#
yfinal = sol.y[:,-1]
T1final = yfinal[0]
T2final = yfinal[1]
S1final = yfinal[2]
#############  à compléter   #########
S2final = ##...
mfinal  = ##...
#######################################

print("m = ",mfinal)
print("F = ",(S1r - S1final)/tau)

#
# on peut aussi regarder l'évolution temporelle de la circulation m
#
def mfunc(y):
# on renomme les variables pronostiques et on en déduit les variables diagnostiques
    T1 = y[0]
    T2 = y[1]
    S1 = y[2]
#############  à compléter   #########
    S2 = ##...
    m  = ##...
#######################################
    return m

ym = mfunc(sol.y)

plt.plot(sol.t,ym)
plt.show()
