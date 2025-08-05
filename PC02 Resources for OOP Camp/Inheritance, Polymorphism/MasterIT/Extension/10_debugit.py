# Fix the errors in this program
# Use the correct syntax when overriding the instance function
class A:
    def output_info(self):
        print("A is the parent class")


class B(A):
    def out_info(self):
        print("B is one of the children class")


class C(A):
    def output_info():
        print("C is also a child class")


class D(A):
    def info(self):
        print("D is the final child class")


my_objects = [A(), B(), C(), D()]
for child in my_objects:
    child.output_info()
