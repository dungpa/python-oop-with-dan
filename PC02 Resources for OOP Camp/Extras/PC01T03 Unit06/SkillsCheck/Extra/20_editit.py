# Edit this program by adding a docstring to the 'func' function
def func(param: str) -> bool:
    val_1 = 0
    val_2 = len(param) - 1
    while val_1 <= val_2:
        if param[val_1] != param[val_2]:
            return False
        val_1 += 1
        val_2 -= 1
    return True


print(func("level"))
print(func("program"))
