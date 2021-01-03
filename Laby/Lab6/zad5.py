import random

x = int(input("daj liste od: "))
z = int(input("daj liste do: "))
n = int(input("daj ile liczb w liście: "))
tab5 = []
for i in range (0, n):
    tab5.append(random.randint(x,z))
print(tab5)
print("3 element od końca {}".format(tab5[-3]))
k = int(input("daj k(usuwanie elementa): "))
tab5.pop(-k)
print(tab5)
tab6 = []
for i in range (0, n):
    tab6.append(random.randint(x,z))
print(tab6)
tab7 = sum([tab5, tab6],[])
print(tab7)
print("Długość nowej tablicy: ", len(tab7))
# a1 = set(tab5)
# a2 = set(tab6)
# if a1.intersection(a2) != None:
#     print("Niema liczb, które się powtarzają")
# else:
#     print("Powtarzają się liczby {}".format(a1.intersection(a2)))
y = 0
while y<len(tab7):
    z = tab7.count(tab7[y])
    if z>1:
        print("Liczba", tab7[y] ,"powtarza się", z ,"raz/y")
    y +=z


