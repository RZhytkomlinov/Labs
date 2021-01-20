class Calc:
    def suma(x, y):
        return x + y

    def roznica(x, y):
        return x - y

    def mnozenie(x, y):
        return x * y

    def dzielenie(x, y):
        return x / y

    def pierwiastek(x):
        return x ** 0.5


print("""
1 - Dodawanie
2 - Odejmowanie
3 - Mnożenie
4 - Dzielenie
5 - Pierwiastek Kwadratowy
""")

wybor = int(input("Podaj jakie działanie chcesz wykonać: "))

if wybor != 5:
    inp1 = float(input("Podaj pierwszą liczbę: "))
    inp2 = float(input("Podaj drugą liczbę: "))
else:
    inp1 = float(input("Podaj pierwszą liczbę: "))

if wybor == 1:
    print(Calc.suma(inp1, inp2))

elif wybor == 2:
    print(Calc.roznica(inp1, inp2))

elif wybor == 3:
    print(Calc.mnozenie(inp1, inp2))

elif wybor == 4:
    print(Calc.dzielenie(inp1, inp2))

elif wybor == 5:
    print(Calc.pierwiastek(inp1))