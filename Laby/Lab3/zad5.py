ile = 0
suma = 0
while True:
    a = input("liczba:")
    if a == 0:
        print("Dałeś 0, jesteś zjebany")
        break
    ile +=1;
    suma = int(suma) + int(a);
    srednia = suma/ile;
    print(float(srednia))
