from random import randint

def coin_flip_guess():
    trueanswer = randint(1, 2)
    guess = (int(input("Say 1 if you think it hit heads, say 2 if you think it hit tails.")))
    if guess == trueanswer:
        print("You are correct")
    else:
        print("You are not correct")

countingrange = int(input("How many times would you like to flip the coin?"))
for i in range(countingrange):
    coin_flip_guess()