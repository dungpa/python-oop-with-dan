# Fix the errors in this program
# The program should continuously ask the user for an integer until they input one between 50 and 100
while True:
    num = int(input("Enter a number between 50 and 100: "))
    if num < 50 or num > 100:
        break
    else:
        print("Please try again")
