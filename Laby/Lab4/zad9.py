import math
suma = 0
a = 0
b = 0
while True:
    b = a
    a = int(input("daj a:"))
    suma = suma + a
    print(suma)
    c = a - b
    if math.fabs(c) == a:
        continue
    elif math.fabs(c) < 5:
        print("|a-b|<5")
        break