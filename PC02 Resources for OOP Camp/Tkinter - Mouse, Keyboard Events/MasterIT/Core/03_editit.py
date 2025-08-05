# Edit this program by binding the 'draw_circle' instance function to a left click on the Canvas
# - This should make it draw a yellow circle wherever you left click on the Canvas
import tkinter as tk


class CircleDrawer:
    def draw_circle(self, event):
        self.canvas.create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20, fill="#FFFF00")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("01. DebugIT")
        self.canvas = tk.Canvas(self.window, bg="#FFFFFF", width=400, height=400)
        self.canvas.pack()

    def start(self):
        self.window.mainloop()


program = CircleDrawer()
program.start()
