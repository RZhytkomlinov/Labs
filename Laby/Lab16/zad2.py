import sqlite3


class Baza:
    def __init__(self):
        self.baza = sqlite3.connect("kontakty1.db")
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
            miejscowosc TEXT,
            zarobki INT
            )""")
        except:
            print("Baza danych już istnieje.")

    def update_program(self):
        cur = self.baza.execute("SELECT * from kontakty")
        for x in cur:
            temp = Osoba(x[0], x[1], x[2], x[3])
            self.lista_osob.append(temp)

    def add_osobe(self, osoba):
        self.baza.execute(
            f"""INSERT INTO kontakty(imie, nazwisko, miejscowosc, zarobki) 
        VALUES('{osoba.imie}','{osoba.nazwisko}','{osoba.miejscowosc}','{osoba.zarobki}')""")
        self.baza.commit()
        self.lista_osob.append(osoba)

    def remove_osobe(self, osoba):
        for x in self.lista_osob:
            if x.imie == osoba.imie and x.nazwisko == osoba.nazwisko and x.miejscowosc == osoba.miejscowosc and x.zarobki == osoba.zarobki:
                self.baza.execute(
                    f"""DELETE FROM kontakty WHERE imie = '{osoba.imie}' AND nazwisko = '{osoba.nazwisko}' 
                    AND miejscowosc = '{osoba.miejscowosc}' AND zarobki = '{osoba.zarobki}'""")
                self.baza.commit()
        self.lista_osob = [x for x in self.lista_osob if
                           x.imie != osoba.imie and x.nazwisko != osoba.nazwisko and x.miejscowosc != osoba.miejscowosc and x.zarobki == osoba.miejscowosc]

    def sortowanie(self):
        templist = sorted(self.lista_osob, key=lambda Osoba: Osoba.nazwisko)
        for x in templist:
            print(f"{x.nazwisko} {x.imie}; Zarabia = {x.zarobki}")

    def zarobki_up(self):
        templist = sorted(self.lista_osob, key=lambda Osoba: Osoba.zarobki)
        for x in templist:
            print(f"{x.nazwisko} zarabia {x.zarobki}")

    def zarobki_down(self):
        templist = sorted(self.lista_osob, key=lambda Osoba: Osoba.zarobki, reverse=True)
        for x in templist:
            print(f"{x.nazwisko} zarabia {x.zarobki}")


class Osoba:
    def __init__(self, imie, nazwisko, miejscowosc, zarobki):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejscowosc = miejscowosc
        self.zarobki = zarobki

    def __repr__(self):
        return f"{self.nazwisko} from {self.miejscowosc} zarabia {self.zarobki}"


b1 = Baza()
os1 = Osoba("Imie1", "Nazwisko1", "Miejscowość1", 531038472)
os2 = Osoba("Imie2", "Nazwisko2","Miejscowość2", 645839103)
os3 = Osoba("Imie3", "Nazwisko3", "Miejscowość3", 860478362)
os4 = Osoba("Imie4", "Nazwisko4", "Miejscowość4", 927563812)
# b1.add_osobe(os1)
# b1.add_osobe(os3)
# b1.add_osobe(os4)
# b1.add_osobe(os2)
print("Sortowanie")
b1.sortowanie()
print("Up")
b1.zarobki_up()
print("Down")
b1.zarobki_down()
