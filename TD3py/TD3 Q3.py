#
# TD 3 "Sciences du Climat" - Question 3
# équilibre : calcul direct
#
import numpy as np

#les paramètres
swA=67
swS=168
LH=78
SH=24
eta=0.9
sigma=5.67e-8

#système d'equation linéaire en xa = sigma Ta^4 et xs = sigma Ts^4
#  0 == Ca dTa/dt = swa + ...
#  0 == Cs dTs/dt = sws + ...

#On résoud l'équation matricielle a.x = b

#############  à compléter   #########
a=np.array([[#...,...],[...,...]])
b=np.array([#...,...])
######################################

x = np.linalg.solve(a, b)

print( "sigmaT4 = ",x )
print( "T = ",pow(x/sigma,0.25) )
print( "T celcius = ",pow(x/sigma,0.25) - 273.15 )

