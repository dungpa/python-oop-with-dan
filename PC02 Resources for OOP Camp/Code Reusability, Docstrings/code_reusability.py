import random

while True:
    print("What type of list would you like to generate: ")
    print("\t1. Sequential (0 to maximum value)")
    print("\t2. Sequential (minimum value to maximum value)")
    print("\t3. Random (0 to 100)")
    print("\t4. Random (minimum value to maximum value)")
    print("\t5. Exit program")
    choice = input("Enter your choice: ")
    if choice == "1":
        while True:
            try:
                maximum_value = int(input("Enter a maximum value greater than 0: "))
                if maximum_value > 0:
                    break
            except ValueError:
                print("Please enter a valid integer")
        numbers = []
        for number in range(maximum_value):
            numbers.append(number)
        print(f"Your list is {numbers}")
    elif choice == "2":
        while True:
            try:
                minimum_value = int(input("Enter a minimum value greater than 0: "))
                if minimum_value > 0:
                    break
            except ValueError:
                print("Please enter a valid integer")
        while True:
            try:
                maximum_value = int(input("Enter a maximum value greater than the minimum value: "))
                if maximum_value > minimum_value:
                    break
            except ValueError:
                print("Please enter a valid integer")
        numbers = []
        for number in range(minimum_value, maximum_value):
            numbers.append(number)
        print(f"Your list is {numbers}")
    elif choice == "3":
        while True:
            try:
                size = int(input("Enter a size of the list greater than 0: "))
                if size > 0:
                    break
            except ValueError:
                print("Please enter a valid integer")
        numbers = []
        for count in range(size):
            numbers.append(random.randint(0, 100))
        print(f"Your list is {numbers}")
    elif choice == "4":
        while True:
            try:
                size = int(input("Enter a size of the list greater than 0: "))
                if size > 0:
                    break
            except ValueError:
                print("Please enter a valid integer")
        while True:
            try:
                minimum_value = int(input("Enter a minimum value greater than 0: "))
                if minimum_value > 0:
                    break
            except ValueError:
                print("Please enter a valid integer")
        while True:
            try:
                maximum_value = int(input("Enter a maximum value greater than the minimum value: "))
                if maximum_value > minimum_value:
                    break
            except ValueError:
                print("Please enter a valid integer")
        numbers = []
        for count in range(size):
            numbers.append(random.randint(minimum_value, maximum_value))
        print(f"Your numbers are {numbers}")
    elif choice == "5":
        break
