import random

def getAddition():
    number1 = random.randrange(10)
    number2 = random.randrange(10)

    return number1, number2, (number1+number2), "+"

def getSubtract():
    number1 = random.randrange(10)
    number2 = random.randrange(10)

    if number1 > number2:
        return number1, number2, (number1-number2), "-"
    else:
        return number2, number1, (number2-number1), "-"

def getMultiplication():
    number1 = random.randrange(11)
    number2 = random.randrange(10)

    return number1, number2, (number1*number2), "x"
