# i = int(input("Podaj liczbe"))
# j = int(input("Podaj liczbe"))
# n = j
# while n != 0:
#     n = i % j
#     if n != 0:
#         i = j
#         j = n
# print(j)

import math
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
while a != 0 and b != 0:
    math.gcd(a, b)
    print("Największy wspólny dzielnik to: ", math.gcd(a, b))
    break
else:
    print("Nie dzielimy, przez zero")