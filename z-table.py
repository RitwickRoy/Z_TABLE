# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:44:48 2021

@author: Ritwick
"""

#######################################################################
# This code reproduces the Z-table functionality
# If the Z-Value is input the code returns the cumulative probability
# If the cummulative probability is input the code returns the Z-value
#######################################################################


import math


def norm(z):
    val_std_norm = (1.0/math.sqrt(2*math.pi))*math.exp(-(z*z)/2.0)
    return val_std_norm

def Num_integrate(z_end):
    h = 0.0001
    z_start = -11.0
    z_int = z_end - z_start
    n = int(z_int/ h)
    sum = 0.5*norm(z_start)
    z = z_start
    for i in range(n):
        z = z + h
        sum = sum + norm(z)
    sum = sum + 0.5*norm(z_end)
    return sum*h

def p_func(Z,prob):
    val = Num_integrate(Z) - prob
    return val


def find_root(prob):
    Z_L = -10.0
    Z_H = 10.0
    V_L = p_func(Z_L,prob)
    V_H = p_func(Z_H,prob)
    tol = 0.00000001
    diff = Z_H - Z_L
    while diff > tol:
        Z_M = 0.5*(Z_H + Z_L)
        V_M = p_func(Z_M,prob)
        if V_M > 0.0:
            Z_H = Z_M
        else:
            Z_L = Z_M
        diff = Z_H - Z_L
    return Z_M

print("Standard normal distribution")
u_str1 = input('for cummulative probability enter 1 | for Z-value enter 2   :')
choice = int(u_str1)

if(choice == 1):
    u_str = input('input the value of Z:  ')
    z_end = float(u_str)
    print("cummulative probability:", Num_integrate(z_end))
elif(choice == 2):
    u_str = input('input the cummulative probability:  ')
    prob = float(u_str)
    print('Z-Value:',find_root(prob))