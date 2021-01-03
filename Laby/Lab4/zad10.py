a = 0
b = 0
suma = 0
while True:
    a = int(input("daj a:"))
    suma = suma + a
    print(suma)
    if a==b:
        print("a=b")
        break
    b = a
#           PUTEK
# i = 0
# b = 0 # suma
# c = 0 # ostatnia wpisana liczba
# while True:
#     i = int(input("Podaj liczbę: "))
#     b = b + i
#     if c == i:
#         print("Podałeś dwie takie same liczby a suma dodawania to:", b)
#         break
#     c = i