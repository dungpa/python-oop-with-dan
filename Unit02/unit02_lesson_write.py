from random import randint
file = open("data.txt", "w")
result = randint(1,2)
answer = input("Write whatever you want.")
file.write(answer)
file.write("\nOne more line")
if result == 1:
    file.write("\nHeads")
elif result == 2:
    file.write("\nTails")
file.close()
