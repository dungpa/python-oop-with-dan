# Edit this program by defining a child class of Building called Mansion
# - Override the constructor so it accepts a parameter for the address and another parameter for the number of rooms
#   = Call Building's constructor with the address, and then declare an instance variable for the number of rooms
# - Override the assess() abstract function
#   = It should output the address and the number of rooms the Mansion has
# - Ask the user for the address of a Mansion to explore
#   = Instantiate a Mansion object with that address and a random number of rooms (between 12 and 20)
#   = Call this Mansion object's assess() function to test
from abc import ABC, abstractmethod


class Building(ABC):
    def __init__(self, address: str):
        self.address = address

    @abstractmethod
    def assess(self):
        pass
