# Edit this program by defining a child class of 'Chair' called 'BabyChair'
# - Override the 'sit' function
#   = Ask the user for the age of the person sitting in the chair
#   = If their age is greater than 2, the function should output "You are too old to use this chair"
#   = Otherwise, it should ask for their name and output "Welcome {name}"
# Instantiate a 'BabyChair' object and call its 'sit' function to test
from abc import ABC, abstractmethod


class Chair(ABC):
    def __init__(self, material: str):
        self.material = material

    @abstractmethod
    def sit(self):
        pass
