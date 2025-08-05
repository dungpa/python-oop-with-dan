# Fix the errors in this program
# - It should show a tkinter Window that contains a Canvas and a Button
#   = The Canvas draws a red rectangle
#   = Clicking the Button should change the rectangle's colour
import tkinter as tk


class ColourChangingRectangle:
    def change_colour(self):
        self.colour_index = (self.colour_index + 1) % len(self.colours)
        self.canvas.itemconfig(self.rectangle, fill=self.colours[self.colour_index])

    def __init__(self):
        self.colours = ["#FFAAAA", "#AAFFAA", "#AAAAFF"]
        self.colour_index = 0
        self.window = tk.Tk()
        self.window.title("01. DebugIT")
        self.canvas = tk.Canvas(self.window, width=0, height=0)
        self.canvas.pack()
        self.rectangle = self.canvas.create_rectangle(100, 100, 400, 400, fill=self.colours[self.colour_index])
        self.button = tk.Button(self.window, text="Change Rectangle Colour", font=("Calibri", 32), command=self.change_colour)
        self.button.pack()

    def start(self):
        self.window.mainloop()


program = ColourChangingRectangle()
program.start()
