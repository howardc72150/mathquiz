import random
from tkinter import *
from functools import partial

class Start:
    def __init__(self, root):

        self.frame = Frame()
        self.frame.grid()
        self.headingFrame               = Frame(self.frame, width=500, height=18, bg="#CCE5FF")
        self.underHeadingFrame          = Frame(self.frame, width=500, height=6, bg="#BDDEFF")
        self.blankFrame                 = Frame(self.frame, height=40, width=500)
        self.labelBackgroundFrame       = Frame(self.frame, height=150, width=500, bg="white")
        self.headingLabel               = Label(self.labelBackgroundFrame, height=3, width=41, text="Math Quiz", font=("Helvetica 15 bold"), 
                                                fg="#6C6C6C", justify=CENTER, bg="white")
        self.underLabelFrame            = Frame(self.frame, width=500, height=7, bg="#E8E8E8")
        self.startGameButton            = Button(self.frame, text="PLAY", font=("Helvetica 15 bold"), fg="#747475", border=0, command=lambda: self.toGame())

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
            # create random math equation
        operators = ['+', '-', '*', '/']
        equation = "{} {} {}".format(random.randint(0,12), random.choice(operators), random.randint(0,12))
        self.frame = Frame(width=500, height=600)
        self.frame.grid()

        self.heading_frame              = Frame(self.frame, width=500, height=65, bg="#CCE5FF")
        self.under_heading_frame        = Frame(self.frame, width=500, height=6, bg="#BDDEFF")
        self.heading_label              = Label(self.heading_frame, text="Math Quiz", font=("Helvetica 15"),
                                                fg="#6C6C6C", bg="#CCE5FF", width=45, height=2, justify=CENTER)
        self.info_frame                 = Frame(self.frame, width=500, height=100)
        self.question_info_frame        = Frame(self.frame, width=500, height=80, bg="white")
        self.question_label             = Label(self.question_info_frame, bg="white", width=45, height=5, text=equation, font=("Helvetica 15"), justify=CENTER)
        self.under_question_info_frame  = Frame(self.frame, width=500, height=5, bg="#E8E8E8")
        self.blank_frame                = Frame(self.frame, width=500, height=40)
        self.user_input                 = Entry(width=21, font=("Helvetica 15"))
        self.second_blank_frame         = Frame(width=500, height=40)
        self.help_button                = Button(text="Help", font=("Helvetica 12"), width=15, command=lambda: self.toHelp())
        self.stats_button               = Button(text="Statistics", font=("Helvetica 12"), width=15)
    
        self.heading_label.grid(row=1)
        self.heading_frame.grid(row=1)
        self.under_heading_frame.grid(row=2)
        self.info_frame.grid(row=3)
        self.question_info_frame.grid(row=4)
        self.question_label.grid(row=4)
        self.under_question_info_frame.grid(row=5)
        self.blank_frame.grid(row=6)
        self.user_input.grid(row=7)
        self.second_blank_frame.grid(row=8)
        self.help_button.grid(row=9)
        self.stats_button.grid(row=10)

    def checkAnswer(self, equation):
        user_input = self.user_input.get()
        print("{} = {}").format(equation, eval(equation)))


    def toHelp(self):   
        self.frame.destroy()
        self.user_input.destroy()
        self.help_button.destroy()
        self.blank_frame.destroy()
        self.stats_button.destroy()
        self.second_blank_frame.destroy()
        Help()

class Help:
    def __init__(self):
        self.frame = Frame()
        self.frame.grid()

        self.heading_frame              = Frame(self.frame, width=500, height=20, bg="#CCE5FF")
        self.under_heading_frame        = Frame(self.frame, width=500, height=6, bg="#BDDEFF")
        self.blank_frame                = Frame(self.frame, height=50)
        self.heading_label              = Label(self.frame, text="Help and Instructions", font=("Helvetica 15 bold"), fg="#6C6C6C", justify=CENTER)
        self.second_blank_frame         = Frame(self.frame, height=50)
        self.instructions_text          = Label(self.frame, text="Begin the quiz by clicking the Play button.\n"
                                                                 "Type your answer in the entry form below\n"
                                                                 "the question and click the button to submit it.",  font=("Helvetica 12"), justify=CENTER)
        self.third_blank_frame          = Frame(self.frame, width=500, height=50)
        self.dismiss_button             = Button(self.frame, text="Dismiss", font=("Helvetica 12"), width=15, command=lambda: self.dismissHelp())
        self.fourth_blank_frame         = Frame(self.frame, width=500, height=35)

        self.heading_frame.grid()
        self.under_heading_frame.grid()        
        self.blank_frame.grid()
        self.heading_label.grid()
        self.second_blank_frame.grid() 
        self.instructions_text.grid()
        self.third_blank_frame.grid()
        self.dismiss_button.grid()
        self.fourth_blank_frame.grid()
    
    def dismissHelp(self):
        self.frame.destroy()
        Game()


gui = Tk()
gui.title("Math Quiz")
var = Start(gui)
gui.mainloop()  