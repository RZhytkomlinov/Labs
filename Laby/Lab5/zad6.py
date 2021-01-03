import random
randA = int(random.randint(1, 100))
i = 1
print("Wylosowano: ", (randA))
while i<=3:

    guessB = int(input("Zgadywaj: "))
    if guessB == randA:
        print("Dobra, wygrałeś")
        break
    elif guessB > randA:
        print("Podałeś za dużą liczbę")
    elif guessB < randA:
        print("Podałeś za małą liczbę")
    else:
        print("Nie nie nie")
    if i>=3:
        print("Haha xD 69 420 przegrałeś")
    i += 1