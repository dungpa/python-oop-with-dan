# Edit this program by drawing many white squares to the dark blue rectangle
# - They should form windows on a skyscraper
import tkinter as tk


class SkyscraperDrawer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("10. EditIT")
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_rectangle(150, 0, 350, 500, fill="#222266")

    def start(self):
        self.window.mainloop()


program = SkyscraperDrawer()
program.start()
