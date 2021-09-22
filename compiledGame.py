
    # import required libraries 
import random
from tkinter import *

class Start:
    def __init__(self, root):
            # set up and grid first displayed frame
        self.frame = Frame()
        self.frame.grid()
            # creates design for the first frame
        self.heading_frame                = Frame(self.frame, width=500, height=18, bg="#CCE5FF")
        self.under_heading_frame          = Frame(self.frame, width=500, height=6, bg="#BDDEFF")
        self.blank_frame                  = Frame(self.frame, height=40, width=500)
        self.label_background_frame       = Frame(self.frame, height=150, width=500, bg="white")
        self.heading_label                = Label(self.label_background_frame, height=3, width=41, text="Math Quiz", font=("Helvetica 15 bold"), 
                                                fg="#6C6C6C", justify=CENTER, bg="white")
        self.under_label_frame            = Frame(self.frame, width=500, height=7, bg="#E8E8E8")
        self.start_game_button            = Button(self.frame, text="PLAY", font=("Helvetica 15 bold"), fg="#747475", border=0, command=lambda: self.toGame())

            # grid all created objects above
        self.heading_label.grid()
        self.heading_frame.grid(row=0)
        self.under_heading_frame.grid(row=1)
        self.blank_frame.grid(row=2)
        self.label_background_frame.grid(row=3)
        self.under_label_frame.grid(row=4)
        self.start_game_button.grid(row=6, pady=50)

        # function to send user to Game class
    def toGame(self, ):
            # deletes the current frame
        self.frame.destroy()
        Game()
        
class Game:
    def __init__(self):
            # set up variables
        self.round_number = IntVar()
        self.round_number.set(1)

        self.correctly_answered = IntVar()
        self.correctly_answered.set(0)

        self.incorrectly_answered = IntVar()
        self.incorrectly_answered.set(0)

        current_equation = StringVar()
            # set up and grid first displayed frame
        self.frame = Frame(width=500, height=600)
        self.frame.grid()
            # creates design for the main Game frame
        self.heading_frame              = Frame(self.frame, width=500, height=65, bg="#CCE5FF")
        self.under_heading_frame        = Frame(self.frame, width=500, height=6, bg="#BDDEFF")
        self.heading_label              = Label(self.heading_frame, text="Math Quiz", font=("Helvetica 15"),
                                                fg="#6C6C6C", bg="#CCE5FF", width=45, height=2, justify=CENTER)
        self.blank_frame                = Frame(self.frame, width=500, height=30)
        self.label                      = Label(self.frame, text="Round {}\n\nEnter your answer in the entry\nbox below and click Check Answer.".format(self.round_number.get()), font=("Helvetica 12"), justify=CENTER)
        self.second_blank_frame         = Frame(self.frame, width=500, height=30)
        self.question_info_frame        = Frame(self.frame, width=500, height=30, bg="white")
        self.question_label             = Label(self.question_info_frame, bg="white", width=45, height=3, text=self.newQuestion(), font=("Helvetica 15"), justify=CENTER)
        self.under_question_info_frame  = Frame(self.frame, width=500, height=5, bg="#E8E8E8")
        self.third_blank_frame          = Frame(self.frame, width=500, height=40)
        self.user_input                 = Entry(self.frame, width=21, font=("Helvetica 15"))
        self.check_answer_button        = Button(self.frame, text="Check Answer", font=("Helvetica 12"), width=15, command=lambda: self.checkAnswer())
        self.fourth_blank_frame         = Frame(self.frame, width=500, height=40)
        self.help_button                = Button(self.frame, text="Help", font=("Helvetica 12"), width=15, command=lambda: self.toHelp())
        self.stats_button               = Button(self.frame, text="Statistics", font=("Helvetica 12"), width=15, command=lambda: self.toStats())
        self.footer_blank               = Frame(self.frame, width=500, height=20)
        self.footer                     = Frame(self.frame,width=500, height=6, bg="#CCE5FF")

            # grid all created objects above
        self.heading_label.grid(row=1)
        self.heading_frame.grid(row=1)
        self.under_heading_frame.grid(row=2)
        self.blank_frame.grid(row=3)
        self.label.grid(row=4)
        self.second_blank_frame.grid(row=5)
        self.question_info_frame.grid(row=6)
        self.question_label.grid(row=7)
        self.under_question_info_frame.grid(row=8)
        self.third_blank_frame.grid(row=9)
        self.user_input.grid(row=10)
        self.check_answer_button.grid(row=11)
        self.fourth_blank_frame.grid(row=12)
        self.help_button.grid(row=13)
        self.stats_button.grid(row=14)
        self.footer_blank.grid(row=15)
        self.footer.grid(row=16)

        # function to generate a new question
    def newQuestion(self):
            # creates a random question using operators 
            # from list variable and the random library
        operators = ["+", "-", "*"]
        equation = "{} {} {}".format(random.randint(0,12), random.choice(operators), random.randint(0,12))
        self.current_equation = equation
            # returns newly generated question to question label
        return equation

        # function to check if the user's answer is correct
    def checkAnswer(self):
        equation = self.current_equation
        
        try:
                # checks if user input is empty
            if self.user_input.get() != "":
                    # compare user's answer with correct answer
                if (int(self.user_input.get())) == eval(equation):
                        # sets user input background to green
                        # and adds 1 to correctly_answered
                    self.user_input.configure(bg="#90EE90")
                    is_right = self.correctly_answered.get()
                    is_right += 1
                    self.correctly_answered.set(is_right)
                else:
                        # sets user input background to red
                        # and adds 1 to incorrectly_answer
                    self.user_input.configure(bg="#FF5733")
                    is_wrong = self.incorrectly_answered.get()
                    is_wrong += 1
                    self.incorrectly_answered.set(is_wrong)
            else:
                    # if user input is empty set background to red
                    # doesn't skip round.
                self.user_input.configure(bg="#FF5733")
                return
            
                # adds 1 to round counter and updates
                # label on main Game frame
            self.question_label.config(text=self.newQuestion())
            rnum = self.round_number.get()
            rnum += 1
            self.round_number.set(rnum)
            self.label.config(text="Round {}\n\nEnter your answer in the entry\nbox below and click Check Answer.".format(rnum))
        
            # parses user input as integer, if not 
            # sets user input background to red
        except ValueError:
            self.user_input.configure(bg="#FF5733")

        # functions to send user to Stats and Help classes
    def toStats(self):
        num_correct = self.correctly_answered.get()
        num_wrong = self.incorrectly_answered.get()
            # deletes the current frame
            # and sends user to Stats
        self.frame.destroy()
        Stats(num_correct, num_wrong)

    def toHelp(self):
            # deletes the current frame 
            # and sends user to Help
        self.frame.destroy()
        Help()

