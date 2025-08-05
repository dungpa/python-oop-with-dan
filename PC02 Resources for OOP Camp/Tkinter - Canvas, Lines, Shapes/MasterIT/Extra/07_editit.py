# Edit this program by drawing red ovals in the tree to represent apples
import tkinter as tk


class TreeDrawer:
    def __init__(self):
        self.moving_direction = 0
        self.movement_time = 0
        self.window = tk.Tk()
        self.window.title("07. EditIT")
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_rectangle(200, 100, 300, 500, fill="#996600")
        self.canvas.create_oval(130, 20, 350, 240, fill="#009933")
        self.canvas.create_oval(30, 120, 250, 340, fill="#009933")
        self.canvas.create_oval(230, 120, 450, 340, fill="#009933")

    def start(self):
        self.window.mainloop()


program = TreeDrawer()
program.start()
