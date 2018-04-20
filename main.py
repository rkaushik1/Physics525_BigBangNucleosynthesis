import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Rates
from Reaction import Reaction
from Species import Species
from SpeciesEnum import SpeciesEnum

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

    species = [species[i].update_abundance(species[i].abundance + (h/6)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])) for i in range(len(species))]
    
    return

def main():
    # my code here
    reactionData = pd.read_csv('ReactionData.csv')
    reactionData.lhs = [[ SpeciesEnum[s] for s in lh.split(';')] for lh in reactionData.lhs]
    reactionData.rhs = [[ SpeciesEnum[s] for s in lh.split(';')] for lh in reactionData.rhs]

    reactions = [Reaction(i, reactionData.ix[i].lhs, reactionData.ix[i].rhs, 
                          rates=(Rates.ALL_RATES['forward_'+str(i+1)], Rates.ALL_RATES['backward_'+str(i+1)]) 
                          ) for i in range(len(reactionData))]

    speciesData = pd.read_csv('SpeciesData.csv')
    species = {SpeciesEnum[speciesData.ix[i]['Name']]:
               Species(SpeciesEnum[speciesData.ix[i]['Name']], speciesData.ix[i]['Mass Number'], speciesData.ix[i]['Initial Abundance'], reactions)
                       for i in range(len(speciesData))}

    print(reactions)
    print(reactionData)
    print(species)
    
    step_rk4(list(species.values()), reactions, 1, 100, 100)
    print(species)

if __name__ == "__main__":
    main()
