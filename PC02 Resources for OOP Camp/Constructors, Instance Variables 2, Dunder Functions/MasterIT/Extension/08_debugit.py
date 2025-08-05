# Fix the errors in this program
class Table:
    def constructor(self, num_legs, material):
        num_legs = num_legs
        material = material

    def string(self):
        return f"The table has {self.num_legs} and is made from {self.material}"


kitchen_table = Table(6, "Oak")
print(kitchen_table)
