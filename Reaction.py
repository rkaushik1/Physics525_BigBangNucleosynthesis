import numpy as np

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
        left_species = [ specie for specie in species if self.left_contain(specie.name) ]
        right_species = [ specie for specie in species if self.right_contain(specie.name) ]
        
        # Use parameters to calculate rates from functions
        forward_rate = self.forward(temp, rho)
        backward_rate = self.backward(temp, rho)
        print(forward_rate, backward_rate, name, self.reaction_number)
        
        # Use rates to calculate contributions to dX/dt
        forward_dXdt = np.product([specie.abundance/specie.mass for specie in left_species]) * forward_rate
        backward_dXdt = np.product([specie.abundance/specie.mass for specie in right_species]) * backward_rate
        print(forward_rate, backward_rate, forward_dXdt, backward_dXdt, name, self.reaction_number)
        print('left', [specie.abundance/specie.mass for specie in left_species], 'right', [specie.abundance/specie.mass for specie in right_species])

        if self.left_contain(name):
            print('left', (backward_dXdt - forward_dXdt) * self.left.count(name))
            print()
            return (backward_dXdt - forward_dXdt) * self.left.count(name)
        elif self.right_contain(name):
            print('right', (forward_dXdt - backward_dXdt) * self.right.count(name))
            print()
            return (forward_dXdt - backward_dXdt) * self.right.count(name)
        else:
            raise ValueError('Species', name, 'is not found in reaction', self) 
    
