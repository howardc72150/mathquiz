from tkinter import *
from functools import partial

class Start:
    def __init__(self, root):
        canvas = Canvas(root, width=600, height=615)
        canvas.create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')

        self.baseFrame = Frame(width=600, height=615)
        self.baseFrame.grid()

        

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("test gui")
    var = Start(root)
    root.mainloop()  