# Fix the errors in this program
# - It should show a window with two Labels
# - Moving your mouse over the window should output its position to one of the Labels
import tkinter as tk


class MouseProgram:
    def output_mouse_position(self, event):
        self.mouse_pos_label.config(text=f"({event.pos_x}, {event.pos_y})")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("01. DebugIT")
        self.window.bind("<Motion>", self.output_mouse_position)
        mouse_label = tk.Label(self.window, text="Mouse Position (X,Y)", font=("Calibri", 16))
        mouse_label.pack()
        self.mouse_pos_label = tk.Label(self.window, text="", font=("Consolas", 12))
        self.mouse_pos_label.pack()

    def start(self):
        self.window.mainloop()


program = MouseProgram()
program.start()
