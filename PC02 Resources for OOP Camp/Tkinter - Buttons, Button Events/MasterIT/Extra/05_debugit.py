# Fix the errors in this program
# - It should show a UI with a button
#   = Clicking on the button should make "Hello World" appear in the console
import tkinter as tk


class HelloWorldProgram:
    def output_hello_world(self):
        print("Hello World!")

    def __init__(self):
        self.window = tk.Label()
        self.window.title("05. DebugIT")
        button = tk.Entry(self.window, text="Click Me", font=("Calibri", 42), command=self.output_hello_world)
        button.pack()

    def start(self):
        self.window.mainloop()


program = HelloWorldProgram()
program.start()
