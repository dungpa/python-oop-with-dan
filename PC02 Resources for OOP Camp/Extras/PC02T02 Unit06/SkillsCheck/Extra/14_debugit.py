# Fix the errors in this program
# - It should should show a UI with a Label and a Button
#   = Clicking on the Button should show a fact about Dogs in the Label
import tkinter


class DogFacts:
    def next_fact(self):
        self.fact_label.config(text=self.facts[self.fact_index])
        self.fact_index = (self.fact_index + 1) % len(self.facts)

    def __init__(self):
        self.facts = [
            "Dogs have a sense of smell at least 40-times better than ours",
            "Some dogs can sniff out medical problems",
            "Dogs can be left-pawed or right-pawed",
            "Dogs have 18 muscles controlling their ears",
            "Dogs are about as intelligent as a two-year-old"
        ]
        self.fact_index = 0
        self.window = tk.Tk()
        self.window.title("14. DebugIT")
        self.fact_label = tk.Label(self.window, text="Facts here...", font=("Calibri", 22))
        self.fact_label.pack()
        button = tk.Button(self.window, text="Next Fact", font=("Calibri", 16), command=self.next_fact)
        button.pack()

    def start(self):
        self.window.mainloop()


program = DogFacts()
program.start()
