inpA = int(input("Podaj liczbe liczb: "))
i = 0
for x in range (1, inpA):
    while i<inpA:
        i += 1
        print("Podawaj liczby: ")
        inpB = int(input("Podaj liczbe {}: ".format(i)))
        if -6<inpB<6:
            print("Podana liczba jest z przedziału [-6;6]")
        else:
            print("Podana liczba nie jest z przedziału [-6;6]")
