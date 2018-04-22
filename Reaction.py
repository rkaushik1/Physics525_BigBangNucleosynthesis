import numpy as np

# Calculate rho from T               
def rho_b(T9):
    h = .673 # Hubble Constant
    rho_crit0 = 1.87847e-29*h**(2) #g cm^(-3)
    omega_b0 = 0.02207*h**(-2)
    T0 = 2.7255e-9 #Kelvin*10^9 units 
    
    return omega_b0*rho_crit0*(T9/T0)**3

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
    def calculate_dXdt_contribution(self, specie_0, time, species):
        temp = 10.4/np.sqrt(time)
        rho = rho_b(temp)

        # Select only the species we need for calculating this reaction
        left_species = [ specie for specie in species if self.left_contain(specie.name) ]
        right_species = [ specie for specie in species if self.right_contain(specie.name) ]
        
        # Use parameters to calculate rates from functions
        forward_rate = self.forward(temp, rho)
        backward_rate = self.backward(temp, rho)
        #print(forward_rate, backward_rate, specie_0.name, self.reaction_number)
        
        # Use rates to calculate contributions to dX/dt
        forward_dXdt = np.product([specie.abundance/specie.mass for specie in left_species]) * forward_rate * specie_0.mass
        backward_dXdt = np.product([specie.abundance/specie.mass for specie in right_species]) * backward_rate * specie_0.mass
        #print(forward_rate, backward_rate, forward_dXdt, backward_dXdt, specie_0.name, self.reaction_number)
        #print('left', [specie.abundance/specie.mass for specie in left_species], 'right', [specie.abundance/specie.mass for specie in right_species])

        if self.left_contain(specie_0.name):
            #print('left', (backward_dXdt - forward_dXdt) * self.left.count(specie_0.name))
            #print()
            return (backward_dXdt - forward_dXdt) * self.left.count(specie_0.name)
        elif self.right_contain(specie_0.name):
            #print('right', (forward_dXdt - backward_dXdt) * self.right.count(specie_0.name))
            #print()
            return (forward_dXdt - backward_dXdt) * self.right.count(specie_0.name)
        else:
            raise ValueError('Species', specie_0.name, 'is not found in reaction', self) 
    
