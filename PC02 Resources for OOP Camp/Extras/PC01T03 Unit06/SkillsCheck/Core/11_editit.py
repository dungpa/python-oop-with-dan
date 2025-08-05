# Edit this program by adding docstrings to the 'func_1' and 'func_2' functions
def func_1(param: float) -> float:
    return param * 2


def func_2(param: float) -> float:
    return param / 2


var = float(input("Enter a number: "))
print(func_1(var))
print(func_2(var))
