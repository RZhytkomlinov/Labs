import sqlite3


class Baza:
    def __init__(self):
        self.baza = sqlite3.connect("kontakty.db")
        self.make_baze()
        self.lista_osob = []
        self.update_program()

    def __del__(self):
        self.baza.close()

    def make_baze(self):
        try:
            self.baza.execute("""CREATE TABLE kontakty(
            imie TEXT,
            nazwisko TEXT,
            numer TEXT
            )""")
        except:
            print("Baza danych już istnieje.")

    def update_program(self):
        cur = self.baza.execute("SELECT * from kontakty")
        for x in cur:
            temp = Osoba(x[0], x[1], x[2])
            self.lista_osob.append(temp)

    def add_osobe(self, osoba):
        self.baza.execute(
            f"INSERT INTO kontakty(imie, nazwisko, numer) VALUES('{osoba.imie}','{osoba.nazwisko}','{osoba.numer}')")
        self.baza.commit()
        self.lista_osob.append(osoba)

    def remove_osobe(self, osoba):
        for x in self.lista_osob:
            if x.imie == osoba.imie and x.nazwisko == osoba.nazwisko and x.numer == osoba.numer:
                self.baza.execute(
                    f"DELETE FROM kontakty WHERE imie = '{osoba.imie}' AND nazwisko = '{osoba.nazwisko}' AND numer = '{osoba.numer}'")
                self.baza.commit()
        self.lista_osob = [x for x in self.lista_osob if
                           x.imie != osoba.imie and x.nazwisko != osoba.nazwisko and x.numer != osoba.numer]

    def numbers(self):
        for x in self.lista_osob:
            print("{} {}; Tel:{}".format(x.imie, x.nazwisko, x.numer))

    def search(self, numer):
        for x in self.lista_osob:
            if x.numer == numer:
                print("Podany numer należy do {} {}".format(x.imie, x.nazwisko))

    def sortowanie(self):
        templist = sorted(self.lista_osob, key=lambda Osoba: Osoba.nazwisko)
        for x in templist:
            print("{} {}; Tel:{}".format(x.nazwisko, x.imie, x.numer))


class Osoba:
    def __init__(self, imie, nazwisko, numer):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} numer tel:{self.numer}"


b1 = Baza()
os1 = Osoba("Imie1", "Nazwisko1", "531038472")
os2 = Osoba("Imie2", "Nazwisko2", "645839103")
os3 = Osoba("Imie3", "Nazwisko3", "860478362")
os4 = Osoba("Imie4", "Nazwisko4", "927563812")

# b1.add_osobe(os1)
b1.add_osobe(os2)
# b1.add_osobe(os3)
# b1.add_osobe(os4)
print(b1.lista_osob)
# b1.remove_osobe(os2)
b1.sortowanie()