# Edit this program by moving the list generation/output code into its own function
# - Define the function and move the program code into it
# - Call the function to test
numbers = []
while True:
    choice = input("Would you like to add another number: ")
    if choice == "yes":
        number = int(input("\tEnter the number: "))
        numbers.append(number)
    elif choice == "no":
        break
print(f"Your list is {numbers}")
