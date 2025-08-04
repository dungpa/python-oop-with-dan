def number_subtract(first_number:int, second_number:int) ->int:
    return first_number - second_number

while True:
    first = input("First number in the argument (you can stop the program by saying 'stop': ")
    if first == 'stop':
        break
    second = input("Second number in the argument (you can stop the program by saying 'stop': ")



    if second == 'stop':
        break

    print(number_subtract(int(first), int(second)))
