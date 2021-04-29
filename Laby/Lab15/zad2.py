class Beer():
    def __init__(self, rating, name, procent, type, price):
        self.rating = rating
        self.name = name
        self.procent = procent
        self.type = type
        self.price = price

    def __repr__(self):
        return f"Piwo : {self.name}, Rating: {self.rating}"


class Shop():
    def __init__(self):
        pass

    fridge = []

    def buy(self):
        check = str(input("Czy masz 18 lat?"))
        if check == 'tak':
            self.sell(self.fridge)
        if check == 'nie':
            print("Nie możemy sprzedać")

    def sell(self, fridge):
        choice = str(input("Jakie piwo chcesz kupić: "))
        if choice in fridge:
            print("Sprzedano")
        else:
            print("Nie mamy takiego piwa")

    def sorto_by_rate(self):
        print(sorted(self.fridge, key=lambda Beer: Beer.rating))

    def sorto_by_name(self):
        print(sorted(self.fridge, key=lambda Beer: Beer.name))



class Bar(Shop):
    def __init__(self, rating, name, location):
        super().__init__()
        self.rating = rating
        self.name = name
        self.location = location
    fridge = []

    def buy(self):
        check = str(input("Czy masz 18 lat?"))
        if check == 'tak':
            self.sell(self.fridge)
        if check == 'nie':
            print("Nie możemy sprzedać")

    def sell(self, fridge):
        choice = str(input("Jaki drink chcesz kupić: "))
        if choice in fridge:
            print("Sprzedano")
        else:
            print("Nie mamy takiego drinka")


class Drink():
    def __init__(self, rating, name, price):
        self.rating = rating
        self.name = name
        self.price = price


kont = Bar(9, "Kontynuacja", "Wrocław")
biedronka = Shop()
harnas = Beer(10, "Harnas", 5, "Lager", 3.20)
biedronka.fridge.append(harnas)
kont.fridge.append(harnas)
kustosz = Beer(10, "Kustosz", 5, "Lager", 1.50)
biedronka.fridge.append(kustosz)
kont.fridge.append(kustosz)
kasztelan = Beer(4, "Kasztelan", 5, "Lager", 2.20)
biedronka.fridge.append(kasztelan)
kont.fridge.append(kasztelan)
biedronka.buy()
mojito = Drink(8, "Mojito", 15)
kont.fridge.append(mojito)
kont.buy()
print(biedronka.fridge)
biedronka.sorto_by_name()
biedronka.sorto_by_rate()







