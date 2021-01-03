n = int(input("Podaj liczbę którą mam odwrocić: "))
tyl = int(str(n)[::-1])
if int(tyl) == n:
    print("Liczba jest palindromem, debilu")
else:
    print(tyl)