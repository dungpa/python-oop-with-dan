import random
type = int(input("Enter 1 to generate a score, enter 2 to input it yourself."))


if type == 1:
    score = random.randint(0, 100)
else:
    score = int(input("Enter an example of an exam score. "))

if score > 90 and score <= 100:
    print("You get an A*")
elif score > 80 and score <= 90:
    print("You get an A")
elif score > 70 and score <= 80:
    print("You get a B")
elif score > 50 and score <= 70:
    print("You get a C")
elif score > 30 and score <= 50:
    print("You get a D")
elif score > 0 and score <= 30:
    print("You get an E")
else:
    print("ERROR 404. Just give me a realistic number because you didn't make the smartest decision.")

