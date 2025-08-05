# Fix the errors in this program
# - It should define an interface called 'Eatable' which has an abstract function called 'eat'
# - It should then define a class called 'Fruit' which inherits the 'Eatable' interface
#   = This class overrides the 'eat' function and outputs one of two messages when called
# - The program then instantiates a 'Fruit' object and calls its 'eat' function to test
from abc import ABC, abstractmethod


interface Eatable(ABC)
@abstractmethod
def eat(self)
    pass


class Fruit(Eatable):
    def __init__(self, name: str, sweetness: int):
        self.name = name
        self.sweetness = sweetness

    def eat(self):
        if self.sweetness < 10:
            print(f"This {self.name} is quite sour")
        else:
            print(f"This {self.name} is nice and sweet")


apple = Fruit("apple", 36)
apple.eat()
