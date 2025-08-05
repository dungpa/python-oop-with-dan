# Fix the errors in this program
# - The 'calculate_rectangle_area' function should return the area of a rectangle with the width/height parameter
#   = It should also contain a fully descriptive docstring
# - The program should call this function and output the returned area to test
def calculate_rectangle_area(width: float, height: float) -> float:
    #
    Calculates the area of a rectangle using the width/height parameters
    :param width: the width of the rectangle
    :pam height: the height of the rectangle
    :return: the area of the rectangle
    #
    return width * height


area = calculate_rectangle_area(12, 53)
print(area)
