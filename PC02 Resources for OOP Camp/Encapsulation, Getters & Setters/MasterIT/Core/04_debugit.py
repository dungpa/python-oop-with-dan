# Fix the errors in this program
# - Use the correct access modifier when accessing instance variables
class Animal:
    def __init__(self, name: str, age: int, species: str):
        self._name = name
        self._age = age
        self._species = species


class Cow(Animal):
    def __init__(self, name: str, age: int):
        Animal.__init__(self, name, age, "Cow")

    def __str__(self):
        return f"About this {self.species}:\n\t- Name: {self.__name}\n\t- Age: {self.age}"


cow = Cow("Bessie", 4)
print(cow)
