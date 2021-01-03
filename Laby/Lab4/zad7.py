inp = int(input("Podaj liczbę: "))
i = 2
while inp > 0:
    if inp == 2:
        print("To jest liczba pierwsza")
        break
    elif inp % i == 0:
        print("To nie jest liczba pierwsza")
        break
    else:
        print("To jest liczba pierwsza")
        break