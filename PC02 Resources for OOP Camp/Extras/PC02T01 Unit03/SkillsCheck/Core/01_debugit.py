# Fix the errors in this program
# It should output one of three messages based on the input number
# - If the number is positive (more than 0) output "# is positive"
# - If the number is negative (less than 0) output "# is negative"
# - If the number is equal to 0 output "# is zero"
num = int(input("Enter a number: "))
if num <= 0:
    print(f"{num} is positive")
elif num == 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")
