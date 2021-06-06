def pl():
    inp = input("Podaj kod: ")
    try:
        tab = inp.split('-')
        print(tab)
        if len(tab[0]) == 2 and len(tab[1]) == 3:
            with open('kodypocztowe.txt','w') as f:
                x = ''
                f.write(f'{x.join(tab)}   ')
    except:
        print("Podałeś zły kod")


def us():
    try:
        inp = int(input("Podaj kod: "))
        if inp == 5:
            with open('kodypocztoweUS.txt', 'w') as f:
                f.write(f'{inp}   ')
    except:
        print("Podałeś zły kod")