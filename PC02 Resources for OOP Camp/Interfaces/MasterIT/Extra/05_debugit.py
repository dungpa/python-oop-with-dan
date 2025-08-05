# Fix the errors in this program
# - It should define an interface called 'CanTalk' which has an abstract function called 'talk'
# - It also defines a class called Human which inherits the 'CanTalk' interface
#   = This class overrides the 'talk' function to output a message
# - The program instantiates a 'Human' object and calls its 'talk' function to test
from abc import ABC, abstractmethod


class CanTalk(ABC):
    @abstractmethod
    def talk(self, target: str):
        pass


class Human(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def talk(self, target: str):
        print(f"{self.name} is talking to {target}")


me = Human("Tutor")
me.talk("Student")
