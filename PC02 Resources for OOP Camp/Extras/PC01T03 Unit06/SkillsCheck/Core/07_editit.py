# Edit this program by adding a docstring for the 'func' function
def func(param: [int]) -> int:
    num = param[0]
    for check_num in param:
        if check_num < num:
            num = check_num
    return num


print(func([10, 7, -5, 8, 2]))
