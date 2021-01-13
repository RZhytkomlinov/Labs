# def cal(cal):
#     print(f"Wysokość w m {wynik / 100}")
#     print(f"Wysokość w cm {wynik}")
#     print(f"Wysokość w mm {wynik * 10}")
#     print(f"Wysokość w km {wynik / 1000}")
cal = int(input("Podaj cale: "))

cale = 2.54*cal
def cm(cale):
    finish = f'W cm: {cale/10}'
    return finish
def mm(cale):
    finish = f'W mm: {cale*10}'
    return finish
def m(cale):
    finish = f'W m: {cale}'
    return finish
def km(cale):
    finish = f'W km: {cale/1000}'
    return finish
if __name__ == "__main__":
    print("Wpisz w co chcesz przekształcić cale: mm,cm,m,km")
    what = input("Podaj co chcesz ode mnie: ")
    if what == 'mm':
        print(mm(cale))
    elif what == 'cm':
        print(cm(cale))
    elif what == 'km':
        print(km(cale))
    elif what == 'm':
        print(m(cale))