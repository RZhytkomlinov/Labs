inp = int(input("Podaj int: "))


def binary(x):
    return bin(x)


def octa(x):
    return oct(x)


def hexa(x):
    return hex(x)

print('Int to 2: ',binary(inp))
print('Int to 8: ',octa(inp))
print('Int to 16: ',hexa(inp))

inpb = int(input("Podaj binarną liczbę: "),2)
print(inpb)
print('Bin to 8:',octa(inpb))
print('Bin to 16:',hexa(inpb))

inhb = int(input("Podaj szesznastkową liczbę: "),16)
print(inhb)
print("16 to 8: ",octa(inhb))