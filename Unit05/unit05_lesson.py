def is_even(even:int):
    if even % 2 == 0:
        print("even")
    else:
        print("not even")


while True:
    number = input("Choose any number (say stop to stop the program). ")
    if number == "stop":
        break
    is_even(int(number))
