# Define a Carryable interface with two abstract functions
# - add_item (which takes a string parameter)
# - show_items (which returns a string parameter)
# Define a class called Sack which inherits from Carryable
# - Give it a constructor which declares an instance variable for the items in the Sack (starting as an empty list)
# - Override both abstract classes
#   = add_item should add the parameter to the items list
#   = show_items should create a string variable by appending each item in the list to it (separating items with spaces)
# Instantiate a Sack class and repeatedly ask the user to add items to the Sack
# - When they input "no", stop the loop and call the show_items() function to output the items in the sack
