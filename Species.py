class Species:
    
    def __init__(self, name, initial_abundance, reactions):
        # Name of this species ie proton, nuetron
        self.name = name

        self.abundance = initial_abundance

        # List of reactions this species is a part of                                                                                                                                                             
        # Maybe an index maybe a reference
        self.reactions = [reaction for reaction in self.reactions if reaction.contains(name) ]

    # Walk through each reaction this species is included in and update the abundance due to each reaction
    def step(self):
        abundance += sum([ reaction.step(self.name) for reaction in self.reactions ])
