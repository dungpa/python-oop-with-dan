# Edit the string dunder function
# - include a docstring explaining what the function does
# - return a neatly formatted string using the unit/amount instance variables
#   = For example, £2.3
# Instantiate a Currency object with:
# - A unit of £
# - An amount of 12.45
# Output this object to test your string dunder function
class Currency:
    def __init__(self, unit: str, amount: float):
        self.unit = unit
        self.amount = amount

    def __str__(self) -> str:
        pass
