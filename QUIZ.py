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
        self.opt_selected = IntVar()
        self.correct_answer = IntVar()
        self.opts = self.checkbtn()
        self.ques = self.question(self.qn)
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0
        
# Creating the title and question for the QUIZ

    def question(self, qn):
        t = Label(root, text="UEFA CHAMPIONS LEAGUE QUIZ", width= 50, bg="deepPink2", fg="white", font=("times",20,"bold"))   
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, fg="white", bg="Midnight Blue", font=("times", 16, "bold"), anchor="w")
        qn.place(x=150, y=100)
        return qn
  
# Creating 4 buttons for answer selection
    
    def checkbtn(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Checkbutton(root, text="", variable=self.opt_selected, onvalue=val + 1, offvalue=0, bg="deepPink2", fg="Midnight Blue", font=("times", 14), command=self.check)
            b.append(btn)
            btn.place(x=150, y=yp)
            val +=1
            yp += 40
        return b
    
    def check(self):
        pass

# Display all options for each question

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.correct_answer.set(a[qn])
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

# Creating next question button and Exit quiz button
# Next will show the next question & answers whereas Exit will close the window

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="deep sky blue", fg="White", font=("times",16,"bold"))
        nbutton.place(x=345,y=380)
        quitbutton = Button(root, text="EXIT", command=root.destroy, width=10, bg="red2", fg="white", font=("times",16,"bold"))
        quitbutton.place(x=665,y=45)

# This method retrieves the users entered value

    def checkans(self, qn):
        selected_option = self.opt_selected.get()
        correct_option = self.correct_answer.get()
        return selected_option == correct_option 

# Checks if the users selected answer is correct
     
    def nextbtn(self):
        selected_option = self.opt_selected.get()
        if selected_option == 0: # Check if an answer option is selected
            mb.showerror("Error", "Please choose an answer.") # Error message
            return  # Stay on the same question until an answer option is selected   

        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result
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