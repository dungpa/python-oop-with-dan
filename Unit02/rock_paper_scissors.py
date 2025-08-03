player_1_throw = input("Enter Player 1's throw (R/P/S): ")
player_2_throw = input("Enter Player 2's throw (R/P/S): ")
if player_1_throw == player_2_throw:
    print("Draw!")
elif (player_1_throw == "R" and player_2_throw == "S") or (player_1_throw == "S" and player_2_throw == "P") or (player_1_throw == "P" and player_2_throw == "R"):
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")
