# Ask the user for an integer larger than 1
# - The program should instantiate that many number of Triangle objects
#   = Ask the user for the base and height of each Triangle object
#   = After instantiating each Triangle object, output them to test the __str__ dunder function
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return f"The triangle with a base of {self.base} and a height of {self.height} has an area of {(self.base * self.height) / 2}"
