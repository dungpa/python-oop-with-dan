# Fix the errors in this program
# - It should a UI with a Label and a Button
#   = Clicking on the Button should show a random fact in the Label
import tkinter as tk
import random


class RandomFactProgram:
    def show_random_fact(self):
        self.fact_label.config(text=random.choice(self.facts))

    def __init__(self):
        self.facts = [
            "The Eiffel Tower can be 15 cm taller during the summer",
            "Australia is wider than the moon",
            "Human teeth are the only part of the body that cannot heal themselves",
            "Baby rabbits are called kits",
            "The Spanish national anthem has no words",
            "Queen Elizabeth II is a trained mechanic",
            "Ketchup was once sold as medicine",
            "Venus is the only planet to spin clockwise"
        ]
        self.window = tk.Tk()
        self.window.title("11. DebugIT")
        self.fact_label = tk.Label(self.window, text="Random fact here...", font=("Calibri", 26))
        self.fact_label.pack()
        button = tk.Button(self.window, text="Show Random Fact", font=("Calibri", 18), on_click=self.show_random_fact())
        button.pack()

    def start(self):
        self.window.mainloop()


program = RandomFactProgram()
program.start()
