# Neil Whippy: Welcome to the code I've created for my UCL QUIZ.
# Here you'll get to see everything relevant to put in my 3 windows.
# The comments will help guide you to where you'll put changes.
# Or comments will help you understand the purpose of what i'm doing with my interface. 

# Importing tkinter

from tkinter import *
from tkinter import messagebox as mb
import json
import threading

#Creating QUIZ window to put questions and answers

root = Tk()
root.geometry("800x500")
root.title("Quiz")
root.configure(background="Midnight Blue")

# Create the AgeScreen class for age input (Boundry)
class AgeScreen:

    def __init__(self):
        self.title_label = Label(root, text="Please enter your age", width=40, fg="white", bg="Midnight Blue", font=("times", 20, "bold"))
        self.title_label.place(x=70, y=140)
        
        t = Label(root, text="UEFA CHAMPIONS LEAGUE QUIZ", width= 50, bg="deepPink2", fg="white", font=("times",20,"bold"))   
        t.place(x=0, y=2)   

        self.age_entry = Entry(root, font=("times", 14))
        self.age_entry.place(x=305, y=220)
        
        self.submit_button = Button(root, text="Submit", bg="deep sky blue", fg="white", command=self.check_age, width=10, font=("times", 16, "bold"))
        self.submit_button.place(x=330, y=280)
   
# Error message to tell users to enter their age

    def check_age(self):
        age = self.age_entry.get()
        if not age:
            mb.showerror("Age Error", "Please enter your age!")
            return
        age = int(age)

# Info message to tell users they aren't old enough or young enough to play

        if age in [15, 16, 17, 18]:
            start_screen = StartScreen()
            self.title_label.destroy()
            self.age_entry.destroy()
            self.submit_button.destroy()
        else:
            mb.showinfo("Age Info", "You are not at the age to play (15-18 yrs)")

# Create an instance of AgeScreen to start with
age_screen = AgeScreen()

# Define the Quiz class for the quiz questions
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
        self.time_left = 60
        self.timer_label = Label(root, text="Timer: 60s", bg="Midnight Blue", fg="white", font=("times", 14, "bold"))
        self.timer_label.place(x=25, y=60)
        self.start_timer()

    def start_timer(self): 
        self.timer_thread = threading.Thread(target=self.timer_countdown) 
        self.timer_thread.start()

    def timer_countdown(self):
        while self.time_left > 0:
            self.timer_label.config(text=f"Timer: {self.time_left}s")    
            self.time_left -= 1
            root.update()
            import time
            time.sleep(1)
        self.display_result()

    def question(self, qn):
        t = Label(root, text="UEFA CHAMPIONS LEAGUE QUIZ", width= 50, bg="deepPink2", fg="white", font=("times",20,"bold"))   
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, fg="white", bg="Midnight Blue", font=("times", 16, "bold"), anchor="w")
        qn.place(x=150, y=100)
        return qn

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
        self.next_button = Button(root, text="Next", command=self.nextbtn, width=10, bg="deep sky blue", fg="White", font=("times",16,"bold"))
        self.next_button.place(x=345,y=380)
        quit_button = Button(root, text="EXIT", command=root.destroy, width=10, bg="red2", fg="white", font=("times",16,"bold"))
        quit_button.place(x=665,y=45)

    def check(self):
        pass
# This method retrieves the users entered value


    def checkans(self, qn):
        selected_option = self.opt_selected.get()
        correct_option = self.correct_answer.get()
        return selected_option == correct_option 

# Checks if the users selected answer is correct

    def nextbtn(self):
        selected_option = self.opt_selected.get()
        if selected_option == 0:
            mb.showerror("Error", "Please choose an answer.")
            return
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

# Display score in Results Screen

    def display_result(self):
        self.ques.destroy()
        for opt in self.opts:
            opt.destroy()
        self.next_button.destroy()
        self.timer_label.destroy()
        result_window = ResultWindow(self.correct, len(q))

# Creating home page with a "Start Quiz" button


