foot = 30.48
cal = 2.54
inp = input("Podaj wysokość w postaci foot'cal: ")
tab = inp.split("'")
wynik = foot*int(tab[0])+cal*int(tab[1])
print(f"Wysokość w m {wynik/100}")
print(f"Wysokość w cm {wynik}")
print(f"Wysokość w mm {wynik*10}")
print(f"Wysokość w km {wynik/1000}")

