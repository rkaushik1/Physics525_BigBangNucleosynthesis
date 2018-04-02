class Species:
    
    def __init__(self, name, initial_abundance, reactions):
        # Name of this species ie proton, nuetron
        self.name = name

        self.abundance = initial_abundance

        # List of reactions this species is a part of                                                                                                                                                             
        # Maybe an index maybe a reference
        self.reactions = [reaction for reaction in reactions if reaction.contains(name) ]

