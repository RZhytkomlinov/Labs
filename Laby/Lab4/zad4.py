ile = 0
suma = 0
while True:
    a = input("liczba:")
    ile +=1
    suma = int(suma) + int(a)
    srednia = suma/ile
    print(float(srednia))
    if a == 0:
        break


#      HUTNICZA
# sum = 0
# i = 0
# while True:
#     inp = input("Podaj liczbę: ")
#     try:
#         intput = int(inp)
#     except:
#         pass
#     if intput == 0 or inp == "s" or inp == "NULL":#wybranym znakiem w tym przypadku jest "s"
#         print(sum/i)
#         break
#     sum = sum + intput
#     i += 1