# Define a Shape3D abstract class
# - Give it an abstract function called get_volume() which returns a float value
# Define three child classes for Cube, Cuboid, and Sphere
# - Give each child class a constructor with all required parameters and assign them to instance variables
#   = For Cube, that is a single float parameter for the size
#   = For Cuboid, that is three float parameters for the width/height/depth
#   = For Sphere, that is a single float parameter for the radius
# - Override the get_volume() function in each child class
#   = For Cube, it should return size * size * size
#   = For Cuboid, it should return width * height * depth
#   = For Sphere, it should return (4 / 3) * 3.14159 * radius * radius * radius
# For the main program
# - Create an empty list of shapes
# - Repeatedly ask the user if they wanted to generate another random shape
#   = If they do, randomly instantiate one of the three child classes
#       == Give that child class the correct number of random arguments (all between 1 and 50)
#   = If they don't, end the loop
# - Loop through all the shapes in the list and output their volume
