# class Cars():
#
#     cars = []
#
#     def __init__(self, color, price, mark, maxspeed, type, started):
#         self.color = color
#         self.price = price
#         self.mark = mark
#         self.type = type
#         self.maxspeed = maxspeed
#         self.started = started
#
#     def jedzprosto(self):
#         return f"{self.mark} jedzie prosto"
#
#     def stop(self):
#         return f"{self.mark} nie jedzie prosto"
#
#     def is_started(self):
#         if not self.started:
#             return f"{self.mark} nie jest odpalony"
#         if self.started:
#             return f"{self.mark} jest odpalony"
#
#
#
#
# if __name__ == '__main__':
#     car_one = Cars('red','60001$','lamborghini','3km/h','Kabriolet', False)
#     car_two = Cars('blue', '12$', 'skoda', '-3km/h', 'NieKabriolet', False)
#     car_three = Cars('czerwony', '60k$', 'ferrari', '3km/h', 'Kabriolet', False)
#     car_four = Cars('black', '111$', 'mercedes', '3km/h', 'NieKabriolet', False)
#     car_five = Cars('white', '12567$', 'ford', '3km/h', 'NieKabriolet', False)
#
#
#     car_choice = str(input("Jaki wybierasz samochód?"))
#     print(Cars)
#     komunikat_startu = str(input("Chcesz odpalić samochód?"))

import time


class Samochod:

    def __init__(self, marka, model, przebieg, kolor, rodzaj):
        self.marka = marka
        self.model = model
        self.przebieg = przebieg
        self.kolor = kolor
        self.rodzaj = rodzaj

    def jedz_prosto(self, predkosc):
        return "Samochód o kolorze {} jedzie prosto z predkoscia {} km/h.".format(self.kolor, predkosc)

    def skrec(self, kierunek):
        while True:
            if kierunek == "lewo":
                return "Samochód o kolorze {} skręca w {}".format(self.kolor, "Lewo")
            elif kierunek == "prawo":
                return "Samochód o kolorze {} skręca w {}".format(self.kolor, "Prawo")
            else:
                print("Podaj właściwy kierunek")

    def stop(self, predkosc):
        while predkosc > 0:
            predkosc = predkosc - 5
            if predkosc < 0:
                predkosc = 0
            print("Prędkość samochodu o rodzaju {} to {}".format(self.rodzaj, predkosc))
            time.sleep(0.1)
        return "Samochód rodzaju {} stoi".format(self.rodzaj)

    def otworz_bagaznik(self, status):
        if status == True:
            return "Samochód modelu {} ma otwarty bagażnik".format(self.model)
        elif status == False:
            return "Samochód modelu {} ma zamknięty bagażnik".format(self.model)


if __name__ == '__main__' :

    samochod1 = Samochod("Ferrari", "Testarossa", "60000", "Czerwony", "Kabriolet")
    samochod2 = Samochod("Skoda", "Octavia", "400000", "Niebieski", "Kombi")
    samochod3 = Samochod("BMW", "Seria 5", "230000", "Granatowy", "Sedan")
    samochod4 = Samochod("Toyota", "Avensis", "333000", "Srebrny", "Kombi")
    samochod5 = Samochod("Ford", "Puma", "120000", "Zielony", "Coupe")

    print(samochod3.stop(45))
    print(samochod5.otworz_bagaznik(True))
    print(samochod1.jedz_prosto(45))
    print(samochod1.skrec("lewo"))