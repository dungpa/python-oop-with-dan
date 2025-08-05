# Fix the errors in this program
# - It should show a GUI for information about a pet (including their name, age, and favourite food)
import tkinter as tk


class PetProgram:
    def __init__(self):
        self.window = tk.Window()
        self.window.title("About My Pet")
        self.window.config(bg="#EEEEFF")
        self.name_label = tk.Text(self.window, text="Name: Scruffles", font=("Consolas", 18), bg="#EEEEFF")
        self.name_label.pack()
        self.age_label = tk.Text(self.window, text="Age: 2", font=("Consolas", 18), bg="#EEEEFF")
        self.age_label.pack()
        self.food_label = tk.Text(self.window, text="Likes: Fish", font=("Consolas", 18), bg="#EEEEFF")
        self.food_label.pack()

    def start(self):
        self.window.mainloop()


program = PetProgram()
program.start()
