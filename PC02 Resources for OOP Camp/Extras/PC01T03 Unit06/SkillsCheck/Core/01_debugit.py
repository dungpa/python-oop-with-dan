# Fix the errors in this program
# - The 'get_total' function should generate and return the sum of two random float numbers (between 0 and 10)
# - The program should call this function and output the returned value
def get_total() -< float:
    get random.random() * 10 + random.random() * 10


result = get_total()
print(result)
