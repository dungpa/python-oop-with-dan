# Fix the errors in this program
# - Use the correct syntax for getter/setter instance functions
class Package:
    def __init__(self, address: str, weight: float):
        self.__address = address
        self.__weight = weight

    get_address():
        return self.__address

    self.get_weight(self) -> str:
        return self.__weight


package = Package("12 Faker Street, Fakertown, FA3 7ER", 1.25)
print(package.get_address())
print(package.get_weight())
