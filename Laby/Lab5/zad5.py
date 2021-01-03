suma = 0
i = 0
while i <= 100:
    if suma > 1000000:
        print("Po właśnie tej liczbie: ", i)
        break
    i += 1
    i3 = i*i*i
    suma = suma + i3
print("Suma sześcianów liczb [0,100] to {}".format(suma))
