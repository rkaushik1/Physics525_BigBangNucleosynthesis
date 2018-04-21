#ALL_SPECIES = ['p', 'n', 'D', 'He3', 'T', 'He4', 'Be7', 'Li7', 'B8', 'B10', 'C11', 'C12', 'B11', 'N12', 'N14', 'N13', 
#               'O16', 'O15', 'C13', 'F17', 'N15', 'Ne19', 'Ne20', 'Ne18', 'F19', 'Na21', 'Na22', 'Na20', 'Na21', 'Mg24', 'Mg23',
#               'Mg22', 'Mg25', 'Al25', 'Al24', 'Al26']

from SpeciesEnum import SpeciesEnum
from Reaction import Reaction

class Species:
    
    def __init__(self, name, mass_number, initial_abundance, reactions):
        # Name of this species ie proton, nuetron
        self.name = name

        self.abundance = initial_abundance
        self.mass = mass_number
        
        # List of reactions this species is a part of                                                                                                                                                             
        # Maybe an index maybe a reference
        self.reactions = [reaction for reaction in reactions if reaction.contains(name) ]

    def __str__(self):
        return str(self.name) + ': ' + str(self.abundance)

    # Create a new species object with an updated abundance
    # Useful for intermediate rk4 values
    def create_intermediate(self, k, h):
        return Species(self.name, self.mass, max(0,self.abundance + h*k), self.reactions)

    # Update the value of abundance for this species
    def update_abundance(self, abundance):
        self.abundance = max(0,abundance)
        return

    '''
    # Walk through each reaction this species is included in and update the abundance due to each reaction
    def step(self, temp, h, species):
        return sum([ reaction.step(self.name, temp, h) for reaction in self.reactions ])
    '''

