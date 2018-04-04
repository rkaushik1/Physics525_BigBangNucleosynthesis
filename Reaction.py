class Reaction:

    def __init__(self, number, lhs, rhs, rates):
        self.reaction_number = number

        # Define the left and right side of the reaction
        self.left = lhs
        self.right = rhs

        # There will be two rates (forward and backward) 
        # Probably need to ba a lambda/functor as it depends on abundance
        self.forward, self.backward = rates

        
    # Returns true is the species is on the left side of the reaction
    def left_contain(self, name):
        return name in self.left

    # Returns true if the species is on the right side of the reaction
    def right_contain(self, name):
        return name in self.right

    # Returns true if the speicies is in this reaction
    def contains(self, name):
        return self.left_contain(name) or self.right_contain(name)

    
    # Code stub to calculate the change in abundance of one species due to one step from this reaction
    def calculate_dXdt_contribution(self, name, temp, rho, species):
        # Select only the species we need for calculating this reaction
        left_species = [ specie for specie in species if self.left_contain(specie) ]
        right_species = [ specie for specie in species if self.right_contain(specie) ]
        
        # Use parameters to calculate rates from functions
        forward_rate = forward(temp, rho)
        backward_rate = backward(temp, rho, forward_rate)

        # Use rates to calculate contributions to dX/dt
        forward_dXdt = np.product([specie.abundance/specie.mass for specie in left_species]) * forward_rate
        backward_dXdt = np.product([specie.abundance/specie.mass for specie in right_species]) * backward_rate

        if self.left_contain(name):
            return backward_dXdt - forward_dXdt
        elif self.right_contain(name):
            return forward_dXdt - backward_dXdt
        else:
            raise ValueError('Species', name, 'is not found in reaction', self) 
    
