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
root.configure(background="Midnight Blue") # Changing the screens background color

# Creating a class for the QUIZ Q&A section

class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.Radiobtn()
        self.display_options(self.qn)
        self.buttons()
        self.correct=0
        
# Creating the title and question for the QUIZ

    def question(self, qn):
        t = Label(root, text="UEFA CHAMPIONS LEAGUE QUIZ", width= 50, bg="deepPink2", fg="white", font=("times",20,"bold"))   
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, fg="white", bg="Midnight Blue", font=("times", 16, "bold"), anchor="w")
        qn.place(x=150, y=100)
        return qn
  
# Creating 4 buttons for answer selection
    
    def Radiobtn(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text="", variable=self.opt_selected, value=val + 1, font=("times", 14), bg="deepPink2", fg="Midnight Blue")
            b.append(btn)
            btn.place(x=150, y=yp)
            val +=1
            yp += 40
        return b

# Display all options for each question

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val] ['text'] = op
            val += 1

# Creating next question button and Exit quiz button
# Next will show the next question & answers whereas Exit will close the window

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="deep sky blue", fg="White", font=("times",16,"bold"))
        nbutton.place(x=345,y=380)
        quitbutton = Button(root, text="EXIT", command=root.destroy, width=10, bg="red2", fg="white", font=("times",16,"bold"))
        quitbutton.place(x=665,y=45)

# This method retrieves the user entered value

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

# Checks if the users selected answer is correct
     
    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct +=1
        self.qn +=1
        if self.qn == len (q):
            self.display_result()
        else:    
            self.display_options(self.qn)         
 
# Display score in message box

    def display_result(self):
        score = int(self.correct / len(q) * 100)
        result = "Score" + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong =  "No. of wrong answers: " + str(wc)
        mb.showinfo("result: ", "\n".join([result, correct, wrong]))



quiz=Quiz()
root.mainloop()