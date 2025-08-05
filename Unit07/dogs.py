class Pitbull:
    pass

class Corgi:
    pass

class Poodle:
    pass

class Husky:
    pass


breed = int(input("Enter a number between 1 and 4, being: 1. Husky, 2. Pitbull, 3. Corgi and 4. Poodle.: "))

if breed == 1:
    husky = Husky()
    print(husky)
elif breed == 2:
    pitbulls = Pitbull()
    print(pitbulls)
elif breed == 3:
    corgi = Corgi()
    print(corgi)
else:
    poodle = Poodle()
    print(poodle)



