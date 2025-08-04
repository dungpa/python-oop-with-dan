file = open("numbers.txt","r")
lines = file.readlines()
file.close()
console_list = []
for line in lines:
    console_list.append(int(line))

for console in console_list:
    print(console)