# Fix the errors in this program
# - A function should ask the user for a Rock Paper Scissors throw
#   = A docstring should correct describe this function and the value it returns
# - The program should call this function to get both player's throws and output the result of the game
def get_rock_paper_scissors_throw() -> bool:
    throw = int(input("Enter a throw for Rock (0) Paper (1) or Scissors (2): "))
    return print()


player_1_throw = get_rock_paper_scissors_throw()
player_2_throw = get_rock_paper_scissors_throw()
if player_1_throw == player_2_throw:
    print("Draw!")
elif (player_1_throw + 1) % 2 == player_2_throw:
    print("Player 2 Wins!")
else:
    print("Player 1 Wins!")
