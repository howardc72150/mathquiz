from tkinter import *
from functools import partial

class Start:
    def __init__(self, root):
        self.frame = Frame()
        self.frame.grid()
        self.headingFrame           = Frame(self.frame, width=500, height=18, bg="#CCE5FF")
        self.underHeadingFrame      = Frame(self.frame, width=500, height=6, bg="#BDDEFF")
        self.blankFrame             = Frame(self.frame, height=40, width=500)
        self.labelBackgroundFrame   = Frame(self.frame, height=150, width=500, bg="white")
        self.headingLabel           = Label(self.labelBackgroundFrame, height=3, width=41, text="Math Quiz", font=("Helvetica 15 bold"), 
                                            fg="#6C6C6C", justify=CENTER, bg="white")
        self.underLabelFrame        = Frame(self.frame, width=500, height=7, bg="#E8E8E8")
        self.startGameButton        = Button(self.frame, text="PLAY", font=("Helvetica 15 bold"), fg="#747475", border=0, command=lambda: self.toGame())

        self.headingLabel.grid()
        self.headingFrame.grid(row=0)
        self.underHeadingFrame.grid(row=1)
        self.blankFrame.grid(row=2)
        self.labelBackgroundFrame.grid(row=3)
        self.underLabelFrame.grid(row=4)
        self.startGameButton.grid(row=6, pady=50)

    def toGame(self):
        self.frame.destroy()
        Game()
        
class Game:
    def __init__(self):
        self.frame = Frame(width=500, height=600, )
        self.frame.grid()


        self.heading_frame = Frame(self.frame, width=500, height=65, bg="#CCE5FF")
        self.under_heading_frame = Frame(self.frame, width=500, height=6, bg="#BDDEFF")
        self.heading_label = Label(self.heading_frame, text="Math Quiz", font=("Helvetica 15"),
                                   fg="#6C6C6C", bg="#CCE5FF", width=45, height=2, justify=CENTER)
        self.info_frame = Frame(self.frame, width=500, height=100)
        self.question_info_frame = Frame(self.frame, width=500, height=80, bg="white")
        self.question_label = Label(self.question_info_frame, bg="white", width=62, height=5, text="What is 5+4?", font=("Helvetica 10"), justify=CENTER)
        self.under_question_info_frame = Frame(self.frame, width=500, height=5, bg="#E8E8E8")
        self.blank_frame = Frame(self.frame, width=500, height=40)
        self.user_input = Entry(width=30)
        self.test = Button(text="help")

        self.heading_label.grid(row=1)
        self.heading_frame.grid(row=1)
        self.under_heading_frame.grid(row=2)
        self.info_frame.grid(row=3)
        self.question_info_frame.grid(row=4)
        self.question_label.grid(row=4)
        self.under_question_info_frame.grid(row=5)
        self.blank_frame.grid(row=6)
        self.user_input.grid(row=7)
        self.test.grid(row=8)
        
        


gui = Tk()
gui.title("Math Quiz")
var = Start(gui)
gui.mainloop()  