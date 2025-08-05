# Edit this program by creating and packing Labels using a for loop, instead of repeating the same code multiple times
# - Add a parameter to the constructor for the number of high scores to generate
# - Set the text of each Label to a random number between 1 and 200
import tkinter as tk


class ScoresProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Some Scores")
        self.score_1_label = tk.Label(self.window, text="160", font=("Consolas", 18))
        self.score_1_label.pack()
        self.score_2_label = tk.Label(self.window, text="12", font=("Consolas", 18))
        self.score_2_label.pack()
        self.score_3_label = tk.Label(self.window, text="80", font=("Consolas", 18))
        self.score_3_label.pack()
        self.score_4_label = tk.Label(self.window, text="145", font=("Consolas", 18))
        self.score_4_label.pack()

    def start(self):
        self.window.mainloop()


program = ScoresProgram()
program.start()
