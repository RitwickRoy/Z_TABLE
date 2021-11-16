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

#
#  Evaluate Standard normal distribution
#
def norm(z):
    val_std_norm = (1.0/math.sqrt(2*math.pi))*math.exp(-(z*z)/2.0)
    return val_std_norm
#
#  Numerically integrate the normal distribution between
#  lower limit (-ve infinity) and the specified z-value using trapezoidal rule.
#  The numerical lower limit is set to -15.0. The interval size is 0.0001.
#  The lower limit can be increased without compromising accuracy.
#
def Num_integrate(z_end):
    h = 0.0001
    z_start = -15.0
    z_int = z_end - z_start
    n = int(z_int/ h)
    sum = 0.5*norm(z_start)
    z = z_start
    for i in range(n):
        z = z + h
        sum = sum + norm(z)
    sum = sum + 0.5*norm(z_end)
    return sum*h
#
#  The integral of the standard normal distribution is a monotonically
#  increase smooth function. To find the z-value given the cumulative probability,
#  we need to find the root of the equation:
#  integral[standard normal distribution] - cumulative probabilty = 0
#
def p_func(Z,prob):
    val = Num_integrate(Z) - prob
    return val
#
#  Find the root of the above function using bisection technique.
#  The starting lower and upper limits for Z are set to -10 and 10
#  respectively. The tolerance for convergence of the root finder
#  is set to a small number.

def find_root(prob):
    Z_L = -10.0
    Z_H = 10.0
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

print()
print("### Standard normal distribution ###")
u_str1 = input('for cummulative probability enter 1 | for Z-value enter 2   :')
choice = int(u_str1)

if(choice == 1):
    u_str = input('input the value of Z:  ')
    z_end = float(u_str)
    print("cummulative probability: %.5f" % Num_integrate(z_end))
elif(choice == 2):
    u_str = input('input the cummulative probability:  ')
    prob = float(u_str)
    print('Z-Value: %.3f' % find_root(prob))