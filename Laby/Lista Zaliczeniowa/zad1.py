def netto(brutto):
    emerytalne = 0.0976 * brutto
    rentowe = 0.015 * brutto
    chorobowe = 0.0245 * brutto
    podstawa_skladki = brutto - (emerytalne+ rentowe + chorobowe)
    zdrowotna = podstawa_skladki * 0.09
    podstawa_opodatkowania = emerytalne + rentowe + chorobowe + zdrowotna
    kwota = brutto - podstawa_opodatkowania
    zus = podstawa_skladki * 0.0775
    zaliczka = kwota * 0.17 - 43.76 - zus
    if zaliczka < 0:
        zaliczka = 0

    return round(brutto - (emerytalne + rentowe + chorobowe + zdrowotna + zaliczka), 2)


print("Kalkulator brutto->netto")
print("""
1 - Kalkulator
2 - Nie kalkulator, tylko wyjście
""")
while True:
    choice=int(input("Wybierz 1 albo 2: "))
    try:
        if choice == 1:
            brutto = int(input("Podaj kwotę brutto: "))
            netto = netto(brutto)
            print(f"Kwota netto wynosi: {netto}")
            print(f"Różnica między brutto a netto: {brutto - netto}")
            break
        elif choice == 2:
            break
        else:
            print("Wpisz 1 albo 2: ")
    except TypeError:
        print("Wpisz 1 albo 2: ")


