# Fix the errors in this program
# - It should should show a UI with a Label and a Button
#   = Clicking on the Button should show a fact about a country in the Label
class CountryFacts:
    def next_fact(self):
        self.fact_label.config(text=self.facts[self.fact_index])
        self.fact_index = (self.fact_index + 1) % len(self.facts)

    def __init__(self):
        self.facts = [
            "Canada has the most lakes in the world",
            "Bolivia is the world’s flattest country",
            "Russia is the world’s largest country",
            "San Marino is the world’s oldest country"
        ]
        self.fact_index = 0
        self.window = tk.Tk()
        self.window.title("01. DebugIT")
        self.fact_label = tk.Label(self.window, text="Facts here...", font=("Calibri", 22))
        self.fact_label.pack()
        button = tk.Button(self.window, text="Next Fact", font=("Calibri", 16))
        button.pack()

    def start(self):
        self.window.mainloop()


program = CountryFacts()
program.start()
