# Fix the errors in this program
# - Use the correct return value for the __add__ dunder function
#   = It should return a new Number object using the current value and the other value as the argument
# - Use the correct return value for the __str__ dunder function
#   = It should return the value instance variable cast to a string
class Number:
    def __init__(self, value: float):
        self.value = value
    
    def __add__(self, other: "Number") -> "Number":
        return ?
    
    def __str__(self) -> str:
        return ?


a = Number(12)
b = Number(23)
print(a + b)
