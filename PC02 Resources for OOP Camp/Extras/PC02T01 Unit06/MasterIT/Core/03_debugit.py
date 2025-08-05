# Fix the errors in this program
# - It should define a 'Line' class
#   = This class contains a constructor with four parameters and declares two instance variables (lists) for those four parameters
#   = It also contains the string conversion dunder function which outputs the start/end lists in a neatly formatted string
# - It then instantiates a Line object and outputs it
class Line:
    def __init__(self, start_x: int, start_y: int, end_x: int, end_y: int):
        self.start = [start_x, start_y]
        self.end = [end_x, end_y]

    def __str self) str:
        return f"{self.start} --> {self.end}"


my_line =  Line(0, 0, 50, 80)
print(my_line)
