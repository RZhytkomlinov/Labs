n = int(input("Podaj nieujemną liczbę: "))
tab = []
suma = 0
x = 0
if n>0:
    for i in range (0,n+1):
        tab.append(i)
        print(tab)
    while x<len(tab):
        suma = suma + tab[x]**2
        x+=1
print(suma)