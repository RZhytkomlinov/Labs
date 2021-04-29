import sqlite3

class Baza:
    def __init__(self):
        self.baza = sqlite3.connect('kontakty.db')
        self.make_tabela()
        self.lista_osob = []
        self.id = 0

    def __del__(self):
        self.baza.close()

    def make_tabela(self):
        try:
            self.baza.execute("""CREATE TABLE kontakty(
            id INTEGER KEY,
            imie TEXT,
            nazwisko TEXT,
            numer TEXT
            )""")
        except:
            print("Baza danych już istnieje")

    def update_baza(self):
        upd = self.baza.execute('SELECT * from kontakty')
        for x in upd:
            self.lista_osob.append(Osoba(x[1],x[2],x[3]))
            self.id += 1

    def add_osoba(self, osoba):
        self.baza.execute(f"INSERT INTO kontakty (id,imie,nazwisko,numer) VALUES ('{self.id}','{osoba.imie}','{osoba.nazwisko}','{osoba.numer}')")
        self.baza.commit()
        self.lista_osob.append(osoba)


class Osoba:
    def __init__(self,imie, nazwisko, numer):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def __repr__(self):
        return f'Imie: {self.imie}, Nazwisko: {self.nazwisko}, Numer: {self.numer}'



b1 = Baza()
osoba = Osoba('Imie1','Nazwisko1','Numer1')
osoba1 = Osoba('Imie2','Nazwisko2','Numer2')
b1.add_osoba(osoba)
b1.add_osoba(osoba1)
print(b1.lista_osob)




