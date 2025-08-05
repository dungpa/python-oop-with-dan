# Edit this program by separating its code into separate functions
# - Call those functions in the correct order so that the program behaves exactly the same
import random


numbers = []
for _ in range(20):
    numbers.append(random.randint(1, 100))
print(f"Generated Numbers: {numbers}")
for _ in range(len(numbers)):
    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
print(f"Sorted Numbers: {numbers}")
