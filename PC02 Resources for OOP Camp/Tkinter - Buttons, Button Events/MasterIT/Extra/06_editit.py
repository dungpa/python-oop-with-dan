# Edit this program by connecting the button to an instance function
# - This instance function should find the larger of the two numbers input in the two Entry objects
# - The largest number should be shown in the answer Label object
import tkinter as tk


class GetLargerProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("06. EditIT")
        self.num_1_field = tk.Entry(self.window, font=("Consolas", 18))
        self.num_1_field.pack()
        self.num_2_field = tk.Entry(self.window, font=("Consolas", 18))
        self.num_2_field.pack()
        self.answer_label = tk.Label(self.window, text="Answer goes here...", font=("Calibri", 22))
        self.answer_label.pack()
        button = tk.Button(self.window, text="Find Largest Number", font=("Calibri", 18))
        button.pack()

    def start(self):
        self.window.mainloop()


program = GetLargerProgram()
program.start()
