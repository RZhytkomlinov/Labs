import random
# ile = 0
# suma = 0
# while True:
#     a = float(input("liczba:"))
#     if a <=0:
#         continue
#     ile += 1
#     suma = float(suma) + float(a)
#     srednia = suma/ile
#     print(float(srednia))


# ile = int(input("daj ile"))
# i=0
# suma = 0
# srednia = 0
# while i<ile:
#     a = float(input("liczba:"))
#     if a <=0:
#         continue
#     i += 1
#     suma = float(suma) + float(a)
#     srednia = suma/i
# print(float(srednia))

ile = int(input("daj ile"))
i=0
suma = 0
srednia = 0
while i<ile:
    a = random.uniform(-100, 100)
    if a <=0:
        continue
    i += 1
    suma = float(suma) + float(a)
    srednia = suma/i
x = round(srednia, 3)
print(float(x))





# n = int(input("Podaj ilość liczb: "))
# sum = 0
# i = n
# int_count = 0
# float_count = 0
#
# while i > 0:
#     inp = random.uniform(-100, 100)
#     if inp.is_integer():
#         int_count += 1
#     else:
#         float_count += 1
#     if inp < 0:
#         continue
#     sum = sum + inp
#     i -= 1
#
# print("Średnia arytmetyczna twoich liczb to {}.".format(sum/n))
# print("Wystąpiło {} floatów i {} intów".format(float_count, int_count))




