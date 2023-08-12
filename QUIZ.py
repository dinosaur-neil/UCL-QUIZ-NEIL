# Neil Whippy: Welcome to the code I've created for my UCL QUIZ.
# Here you'll get to see everything relevant to put in my 3 windows.
# The comments will help guide you to where you'll put changes.
# Or comments will help you understand the purpose of what i'm doing with my interface. 

# Importing tkinter

from tkinter import*
from tkinter import messagebox as mb
import json

#Creating QUIZ window to put questions and answers

root = Tk()
root.geometry("800x500")
root.title("Quiz")
with open('File.json') as f:
    obj = json.load(f)
q = (obj ['ques'])
options = (obj['options'])
a = (obj ['ans'])

# Creating a class for the QUIZ Q&A section

class Quiz:
    def __init__(self):
        self.qn = 0
        self.opt_selected = IntVar()
        self.opts = self.Radiobtn()
        self.ques = self.question(self.qn)
        self.correct = 0
        
# Displaying the title and question for the QUIZ

    def question(self, qn):
        t = Label(root, text="UEFA CHAMPIONS LEAGUE QUIZ", width= 50, bg="blue", fg="white", font=("times",20,"bold"))   
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70,y=100)
        return qn
  

    
    def Radiobtn(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text="", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val +=1
            yp += 40
        return b
        


quiz=Quiz()

root.mainloop()