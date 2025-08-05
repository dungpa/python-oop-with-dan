# Edit this program by adding a Button to the bottom of the window
# - The Button should call an instance function when clicked
#   = This instance function should show "Registered" in the 'title_label' Label object
import tkinter as tk


class RegisterForm:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("10. EditIT")
        self.title_label = tk.Label(self.window, text="Enter your Username/Password", font=("Calibri", 20))
        self.title_label.pack()
        username_label = tk.Label(self.window, text="Username", font=("Calibri", 18))
        username_label.pack()
        self.username_field = tk.Entry(self.window, font=("Consolas", 16))
        self.username_field.pack()
        password_label = tk.Label(self.window, text="Password", font=("Calibri", 18))
        password_label.pack()
        self.password_field = tk.Entry(self.window, font=("Consolas", 16))
        self.password_field.pack()

    def start(self):
        self.window.mainloop()


program = RegisterForm()
program.start()
