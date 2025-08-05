# Fix the errors in this program
# - Use the correct instance variable identifier/access modifier in all locations
# - Use the correct syntax for getter/setter instance function syntax
class D:
    def __init__(self, a: str, b: str):
        self._a = a
        self._b = b

    def get_a(self) -> int:
        pass

    get_b():
        return self.b


class E(D):
    def set_a(new_a: str):
        self.__a = new_a


d = D("A", "B")
print(d.get_a())
print(d.get_b())

e = E("A", "B")
e.set_a("C")
print(e.get_a())
print(e.get_b())
