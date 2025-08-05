# Fix the errors in this program
# - It should show a window with a Canvas
# - Pressing the Space Bar should draw a  red rectangle at a random position on the Canvas
class RectangleDrawer:
    def draw_rectangle(self, event):
        if event.keysym == "space":
            pos_x = random.randint(0, 350)
            pos_y = random.randint(0, 350)
            self.canvas.create_rectangle(pos_x, pos_y, pos_x + 50, pos_y + 50, fill="#FF0000")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("01. DebugIT")
        self.window.bind("<KeyPress>", self.draw_rectangle)
        self.canvas = tk.Canvas(self.window, bg="#FFFFFF", width=400, height=400)
        self.canvas.pack()

    def start(self):
        self.window.mainloop()


program = RectangleDrawer()
program.start()
