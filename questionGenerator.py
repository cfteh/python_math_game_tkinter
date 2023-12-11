import random

def getAddition():
    number1 = random.randrange(1000)
    number2 = random.randrange(1000)

    return number1, number2, (number1+number2), "+"

def getSubtract():
    number1 = random.randrange(1000)
    number2 = random.randrange(1000)

    if number1 > number2:
        return number1, number2, (number1-number2), "-"
    else:
        return number2, number1, (number2-number1), "-"
