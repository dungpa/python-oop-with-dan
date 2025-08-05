# Edit this program by separating its code into separate functions
# - Call those functions in the correct order so that the program behaves exactly the same
print("Player 1")
while True:
    player_1_throw = input("\tEnter your throw: ")
    if throw == "Rock" or throw == "Paper" or throw == "Scissors":
        break
print("Player 2")
while True:
    player_2_throw = input("\tEnter your throw: ")
    if throw == "Rock" or throw == "Paper" or throw == "Scissors":
        break
if player_1_throw == player_2_throw:
    print("Draw")
elif player_1_throw == "Rock" and player_2_throw == "Scissors" or player_1_throw == "Scissors" and player_2_throw == "Paper" or player_1_throw == "Paper" and player_2_throw == "Rock":
    print("Player 1 Wins")
else:
    print("Player 2 Wins")
