def leap_year(year:int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False


while True:
    ask = input("enter in the year, but use 'stop' to end the program")
    if ask == "stop":
        break
    print(leap_year(int(ask)))

