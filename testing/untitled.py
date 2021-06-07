from tkinter import *

class Start:
    def __init__(self, root):
        self.headingFrame = Frame(width=600, height=75, bg="#9DBBF3")
        self.underHeadingFrame = Frame(width=606, height=9, bg="#AEC7F5")
        self.headingFrame.grid(row=0)
        self.underHeadingFrame.grid(row=1)

        self.headingLabel = Label(self.headingFrame, height=3, width=60, text="Math Quiz", font=("Verdana 12"), 
                                  justify=CENTER, bg="#9DBBF3", fg="#F0F1F4")
        self.headingLabel.grid(row=0)







        self.mainFrame = Frame(width=600, height=515)
        self.mainFrame.grid(row=2)
        
if __name__ == "__main__":
    root = Tk()
    root.title("test gui")
    var = Start(root)
    root.mainloop()  