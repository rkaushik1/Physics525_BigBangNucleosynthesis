class Species:
    
    def __init__(self, name, mass_number, initial_abundance, reactions):
        # Name of this species ie proton, nuetron
        self.name = name

        self.abundance = initial_abundance
        self.mass = mass_number
        
        # List of reactions this species is a part of                                                                                                                                                             
        # Maybe an index maybe a reference
        self.reactions = [reaction for reaction in self.reactions if reaction.contains(name) ]

    # Create a new species object with an updated abundance
    # Useful for intermediate rk4 values
    def create_intermediate(self, k, h):
        return Species(self.name, self.abundance + h*k, self.reactions)

    # Update the value of abundance for this species
    def update_abundance(self, abundance):
        self.abundance = abundance

    '''
    # Walk through each reaction this species is included in and update the abundance due to each reaction
    def step(self, temp, h, species):
        return sum([ reaction.step(self.name, temp, h) for reaction in self.reactions ])
    '''
