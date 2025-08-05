# Edit this program by drawing an arc whenever the user left clicks on the Canvas
# - Get the start and extent angles of the arc from the 'self.start_field' and 'self.extent_field' Entry objects
import tkinter as tk


class ArcDrawer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("12. DebugIT")
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="#FFFFFF")
        self.canvas.pack()
        start_label = tk.Label(self.window, text="Start Angle", font=("Calibri", 22))
        start_label.pack()
        self.start_field = tk.Entry(self.window, font=("Consolas", 18))
        self.start_field.pack()
        extent_label = tk.Label(self.window, text="Extent Angle", font=("Calibri", 22))
        extent_label.pack()
        self.extent_field = tk.Entry(self.window, font=("Consolas", 18))
        self.extent_field.pack()

    def start(self):
        self.window.mainloop()


program = ArcDrawer()
program.start()
