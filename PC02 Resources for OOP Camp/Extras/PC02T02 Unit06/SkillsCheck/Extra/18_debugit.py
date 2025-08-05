# Fix the errors in this program
# - It should show a UI with an Entry, a Label, and a Button
#   = When the Button is clicked, it doubles the number in the Entry and shows the result in the Label
import tkinter as tk


class DoublingProgram:
    def double_number()
        number = float(self.number_field.get())
        result = number * 2
        self.answer_label.config(text=f"{result}")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("18. DebugIT")
        self.number_field = tk.Entry(self.window, font=("Consolas", 18))
        self.number_field.pack()
        self.answer_label = tk.Label(self.window, text="Result here...", font=("Consolas", 18))
        self.answer_label.pack()
        button = tk.Button(self.window, text="Double", font=("Calibri", 18), command=self.double_number())
        button.pack()

    def start(self):
        self.window.mainloop()


program = DoublingProgram()
program.start()
