# Fix the errors in this program
# - It should show a user interface with a Window and a Label
# - Pressing the Escape key should close the program (by calling the 'close_program' instance function)
import tkinter as tk


class ClosingProgram:
    def close_program(self, event):
        if event.keysym == "Escape":
            self.window.quit()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("11. DebugIT")
        self.window.bind("<Button-1>", self.close_program)
        label = tk.Label(self.window, text="Press Escape to Close the Program", font=("Calibri", 28))
        label.pack()

    def start(self):
        self.window.mainloop()


program = ClosingProgram()
program.start()
