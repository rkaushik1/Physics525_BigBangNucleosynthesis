import matplotlib.pyplot as plt
import numpy as np

# Given all species and all reactions
# This function should  walk through one iteration of rk4
def step_rk4(species, reactions, h, T, rho):
    k1 = np.array([ sum([ reaction.calculate_dXdt_contribution(specie.name, T, rho, species) for reaction in specie.reactions ]) for specie in species ])

    # Create intermediate species to have *updated* abundances
    rho2 = rho
    species2 = [ species[i].create_intermediate(k1[i]/2, h) for i in range(len(species)) ]
    k2 = np.array([ sum([ reaction.calculate_dXdt_contribution(specie.name, T + h/2, rho2, species2) for reaction in specie.reactions ]) for specie in species2 ])
    
    rho3 = rho
    species3 = [ species2[i].create_intermediate(k2[i]/2, h) for i in range(len(species2)) ]
    k3 = np.array([ sum([ reaction.calculate_dXdt_contribution(specie.name, T + h/2, rho3, species3) for reaction in specie.reactions ]) for specie in species3 ])
    
    rho4 = rho
    species4 = [ species3[i].create_intermediate(k3[i], h) for i in range(len(species3)) ]
    k4 = np.array([ sum([ reaction.calculate_dXdt_contribution(specie.name, T + h, rho4, species4) for reaction in specie.reactions ]) for specie in species4 ])

    species = [species[i].update(species[i].abundance + (h/6)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])) for i in range(len(species))]
    
    return

def main():
    # my code here

if __name__ == "__main__":
    main()
