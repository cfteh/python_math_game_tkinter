import random
import tkinter as tk
import questionGenerator
from tkinter import ttk

number1 = 0
number2 = 0 
correctAnswer = 0
inputAnswer = 0
consecutiveCorrect = 0
operator = ""

def isValidAnswer(testString):
    try:
        int(testString)
        return True
    except:
        reportLabel.config(text="Wrong Answer Format")
    

def newQuestion():
    generateQuestion()
    entry.delete(0, 'end')

def checkAnswer():
    global consecutiveCorrect

    string = entry.get()
    if ((string != '') and (isValidAnswer(string))):
        inputAnswer = int(entry.get())
        print(f"Input Answer: {inputAnswer}, type: {type(inputAnswer)}")
        print(f"Correct Answer: {correctAnswer}, type: {type(correctAnswer)}")
        if correctAnswer == inputAnswer:
            reportLabel.config(text="Correct!")
            consecutiveCorrect = consecutiveCorrect + 1
            print("Correct")
        else:
            reportLabel.config(text=f"Incorrect. Correct Answer: {correctAnswer}")
            consecutiveCorrect = 0
            print(f"Incorrect. Correct Answer: {correctAnswer}")
        consecutiveCorrectLabel.config(text=f"Score = {consecutiveCorrect}")
        newQuestion()
    else:
        reportLabel.config(text="No Answer")


def generateQuestion():
    global number1
    global number2
    global correctAnswer
    global operator

    questionType = random.randrange(3)
    print(questionType)
    if questionType == 0:
        question = questionGenerator.getAddition()
        number1 = question[0]
        number2 = question[1]
        correctAnswer = question[2]
        operator = question[3]
    elif questionType == 1:
        question = questionGenerator.getSubtract()
        number1 = question[0]
        number2 = question[1]
        correctAnswer = question[2]
        operator = question[3]
    else:
        question = questionGenerator.getMultiplication()
        number1 = question[0]
        number2 = question[1]
        correctAnswer = question[2]
        operator = question[3]
        

    label.config(text = f"Question:  {number1} {operator} {number2} = ?")


root = tk.Tk()
root.title("Maths App")
root.geometry("1048x480")

label = ttk.Label(root, text="", padding=10)
label.pack()

answerLabel = ttk.Label(root, text="Enter Answer: ", padding=10)
answerLabel.pack()

entry = ttk.Entry(root)
entry.pack()

checkAnswerButton = ttk.Button(root, text="Check Answer", command=checkAnswer, padding=10)
checkAnswerButton.pack()

reportLabel = ttk.Label(root, text="", padding=10)
reportLabel.pack()

consecutiveCorrectLabel = ttk.Label(root, text=f"Consecutive Correct = {consecutiveCorrect}", padding=10)
consecutiveCorrectLabel.pack()

newQuestion()

root.mainloop()