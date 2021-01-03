# 6

s1 = input("podaj dystans w km:")
t1 = input("podaj czas w godzinach:")
v1 = (float(s1)) / (float(t1))
s2 = input("podaj dystans2 w km:")
t2 = input("podaj czas2 w godzinach:")
v2 = (float(s2)) / (float(t2))

zmiana = (float(v2)) - (float(v1))

v3 = (v2+v1)/2

print("V1:",v1,"Zmiana:",zmiana,"Prędkość średnia:",v3)
