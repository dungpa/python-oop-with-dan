# Edit the 'draw_rectangle' instance function in the 'RandomRectangleDrawer' class
# - This function should draw a rectangle at a random position in the Canvas
#   = Generate a random start X/Y position
#   = Calculate the end X/Y position by adding 100 to the start X/Y
#   = Choose a random colour of red "#FF0000", green "#00FF00#", or blue "#0000FF" for the fill of the rectangle
import tkinter as tk
import random


class RandomRectangleDrawer:
    def draw_rectangle(self):
        pass

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("04. EditIT")
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.button = tk.Button(self.window, text="Draw Rectangle", font=("Calibri", 32), command=self.draw_rectangle)
        self.button.pack()

    def start(self):
        self.window.mainloop()


program = RandomRectangleDrawer()
program.start()
