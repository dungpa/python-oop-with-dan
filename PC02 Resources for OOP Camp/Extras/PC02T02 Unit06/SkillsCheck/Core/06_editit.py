# Edit this program by connecting the Button to an instance function
# - This instance function should retrieve the input from the 'colour_field' Entry
# - It should then use that retrieved value as the hexadecimal colour for the Button's background
import tkinter as tk


class ButtonColourChanger:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("06. EditIT")
        self.colour_field = tk.Entry(self.window, font=("Consolas", 12))
        self.colour_field.pack()
        self.colour_button = tk.Button(self.window, text="Change Colour", font=("Calibri", 16))
        self.colour_button.pack()

    def start(self):
        self.window.mainloop()


program = ButtonColourChanger()
program.start()
