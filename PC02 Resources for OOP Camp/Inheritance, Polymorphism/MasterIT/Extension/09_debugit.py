# Fix the errors in this program
# Use the correct syntax for the children classes
class A:
    def __init__(self):
        print("Constructing the parent object")


class B():
    def __init__(self):
        A._init__(self)
        print("Constructing a B object")


class C A:
    class __init__(self):
        A __init__(self)
        print("Constructing a C object")


class D A);
    def __init__(self):
        A.__init_(self)
        print("Constructing a D object")


a = A()
b = B()
c = C()
d = D()
