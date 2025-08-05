# Edit the setter in this class so that it validates the integer parameter
# - It should only update the instance variable if the integer parameter is
#   = Greater than 0
#   = Less than 100
class Wallet:
    def __init__(self, starting_amount: int):
        self.__amount = starting_amount

    def get_amount(self) -> int:
        return self.__amount

    def set_amount(self, new_amount: int):
        self.__amount = new_amount


wallet = Wallet(12)
print(wallet.get_amount())
wallet.set_amount(106)
print(wallet.get_amount())
wallet.set_amount(45)
print(wallet.get_amount())
