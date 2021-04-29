import random


class Hotel:
    def __init__(self, pietra, liczba_pokoji):
        self.pietra = pietra
        self.pokoje = liczba_pokoji
        self.nowa_ilosc_pokoi = liczba_pokoji
        self.liczba_pieter = []
        self.liczba_wolnych_pokoi = []
        self.zajete_pokoje = {}

        for x in range(self.pietra):
            self.liczba_pieter.append([])

    y = 0
    debug_pokoju = 1

    def utworz(self, n):
        polowa = round(self.nowa_ilosc_pokoi / 3)
        # print(f"Polowa is {polowa}")
        r = random.randint(1, polowa)
        # print(f"r is {r}")
        if self.y == self.pietra - 1:
            for x in range(self.nowa_ilosc_pokoi):
                self.liczba_pieter[self.pietra - 1].append(Pokoj(self.debug_pokoju + x, self.y, False))
        else:
            for x in range(r):
                self.liczba_pieter[self.y].append(Pokoj(self.debug_pokoju + x, self.y, False))
            self.debug_pokoju += r
            self.nowa_ilosc_pokoi = self.nowa_ilosc_pokoi - r
            self.y += 1
            self.utworz(n + 1)

    def zmiana(self, numer1, pietro1):
        for x in self.liczba_pieter:
            for y in x:
                if y.numer == numer1 and y.pietro == pietro1:
                    y.zajety = not y.zajety
                    print(f"Status {y} zostaw zmieniony z {not y.zajety} na {y.zajety}")

    def is_zajety(self, numer, pietro):
        for x in self.liczba_pieter:
            for y in x:
                if y.numer == numer and y.pietro == pietro:
                    print(f"Status {y} jest {y.zajety}")

    def ile_wolnych(self):
        # self.liczba_wolnych_pokoi = [x for x in range(self.liczba_pieter) if self.liczba_pieter[x].zajety == False]
        # print(f"Liczba wolnych pokoi to {len(self.liczba_wolnych_pokoi)}")
        for x in self.liczba_pieter:
            for y in x:
                if not y.zajety:
                    self.liczba_wolnych_pokoi.append(y)
        print(f"Liczba wolnych pokoi to {len(self.liczba_wolnych_pokoi)}")

    def wynajmij_pokoj(self, osoba, numer_pokoju, pietro):
        for x in self.liczba_pieter:
            for y in x:
                if y.numer == numer_pokoju and y.pietro == pietro:
                    y.zajety = not y.zajety
                    if osoba in self.zajete_pokoje:
                        self.zajete_pokoje[osoba].append(y)
                        print("tak")
                        print(self.zajete_pokoje)
                        self.liczba_wolnych_pokoi.remove(y)
                        print("Liczba wolnych ", len(self.liczba_wolnych_pokoi))
                    elif osoba not in self.zajete_pokoje:
                        self.zajete_pokoje[osoba] = []
                        self.zajete_pokoje[osoba].append(y)
                        self.liczba_wolnych_pokoi.remove(y)
                        print(self.zajete_pokoje)
                        print("Liczba wolnych ", len(self.liczba_wolnych_pokoi))

    def zwolnij_pokoj(self, osoba, numer_pokoju, pietro):
        for x in self.liczba_pieter:
            for y in x:
                if y.numer == numer_pokoju and y.pietro == pietro and y.zajety == True:
                    self.zajete_pokoje[osoba].remove(y)
                    self.liczba_wolnych_pokoi.append(y)
                    y.zajety = not y.zajety
                    print(self.zajete_pokoje)
                    print("Liczba wolnych ", len(self.liczba_wolnych_pokoi))
                elif osoba not in self.zajete_pokoje:
                    print("Ta Osoba nie wynajmuje tego pokoju")

    def zwolnij_all(self, osoba):
        if osoba in self.zajete_pokoje:
            for x in self.zajete_pokoje[osoba]:
                self.liczba_wolnych_pokoi.append(x)
            self.zajete_pokoje.pop(osoba)
            print("Liczba wolnych ", len(self.liczba_wolnych_pokoi))




class Pokoj:

    def __init__(self, numer, pietro, zajety):
        self.numer = numer
        self.pietro = pietro
        self.zajety = zajety

    def __repr__(self):
        return repr(f"Pokój #{self.numer} znajduje się na pietrze #{self.pietro}")


class Osoba:

    def __init__(self, name ):
        self.name = name


    def __repr__(self):
        return repr(f"{self.name}")


h1 = Hotel(6, 50)
h1.utworz(0)
NazwiskoA = Osoba("Adaś")
NazwiskoB = Osoba("Adam")
print("Wszystkie pokoje")
print(h1.liczba_pieter)
# print("Is zajety")
# h1.is_zajety(3,1)
# print("Zmiana")
# h1.zmiana(3,1)
# h1.is_zajety(3,1)
print("Ile wolnych pokoji")
h1.ile_wolnych()
print("Wynajmij pokoj")
h1.wynajmij_pokoj(NazwiskoA, 3, 0)
h1.wynajmij_pokoj(NazwiskoB, 2, 0)
h1.wynajmij_pokoj(NazwiskoA, 1, 0)
print("Zwolnij pokoj")
h1.zwolnij_pokoj(NazwiskoA, 3, 0)
print("Zwolnij all")
h1.zwolnij_all(NazwiskoB)
