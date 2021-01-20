while True:
    try:
        x = int(input('Na jakiej wysokosci lecimy [m]: '))
        break
    except:
        print('To nie jest liczba')
km = x / 1000


def wysoko(km):
    if km > 5:
        print('Na tej wysokosci jestes bezpieczny')
    else:
        print(km, 'km to za nisko!')


print('''
Witaj lotniku co chcesz zrobic
[1] - Sprawdź wysokość
[2] - Katapultacja
''')

k = True
while k:
    wybor = input('Wybierz liczbe z podanych: ')
    if wybor == '1':
        print(wysoko(km))
        k = False
    if wybor == '2':
        if km > 2:
            print('Proces katapultacji rozpoczety powodzenia')
            break
        else:
            print('Nie mozesz sie katapultowac na tej wysokosci')
            k = False