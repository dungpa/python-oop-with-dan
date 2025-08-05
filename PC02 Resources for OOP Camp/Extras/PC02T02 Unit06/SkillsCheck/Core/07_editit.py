# Edit this program by connecting the Button to an instance function
# - It should generate a random number between 0 and 9
#   = This number should be shown in the 'random_number_label'
# - Get the value from the 'guess_field' and check if it matches the randomly generated integer
#   = If so, output "Correct!" to the console
#   = Otherwise, output "Incorrect..." to the console
import tkinter as tk


class RandomNumberGuesser:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("07. EditIT")
        self.random_number_label = tk.Label(self.window, text="Random numbers go here...", font=("Consolas", 16))
        self.random_number_label.pack()
        self.guess_field = tk.Entry(self.window, font=("Consolas", 16))
        self.guess_field.pack()
        button = tk.Button(self.window, text="Next Guess", font=("Calibri", 16))
        button.pack()

    def start(self):
        self.window.mainloop()


program = RandomNumberGuesser()
program.start()
