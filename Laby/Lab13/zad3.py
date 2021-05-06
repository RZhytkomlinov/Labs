class Smartphone:
    def __init__(self, network, age, color, battery, fuelType):
        self.network = network
        self.age = age
        self.color = color
        self.battery = battery
        self.fuelType = fuelType

    def refueling(self):
        print(f"Zatankowano: {self.fuelType} {self.battery} litrów ")

    def carInfo(self):
        print("Sieć:", self.network)
        print("Wiek:", self.age)
        print("Kolor:", self.color)
        print("Pojemność baterii:", self.battery)
        print("Rodzaj paliwa:", self.fuelType)

    def changeColor(self, newColor):
        print(f"Zmieniono kolor z {self.color} na {newColor}")

    def velocity(self):
        if (self.color == "red"):
            print("Bardzo szybki")
        else:
            print("Nie tak szybki jak czerwony")

    def callService(self):
        print("Jesteś 10 w kolejce")


opelek = Smartphone("Audi", 10, "Green", 50, "Benz")
opelek.refueling()
opelek.changeColor("blue")
opelek.carInfo()
opelek.velocity()
opelek.callService()