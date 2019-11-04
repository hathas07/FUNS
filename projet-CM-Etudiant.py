#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:47:08 2019

@author: Hassen Drira
"""

from Shadock import Exemple
from Shadock import Diagonalisation
from Shadock import stationnaire
from Shadock import simulation
from Shadock import stochastique
from Shadock import puits
from Shadock import Puissance
from Shadock import Convergence
import numpy as np

#P = np.array([ [5/6 , 1/12, 1/12],  [ 1/4, 1/2, 1/4] , [ 1/4, 0, 3/4] ])
#pi0 = [1 , 0, 0]

num = 1 # num entre 1 et 4
P,pi0 = Exemple(num)
n = 10000

print("\nRegime stationaire :\n",stationnaire(P))
D, V = Diagonalisation(P)
print("\nValeurs Propres :\n",D)

print("\nConvergence :",Convergence (P))

print("\nMatrice à la puissance",n,":\n",Puissance(P,n))

Ouiounon = np.allclose(P,Puissance(P,1),rtol=0.001)
print("\nComparaison entre P et P^1:",Ouiounon)

# Initialement en bonne santé
pi0 = [1 , 0, 0]

print("\nP :\n",P)
print("pi0",pi0)

[t,pi] = simulation(P,pi0,1,20)
print('pi[5]',pi[4])
print('pi[10]',pi[9])
print('pi[20]',pi[19])
print('pi[50]',pi[49])
print('pi[100]',pi[99])

# Initialisation differente
pi0 = [0.4 , 0.2, 0.4]

[t,pi] = simulation(P,pi0,1,100)
print('pi[5]',pi[4])
print('pi[10]',pi[9])
print('pi[20]',pi[19])
print('pi[50]',pi[49])
print('pi[100]',pi[99])

# Initialisation differente
pi0 = [0.1 , 0.4, 0.5]

[t,pi] = simulation(P,pi0,1,100)
print('pi[5]',pi[4])
print('pi[10]',pi[9])
print('pi[20]',pi[19])
print('pi[50]',pi[49])
print('pi[100]',pi[99])

#limite(pi)= [0.6 0.1 0.3]





