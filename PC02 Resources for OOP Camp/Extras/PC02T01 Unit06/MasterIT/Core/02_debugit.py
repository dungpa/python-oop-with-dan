# Fix the errors in this program
# - It defines a 'Box' class
#   = This class contains a constructor with two parameters and declares instance variables for those parameters
# - It then instantiates a Box object
import random


class Box:
    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper

    class open () self
        return random.randint(self.lower, self.upper)


my_box = Box(0, 100)
