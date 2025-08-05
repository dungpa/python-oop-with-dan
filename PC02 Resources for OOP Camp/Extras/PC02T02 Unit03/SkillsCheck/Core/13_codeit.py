# Define a Drinkable interface
# - Give it an abstract function called drink (which takes a float parameter for the amount to drink)
# Define a class called WaterBottle which inherits the Drinkable interface
# - Give it a constructor which requires a parameter for the max water in the bottle
#   = It should declare two instance variables for the max amount and the current amount (both using that parameter)
# - Override the drink abstract function
#   = It should check if there is enough current water in the bottle to drink the parameter amount
#       == If so, remove the parameter amount from the current water and output "Drinking {amount}ml"
#       == Otherwise, output "There is not enough water, there is only {current_amount}ml left"
# Instantiate a WaterBottle object with a random max amount (between 400 and 800)
# - Call the drink function 5 times, each drinking a random amount (between 50 and 200)
