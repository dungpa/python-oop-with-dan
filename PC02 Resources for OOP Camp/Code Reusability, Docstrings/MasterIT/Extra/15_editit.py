# Edit this program by separating its code into separate functions
# - Call those functions in the correct order so that the program behaves exactly the same
while True:
    try:
        number = int(input("Enter a number to check: "))
        break
    except ValueError:
        print("Please enter an integer...")
if number % 2 == 0:
    print("That number is even")
else:
    print("That number is not even, it is odd")
