# Fix the errors in this program
number = int(input("Enter a number (greater than 0): "))
print(f"Counting down from {number} to 0")
while number < 0:
    print(f"{number}")
    number -= 1
