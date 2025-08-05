# Edit this program by connecting the Button to an instance function
# - This instance function should retrieve the values from the 'num_1_field' and 'num_2_field' Entry objects
# - It should then convert those values to float values and add them together to get the correct result
# - This result should be shown in the 'answer_label' Label object
import tkinter as tk


class SumProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("03. EditIT")
        self.num_1_field = tk.Entry(self.window, font=("Consolas", 18))
        self.num_1_field.pack()
        self.num_2_field = tk.Entry(self.window, font=("Consolas", 18))
        self.num_2_field.pack()
        self.answer_label = tk.Label(self.window, text="Answer goes here...", font=("Calibri", 22))
        self.answer_label.pack()
        button = tk.Button(self.window, text="Add", font=("Calibri", 18))
        button.pack()

    def start(self):
        self.window.mainloop()


program = SumProgram()
program.start()
