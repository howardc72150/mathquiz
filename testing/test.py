from tkinter import *
from functools import partial
import time

class Start:
    def __init__(self, root):
            # initalize variables
        timer = StringVar()

        timer.set("5")
        ui = "hello"

        self.mainframe = Frame(padx=10, pady=10, width=200, height=200)
        self.mainframe.grid()

        self.timerlabel = Label(self.mainframe, textvariable=timer, justify=CENTER, font=("Verdana 16 bold"), pady=50)
        self.timerlabel.grid(row=0)

        self.testlabel = Label(self.mainframe, text=ui, justify=CENTER, font=("Verdana 16 bold"), pady=50)
        self.testlabel.grid(row=1)

        self.buttonframe = Frame(self.mainframe, padx=75, pady=50)
        self.buttonframe.grid(row=2)

        self.userinput = Entry(self.buttonframe, font=("Verdana", "15", "bold"), width=20)
        self.userinput.grid(row=3, column=0)

        self.grabbutton = Button(self.buttonframe, text="Grab", justify=CENTER, font=("Verdana 16 bold"), command=lambda: self.grabUserInput())
        self.grabbutton.grid(row=3, column=1)

        self.startframe = Frame(self.mainframe, padx=10, pady=10)
        self.startframe.grid(row=4)
        
        self.startbutton = Button(self.startframe, text="Start", justify=CENTER, font=("Verdana 16 bold"), command=lambda: self.updateTimer(timer))
        self.startbutton.grid(row=4)

    def grabUserInput(self):
        ui = self.userinput.get()
        self.testlabel.config(text=ui)
        root.update()
        
    def updateTimer(self, timer):
        currenttime = int(timer.get())
        self.mainframe.config(width=500, height=500)
        root.title("Math Quiz   |   You have {} seconds remaining!".format(currenttime))
        
        while currenttime > 0:
            root.update()
            time.sleep(1)
            currenttime -= 1
            timer.set(currenttime)
            if currenttime == 1:
                root.title("Math Quiz   |   You have {} second remaining!".format(currenttime))
            else:
                root.title("Math Quiz   |   You have {} seconds remaining!".format(currenttime))
        timer.set("Time's up!")   

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("test gui")
    var = Start(root)
    root.mainloop()  
            





