from math import *
n = int(input("Podaj n: "))
tab9 = []
maxN = 0
p = 1
for i in range (0,n):
    inp = int(input("Podawaj liczby:"))
    tab9.append(inp)
    if inp == maxN:
        p+=1
    if inp>maxN:
        maxN = inp

print("Maksymalna liczba: ",maxN)
print("Wystąpiła {} razy".format(p))



