# Edit this program by defining a child class of 'Shape' called 'Rectangle'
# - It should contain a constructor
#   = This constructor should require two float parameters for a width/height
#   = The constructor should assign those parameters to instance variables
# - It should then override 'get_perimeter'
#   = Which should return the addition of the width/height instance variables multiplied by 2
# - Finally, it should override 'get_area'
#   = Which should return the width instance variable times the height instance variable
# Instantiate a Rectangle object with a width of 12 and a height of 7
# - Call both overridden functions and output their returned values to test
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass
