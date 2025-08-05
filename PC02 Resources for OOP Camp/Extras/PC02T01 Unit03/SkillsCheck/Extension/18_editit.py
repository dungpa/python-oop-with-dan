# Edit the loop so that it creates a rectangle of Os
size = int(input("Enter the square size: "))
for row in range(size):
    line = ""
    for col in range(row):
        line += "O"
    print(line)
