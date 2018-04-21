# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:48:40 2018

@author: Kevin
"""
import numpy as np
import math
Mp = 938.272081 #MeV/c^2
Mn = 939.57 #MeV/c^2
c = 299792458
kb = 8.6173303e-2 #MeV/K*10^9
T90 = 60 #K*10^9
print((Mn-Mp)/(kb*T90))
XpXn = np.exp((Mn-Mp)/(kb*T90))
print(XpXn)
Xp = XpXn/(1+XpXn)
Xn = 1/(1 + XpXn)

print(Xp)
print(Xn)