class Car:
    def __init__(self, make, colour, speed):
        self.make = make
        self.speed = speed
        self.colour = colour

    def __str__(self):
        return f'{self.colour} {self.make}'

    def __int__(self):
        return f'{self.speed}'

    def drive(self):
        print(f"Driving a {self.colour} {self.make} car at {self.speed} miles per hour. ")

class MiniVan(Car):
    def __init__(self, make, colour):
        Car.__init__(self, make, colour, 111)

    def drive(self):
          print(f"Driving a {self.colour} {self.make} minivan at a slower speed of {self.speed} miles per hour. ")

car = Car("Lamborghini", "Giallo Auge", 190)
car.drive()
minivan = MiniVan("Honda", "Smoke Blue Pearl")
minivan.drive()