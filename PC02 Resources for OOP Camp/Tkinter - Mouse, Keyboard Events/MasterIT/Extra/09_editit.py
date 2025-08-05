# Edit this program by binding a key press event to the Window
# - When a key is pressed and it is the Space Bar, delete all the drawings in the Canvas
#   = All Canvas drawings can be deleted by using the instruction 'self.canvas.delete("all")'
import tkinter as tk


class RectangleDrawer:
    def draw_rectangle(self, event):
        self.canvas.create_rectangle(event.x - 20, event.y - 20, event.x + 20, event.y + 20, fill="#33BB33")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("09. EditIT")
        self.canvas = tk.Canvas(self.window, bg="#FFFFFF", width=400, height=400)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.draw_rectangle)

    def start(self):
        self.window.mainloop()


program = RectangleDrawer()
program.start()
