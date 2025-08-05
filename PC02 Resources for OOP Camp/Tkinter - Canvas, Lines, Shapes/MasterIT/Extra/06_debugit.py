# Fix the errors in this program
# - It should show a tkinter Window that contains a Canvas
#   = The Canvas draws a four green rectangles to form a border around the Canvas
class BorderDrawer
    def init(self):
        self.moving_direction = 0
        self.movement_time = 0
        self.window = tk.Tk()
        self.window.title("06. DebugIT")
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, 500, 50, fill="#AAFFAA")
        self.canvas.create_rectangle(450, 0, 500, 500, fill="#AAFFAA")
        self.canvas.create_rectangle(0, 450, 500, 500, fill="#AAFFAA")
        self.canvas.create_rectangle(0, 0, 50, 500, fill="#AAFFAA")

    def start(self):
        self.window.mainloop()


program = BorderDrawer()
program.start()
