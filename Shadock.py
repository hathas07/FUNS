#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:18:29 2019

@author: drira
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import null_space


def stationnaire (P):
    
    #On cherche le noyau
    N = (null_space(np.eye(len(P))-np.transpose(P)))
    
    #Normalisation
    Somme = 0
    for j in range(len(P)):
        Somme+=N[j]
        
    return N/Somme

def stochastique (P):
    for x in range (len(P)):
        Somme = 0
        for y in range(len(P)):
           Somme+=P[x,y]
        if Somme != 1:
           return False
    return True

def puits (P,i):
    if P[i,i]==1:
        return True
    else:
        return False



def simulation(P, pi0, t0, tf):
# Simulation numerique d'une chaine de Markov en temps discret
# P	    : matrice de transition
# pi0	: vecteur stochastique initial (a l'instant t0)
# t0	: instant initial (debut de la simulation)
# tf	: instant final
# pi	: matrice des valeurs successives du vecteur stochastique
# t     : liste des instants (t0 <= t <= tf)  

    t = np.arange(t0,tf+1)
# controles
    if P.shape[0] != P.shape[1] | P.shape[0] != pi0.len :  
        print('dimensions incorrectes')
    elif not stochastique (P):
        print ('la matrice n est pas stochastique')

# evolution du vecteur stochastique
    pi = np.array(np.zeros((len(t),P.shape[1])))
    pi[0] = pi0  
    for i in range(1,len(t)):
        pi[i] = pi[i-1].dot(P)
    plt.plot(t,pi)
    return t,pi


def Diagonalisation (P):
    
   if np.linalg.det(P) == 0:
       print("La matrice n'est pas invertible")
       
       return False
   else:
       D, V = np.linalg.eig(P)
       
       return np.diag(D), V

def Puissance (P, n):
    D, V = Diagonalisation(P)
    D = D**n
    P = V.dot(D).dot(np.linalg.inv(V))
    return P

def Convergence (P):
    D, V = Diagonalisation(P)
    
    A = D[0][0]
    B = 0
    for i in range(len(D)):
        if D[i][i] > A:
            B = A
            A = D[i][i]
        elif D[i][i] < A and D[i][i] > B:
            B = D[i][i]
    
    return B
    
# liste d'exemples de chaines de Markov
def Exemple(n):
   if n==1: 
       print('shadock')
       P = np.array([ [5/6 , 1/12, 1/12],  [ 1/4, 1/2, 1/4] , [ 1/4, 0, 3/4] ])
       pi0 = [1 , 0, 0]
   elif n==2:
       print('imprimante')
       P = np.array([ [.2, .8, 0],  [ .04, .95, .01] , [ .3, 0, .7] ])
       pi0 = [1 , 0, 0]
       
       #  ajouter d'autres exemples
       
   return P,pi0
