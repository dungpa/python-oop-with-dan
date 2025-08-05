# Fix the errors in this program
# - It should show a GUI with labels for 'Subject' and 'Teacher' with text fields underneath them
import tkinter as tk


class SubjectProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My Favourite Subject")
        self.subject_name_label = tk.Entry(self.window, text="Subject Name", font=("Consolas", 18))
        self.subject_name_label.pack()
        self.subject_name_field = tk.Label(self.window, font=("Consolas", 18))
        self.subject_name_field.pack()
        self.subject_teacher_label = tk.Entry(self.window, text="Teacher", font=("Consolas", 18))
        self.subject_teacher_label.pack()
        self.subject_teacher_field = tk.Label(self.window, font=("Consolas", 18))
        self.subject_teacher_field.pack()

    def start(self):
        self.window.mainloop()


program = SubjectProgram()
program.start()
