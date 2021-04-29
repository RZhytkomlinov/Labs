class Vehicle:
    def __init__(self, nr_tablicy, marka):
        self.nr_tablicy = nr_tablicy
        self.marka = marka

    def __del__(self):
        print(f"Pojazd o nr_tablicy {self.nr_tablicy} został usunięty")

    def show_tablica(self):
        print(f"Tablica rejestracyjna tego pojazdu to {self.nr_tablicy}")


class Car(Vehicle):
    def __init__(self, nr_tablicy, marka, kolor):
        super().__init__(nr_tablicy, marka)
        self.kolor = kolor

    def brrr(self):
        print(f"Samochód marki {self.marka} o kolorze {self.kolor} robi brrr")


class Moto(Vehicle):
    def __init__(self, nr_tablicy, marka, halas):
        super().__init__(nr_tablicy, marka)
        self.halas = halas

    def wziuuum(self):
        print(f"Motocykl marki {self.marka} robi wziuuum z głośnością {self.halas} decybeli")

def utilize(vehicle):
    wybor = input(f"Czy usunąć samochód o nr tablic {c1.nr_tablicy}?(Tak-litera, Nie-Cyfra)")
    if wybor is str():
        del vehicle


c1 = Car("DLB 12DUV", "Audi", "Black")
m1 = Moto("DUD 83DJF", "Yamaha", 13)
print(c1.marka, c1.nr_tablicy, c1.kolor)
print(m1.marka, m1.nr_tablicy, m1.halas)
c1.show_tablica()
c1.brrr()
m1.show_tablica()
m1.wziuuum()



usuwanie(c1)
usuwanie(m1)