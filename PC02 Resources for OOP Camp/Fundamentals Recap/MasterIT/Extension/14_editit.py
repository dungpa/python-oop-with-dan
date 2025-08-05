# Ask the user for numbers to append to 'my_list' before the rest of the program uses that list
# This means repeatedly asking the user to input a number
#   If they input a number, append it to the list
#   If they input the word "quit", end the loop and continue with the rest of the program
my_list = []

print(f"Before: {my_list}")
for count in range(len(my_list)):
    for index in range(len(my_list) - 1 - count):
        if my_list[index] > my_list[index + 1]:
            temp = my_list[index]
            my_list[index] = my_list[index + 1]
            my_list[index + 1] = temp
print(f"Sorted: {my_list}")
