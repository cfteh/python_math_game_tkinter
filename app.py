import random
import tkinter as tk
from tkinter import ttk

number1 = 0
number2 = 0 
correctAnswer = 0
inputAnswer = 0
consecutiveCorrect = 0


def checkAnswer():
    global number1
    global number2
    global consecutiveCorrect

    string = entry.get()
    if string != '':
        inputAnswer = int(entry.get())
        print(f"Input Answer: {inputAnswer}, type: {type(inputAnswer)}")
        correctAnswer = number1 + number2
        print(f"Correct Answer: {correctAnswer}, type: {type(correctAnswer)}")
        if correctAnswer == inputAnswer:
            reportLabel.config(text="Correct!")
            consecutiveCorrect = consecutiveCorrect + 1
            print("Correct")
        else:
            reportLabel.config(text="Incorrect!")
            consecutiveCorrect = 0
            print("Incorrect")
        consecutiveCorrectLabel.config(text=f"Consecutive Correct = {consecutiveCorrect}")
        generateQuestion()
    else:
        reportLabel.config(text="No Answer")


def generateQuestion():
    global number1
    global number2
    number1 = random.randrange(1000)
    number2 = random.randrange(1000)

    label.config(text = f"Question: {number1} + {number2} = ?")

def generateSecondNumber():
    number2 = random.range(1000)
    print("World")

root = tk.Tk()
root.title("Maths App")
root.geometry("1048x480")

button = ttk.Button(root, text="Generate Question",  command=generateQuestion, padding=10)
button.pack()

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

root.mainloop()