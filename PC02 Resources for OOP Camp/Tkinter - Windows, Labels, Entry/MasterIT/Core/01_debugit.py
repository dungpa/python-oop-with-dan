# Fix the errors in this program
# - It should show a GUI for information about a person (including their name, age, and hobby)
class PersonProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("About Me")
        self.name_label = tk.Label(self.window, text="Name: Tutor", font=("Consolas", 18))
        self.name_label.pack()
        self.age_label = tk.Label(self.window, text="Age: 24", font=("Consolas", 18))
        self.age_label.pack()
        self.hobby_label = tk.Label(self.window, text="Hobby: Programming", font=("Consolas", 18))
        self.hobby_label.pack()

    def start(self):
        self.window.mainloop()


program = PersonProgram()
program.start()
