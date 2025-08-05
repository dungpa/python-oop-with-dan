# Fix the errors in this program
# - It defines a class called 'Foo'
#   = This class contains a constructor with one parameter and declares an instance variable for that parameter
#   = It contains the addition dunder function and returns the addition of the current and other objects' value instance variables
#   = It contains the string conversion dunder function which returns 'Foo'
# - It instantiates two Foo objects and outputs the addition of them
class Foo:
    def __init__(self, value: float):
        print("Building an object")
        self.value = value

    def add(self, other
        return self.value + other.value

    def __str self -> str:
        return "Foo"


value_1 = Foo(12)
value_2 = Foo(24)
print(value_1 + value_2)
