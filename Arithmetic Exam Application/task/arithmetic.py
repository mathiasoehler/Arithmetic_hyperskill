import random

arithmetic = {"+": lambda x, y: x + y,
              "-": lambda x, y: x - y,
              "*": lambda x, y: x * y,}

# erstellt die aufgabe
a = random.randint(2,9)
b = random.randint(2,9)
zeichen = ( "+", "-","*")
operator = random.choice(zeichen)
ergebnis = (arithmetic[operator](int(a),int(b)))

print(a,operator, b)  # druckt die aufgabe
userein = int(input())  # user eingabe

if userein  == ergebnis:  # kontrolle/bewertung der eingabe
    print("Right!")
else:
    print("Wrong!")



