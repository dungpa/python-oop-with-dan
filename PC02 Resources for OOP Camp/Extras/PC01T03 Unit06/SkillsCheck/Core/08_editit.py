# Edit this program by adding a docstring to the 'func' function
def func(param: int) -> bool:
    for num in range(2, param):
        if param % num == 0:
            return False
    return True


print(func(10))
print(func(13))
