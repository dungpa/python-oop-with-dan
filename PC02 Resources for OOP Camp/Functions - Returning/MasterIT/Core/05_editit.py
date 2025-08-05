# Edit this program by defining a new function called 'validate_rectangle' which validates a rectangle input by the user
# - This function should ask the user to input integers for the width/height of a rectangle
#   = Both values should be between the parameter lower/upper bounds
#   = Repeatedly ask the user for an integer until they input a valid value
# - When the user has input a valid width/height, call the 'create_rectangle' function using the width/height as arguments
# Call 'validate_rectangle' using arguments of 1 and 20 to test
def create_rectangle(width: int, height: int):
    for row in range(height):
        line = ""
        for col in range(width):
            line += "O"
        print(line)
