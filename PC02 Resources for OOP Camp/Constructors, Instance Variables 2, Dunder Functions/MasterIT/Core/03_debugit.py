# Fix the errors in this program
class Money:
    def __init__(self, starting_amount):
        self.amount = starting_amount

    def _string_(self):
        return f"£{self.amount}"


wallet = Money(10)
print(f"I have {wallet} currently in my wallet")
