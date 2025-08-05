# Edit the StudentRegister class by adding two Buttons to the user interface
# - One Button should call a new instance function which appends a Student object to the students list
#   = Get the name and school year values from the correct Entry objects
# - The other Button should call a new instance function which loops through all the Student objects in the students list and outputs them
#   = It should output the name and school year of each Student in a bullet point list, in the format "Student Name: (7)"
# Run the program and make sure you can register new Students and output the Student register with the two Buttons you added
import tkinter as tk


class Student:
    def __init__(self, name: str, school_year: int):
        self.name = name
        self.school_year = school_year


class StudentRegister:
    def __init__(self):
        self.students = []
        self.window = tk.Tk()
        self.window.title("10. CodeIT")
        self.student_name_label = tk.Label(self.window, text="Student Name", font=("Calibri", 18))
        self.student_name_label.pack()
        self.student_name_field = tk.Entry(self.window, font=("Consolas", 16))
        self.student_name_field.pack()
        self.student_school_year_label = tk.Label(self.window, text="School Year", font=("Calibri", 18))
        self.student_school_year_label.pack()
        self.student_school_year_field = tk.Entry(self.window, font=("Consolas", 16))
        self.student_school_year_field.pack()

    def start(self):
        self.window.mainloop()


program = StudentRegister()
program.start()
