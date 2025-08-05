# Fix the errors in this program
# - It should show a UI with a button
#   = Clicking on that button should change the button's colour randomly
class ColourChangingProgram:
    def change_colour(self):
        self.button.config(bg="#{:02x}{:02x}{:02x}".format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ))

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("01. DebugIT")
        self.button = tk.Button(self.window, text="Change Colour", font=("Calibri", 42), command=self.change_colour)
        self.button.pack()

    def start(self):
        self.window.mainloop()


program = ColourChangingProgram()
program.start()
