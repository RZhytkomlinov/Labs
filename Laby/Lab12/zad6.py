def binarna(n):
    return bin(n).replace("0b", "")


def dzies(n):
    n = int(n, 2)
    return n


print("""
Jakie dzialanie chcesz wykonać ?
1. dzies -> bin
2. bin -> dzies""")

while True:
    a = int(input("Podaj które dzialanie chcesz wykonac: "))
    if a == 1:
        n = int(input("Podaj liczbę dziesietna: "))
        print(binarna(n))
        break
    if a == 2:
        n = input("Podal liczbe binarna: ")
        try:
            print(dzies(n))
            break
        except:
            print("To nie jest liczba binarna")
    else:
        print("Wybierz poprawne dzialanie.")