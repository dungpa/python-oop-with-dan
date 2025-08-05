# Edit this program by connecting the 'output_shapes_button' object to an instance function
# - This instance function should loop through and output all the Shape objects in the 'shapes' list
#   = Each one should be output to the console in a bullet point style list
from abc import ABC, abstractmethod
import tkinter as tk
import random


class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        return f"Rectangle ({self.width}, {self.height})"


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return (self.base * self.height) / 2

    def __str__(self) -> str:
        return f"Triangle ({self.base}, {self.height})"


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return 3.14159 * self.radius * self.radius

    def __str__(self) -> str:
        return f"Circle ({self.radius})"


class ShapeCreator:
    def create_random_shape(self):
        shape_type = random.randint(0, 2)
        if shape_type == 0:
            self.shapes.append(Rectangle(random.randint(1, 20), random.randint(1, 20)))
        elif shape_type == 1:
            self.shapes.append(Triangle(random.randint(1, 20), random.randint(1,  20)))
        else:
            self.shapes.append(Circle(random.randint(1, 20)))

    def __init__(self):
        self.shapes = []
        self.window = tk.Tk()
        self.window.title("08. EditIT")
        create_shape_button = tk.Button(self.window, text="Create Random Shape", font=("Calibri", 26), command=self.create_random_shape)
        create_shape_button.pack()
        output_shapes_button = tk.Button(self.window, text="Output Shapes", font=("Calibri", 26))
        output_shapes_button.pack()

    def start(self):
        self.window.mainloop()


program = ShapeCreator()
program.start()
