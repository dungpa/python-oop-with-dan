# Fix the errors in this program
# - The program defines the parent class 'A'
#   = This class outputs "Constructing the parent object" when instantiated
# - The program then defines the child class 'B'
# - The program instantiates an object of both classes
clas A
    def __it__(self):
        print("Constructing the parent object")


class B(A):
    pass


a = A()
b = B()
