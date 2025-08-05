# Edit this program by splitting this program into two functions
# - Call both of those functions so the program behaves the same after your edits
while True:
    try:
        num = int(input("Enter a number greater than 0: "))
        if num > 0:
            break
    except ValueError:
        print("Please input a valid integer...")
numbers = []
for count in range(num):
    numbers.append(count)
print(numbers)
