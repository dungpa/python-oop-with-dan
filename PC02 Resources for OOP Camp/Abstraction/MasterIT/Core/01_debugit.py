# Fix the errors in this program
# - It defines an abstract class called 'Animal'
# - It then defines a child class of 'Animal' called 'Dog'
# - The program instantiates a Dog object and outputs its name instance variable to test

class Animal(AbstractClass):
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    pass


dog = Dog("Barney")
print(dog.name)
