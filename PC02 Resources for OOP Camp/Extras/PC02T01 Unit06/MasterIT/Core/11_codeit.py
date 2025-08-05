# Define a DataConverter class which has two instance variables for an amount (float) and a unit (string)
#   - Assign values for both instance variables from parameters in the constructor
# Define an instance function that takes a parameter for a target unit and returns the converted float value from the current unit to the target unit
#   - Limit yourself to three units: metres (m), kilometres (km), and miles (mi)
#   - Here are the conversions from each unit to the other units
#       = Starting from metres
#           == To kilometres:   / 1000.0
#           == To miles:        / 1609.34
#       = Starting from kilometres
#           == To metres:       * 1000.0
#           == To miles:        * 0.621371
#       = Starting from miles
#           == To metres:       * 1609.34
#           == To kilometres:   * 1.60934
# Add the string dunder function which outputs the amount and its unit, e.g. 12mi or 45km
# Instantiate a DataConverter object and test the conversion instance function
