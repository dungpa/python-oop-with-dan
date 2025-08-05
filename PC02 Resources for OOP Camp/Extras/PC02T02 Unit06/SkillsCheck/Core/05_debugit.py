# Fix the errors in this program
# - It should show a UI with a Button
#   = Clicking on the Button should output a random integer (between 0 and 9) to the console
import tkinter as tk
import random


class RandomWordProgram:
    def output_number(self):
        print(random.randint(0, 9))

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("05. DebugIT")
        hello_button = tk.Button(self.window, contents="Click Me", bg=("Calibri", 22), event=self.output_number())
        hello_button.pack()

    def start(self):
        self.window.mainloop()


program = RandomWordProgram()
program.start()
