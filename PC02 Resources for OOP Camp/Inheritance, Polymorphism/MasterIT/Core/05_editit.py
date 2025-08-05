# Override the parent's instance function in the given children classes
# - They should output information specific to the Motorbike/Car
class Vehicle:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get_info(self):
        print(f"This Vehicle has a capacity of {self.capacity} people")


class Motorbike(Vehicle):
    def __init__(self, engine: int, make: str):
        Vehicle.__init__(self, 2)
        self.engine = engine
        self.make = make


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        Vehicle.__init__(self, 5)
        self.make = make
        self.model = model


a = Vehicle(4)
b = Motorbike(1, "Ford")
c = Car("BMW", "6 Series")
a.get_info()
b.get_info()
c.get_info()
