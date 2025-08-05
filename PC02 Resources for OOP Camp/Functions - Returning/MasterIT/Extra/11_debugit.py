# Fix the errors in this program
# - It should define a function called 'roll_dice' which returns a random roll of the dice (1 to 6)
# - This program should call the function and output the returned roll to test
roll_dice
    return random.randint(1, 6)


print(f"Your roll is [roll_dice()]")
