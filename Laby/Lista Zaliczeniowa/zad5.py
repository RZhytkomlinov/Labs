def choices(choice):
    if choice == 1:
        baht()
    elif choice == 2:
        btc()

    elif choice == 3:
        btn()
    elif choice == 4:
        mro()
    elif choice == 5:
        eth()


def baht():
    while True:
        try:
            string = str(input("Konwertuję z(wpisz 'thb' lub 'usd'): "))
            amount = int(input("Podaj ile:"))
            if string == 'thb':
                result = amount*0.033
                print(f'{amount} THB to {round(result,2)} USD')
                break
            elif string == 'usd':
                result = amount*29.86
                print(f'{amount} USD to {round(result,2)} THB')
                break
            else:
                print("THB albo USD")
        except not (not TypeError and not ValueError):
            print("Musisz wpisać cyferki")


def btc():
    while True:
        try:
            string = str(input("Konwertuję z(wpisz 'btc' lub 'usd'): "))
            amount = int(input("Podaj ile:"))
            if string == 'btc':
                result = amount*32400
                print(f'{amount} BTC to {round(result,2)} USD')
                break
            elif string == 'usd':
                result = amount*0.000031
                print(f'{amount} USD to {round(result,2)} BTC')
                break
            else:
                print("BTC albo USD")
        except not (not TypeError and not ValueError):
            print("Musisz wpisać cyferki")


def btn():
    while True:
        try:
            string = str(input("Konwertuję z(wpisz 'btn' lub 'usd'): "))
            amount = int(input("Podaj ile:"))
            if string == 'btn':
                result = amount*0.014
                print(f'{amount} BTN to {round(result,2)} USD')
                break
            elif string == 'usd':
                result = amount*72.81
                print(f'{amount} USD to {round(result,2)} BTN')
                break
            else:
                print("BTN albo USD")
        except not (not TypeError and not ValueError):
            print("Trzeba było wpisać kwotę")


def mro():
    while True:
        try:
            string = str(input("Konwertuję z(wpisz 'mro' lub 'usd'): "))
            amount = int(input("Podaj ile:"))
            if string == 'mro':
                result = amount*0.028
                print(f'{amount} MRO to {round(result,2)} USD')
                break
            elif string == 'usd':
                result = amount*36.08
                print(f'{amount} USD to {round(result,2)} MRO')
                break
            else:
                print("MRO albo USD")
        except not (not TypeError and not ValueError):
            print("Trzeba było wpisać kwotę")


def eth():
    while True:
        try:
            string = str(input("Konwertuję z(wpisz 'eth' lub 'usd'): "))
            amount = int(input("Podaj ile:"))
            if string == 'eth':
                result = amount*0.00077
                print(f'{amount} ETH to {round(result,2)} USD')
                break
            elif string == 'usd':
                result = amount*1297.85
                print(f'{amount} USD to {round(result,2)} ETH')
                break
            else:
                print("ETH albo USD")
        except not (not TypeError and not ValueError):
            print("Trzeba było wpisać kwotę")



print("Program pozwalający przeliczyć z podanych walut w obie strony:")
print("""
1) Baht Tajski (THB) - Dolary amerykańskie (USD).
2) Bitcoin (BTC) - Dolary amerykański(USD)
3) Ngultrum bhutański(BTN) - Dolary amerykańskie(USD)
4) Ugija mauretańska(MRO) - Dolary amerykańskie (USD)
5) Ethereum(ETH) – Dolary amerykańskie (USD)
""")
while True:
    choice = int(input("Wybierz z menu (1-5): "))
    try:
        if choice > 5 or choice < 1:
            print("Wybierz 1-5: ")
        else:
            choices(choice)
            break
    except TypeError or ValueError:
        print("Musisz wpisać cyferkę: ")
