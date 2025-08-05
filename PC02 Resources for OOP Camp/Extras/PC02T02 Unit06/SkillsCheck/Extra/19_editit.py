# Edit this program by adding another Label and another Button
# - When this Button is clicked, the program should calculate the half of the number in the Entry
#   = This result should be shown in the new Label object
import tkinter as tk


class DoublingProgram:
    def double_number(self):
        number = float(self.number_field.get())
        result = number * 2
        self.answer_label.config(text=f"{result}")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("19. EditIT")
        self.number_field = tk.Entry(self.window, font=("Consolas", 18))
        self.number_field.pack()
        self.answer_label = tk.Label(self.window, text="Result here...", font=("Consolas", 18))
        self.answer_label.pack()
        button = tk.Button(self.window, text="Double", font=("Calibri", 18), command=self.double_number)
        button.pack()

    def start(self):
        self.window.mainloop()


program = DoublingProgram()
program.start()
