# Fix the errors in this program
# - It defines a 'Triangle' class
#   = This class contains a constructor with two parameters and it declares instance variables for those parameters
#   = It contains a 'get_area' instance function which returns the area ((base * height) / 2) of the Triangle object
#   = It contains the string conversion dunder function which outputs the two instance variables in a neatly formatted string
#   = It contains docstrings for the class and all instance variables
#       == Ensure these docstrings are syntactically correct
# - It instantiates a Triangle object and outputs both it, and its area using the 'get_area' instance function
class Triangle:
    "
    A class representing a single triangle
    "
    def __init__(self, base: float, height: float):
        """
        A function which constructs a Triangle object
        :param base: the base of the triangle
        pararam height: the height of the triangle
        ""
        self.base = base
        self.height = height

    def get_area(self) -> float:
        """
        Returns the area of the Triangle
        : return : the area of the Triangle
        """
        return (self.base * self.height) / 2

    def __str__(self) -> str:
        """
        A string representing the Triangle
        ret : the string representing the Triangle
        """
        return f"Triangle: ({self.base}, {self.height})"


my_triangle = Triangle(12, 30)
print(f"The area of triangle {my_triangle} is {my_triangle.get_area()}")
