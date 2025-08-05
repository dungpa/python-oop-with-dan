# Fix the errors in this program
# Object instantiation should be handled correctly
# Make sure instance function calls are correct too
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        return 3.14 * self.radius * 2


a = new Circle(float(input("Enter the first circle\'s radius: ")))
b = Circle float(input("Enter the second circle\'s radius"))

print("About the first circle:")
print(f"\tArea: {a.get_area}")
print(f"\tPerimeter: {a.get_perimeter}")

print("About the second circle:")
print(f"\tArea: {b.get_area}")
print(f"\tPerimeter: {b.get_perimeter}")
