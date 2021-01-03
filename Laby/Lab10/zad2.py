imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
numer = input("Podaj numer: ")
but = input("Podaj numer buta: ")
if not imie.istitle() or not nazwisko.istitle():
    print(imie.title() + ' ' + nazwisko.title())
if not numer.isdigit() or len(numer) != 9:
    print("Nieprawidłowy numer")
if not but.isdigit():
    print("Nieprawidłowy numer buta")
if imie.endswith('a') and nazwisko.endswith('a'):
    print("Pewnie kobieta")
else:
    print("Pewnie nie kobieta")
