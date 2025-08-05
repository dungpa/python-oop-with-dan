# Fix the errors in this program
# - It should show a GUI for a login form (containing a username/password field)
import tkinter as tk


class LoginForm:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Some Scores")
        self.username_label = tk.Label(self.window, "Username")
        self.username_label.pack()
        self.username_field = tk.Entry(self.window)
        self.username_field.pack()
        self.password_label = tk.Label(self.window, "Password")
        self.password_label.pack()
        self.password_field = tk.Entry(self.window)
        self.password_field.pack()

    def start(self):
        self.window.mainloop()


program = LoginForm()
program.start()
