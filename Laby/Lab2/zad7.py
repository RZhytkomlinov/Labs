from math import *
a = int(input("podaj a: "))
b = int(input("podaj b: "))
c = int(input("podaj c: "))

delta = b*b - 4*a*c
print(delta)
try:
    d = sqrt(delta)
    wynik1 = (-b + d)/2*a
    wynik2 = (-b - d)/2*a
    print("Wyniki: ")
    print("x1: ",wynik1)
    print("x2: ",wynik2)
except:
    print("Delta < 0")