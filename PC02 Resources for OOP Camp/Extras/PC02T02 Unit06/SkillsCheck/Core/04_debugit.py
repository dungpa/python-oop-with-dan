# Fix the errors in this program
# - It should show a UI with a Button
#   = Clicking on the Button should output "Hello World!" to the console
import tkinter as tk


class HelloWorldProgram:
    def output_hello(self):
        print("Hello World!")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("04. DebugIT")
        hello_button = tk.Button(self.window, contents="Click Me", bg=("Calibri", 22), event=self.output_hello)
        hello_button.pack()

    def start(self):
        self.window.mainloop()


program = HelloWorldProgram()
program.start()
