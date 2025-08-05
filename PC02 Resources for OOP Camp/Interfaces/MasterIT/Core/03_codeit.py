# Define an interface called 'Wearable'
# - Give it two abstract functions called 'wear' and 'take_off'
# Define another interface called 'TemperatureControlled'
# - Give it an abstract function called 'at_ideal_temperature' which returns a boolean value
# Define a class called 'Coat' which inherits both interfaces
# - Give it a constructor which declares an instance variable called 'temperature' which starts at 30
# - Override the 'wear' function which sets 'temperature' to 40 and outputs "Wearing the coat"
# - Override the 'take_off' function which sets 'temperature' to 30 and outputs "Taking off the coat"
# - Override the 'at_ideal_temperature' function
#   = It should return True if the 'temperature' is between 25 and 35
#   = Otherwise it should return False
# Instantiate a 'Coat' object and use the 'wear', 'take_off', and 'at_ideal_temperature' functions to check that they work
