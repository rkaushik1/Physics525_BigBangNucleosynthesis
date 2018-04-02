class Reaction:

    def __init__(self, lhs, rhs, rates):
        # Define the left and right side of the reaction
        self.left = lhs
        self.right = rhs

        # There will be two rates (forward and backward) 
        # Probably need to ba a lambda/functor as it depends on abundance
        self.forward, self.backward = rates

    def contains(name):
        return name in self.left or name in self.right
