# Edit the Wallet class
# - Add the string dunder function
#   = It should return the value of the wallet in the format "£{value}"
# - Add the addition dunder function
#   = It should return a new Wallet object
#   = Use the current amount added to the other amount for the Wallet object's argument
class Wallet:
    def __init__(self, amount: float):
        self.amount = amount


my_wallet = Wallet(12)
friend_wallet = Wallet(6)
print(f"The total you can spend together is {my_wallet + friend_wallet}")
