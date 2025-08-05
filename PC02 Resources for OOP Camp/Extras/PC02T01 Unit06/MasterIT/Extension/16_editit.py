# Add the add, subtract, multiply, and divide dunder functions to this class
# - Each one should take another Currency object
# - And perform the correct addition/subtraction/multiplication/division between their amounts
# - It should return a new Currency object with the newly calculated amount
# Add the string dunder function to output the Currency in this format (as an example): $50.04
# Instantiate two Currency objects (any amounts) and output the results of the addition/subtraction/multiplication/division operations
class Currency:
    def __init__(self, unit: str, amount: float):
        self.unit = unit
        self.amount = amount
