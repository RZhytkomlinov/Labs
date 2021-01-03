tupla4 = ("a", "b", "c", "abcabc", "bacbac","hutnicza")
input = input("daj wyraz: ")
if_in = input in tupla4
i=0
if if_in == True:
    print(tupla4.index(input))

