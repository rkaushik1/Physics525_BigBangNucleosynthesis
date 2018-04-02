class Reaction:

    def __init__(self, number, lhs, rhs, rates, species):
        self.reaction_number = number

        # Define the left and right side of the reaction
        self.left = lhs
        self.right = rhs

        # There will be two rates (forward and backward) 
        # Probably need to ba a lambda/functor as it depends on abundance
        self.forward, self.backward = rates

        # Keep a reference to all species needed to calculate rates
        self.species = species

    # Returns true is the species is on the left side of the reaction
    def left_contain(name):
        return name in self.left

    # Returns true if the species is on the right side of the reaction
    def right_contain(name):
        return name in self.right

    # Returns true if the speicies is in this reaction
    def contains(name):
        return self.left_contain(name) or self.right_contain(name)


    # Code stub to calculate the change in abundance of one species due to one step from this reaction
    def step(name, args=None):
        if left_contain(name):
            # TODO:
            # Calculate change in abundance
            return 0
        elif right_contain(name):
            # TODO:
            # Calculate chance in abundance
            return 0
        else:
            raise ValueError('Species', name, 'is not found in reaction', self) 
