colours = ["red", "green", "blue"]
method = int(input("Enter 1 to use the index, or 2 to use the value."))
if method == 1:
    index_input = int(input("Enter the index of the colour you have the biggest grudge against."))
    change = input("What do you want to replace the colour you hate with?")
    colours.pop(index_input)
else:
    value_input = input("Enter the value of the colour you have the biggest grudge against.")
    change = input("What do you want to replace the colour you hate with?")
    colours.remove(value_input)

colours.append(change)
print(colours)