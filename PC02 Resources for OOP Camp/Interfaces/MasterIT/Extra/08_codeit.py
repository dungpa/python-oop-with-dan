# Define an interface called 'Comparable'
# - This interface should have one abstract function 'get_value' which returns a float value
# - It should also have an instance function 'compare' which returns an integer value
#   = It should accept a Comparable parameter (wrap "Comparable" in speech marks for the type hint to use it as a type hint in its own class)
#   = This function should compare the current object's get_value() returned value, against the parameter's get_value() returned value
#       == 1 is returned if the current object's value is greater
#       == 0 is returned if they are the same
#       == -1 is returned if either previous possibilities is not true
# Define a class called 'Money' which inherits 'Comparable'
# - Give it a constructor with a float parameter for the amount of Money (saved to an instance variable)
# - Add the string conversion dunder function which returns the amount of Money in a formatted string
#   = E.g. "£12.52"
# - Override 'get_value' and return the 'amount' instance variable
# Instantiate two Money objects (with any amount)
# Compare both objects using the 'compare' function and output the object with the larger amount
