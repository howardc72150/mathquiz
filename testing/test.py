import tkinter as tk

equation="5+5"
def checkAnswer(event, equation):
    label.configure(text="{} = {}").format(equation, eval(equation))

app = tk.Tk()
app.geometry("200x100")
app.bind('<Return>', checkAnswer(equation))
label = tk.Label(app, text="")
label.pack()

app.mainloop()