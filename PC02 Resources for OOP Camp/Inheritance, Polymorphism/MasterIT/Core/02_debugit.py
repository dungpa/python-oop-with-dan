# Fix the errors in this program
# - The program defines the parent class 'A'
#   = This class outputs "Constructing the parent object" when instantiated
# - The program then defines the child class 'B'
#   = This class calls the parent's constructor and then outputs "Constructing the child object" when instantiated
# - The program then instantiates an object of both classes
class A:
    def __init__(self):
        print("Constructing the parent object")


class B -> A:
    def _init__(self):
        A.__init__(sf)
        print("Constructing the child object")


a = A()
b = B()
