from pytemp import pytemp

def choices(choice):
    if choice == 1:
        fahrenheit_celcius()
    elif choice == 2:
        fahrenheit_kelvin()
    elif choice == 3:
        celcius_kelvin()


def fahrenheit_celcius():
    while True:
        try:
            string = str(input("Konwertuję z(wpisz 'celcius' lub 'fahrenheit'): "))
            amount = int(input("Podaj ile stopni:"))
            if string == 'celcius':
                f = pytemp(amount, 'c', 'f')
                print(f'{amount} Celcius to {round(f,2)} Fahrenheit')
                if f >= 212:
                    print("Woda wrze")
                elif f < 32:
                    print("Woda zamarza")
                break
            elif string == 'fahrenheit':
                f = pytemp(amount, 'f', 'c')
                print(f'{amount} Fahrenheit to {round(f,2)} Celcius')
                break
            else:
                print("Celcius albo Fahrenheit")
        except not (not TypeError and not ValueError):
            print("Trzeba było wpisać stopnie")


def fahrenheit_kelvin():
    while True:
        try:
            string = str(input("Konwertuję z(wpisz 'kelvin' lub 'fahrenheit'): "))
            amount = int(input("Podaj ile stopni:"))
            if string == 'kelvin':
                f = pytemp(amount, 'k', 'f')
                print(f'{amount} Kelvin to {round(f,2)} Fahrenheit')
                if f >= 212:
                    print("Woda wrze")
                elif f < 32:
                    print("Woda zamarza")
                break
            elif string == 'fahrenheit':
                f = pytemp(amount, 'f', 'k')
                print(f'{amount} Fahrenheit to {round(f,2)} Kelvin')
                break
            else:
                print("Kelvin albo Fahrenheit")
        except not (not TypeError and not ValueError):
            print("Trzeba było wpisać stopnie")

def celcius_kelvin():
    while True:
        try:
            string = str(input("Konwertuję z(wpisz 'kelvin' lub 'fahrenheit'): "))
            amount = int(input("Podaj ile stopni:"))
            if string == 'kelvin':
                f = pytemp(amount, 'k', 'c')
                print(f'{amount} Kelvin to {round(f,2)} Celcius')
                break
            elif string == 'celcius':
                f = pytemp(amount, 'c', 'k')
                print(f'{amount} Celcius to {round(f,2)} Kelvin')
                break
            else:
                print("Kelvin albo Celcius")
        except not (not TypeError and not ValueError):
            print("Trzeba było wpisać stopnie")


print("Przeliczanie temperatury:")
print("""
1) Celcius i Fahrenheit
2) Kelvin i Fahrenheit
3) Celcius i Kelvin
""")
while True:
    choice = int(input("Wybierz z menu (1-3): "))
    try:
        if choice > 3 or choice < 1:
            print("Wybierz 1-3: ")
        else:
            choices(choice)
            break
    except TypeError or ValueError:
        print("Musisz wpisać cyferkę: ")