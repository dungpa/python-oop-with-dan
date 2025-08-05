# Fix the errors in this program
# - It should should show a UI with a Label and a Button
#   = Clicking on the Button should show a fact about a food in the Label
import tkinter as tk


class FoodFacts:
    def next_fact(self):
        self.fact_label.config(text=self.facts[self.fact_index])
        self.fact_index = (self.fact_index + 1) % len(self.facts)

    def __init__(self):
        self.facts = [
            "Broccoli contains more protein than steak",
            "Apples give you more energy than coffee",
            "Pecans are rich with antioxidants",
            "Pistachios are actually fruits",
            "Bananas are berries"
        ]
        self.fact_index = 0
        self.window = tk.Tk()
        self.window.title("02. DebugIT")
        self.fact_label = tk.TextLabel(self.window, contents="Facts here...", appearance=("Calibri", 22))
        self.fact_label.pack()
        button = tk.Button(self.window, text="Next Fact", font=("Calibri", 16))
        button.pack()

    def start(self):
        self.window.mainloop()


program = FoodFacts()
program.start()
