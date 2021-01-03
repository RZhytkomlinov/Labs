print("Symulator badania alkomatem")

# promile = float(input("Dmuchaj:"))
# if promile <= 0.2:
#     print("Jesteś trzeźwy")
# elif promile > 0.2:
#     print("jesteś napity")
# #     if promile > 1.5:
# #         print("jesteś napierdolony")
# elif promile > 1.5:
#     print("jesteś napierdolony")

a = float(input("Podaj ilość alkoholu w wydychanym powietrzu(mg/L):"))
b = a * 2.1
print("Wynik w promilach", b, "%o")
if((b == 0.2) or (b < 0.2)):
    print("Jesteś trzeźwy mozesz jechać:")
else:
    print("Jesteś pijany i nie mozesz jechac")