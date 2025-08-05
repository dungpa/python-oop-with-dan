# Add the string dunder function to this class
# It should return a string that outputs the Subject's:
# - name
# - teacher
# - num_times_a_week
# The string should look like this (including new lines)
# My Maths lessons:
#   The teacher is Mrs Band
#   I have lessons 3 times a week
class Subject:
    def __init__(self, name: str, teacher: str, num_times_a_week: int):
        self.name = name
        self.teacher = teacher
        self.num_times_a_week = num_times_a_week


my_subject = Subject("Maths", "Mrs Band", 3)
print(my_subject)
