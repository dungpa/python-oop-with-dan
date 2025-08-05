# Fix the errors in this program
# - It should define a function called 'create_list' which creates and returns a list of integers
# - The program should call this function and output the returned list to test
def create_list():
    numbers = []
    for num in range(10):
        numbers.append(num)


my_numbers = create_list()
print("The numbers generated are:")
for number in my_numbers:
    print(f"\t{number}")