class StartScreen:
    def __init__(self):
        self.title_label = Label(root, text="UEFA CHAMPIONS LEAGUE QUIZ", width=50, bg="DeepPink2", fg="white", font=("times", 20, "bold"))
        self.title_label.place(x=0, y=2)
        self.title_label = Label(root, text="Welcome to my Quiz, test your UCL knowledge!", width=40, fg="white", bg="Midnight Blue", font=("times", 20, "bold"))
        self.title_label.place(x=70, y=140)
        self.start_button = Button(root, text="START QUIZ!", bg="deep sky blue", fg="white", command=self.start_quiz, width=15, font=("times", 16, "bold"))
        self.start_button.place(x=300, y=250)
        quit_button = Button(root, text="EXIT", fg="white", bg="red2", command=root.destroy, width=10, font=("times", 16, "bold"))
        quit_button.place(x=665, y=45)

    def start_quiz(self):
        self.title_label.destroy()
        self.start_button.destroy()
        quiz = Quiz()

# Creating a results window for users to go to after finishing QUIZ, and a "Restart" button to retake the quiz

class ResultWindow:
    def __init__(self, correct, total):
        self.result_label = Label(root, text="UEFA CHAMPIONS LEAGUE QUIZ FINISHED!", width=50, bg="DeepPink2", fg="white", font=("times", 20, "bold"))
        self.result_label.place(x=0, y=2)

        score = str(correct) + "/" + str(total)
        result = "Score: " + score
        result_label = Label(root, text=result, bg="Midnight Blue", fg="white", font=("times", 18, "bold"))
        result_label.place(x=345, y=200)

# Display the "Congratulations" label if the score is perfect (all questions correct)

        if correct == total:
            congrats_label = Label(root, text="Congratulations Champ!", bg="Midnight Blue", fg="White", font=("times", 18, "bold"))
            congrats_label.place(x=275, y=150)

        if correct == 0:
            unlucky_label = Label(root, text="Unlucky Mate!", bg="Midnight Blue", fg="White", font=("times", 18, "bold"))
            unlucky_label.place(x=318, y=150)
            
        if correct == 1:
            unlucky_label = Label(root, text="Nice Try Mate!", bg="Midnight Blue", fg="White", font=("times", 18, "bold"))
            unlucky_label.place(x=320, y=150)

        if correct == 2:
            unlucky_label = Label(root, text="Solid Try Mate!", bg="Midnight Blue", fg="White", font=("times", 18, "bold"))
            unlucky_label.place(x=318, y=150)

        if correct == 3:
            unlucky_label = Label(root, text="Good job Mate!", bg="Midnight Blue", fg="White", font=("times", 18, "bold"))
            unlucky_label.place(x=318, y=150)    
       
        if correct == 4:
            unlucky_label = Label(root, text="Great Job Genius!", bg="Midnight Blue", fg="White", font=("times", 18, "bold"))
            unlucky_label.place(x=308, y=150)

        self.restart_button = Button(root, text="Restart", fg="white", bg="deep sky blue", command=self.restart_quiz, width=10, font=("times", 16, "bold"))
        self.restart_button.place(x=340, y=380)

        quit_button = Button(root, text="EXIT", fg="white", bg="red2", command=root.destroy, width=10, font=("times", 16, "bold"))
        quit_button.place(x=665, y=45)

    def on_close(self):
        root.destroy()

        

    def restart_quiz(self):
        self.result_label.destroy()
        self.restart_button.destroy()
        for widget in root.winfo_children():
            widget.destroy()
        start_screen = StartScreen()

# Define your quiz questions, correct answers, and answer options
q = ["1) Who scored the most goals?", "2) How many clubs won the Champions League", "3) What year did the first tournament take place?", "4) Which clubs were banned for 5 years?", "5) Which club has won the most champions league titles?"]
a = [4, 2, 4, 3, 1]  # 1, 2, 3, 4 represent the correct answer options for each question
options = [
    ["Messi", "Benzema", "Neymar", "Ronaldo"],
    ["10","23","35","47"],
    ["1898", "2000", "1985", "1956"],
    ["Spainish Clubs","German Clubs","English Clubs","Italian Clubs"],
    ["Real Madrid", "Barcelona","AC Milan", "Bayern Munich"]
]

root.mainloop()