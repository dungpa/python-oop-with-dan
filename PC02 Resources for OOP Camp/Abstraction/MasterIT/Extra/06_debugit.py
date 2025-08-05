# Fix the errors in this program
# - It should define an abstract class called 'Animal' with the abstract function 'talk'
# - It should then define two children class called 'Bird' and 'Fish'
#   = 'Bird' should override 'talk' and make it output "Squawk"
#   = 'Fish' should override 'talk' and make it output "Blub"
# - The program then instantiates 'Bird' and 'Fish' objects and calls their 'talk' functions to test
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def talk(self):
        pass


class Bird:
    pass


class Fish:
    pass


bird = Bird()
fish = Fish()
bird.talk()
fish.talk()
