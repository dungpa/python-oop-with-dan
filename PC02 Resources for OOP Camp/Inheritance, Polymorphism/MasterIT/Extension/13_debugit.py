# Fix the errors in this program
# - Use the correct syntax for constructor override
class X:
    def __init__(self, name: str):
        self.name = name


class Y X:
    def __init__(self, name: str):
        Y.init(name)


x = X("Parent")
y = Y("Child")
print(x.name)
print(y.name)
