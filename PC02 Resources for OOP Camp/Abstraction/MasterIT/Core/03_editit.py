# Edit this program by defining an abstract class called 'Shape'
# - Give it an abstract function called 'output_info'
# Inherit this class in both 'Rectangle' and 'Triangle'
# - Both classes should override the 'output_info' function
#   = The 'Rectangle' version should output "Rectangle with width={width} and height={height}"
#   = The 'Triangle' version should output "Triangle with base={base} and height={height}"
# Call the 'output_info' function on both Rectangle/Triangle objects to test
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height


rectangle = Rectangle(12, 7)
triangle = Triangle(20, 12)
