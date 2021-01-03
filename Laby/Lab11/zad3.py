import math
kat = int(input("Daj kąt:"))
kat1 = math.radians(kat)
print(kat1)
sin_kat = round(math.sin(kat1), 3)
cos_kat = round(math.cos(kat1), 3)
tg_kat = round(math.tan(kat1), 3)
ctg_kat = round(1/tg_kat, 3)

if kat == 90:
    tg_kat = "Nie ma czegoś takiego"

print('Sin kąta = ', sin_kat)
print('Cos kąta = ', cos_kat)
print('Tg kąta = ', tg_kat)
print('Ctg kąta = ', ctg_kat)