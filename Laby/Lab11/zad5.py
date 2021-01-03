inp = int(input("Na jakiej wysokości lecimy? [w metrach]:"))
if inp/1000<5:
    print(f"{inp/1000}km to za nisko")
else:
    print("Na tej wysokości jesteś już bezpieczny")