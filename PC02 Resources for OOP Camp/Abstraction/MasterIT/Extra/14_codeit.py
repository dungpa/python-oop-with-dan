# Define an abstract class called 'Container'
# - Give it a constructor which accepts a string parameter for its 'contents' and assigns it to an instance variable
# - Define an abstract function called 'replace_contents' which accepts a string parameter for new contents
# Define a child class called 'Bottle'
# - Override the constructor and give it the string contents parameter as well as a maximum amount of liquid
#   = Call the parent's constructor
#   = Assign the maximum liquid to an instance variable
#   = Declare another instance variable called 'current_amount' which starts at the maximum amount
# - Override the 'replace_contents' function
#   = Set the contents to the new contents
#   = Set the current amount to the maximum amount
# - Define a function called 'drink' with a float parameter for an amount to drink
#   = If the amount to drink is greater than the current amount, it should output "There is not enough to drink"
#   = Otherwise, output "Drinking {amount}ml of {contents}" and subtract the amount from the current amount
# Ask the user what bottle they would like to take with them (contents and maximum amount)
# Instantiate a Bottle object with that contents/maximum amount
# - Repeatedly ask them if they want to drink from the Bottle
#   = If so, ask for the amount and call the 'drink' function with that amount
#   = Otherwise, end the program
