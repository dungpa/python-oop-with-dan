file = open("data.txt","r")
lines = file.readlines()
file.close()
for line in lines:
    print(line[:-1])