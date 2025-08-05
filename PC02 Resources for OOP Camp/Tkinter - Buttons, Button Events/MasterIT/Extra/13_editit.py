# Edit this program by adding a 'Login' Button to the bottom of the window
# - When clicked, the program should check if the Username and Password fields contain "student" and "password"
#   = If they do, output "Logged in!" to the console
#   = Otherwise, output "Incorrect username/password" to the console
import tkinter as tk


class LoginForm:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("13. EditIT")
        title_label = tk.Label(self.window, text="Login", font=("Calibri", 22))
        title_label.pack()
        username_label = tk.Label(self.window, text="Username", font=("Calibri", 16))
        username_label.pack()
        self.username_field = tk.Entry(self.window, font=("Consolas", 12))
        self.username_field.pack()
        password_label = tk.Label(self.window, text="Password", font=("Calibri", 16))
        password_label.pack()
        self.password_field = tk.Entry(self.window, font=("Consolas", 12))
        self.password_field.pack()

    def start(self):
        self.window.mainloop()


program = LoginForm()
program.start()
