import roman


def rzymska():
    while True:
        try:
            arabska = int(input("Podaj liczbę: "))
            break
        except:
            print("Proszę podać liczbę całkowitą.")
    rzymska = roman.toRoman(arabska)
    print(rzymska)


def arabska():
    while True:
        try:
            rzymska = (input("Podaj liczbę: "))
            arabska = roman.fromRoman(rzymska)
            break
        except:
            print("Proszę podaj właściwą liczbę rzymską")
    print(arabska)


print("Witaj w programie zamieniającym liczby rzymskie na arabskie i odwrotnie")
print("1.Arabska ==> Rzymska")
print("2.Rzymska ==> Arabska")

while True:
    wybor = input("Podaj co chcesz zrobić:")
    if wybor == "1":
        rzymska()
        break
    if wybor == "2":
        arabska()
        break
    print("Proszę wybrać spośród opcji na ekranie (1, 2)")