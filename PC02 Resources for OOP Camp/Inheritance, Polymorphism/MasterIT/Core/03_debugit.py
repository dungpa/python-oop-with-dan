# Fix the errors in this program
# - The program defines the parent class 'Container'
# - The program then defines the child class 'WaterBottle'
#   = It overrides the 'output_contents' instance function and outputs the amount of water in the water bottle instead
# - The program then instantiates an object of both classes and calls their 'output_contents' instance functions
class Container:
    def __init__(self, contents: str):
        self.contents = contents

    def output_contents(self):
        print(f"This container has {self.contents}")


class WaterBottle(Container):
    def __init__(self, amount: int):
        Container.__init__(self, "Water")
        self.amount = amount

    def out_contents(self:
        print(f"This water bottle has {self.amount}ml of water")


bottle = Container("tea")
water_bottle = WaterBottle(500)
bottle.output_contents()
water_bottle.output_contents()
