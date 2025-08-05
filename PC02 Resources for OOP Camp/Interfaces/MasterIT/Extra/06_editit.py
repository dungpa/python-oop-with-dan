# Edit this program by defining another interface called 'CanWalk'
# - Give it an abstract function called 'walk' with a float parameter for the distance to walk
# Inherit this interface in the 'Human' class
# - Override the 'walk' function and make it output the message "{name} is walking {distance} miles"
# Call the 'walk' function with the 'Human' object with a distance of 1.4 to test
from abc import ABC, abstractmethod


class CanTalk(ABC):
    @abstractmethod
    def talk(self, target: str):
        pass


class Human(CanTalk):
    def __init__(self, name: str):
        self.name = name

    def talk(self, target: str):
        print(f"{self.name} is talking to {target}")


me = Human("Tutor")
me.talk("Student")
