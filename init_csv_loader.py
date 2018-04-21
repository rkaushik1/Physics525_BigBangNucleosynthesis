#Script for populating initial abundencies CSV file
#Values for reactions from Wagoner et al. 1975
#Values for today from Particle Data Group

import numpy as np

def rho_b(T9):
    h = .673 #Hubble Constant
    rho_crit0 = 1.87847e-29*h**2 #g cm^(-3)
    omega_b0 = 0.02207*h**(-2)
    T0 = 2.7255e-9 #Kelvin*10^9 units
    return omega_b0*rho_crit0*(T9/T0)**3


def get_initial_abund(comp1_abund, comp2_abund, Q, T9,):
    '''Returns initial abundence of element e based of reaction comp1 + comp2 = e + photon
       with heat released Q. '''
    return SCALE*comp1_abund*comp2_abund*rho_b(T9)*T9**(-3/2)*np.exp(Q/(kb*T9))


kb = 8.6173303e-2 #MeV/K*10^9
SCALE = 1e-10 # From Wagoner
    