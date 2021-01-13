import math
a = int(input("Daj 1 liczbe: "))
b = int(input("Daj 2 liczbe: "))

def dzialania(a,b):
    finish = f'+: {a+b},-: {a-b},*: {a*b},/: {a/b},sqrt: {math.sqrt(a)}, {math.sqrt(b)}'
    return finish

print(dzialania(a,b))