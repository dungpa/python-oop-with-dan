# Fix the errors in this program
# Use the correct syntax for the constructor and dunder functions
class Distance:
    def init(self, unit: str, amount: float):
        self.unit = unit
        self.amount = amount

    def __str self -> str:
        return f"{self.amount}{self.unit}"

    def add__(self, other: "Distance") -> "Distance":
        if self.unit == other.unit:
            return Distance(self.unit, self.amount + other.amount)
        else:
            print("Mismatched Unit")
            return self
