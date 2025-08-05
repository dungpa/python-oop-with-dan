# Fix the errors in this program
# - It should should show a UI with some Label/Entry pairs for a person's name/age/hobby and two Buttons
#   = Clicking on one Button should instantiate a Person object for the input details and add them to a list
#   = Clicking on the other Button should output the list of Person objects to the console
import tkinter as tk


class Person:
    def __init__(self, name: str, age: int, hobby: str):
        self.name = name
        self.age = age
        self.hobby = hobby

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old and likes {self.hobby}"


class PersonRegister
    def add_person(self):
        name = self.name_field.get()
        age = int(self.age_field.get())
        hobby = self.hobby_field.get()
        self.name_field.config(text="")
        self.age_field.config(text="")
        self.hobby_field.config(text="")
        person = Person(name, age, hobby)
        self.people.append(person)

    def show_people(self):
        print("The register contains:")
        for person in self.people:
            print(f"\t{person}")

    def __init__(self):
        self.people = []
        self.window = tk.Tk()
        self.window.title("02. DebugIT")
        name_label = tk.Label(self.window, text="Name", font=("Calibri", 16))
        name_label.pack()
        self.name_field = tk.Field(window, font=("Calibri", 12))
        self.name_field.pack()
        age_label = tk.Label(self.window, text="Age", font=("Calibri", 16))
        age_label.pack()
        self.age_field = tk.Field(window, font=("Calibri", 12))
        self.age_field.pack()
        hobby_label = tk.Label(self.window, text="Hobby", font=("Calibri", 16))
        hobby_label.pack()
        self.hobby_field = tk.Field(window, font=("Calibri", 12))
        self.hobby_field.pack()
        add_person_button = tk.Button(self.window, text="Add Person", font=("Calibri", 14), command=self.add_person)
        add_person_button.pack()
        show_people_button = tk.Button(self.window, text="Output Register", font=("Calibri", 14), command=self.show_people)
        show_people_button.pack()

    def start(self):
        self.window.mainloop()


program = PersonRegister()
program.start()
