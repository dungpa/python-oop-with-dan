# Fix the errors in this program
# - It should show a tkinter Window that contains a Canvas
#   = The Canvas draws a blue oval in the top left corner
#   = That blue oval should move around the Canvas on its own
import tkinter as tk


class CircleMovingProgram:
    def move_circle(self):
        movement = 0.0016 * 900
        self.movement_time += 0.0016
        if self.moving_direction == 0:
            self.canvas.move(self.circle, movement, 0)
        elif self.moving_direction == 1:
            self.canvas.move(self.circle, 0, movement)
        elif self.moving_direction == 2:
            self.canvas.move(self.circle, -movement, 0)
        else:
            self.canvas.move(self.circle, 0, -movement)
        if self.movement_time >= 0.5:
            self.movement_time = 0
            self.moving_direction = (self.moving_direction + 1) % 4
        self.window.after(16, self.move_circle)

    def __init__(self):
        self.moving_direction = 0
        self.movement_time = 0
        self.window = tk.Tk()
        self.window.title("02. DebugIT")
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.circle = self.canvas.create_rectangle(0, 0, 50, 50, fill="#FFFF00")
        self.window.after(16, self.move_circle)

    def start(self):
        self.window.mainloop()


program = CircleMovingProgram()
program.start()
