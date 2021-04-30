class Parking:
    tablice = {}#{tablica}: {czy na parkingu}
    def __init__(self):
        pass
    def zarejestruj(self, blachy):
        if blachy not in self.tablice:
            self.tablice[blachy] = False
        else:
            print("Samochód jest już w bazie.")

    def wjazd(self, blachy):
        self.tablice[blachy] = True
    def wyjazd(self, blachy):
        self.tablice[blachy] = False
    def sprawdz_blache(self, blachy):
        if self.tablice[blachy]:
            print("Samochód znajduje się na parkingu.")
        else:
            print("Samochód nie znajduje się na parkingu.")


parking1 = Parking()

parking1.zarejestruj("DW1234")
parking1.zarejestruj("DW1235")
parking1.zarejestruj("DW1236")
parking1.zarejestruj("DW1236")

parking1.wjazd("DW1234")
parking1.sprawdz_blache("DW1234")
parking1.sprawdz_blache("DW1235")

print(parking1.tablice)

