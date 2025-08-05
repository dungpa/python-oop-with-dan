# Fix the errors in this program
# - It defines an abstract function called 'Animal' which has an 'eat' function
# - It then defines a child class called 'Fish' which overrides the 'eat' function
# - The program instantiates a 'Fish' object and calls its 'eat' function to test
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, age: int):
        self.age = age

    @abstractmethod
    def eat(self, food: str):
        pass


class Fish(Animal):
    def eat(self, food: str):
        print(f"The {self.age} year old fish is eating {food}")


fish = Animal(4)
fish.eat("bread crumbs")
