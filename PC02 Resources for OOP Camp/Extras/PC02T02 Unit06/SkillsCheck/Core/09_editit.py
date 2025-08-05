# Edit this program by instantiating a Button object, showing it in the UI, and connecting it to an instance function
# - The instance function should close the program
#   = The program can be closed using the 'self.window.quit()' function
import tkinter as tk


class ClosingProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("09. EditIT")
        label = tk.Label(self.window, text="Simple Closing Program", font=("Calibri", 22))
        label.pack()

    def start(self):
        self.window.mainloop()


program = ClosingProgram()
program.start()