class Stats:
    def __init__(self, correctly_answered, incorrectly_answered):
            # set up and grid first displayed frame 
        self.frame = Frame()
        self.frame.grid()
            # creates design for the main Stats frame 
        self.heading_frame              = Frame(self.frame, width=500, height=20, bg="#CCE5FF")
        self.under_heading_frame        = Frame(self.frame, width=500, height=6, bg="#BDDEFF")
        self.blank_frame                = Frame(self.frame, height=50)
        self.heading_label              = Label(self.frame, text="Statistics", font=("Helvetica 15 bold"), fg="#6C6C6C", justify=CENTER)
        self.second_blank_frame         = Frame(self.frame, height=50)
        self.instructions_text          = Label(self.frame, text="Answered correctly: {}\nAnswered incorrectly: {}\n".format(correctly_answered, incorrectly_answered),  font=("Helvetica 12"), justify=CENTER)
        self.third_blank_frame          = Frame(self.frame, width=500, height=50)
        self.dismiss_button             = Button(self.frame, text="Dismiss", font=("Helvetica 12"), width=15, command=lambda: self.dismissStats())
        self.fourth_blank_frame         = Frame(self.frame, width=500, height=35)

            # grid all created objects above
        self.heading_frame.grid()
        self.under_heading_frame.grid()        
        self.blank_frame.grid()
        self.heading_label.grid()
        self.second_blank_frame.grid() 
        self.instructions_text.grid()
        self.third_blank_frame.grid()
        self.dismiss_button.grid()
        self.fourth_blank_frame.grid()

        # function to send user back to Game class
    def dismissStats(self):
            # deletes the current frame
            # and sends user to Game
        self.frame.destroy()
        Game()

class Help:
    def __init__(self):
            # set up and grid first displayed frame 
        self.frame = Frame()
        self.frame.grid()
            # creates design for the main Stats frame
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

            # grid all created objects above
        self.heading_frame.grid()
        self.under_heading_frame.grid()        
        self.blank_frame.grid()
        self.heading_label.grid()
        self.second_blank_frame.grid() 
        self.instructions_text.grid()
        self.third_blank_frame.grid()
        self.dismiss_button.grid()
        self.fourth_blank_frame.grid()
    
        # function to send user back to Help class
    def dismissHelp(self):
            # deletes the current frame
            # and sends user to Game
        self.frame.destroy()
        Game()

    # tkinter
gui = Tk()
gui.title("Math Quiz")
var = Start(gui)
gui.mainloop()