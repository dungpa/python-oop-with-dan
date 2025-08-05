# Edit the 'check_correct_button' instance function in the 'ButtonProgram' class
# - It should check if the 'button_number' parameter is equal to the 'self.button_to_click' instance variable
#   = This means the user clicked correct (with a Left Click or a Right Click)
# - If they are correct:
#   = Output "Good Job!" to the console
#   = Generate a new random integer (0 or 1) and store it in 'self.button_to_click'
#   = Check if this new random integer is 0
#       == If so, show "Click the Left Button" in the 'self.button_label'
#       == Otherwise, show "Click the Right Button" in the 'self.button_label'
# - If they are not correct:
#   = Output "Incorrect! Ending the program"
#   = End the program by calling the 'quit' function on the Window
import random
import tkinter as tk


class ButtonProgram:
    def check_correct_button(self, button_number: int):
        pass

    def click_left_button(self, event):
        self.check_correct_button(0)

    def click_right_button(self, event):
        self.check_correct_button(1)

    def __init__(self):
        self.button_to_click = 0
        self.window = tk.Tk()
        self.window.title("06. EditIT")
        self.button_label = tk.Label(self.window, text="Click the Left Button", font=("Calibri", 64))
        self.button_label.pack()
        self.button_label.bind("<Button-1>", self.click_left_button)
        self.button_label.bind("<Button-3>", self.click_right_button)

    def start(self):
        self.window.mainloop()


program = ButtonProgram()
program.start()
