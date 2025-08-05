# Edit this program by defining another interface called 'Perishable'
# - It should define an abstract function called 'get_perish_date' which returns an integer
# Inherit 'Perishable' in the 'Food' class
# - Override 'get_perish_date' and return the 'eat_date' instance variable
# - Edit the 'eat' override to ask the user for the year they want to eat the food on
#   = If this year is before the perish date, output "Eating a {name}"
#   = Otherwise, output "You shouldn't eat {name} then, it will go out of date"
from abc import ABC, abstractmethod


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Food(Eatable):
    def __init__(self, name: str, eat_date: int):
        self.name = name
        self.eat_date = eat_date

    def eat(self):
        print(f"Eating a {self.name}")


beans = Food("can of beans", 2051)
beans.eat()
