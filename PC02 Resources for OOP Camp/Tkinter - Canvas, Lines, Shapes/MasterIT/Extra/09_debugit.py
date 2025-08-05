# Fix the errors in this program
# - It should show a tkinter Window that contains a Canvas
#   = The canvas should draw a red car with black wheels
import tkinter as tk


class CarDrawer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("09. DebugIT")
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_oval(20, 250, 170, 400, fill="#000000")
        self.canvas.create_oval(330, 250, 480, 400, fill="#000000")
        self.canvas.create_rectangle(0, 200, 500, 350, fill="#228822")
        self.canvas.create_arc(0, 150, 200, 250, start=90, extent=90, fill="#FFFFFF")
        self.canvas.create_rectangle(100, 150, 500, 200, fill="#228822")

    def start(self):
        self.window.mainloop()


program = CarDrawer()
program.start()
