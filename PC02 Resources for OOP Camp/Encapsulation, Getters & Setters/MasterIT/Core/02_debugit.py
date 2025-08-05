# Fix the errors in this program
# - The getter function should return the correct variable
class B:
    def __init__(self, x: str):
        self.__x = x

    def get_x(self) -> str:
        return self


b = B(12)
print(b.get_x())
