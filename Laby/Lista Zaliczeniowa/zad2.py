def koszt_pracodawcy(brutto):
    emerytalne = 0.0976 * brutto
    rentowe = 0.065 * brutto
    wypadkowe = 0.0167 * brutto
    fundusz = 0.0245 * brutto
    fgsp = 0.01 * brutto
    return brutto + emerytalne + rentowe + wypadkowe + fundusz + fgsp
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

print("Kalkulator brutto/netto Pracodawca Edition")
brutto=int(input("Podaj kwotę brutto:"))
netto = netto(brutto)
print(f"Jako pracodawca wydasz: {koszt_pracodawcy(brutto)}")
print(f"Kwota netto dla pracownika wynosi: {netto}")
