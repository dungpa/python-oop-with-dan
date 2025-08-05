# Fix the errors in this program
# - It should show a user interface with a Window and a Canvas
# - Left clicking on the Canvas starts a 'drag' (which draws a line)
# - Right clicking on the Canvas ends a 'drag' (which stops drawing a line)
import tkinter as tk


class LineDrawer:
    def start_drag(self, event):
        self.dragging = True

    def end_drag(self, event):
        self.dragging = False

    def draw_line(self, event):
        if self.dragging:
            self.canvas.create_line(self.previous_position[0], self.previous_position[1], event.x, event.y, width=4)
        self.previous_position = [event.x, event.y]

    def __init__(self):
        self.previous_position = []
        self.dragging = False
        self.window = tk.Tk()
        self.window.title("08. DebugIT")
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="#FFFFFF")
        self.canvas.pack()
        self.canvas.bind("<LeftClick>", self.start_drag)
        self.canvas.bind("<RightClick>", self.end_drag)
        self.canvas.bind("<Move>", self.draw_line)

    def start(self):
        self.window.mainloop()


program = LineDrawer()
program.start()
