# Fix the errors in this program
# - It defines an interface called 'Eatable' with an abstract function called 'eat'
# - It defines another interface called 'IsHealthy' with an abstract function called 'output_health_value'
# - It then defines a class called 'Vegetable' which inherits 'Eatable'
#   = This class overrides 'eat' and 'output_health_value' functions which output messages
# - The program instantiates a Vegetable object and calls its 'eat' and 'output_health_value' functions to test
from abc import ABC, abstractmethod


class Eatable:
def eat():
    None


class IsHealthy(ABC):
    @ABC
    def output_health_value(self):
        pass


class Vegetable(Eatable, IsHealthy):
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"Eating a {self.name}")

    def output_health_value(self):
        print(f"{self.name} is a good source of vitamins and minerals")


carrot = Vegetable("carrot")
carrot.eat()
carrot.output_health_value()
