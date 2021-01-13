import math

a = int(input("Daj 1 liczbe: "))
b = int(input("Daj 2 liczbe: "))

print("1 - Dodawanie"
      "2 - Odejmowanie"
      "3 - Mnożenie"
      "4 - Dzielenie"
      "5 - Pierwiastkowanie"
      )


def dzialania(a, b):
    finish = f'+: {a + b},-: {a - b},*: {a * b},/: {a / b},sqrt: {math.sqrt(a)}, {math.sqrt(b)}'
    return finish


print(dzialania(a, b))
