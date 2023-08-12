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


root.mainloop()