# Edit the instance variables in the parent class so they are protected
# - Also edit their use in the child class
class A:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y


class B(A):
    def __init__(self, x: int, y: int, z: int):
        A.__init__(self, x, y)
        self.z = z

    def get_z(self):
        return self.z

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"


a = A(0, 1)
b = B(10, 20, 30)
print(f"[{a.get_x()}, {a.get_y()}]")
print(b)
