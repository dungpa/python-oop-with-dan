# Fix the errors in this program
# - This program defines a parent class called 'C'
#   = This class outputs "Constructing a C object" when instantiated
# - It then defines a child class called 'D'
#   = This class calls the parent's constructor and then outputs "Constructing a D object" when instantiated
# - It instantiates an object of both classes
class C:
    def __init__(self):
        print("Constructing a C object")


class D(C):
    def __init__(self):
        C.init()
        print("Constructing a D object")


c = C()
d = D()
