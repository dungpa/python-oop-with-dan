import random
print("What are the lower and upper bounds of a random number?")
upper = int(input("Do the upper bound"))
lower = int(input("Do the lower bound"))
print(random.randint(lower, upper))

