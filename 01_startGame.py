from tkinter import *

class Start:
    def __init__(self, root):
        self.headingFrame           = Frame(width=600, height=18, bg="#AEC7F5")
        self.underHeadingFrame      = Frame(width=600, height=5, bg="#9DBBF3")
        self.blankFrame             = Frame(height=40, width=600)
        self.labelBackgroundFrame   = Frame(height=100, width=600, bg="white")
        self.headingLabel           = Label(self.labelBackgroundFrame, height=3, width=42, text="Math Quiz", font=("Verdana 15 bold"), 
                                            fg="#747475", justify=CENTER, bg="white")
        self.underLabelFrame        = Frame(width=600, height=7, bg="#e3e3e3")
        self.startGameButton        = Button(text="PLAY", font=("Verdana 15 bold"), fg="#747475", border=0,
                                             command=self.toGame(self))

        self.headingLabel.grid()
        self.headingFrame.grid(row=0)
        self.underHeadingFrame.grid(row=1)
        self.blankFrame.grid(row=2)
        self.labelBackgroundFrame.grid(row=3)
        self.underLabelFrame.grid(row=4)
        self.startGameButton.grid(row=6, pady=50)

    def toGame(self):
        Game(self)


class Game:
    def __init__(self):
        self.frame = Frame(width=200, height=200)
        self.frame.grid()
        
        
gui = Tk()
gui.title("Math Quiz")
var = Start(gui)
gui.mainloop()  