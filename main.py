import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Rates
from Reaction import Reaction
from Species import Species
from SpeciesEnum import SpeciesEnum

# Given all species and all reactions
# This function should  walk through one iteration of rk4
def step_rk4(species, reactions, h, t):
    k1 = np.array([ sum([ reaction.calculate_dXdt_contribution(specie, t, species) for reaction in specie.reactions ]) for specie in species ])
    
    # Create intermediate species to have *updated* abundances
    species2 = [ species[i].create_intermediate(k1[i]/2, h) for i in range(len(species)) ]
    k2 = np.array([ sum([ reaction.calculate_dXdt_contribution(specie, t + h/2, species2) for reaction in specie.reactions ]) for specie in species2 ])
    #print('Species2', end=" ")
    #for _ in list(species2):
    #    print(_, end=" ")
    #print()

    species3 = [ species2[i].create_intermediate(k2[i]/2, h) for i in range(len(species2)) ]
    k3 = np.array([ sum([ reaction.calculate_dXdt_contribution(specie, t + h/2, species3) for reaction in specie.reactions ]) for specie in species3 ])
    #print('Species3', end=' ')
    #for _ in list(species3):
    #    print(_, end=" ")
    #print()

    species4 = [ species3[i].create_intermediate(k3[i], h) for i in range(len(species3)) ]
    k4 = np.array([ sum([ reaction.calculate_dXdt_contribution(specie, t + h, species4) for reaction in specie.reactions ]) for specie in species4 ])
    #print('Species4', end=' ')
    #for _ in list(species4):
    #    print(_, end=" ")
    #print()

    #print(k1, k2, k3, k4)

    for i in range(len(species)):
        #print(i, (h/6)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i]))
        species[i].update_abundance((h/6)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i]))
        #species[i].update_abundance((h/2)*(k1[i] + k2[i]))
        #species = [species[i].update_abundance(species[i].abundance + (h/6)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])) for i in range(len(species))]
    #print('Species', end=' ')
    #for _ in list(species):
    #    print(_, end=" ")
    #print()

    return

def jacobian(species, reactions):
    jacob = np.zeros((7,7))

    for i in range(len(species)):
        for j in range(len(species)):
            species_f = species[i]
            species_g = species[j]
            
            for reaction in species_f.reactions:
                if reaction.contain(species_g.name):
                    return 0
        
    

def main():
    # my code here
    
    # Load all the meta data from ReactionData.csv
    # loads which species are in which reactions
    reactionData = pd.read_csv('ReactionData.csv')
    reactionData.lhs = [[ SpeciesEnum[s] for s in lh.split(';')] for lh in reactionData.lhs]
    reactionData.rhs = [[ SpeciesEnum[s] for s in rh.split(';')] for rh in reactionData.rhs]
    
    # Use the Reaction meta data and all the rate equations in Rates.py to create the reaction objects
    reactions = [Reaction(i+1, reactionData.ix[i].lhs, reactionData.ix[i].rhs, 
                          rates=(Rates.ALL_RATES['forward_'+str(i+1)], Rates.ALL_RATES['backward_'+str(i+1)]) 
                          ) for i in range(len(reactionData))]

    # Load species meta data for initial conditions
    speciesData = pd.read_csv('SpeciesData.csv')
    species = {SpeciesEnum[speciesData.ix[i]['Name']]:
               Species(SpeciesEnum[speciesData.ix[i]['Name']], speciesData.ix[i]['Mass Number'], speciesData.ix[i]['Initial Abundance'], reactions)
                       for i in range(len(speciesData))}

    #print(reactions)
    #print(reactionData)
    for _ in list(species.values()):
        print(_, end=" ")
    print()
    
    T_0 = 60
    t_0 = (10.4 / T_0)**2

    T_end = 10
    t_end = (10.4 / T_end)**2

    h = 1e-3
    #t_end = t_0 + 1000*h
    
    for i in np.arange(t_0, t_end, h):
        print('Current Time:', i, 'of', t_end, '\r', end='')
        step_rk4(list(species.values()), reactions, h, t_0)
        
    print('Starting at', t_0, 'to', t_end, 'with step',h)

    for _ in list(species.values()):
        print(_, end=" ")
    print(sum([specie.abundance for specie in list(species.values()) ]))
    print()

if __name__ == "__main__":
    main()
