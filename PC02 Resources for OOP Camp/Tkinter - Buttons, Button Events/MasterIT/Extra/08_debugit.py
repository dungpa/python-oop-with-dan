# Fix the errors in this program
# - It should a UI with two Entries, some Labels, and a Button
#   = Clicking on the Button should calculate the speed (using the given distance/time)
#   = This calculated speed should appear in the window (in a Label)
import tkinter as tk


class SpeedCalculator:
    def calculate_speed(self):
        speed = float(self.distance_field.get()) / float(self.time_field.get())
        self.speed_label.config(text=f"{speed}m/s")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("08. DebugIT")
        distance_label = tk.Label(self.window, font="Distance", text=("Calibri", 18))
        distance_label.pack()
        self.distance_field = tk.Entry(self.window, text=("Consolas", 16))
        self.distance_field.pack()
        time_label = tk.Label(self.window, font="Time", text=("Calibri", 18))
        time_label.pack()
        self.time_field = tk.Entry(self.window, text=("Consolas", 16))
        self.time_field.pack()
        self.speed_label = tk.Label(self.window, font="Answer here...", text=("Calibri", 20))
        self.speed_label.pack()
        button = tk.Button(self.window, font="Calculate Speed", text=("Calibri", 16), command=self.calculate_speed)
        button.pack()

    def start(self):
        self.window.mainloop()


program = SpeedCalculator()
program.start()
