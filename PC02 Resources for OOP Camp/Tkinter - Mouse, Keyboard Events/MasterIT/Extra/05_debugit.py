# Fix the errors in this program
# - It should show a user interface with a Window and a Label
# - Clicking on the Label should output "Hello World!" to the console
import tkinter as tk


class HelloProgram:
    def output_hello(self, event):
        print("Hello World!")

    def __init__(self):
        self.window = tk.Window()
        self.window.title("05. DebugIT")
        label = tk.Text(self.window, text="Click Me", font=("Calibri", 46), bg="#222266", fg="#FFFFFF")
        label.pack()
        label.bind("<Button-1>", self.output_hello)

    def start(self):
        self.window.mainloop()


program = HelloProgram()
program.start()
