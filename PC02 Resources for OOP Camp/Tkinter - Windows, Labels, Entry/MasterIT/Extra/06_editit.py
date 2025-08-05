# Edit this program by adding text fields to the Email and Username labels
import tkinter as tk


class RegistrationForm:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Some Scores")
        self.email_label = tk.Label(self.window, text="Email", font=("Calibri", 22))
        self.email_label.pack()
        self.username_label = tk.Label(self.window, text="Username", font=("Calibri", 22))
        self.username_label.pack()

    def start(self):
        self.window.mainloop()


program = RegistrationForm()
program.start()
