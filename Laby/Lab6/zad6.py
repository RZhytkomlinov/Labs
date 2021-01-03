import random
tab6 = []
for i in range (0, 10):
    tab6.append(random.randint(0, 7))
print(tab6)
tab6.sort()
print(tab6)
y = 0
while y<len(tab6):
    z = tab6.count(tab6[y])
    if z>1:
        print("Liczba", tab6[y] ,"powtarza się", z ,"raz/y")
    y +=z
# newTab6 = list(dict.fromkeys(tab6))
# print("Nowa tablica: ",newTab6)
# print("Długość nowej tablicy: ",len(newTab6))